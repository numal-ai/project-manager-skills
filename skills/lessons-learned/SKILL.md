---
name: lessons-learned
description: Keep a lessons learned register for projects, and use it. Turns retros, post-mortems, closeout reviews and decisions whose results are now known into short lessons ("when X happens, do Y, because Z") with sources and tags. Brings back the lessons that match a new project, plan or risk, and writes a project closure report. Use it whenever the user mentions lessons learned, a lessons learned template or register, a project closure or closeout report, a post project review, "what did we learn", "have we done this before", "what came of our decision to", or starts a project like an earlier one. Use it after a retrospective or post-mortem to keep what was learned.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Lessons learned

Most lessons-learned documents are written once, at the end of a project, and never opened again. A lesson pays off only when the next project reads it at the moment it matters: at kickoff, when a similar risk shows up, before a similar decision. So this skill does two jobs. It writes lessons short enough to reuse, and it brings them back at the right time.

The register lives in `LESSONS.md` in the working folder.

## Format

```markdown
# Lessons learned

| ID | When this happens | Do this | Because | Tags | Status | Source |
|---|---|---|---|---|---|---|
| L-001 | A launch lands in the same week as a pricing change | Roll out in steps and keep a week between the launch and the price change | The last pricing change doubled the support queue for four days | launch, support, schedule | Active | meetings/2026-11-17-weekly-sync.md |
| L-002 | Work waits on another team's answer | Name a person on that team and a date to answer by, the day the wait starts | The pricing page was blocked for a whole sprint on an answer nobody chased | dependencies, planning | Active | retros/2026-11-16-onboarding-sprint.md |
```

- **When this happens:** a situation someone can spot in advance.
- **Do this:** an action someone can take.
- **Because:** what happened, in one or two short sentences, with numbers if there were any.
- **Tags:** two to four, reusing the tags already in the register: the kind of project or area (launch, vendor, migration, hiring) and the part of the work (planning, risk, stakeholders, schedule, quality).
- **Status:** `Active`, `Replaced by L-0xx`, or `Retired` (no longer true).
- **Source:** a retro, minutes, a closeout report, an incident review, or a decision whose result is now known (`D-001`). For notes outside the folder, a short name and date, such as «Maya's launch review notes, 2026-12-18».

The rows above show the format on a made-up project. Never copy them into a real register.

## What the user may ask for

### Add lessons from a retro, post-mortem or closeout
1. Read the source: a file in `retros/` (the `retrospective` skill writes them), a post-mortem, a closeout discussion, or what the user tells you.
2. Pick three to five lessons per run, across all the sources given, that would change what someone does next time. Fewer is fine. A finding like «communication could be better» doesn't count unless it comes with a concrete practice.
3. Write each one as When, Do, Because, with its source.
4. Check `LESSONS.md` for a lesson on the same thing. Add the new source to it, or replace it, rather than writing a near-copy.
5. Show the rows. A request to add the lessons is the yes to write them.

### What came of a decision?
For a decision in `DECISIONS.md` whose Revisit date has passed, or one the user names:
1. Find what happened since: later minutes, status reports, RAID rows that closed or turned into issues, and what the user says.
2. Say what came of it in two or three lines, with sources: did it work, what did it cost, what surprised people. If the evidence isn't there, say so and ask.
3. If there is a lesson in it, write one with the decision as its source. If the user asked for lessons in the same message, it joins that batch. Otherwise propose it and wait for the yes.
4. If the decision should be looked at again, say so. Changing it is a new decision, recorded with the `decision-log` skill.

### Write a closure report
At the end of a project, write `reports/<date>-<project>-closeout.md`:
- **Goal and success measures** from `PROJECT.md`: target against actual, with sources.
- **Delivered, cut and deferred,** using `CHANGES.md`.
- **Dates:** planned against actual, and how much of the gap the approved changes explain.
- **Decisions** that turned out well or badly.
- **Handed over:** open action items and RAID rows, and who now owns each.
- **Lessons added:** the L-IDs.

Show it first. One yes writes the report and the new lessons.

### Find lessons for a new project or a risk
When a project starts, when a plan or a risk is discussed, or when the user asks «have we done this before?»:
1. Search `LESSONS.md` by tags and by the words of the situation. If there is no register yet, look in `retros/` and closed RAID rows.
2. Show at most five matching lessons, the most relevant first, each with its source.
3. Offer to add the ones that apply to `RAID.md` as risks or assumptions, with the lesson as the source. One yes covers the batch.

## Rules

- **No names, no blame.** A lesson is about the situation and the practice. «The vendor contract took four weeks in legal», never «Sam was slow».
- **Actionable or nothing.** If you can't write the «Do this», it isn't a lesson yet. Leave it as an open question in the retro.
- **Few and real.** Five lessons that get reused beat thirty that don't.
- **Retire, don't delete.** When a lesson stops being true, after a new process or tool, set it to `Retired` and say why.
- **Other records stay as they are.** If the material shows that rows in `ACTIONS.md`, `RAID.md` or `PROJECT.md` are out of date, list them at the end of the reply and offer to update them in one batch. Don't edit them as a side effect.
- **Approvals per run:** one yes per batch of lessons or per closure report. Finding lessons asks nothing.

## Example

A worked example on demo data, with the request, the reply and the files written: [lessons from a retro and a decision](examples/lessons-from-retro.md). Read it when you want to see the expected output; the names and dates in it are made up.
