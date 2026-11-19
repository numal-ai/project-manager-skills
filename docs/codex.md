# Using project manager skills with OpenAI Codex

Codex reads Agent Skills, and it works in a folder, so the skills keep their shared records (`DECISIONS.md`, `ACTIONS.md`, `RAID.md`) between sessions.

## Install

Pick one way.

**As a plugin:**

```bash
codex plugin marketplace add numal-ai/project-manager-skills
```

Then install **project-manager-skills** from the plugins directory.

**As files**, for all your projects:

```bash
git clone https://github.com/numal-ai/project-manager-skills
mkdir -p ~/.agents/skills
cp -R project-manager-skills/skills/* ~/.agents/skills/
```

Or for one project only: copy them into `.agents/skills/` in that project instead.

Restart Codex if the skills don't show up.

## Use them

Codex picks a skill by its description, so plain requests work. To call one by name, start with `$`:

```text
$meeting-minutes write minutes from notes/2026-11-17-sync.txt
```

```text
$status-report Friday update for stakeholders
```

## Where the records go

The skills save to the folder Codex runs in. Start Codex in a project notes folder, or say where to keep them:

```text
Keep the project records in pm/ from now on.
```

## Good to know

- Codex asks before it touches the network. `action-items` also shows the exact list of tickets and creates nothing until you say yes.
- The Codex app and the CLI read the same skills folder.

[Start here by situation](../README.md#start-here-by-situation) has a first prompt for every common case.

[Back to the README](../README.md)
