# Using project manager skills with ChatGPT

ChatGPT supports skills in the same open format these use, so the skill files work as they are. One difference matters: ChatGPT doesn't work in a folder on your computer. The records that connect the skills (`DECISIONS.md`, `ACTIONS.md`, `RAID.md`) need a place to live, and below are two ways to give them one.

## Install as skills

1. Download a skill ZIP from the [latest release](https://github.com/numal-ai/project-manager-skills/releases/latest), for example [meeting-minutes.zip](https://github.com/numal-ai/project-manager-skills/releases/latest/download/meeting-minutes.zip). The [starter pack](https://github.com/numal-ai/project-manager-skills/releases/latest/download/project-manager-skills-starter.zip) holds three of them: unzip it first.
2. In ChatGPT, open **Skills**, choose **Create**, then **Upload from your computer**, and pick the skill ZIP.
3. Repeat for each skill you want.

Whether you see **Skills** depends on your plan and, in a company workspace, on what your admin allows. OpenAI keeps the current list in [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## No Skills menu? Use a project

1. Create a project in ChatGPT, for example "Onboarding launch".
2. Add the `SKILL.md` files you want as project files. Download them from [skills/](../skills) on GitHub.
3. Add this to the project instructions:

```text
When a request matches one of the SKILL.md files in this project, follow that file step by step.
Keep the records it describes (DECISIONS.md, ACTIONS.md, RAID.md) and give me the updated
files at the end so I can add them back to the project.
```

## Keep the records between chats

ChatGPT can't save to your disk, so each skill hands the updated record back to you:

1. After the minutes, ask: `Give me DECISIONS.md and ACTIONS.md as files.`
2. Add those files to the project, replacing the old ones.
3. Next time, the agenda, the status report and the morning brief read them from there.

If you skip this, each chat starts from zero, and the skills still work one meeting at a time.

## First run

```text
Write minutes from this transcript.
```

Paste the transcript or attach the export from Zoom, Meet or Teams. Then:

```text
Prep the agenda for next week's sync from what's still open.
```

[Start here by situation](../README.md#start-here-by-situation) has a first prompt for every common case.

## Good to know

- Tickets and messages: if you've connected a tracker or chat app in ChatGPT, `action-items` shows the exact list and creates nothing until you say yes.
- 1:1 notes are private by default. Keep them in a separate project from the team's records.

[Back to the README](../README.md)
