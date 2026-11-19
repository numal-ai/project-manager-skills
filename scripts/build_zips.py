#!/usr/bin/env python3
"""Check the skills and build the ZIP files for a release.

    python scripts/build_zips.py           check, then build dist/
    python scripts/build_zips.py --check   check only

What it builds in dist/:
    <skill>.zip                          one skill, the skill folder at the root of the ZIP
    project-manager-skills-starter.zip   the starter skills, one ZIP per skill inside
    project-manager-skills-all.zip       every skill, one ZIP per skill inside

claude.ai and Claude Cowork take one skill per upload, so the packs hold
skill ZIPs: unzip the pack, then upload the ZIPs inside it.

Only the Python standard library is used. The ZIPs are reproducible: the same
files give the same bytes, whatever the clock or the file system says.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CLAUDE_PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
CODEX_PLUGIN = ROOT / "plugin.json"
README = ROOT / "README.md"

COLLECTION = "project-manager-skills"
STARTER = ["meeting-minutes", "meeting-agenda", "status-report"]

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
LONG_SKILL_LINES = 500

PACK_NOTE = """How to install

claude.ai and Claude Cowork
1. Open Customize > Skills (on older versions: Settings > Capabilities > Skills).
2. Upload each ZIP from this folder, one at a time. Don't upload the pack itself.
3. Start a new chat and say what you need, for example "Write minutes from this transcript".

Claude Code, Codex, Cursor and other agents
Unzip a skill ZIP into your skills folder, for example ~/.claude/skills/ or ~/.agents/skills/.

More: https://github.com/numal-ai/project-manager-skills
"""


def read_frontmatter(path: Path) -> tuple[dict[str, str], int]:
    """Return the top-level frontmatter keys of a SKILL.md and its line count.

    Enough YAML for SKILL.md files: `key: value`, quoted values, folded or
    literal blocks (`>` / `|`), and nested maps (kept as raw text).
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter: the file must start with ---")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter is not closed with ---") from None

    keys: dict[str, str] = {}
    current = None
    block: list[str] = []
    for line in lines[1:end]:
        if line and not line[0].isspace() and ":" in line:
            if current is not None:
                keys[current] = " ".join(block).strip()
            key, _, value = line.partition(":")
            current, value = key.strip(), value.strip()
            block = [] if value in (">", "|", ">-", "|-", "") else [value.strip("\"'")]
        elif current is not None:
            block.append(line.strip())
    if current is not None:
        keys[current] = " ".join(block).strip()
    return keys, len(lines)


def check_skills() -> tuple[list[str], list[str], list[str]]:
    """Check every skill. Return (skill names, errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []
    names: list[str] = []

    folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not folders:
        errors.append("skills/ has no skill folders")

    for folder in folders:
        where = f"skills/{folder.name}/SKILL.md"
        skill_md = folder / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{where}: missing")
            continue
        try:
            keys, line_count = read_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{where}: {exc}")
            continue

        unknown = sorted(set(keys) - ALLOWED_KEYS)
        if unknown:
            errors.append(f"{where}: keys not allowed in frontmatter: {', '.join(unknown)}")

        name = keys.get("name", "")
        if not name:
            errors.append(f"{where}: name is missing")
        elif not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{where}: name '{name}' must be lowercase words joined by hyphens, up to 64 characters")
        elif name != folder.name:
            errors.append(f"{where}: name '{name}' must match the folder name '{folder.name}'")

        description = keys.get("description", "")
        if not description:
            errors.append(f"{where}: description is missing")
        else:
            if len(description) > 1024:
                errors.append(f"{where}: description is {len(description)} characters, the limit is 1024")
            if "<" in description or ">" in description:
                errors.append(f"{where}: description must not contain < or >")
            if "use it" not in description.lower() and "use when" not in description.lower():
                warnings.append(f"{where}: description doesn't say when to use the skill")

        if COLLECTION not in keys.get("metadata", ""):
            warnings.append(f"{where}: metadata.collection is not {COLLECTION}")
        if line_count > LONG_SKILL_LINES:
            warnings.append(f"{where}: {line_count} lines; move detail into references/ to stay under {LONG_SKILL_LINES}")

        names.append(folder.name)

    for name in STARTER:
        if name not in names:
            errors.append(f"starter pack names '{name}', but skills/{name} doesn't exist")

    check_marketplace(names, errors)
    check_readme(names, errors)
    return names, errors, warnings


def check_marketplace(names: list[str], errors: list[str]) -> None:
    """The full set is the plugin at the root; every skill also has a plugin of its own.

    The full set loads every folder in skills/ through .claude-plugin/plugin.json, which
    Anthropic's plugin directory needs. Each single-skill plugin points at its own skill
    folder, so it never picks up that plugin.json or the other skills.
    """
    try:
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        manifest = json.loads(CLAUDE_PLUGIN.read_text(encoding="utf-8"))
        codex = json.loads(CODEX_PLUGIN.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"plugin files: {exc}")
        return
    plugins = {p.get("name"): p for p in data.get("plugins", [])}

    if manifest.get("name") != COLLECTION:
        errors.append(f".claude-plugin/plugin.json: name must be {COLLECTION}")
    if manifest.get("version") != codex.get("version"):
        errors.append(".claude-plugin/plugin.json and plugin.json must have the same version")

    full = plugins.get(COLLECTION)
    if full is None:
        errors.append(f".claude-plugin/marketplace.json: no plugin named {COLLECTION}")
    elif full.get("source") != "./" or "skills" in full:
        errors.append(f".claude-plugin/marketplace.json: {COLLECTION} must be source ./ with no skills list (plugin.json loads skills/)")

    for name in names:
        single = plugins.get(name)
        if single is None:
            errors.append(f".claude-plugin/marketplace.json: no plugin of its own for {name}")
        elif single.get("source") != f"./skills/{name}" or single.get("skills") != ["."]:
            errors.append(f".claude-plugin/marketplace.json: plugin {name} must be source ./skills/{name} with skills [\".\"]")
    for extra in sorted(set(plugins) - set(names) - {COLLECTION}):
        errors.append(f".claude-plugin/marketplace.json: plugin {extra} has no folder in skills/")


def check_readme(names: list[str], errors: list[str]) -> None:
    """Every skill is linked from the README."""
    text = README.read_text(encoding="utf-8")
    for name in names:
        if f"(skills/{name}/SKILL.md)" not in text:
            errors.append(f"README.md: no link to skills/{name}/SKILL.md")


def zip_bytes(entries: list[tuple[str, bytes]]) -> bytes:
    """A ZIP of (path, content) pairs with fixed times and modes."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for arcname, content in sorted(entries):
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, content)
    return buffer.getvalue()


def skill_zip(name: str) -> bytes:
    """The skill folder, with the folder itself at the root of the ZIP."""
    folder = SKILLS_DIR / name
    entries = []
    for path in folder.rglob("*"):
        rel = path.relative_to(folder)
        if path.is_file() and not any(part.startswith(".") for part in rel.parts):
            entries.append((f"{name}/{rel.as_posix()}", path.read_bytes()))
    return zip_bytes(entries)


def build(names: list[str]) -> list[Path]:
    DIST_DIR.mkdir(exist_ok=True)
    for old in DIST_DIR.glob("*.zip"):
        old.unlink()

    built: dict[str, bytes] = {name: skill_zip(name) for name in names}
    written = []
    for name, data in built.items():
        path = DIST_DIR / f"{name}.zip"
        path.write_bytes(data)
        written.append(path)

    note = PACK_NOTE.encode("utf-8")
    packs = {
        f"{COLLECTION}-starter": STARTER,
        f"{COLLECTION}-all": names,
    }
    for pack, members in packs.items():
        entries = [(f"{pack}/{m}.zip", built[m]) for m in members]
        entries.append((f"{pack}/HOW-TO-INSTALL.txt", note))
        path = DIST_DIR / f"{pack}.zip"
        path.write_bytes(zip_bytes(entries))
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="check the skills, build nothing")
    args = parser.parse_args()

    names, errors, warnings = check_skills()
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error: {line}")
    if errors:
        print(f"\n{len(errors)} error(s). Nothing built.")
        return 1
    print(f"{len(names)} skills checked: {', '.join(names)}")

    if args.check:
        return 0
    for path in build(names):
        print(f"built {path.relative_to(ROOT).as_posix()} ({path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
