# Using project manager skills with Claude Cowork

Cowork is the best home for these skills if you don't live in a terminal. It works inside a folder on your computer, so the skills can keep the shared records (`DECISIONS.md`, `ACTIONS.md`, `RAID.md`) between sessions, the same way they do in Claude Code.

## Install

Pick one way.

**As a plugin.** In the Claude desktop app, open **Customize → Plugins** and add a marketplace from GitHub: `numal-ai/project-manager-skills`. Then install **project-manager-skills** for all seventeen skills, or single skills such as **meeting-minutes**. A plugin you install this way belongs to your Claude account, so it also shows up in claude.ai chats and in Claude Code.

**As skill ZIPs.** Download the [starter pack](https://github.com/numal-ai/project-manager-skills/releases/latest/download/project-manager-skills-starter.zip) or [all skills](https://github.com/numal-ai/project-manager-skills/releases/latest/download/project-manager-skills-all.zip) and unzip it. Upload the skill ZIPs inside it, one at a time, in **Customize → Skills** (on older versions, **Settings → Capabilities → Skills**). Don't upload the pack itself: one ZIP holds one skill.

## Pick the folder

Start a Cowork task in the folder you want to use for one project, for example `Documents/Onboarding launch`. The skills keep their records there. The first time a skill wants to save something, it asks once.

One folder per project works best. The status report and the morning brief can still read several project folders if you point them there.

## First run

Drop a transcript or your notes into the folder, then say:

```text
Write minutes from the transcript in this folder.
```

Then:

```text
Prep the agenda for next Tuesday's sync.
```

The agenda starts with what the minutes left open. Later in the week:

```text
Write my Friday status update for stakeholders.
```

[Start here by situation](../README.md#start-here-by-situation) has a first prompt for every common case.

## Connected tools

If you've connected your calendar, tracker or chat in Cowork, the skills use them:

- `morning-brief` reads today's meetings and assigned tickets. It never writes anywhere.
- `action-items` can create tickets with the meeting context, but only after it shows you the exact list and you say yes.
- `meeting-minutes` drafts the recap message and sends nothing until you say so.

## Good to know

- Install the full set or single skills, not both, or each skill shows up twice.
- 1:1 notes stay in `one-on-ones/` and aren't copied into shared files unless you ask.
- To update, reinstall the plugin, or upload the new skill ZIPs over the old ones.

More about skills in Claude: [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) and [Plugins](https://claude.com/docs/plugins/overview).

[Back to the README](../README.md)
