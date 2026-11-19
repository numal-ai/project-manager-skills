# Using project manager skills with Cursor

Cursor reads Agent Skills, so these work without changes. They suit leads who already keep project notes in a repository next to the code.

## Install

Copy the skills into one of the folders Cursor reads:

| Folder | Who sees the skills |
|---|---|
| `.cursor/skills/` or `.agents/skills/` in a project | Everyone who opens that project |
| `~/.cursor/skills/` or `~/.agents/skills/` | Only you, in every project |

```bash
git clone https://github.com/numal-ai/project-manager-skills
mkdir -p ~/.cursor/skills
cp -R project-manager-skills/skills/* ~/.cursor/skills/
```

Cursor also loads skills from `~/.claude/skills/` and `~/.codex/skills/`, so if you've installed them for Claude Code or Codex, Cursor already sees them. Restart Cursor if they don't show up.

## Use them

The agent picks a skill by its description, so plain requests work:

```text
Write minutes from meetings/raw/2026-11-17-sync.txt
```

To call one by name, type `/` in Agent chat and search for it, for example `/meeting-minutes`.

## Where the records go

The skills save to the folder you work in. In a code repository, keep them out of the code:

```text
Keep the project records in pm/ from now on.
```

Commit `pm/` if the team should see decisions and actions in pull requests. Keep `pm/one-on-ones/` out of Git: add it to `.gitignore`, because 1:1 notes are private.

[Start here by situation](../README.md#start-here-by-situation) has a first prompt for every common case. Cursor's own guide: [Agent Skills](https://cursor.com/docs/skills).

[Back to the README](../README.md)
