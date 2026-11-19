---
name: status-report
description: Write a project status report or weekly update from the real record - decisions made, action items done and overdue, RAID changes, tracker progress - with an honest RAG status (green, amber, red), what changed since the last report, what comes next and what the reader needs to do. Also rolls several projects or teams into one portfolio summary for a head of department or an executive. Use it whenever the user asks for a status report, weekly report, weekly status update, stakeholder update, steering committee update, project update email, "write my Friday update", or a roll-up across teams or projects.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Status report

Readers of a status report want three things, in this order:

1. Is it on track?
2. What changed?
3. Do they need to do anything?

Build the report from the record, not from memory, so it is honest. A report that is green every week until it is suddenly red is worse than no report.

## What you need

- **Project or team name, the period** (default: since the last report in `reports/`, or the last 7 days), and **the audience** (team, stakeholders, executive). The audience decides the length.
- **The record in the working folder, when it exists:**
  - `DECISIONS.md`: decisions made in the period;
  - `ACTIONS.md`: done, overdue and blocked items;
  - `RAID.md`: new or changed risks, issues and dependencies;
  - `CHANGES.md`: change requests raised or decided in the period, and those still waiting;
  - `PROJECT.md`: the goal, the success measures and the milestone dates to report against;
  - `TEAM.md`, section Stakeholders: who gets which version of the report, and what each reader needs from it;
  - `meetings/`: minutes from the period;
  - the last report in `reports/`, to say what changed.
- **Connected tools, read-only:**
  - tracker: closed and open tickets, milestones, cycle or sprint progress;
  - docs: the plan with milestone dates.
- **What the user adds:** context the record doesn't show, such as morale, a customer escalation or a budget change.

## Steps

1. **Collect the facts for the period** from the sources above. Keep the source of each fact, because a reader may ask «where does this come from?».

2. **Set the RAG status by these rules**, not by mood:
   - **Green:** on track for the next milestone; no High risk without a working mitigation. A dependency that isn't late yet but has little margin stays Green, with the margin named in the status line.
   - **Amber:** a milestone is at risk; a High risk's mitigation isn't working yet; or a dependency is late. Recovery is in the team's hands.
   - **Red:** a milestone will be missed without help, or the team can't recover alone. A red status always comes with an ask.
   - If the status changed since the last report, say why in one line. Don't soften amber into green: the record shows the overdue items anyway.

3. **Write the report** in the format below. Size it for the audience:
   - executive: half a page;
   - stakeholders: about one page;
   - team: can include detail.

4. **Save it**, if you can write files, to `reports/YYYY-MM-DD-<short-name>.md`, for example `reports/2026-11-20-onboarding-status.md`.
   - If newer material (the user's notes, a thread) changes rows in `RAID.md` or `ACTIONS.md`, use the newer facts in the report, and offer to update those files.
   - For readers outside the team, write dates marked `(check)` as «(unconfirmed)».
   - A change request still waiting for a decision is an ask in the report, addressed to the person who decides.
   - Offer to send it or post it, and do that only when the user says so.
   - Without file access, return it as text.

## Report format

```markdown
# <Project> - status, <period>

**Status: Amber** (was Green) - onboarding launch at risk: billing price IDs are late (DP-001).

## What changed
- Decided: staged launch, 10% on 1 Dec, everyone on 15 Dec (D-014). Moving to January was not accepted (D-015).
- Done: landing page copy (A-027), support macros (A-030).
- New risk: support overload in pricing week (R-004), mitigated by the staged launch.

## Next
- Next milestone: 10% launch on 2026-12-01.
- This week: rollout note to support (Priya, 19 Nov); legal sign-off on the vendor quote (Sam, 25 Nov).

## Needs from you
- Billing: confirm the price IDs by 2026-11-27 (Ana). Without them the 1 Dec date moves.

## Watch list
| | Item | Owner | Due | Note |
|---|---|---|---|---|
| Blocked | Vendor quote approval (A-029) | Sam | 2026-11-25 | Waiting on legal (I-003) |
```

- Lead with the status line. A reader who stops there should already know the most important thing.
- «Needs from you» is the section that makes a report worth sending. If nothing is needed, write «Nothing needed this week».
- Name the IDs (`D-014`, `A-029`, `R-004`) so the report links back to the record.

## Roll-up across projects or teams

When the reader manages several projects or several leads (a head of department, a director, an executive):

1. Build a short status for each project as above, from its own folder or section. The user says where each project's record lives.
2. Combine them into one page:

```markdown
# Portfolio - week of <date>

| Project | Status | What changed | Needs from you |
|---|---|---|---|
| Onboarding | Amber (was Green) | Staged launch decided; billing IDs late | Push billing for 27 Nov |
| Mobile app | Green | Beta to 200 users | - |
| Data migration | Red | Vendor contract stuck in legal 2 weeks | Escalate to legal lead |

## Across projects
- <a pattern several teams share, e.g. legal review is the bottleneck for 2 projects>
- <decisions in one project that affect another>
```

3. Put red and amber first. Under «Across projects», add only patterns the record shows, not guesses.

## Rules

- **Never invent progress.** If the record and the tracker show no movement on something, say «no update». Don't make one up.
- **Separate facts from the user's judgment.** Facts come from the record. Judgments the user added are written as theirs («Maya: team is stretched this week»).
- **Same structure every week.** Readers learn where to look, so changes stand out.

## Example

A worked example on demo data, with the request, the reply and the files written: [a Friday status report for two stakeholders](examples/friday-status.md). Read it when you want to see the expected output; the names and dates in it are made up.
