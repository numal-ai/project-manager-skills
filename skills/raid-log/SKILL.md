---
name: raid-log
description: Build and maintain a RAID log (Risks, Assumptions, Issues, Dependencies), also called a risk register or risk and issue log, from project notes, meeting minutes, status reports or a conversation. Scores risks by impact and likelihood, names owners and mitigations, flags what changed since the last review, and prepares the risk section for a status or steering meeting. Use it whenever the user mentions RAID, a RAID log or template, risk register, risk log, issue log, dependencies, "what could go wrong", project risks, or is preparing a steering committee or status review.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# RAID log

A RAID log is worth keeping only if it changes what people do. Every row needs an owner and a next step, and the review shows what moved since last time. A log that just lists every worry gets ignored by week three.

The log lives in `RAID.md` in the working folder.

**RAID has two common meanings:**

- this skill uses **Risks, Assumptions, Issues, Dependencies**, and keeps decisions and actions in `DECISIONS.md` and `ACTIONS.md`;
- some organisations read the letters as **Risks, Actions, Issues, Decisions**.

If the user's company uses the second meaning, follow it: put actions and decisions as sections in `RAID.md` with the same columns those other files use.

## Format

```markdown
# RAID log - <project>
Last reviewed: 2026-11-17

## Risks
| ID | Risk | Impact | Likelihood | Owner | Mitigation | Status | Raised | Source |
|---|---|---|---|---|---|---|---|---|
| R-004 | Support is overloaded in the week pricing changes, if onboarding launches to everyone | High | Med | Leo | Staged launch (D-014); extra support shift 1-5 Dec | Watching | 2026-11-17 | meetings/2026-11-17-weekly-sync.md |

## Assumptions
| ID | Assumption | Owner | Check by | Status | Source |
|---|---|---|---|---|---|
| AS-002 | Legal reviews vendor contracts within 5 working days | Sam | 2026-11-25 | Open | ... |

## Issues
| ID | Issue | Impact | Owner | Next step | Status | Raised | Source |
|---|---|---|---|---|---|---|---|
| I-003 | Vendor quote stuck in legal review | Med | Sam | Ask legal for a date by Friday | Open | 2026-11-10 | ... |

## Dependencies
| ID | Dependency | On whom | Needed by | Owner | Status | Source |
|---|---|---|---|---|---|---|
| DP-001 | Billing team ships the new price IDs | Billing (Ana) | 2026-11-27 | Maya | Open | ... |
```

- **Risk:** something that may happen. Write it as cause → effect: «If X, then Y». «Support might struggle» is too vague to mitigate.
- **Issue:** something already happening. A risk that happens becomes an issue: close the risk with «became I-00x».
- **Assumption:** something the plan takes as true without proof. Give it a date to check it. A wrong assumption is a risk nobody listed.
- **Dependency:** something you need from someone outside the team, with a date.
- **Impact and likelihood:** `High`, `Med` or `Low`. Score likelihood as it is now, with the current mitigation in place.
  - If the user's organisation scores 1-5, use that instead and keep it consistent.
  - High impact × high likelihood goes to the top of the review.
- **Status:** `Open`, `Watching` or `Closed`. Never delete a row: closed rows show the project's history and what was learned.

## What the user may ask for

### Build or update the log from material
Sources: minutes, notes, a plan, a status report, a chat.
1. Find the risks («worried that», «if X slips», «we're assuming», «depends on», «blocked by», «waiting for»).
2. Sort them into R, AS, I and DP. Something another team must deliver by a date («if billing is late, the launch slips») is one dependency, not a dependency and a risk. The review still counts it among the top risks when it threatens a milestone.
3. Check `RAID.md` for duplicates. Update an existing row rather than adding a near-copy.
4. Show the new and changed rows. Missing owners go into one grouped question.
5. Write what the user confirms, with the next free IDs. Update «Last reviewed». If the user asked you to start or update the log, that request is the confirmation: write the rows, then ask about owners.

### Review before a status or steering meeting
Produce a short summary for that meeting:
- **What changed since the last review:**
  - new rows;
  - rows whose impact or likelihood went up;
  - risks that became issues;
  - rows closed.
- **Top risks:** at most 5, each with its owner and mitigation, and whether the mitigation is actually happening. Look for a matching item in `ACTIONS.md` or the tracker.
- **Overdue:** dependencies past their «needed by» date, and assumptions past their «check by» date.
- **Asks:** what the project needs from the people in the meeting: a decision, a person, money, a date.

### Seed a log at project start
From the kickoff discussion or the plan, list the obvious items:

- **Assumptions:** dates, people, budget, other teams.
- **Dependencies:** anything another team must deliver.
- **Risks:** three to five real ones.

Fifteen generic risks is not a log. Five real ones is.

If `LESSONS.md` exists, check it for lessons that match this kind of project, and offer the ones that apply as risks or assumptions, with the lesson as the source.

## Rules

- **No row without an owner.** If nobody owns it yet, write `?` in the Owner cell, and the review lists it as unowned until someone does.
- **Mitigation is an action, not a hope.** «Monitor closely» is not a mitigation. «Extra support shift 1-5 Dec (Leo)» is.
- **Escalate by the numbers.** Escalate when impact is High and the mitigation isn't working. Don't escalate everything: the log loses its signal.

## Example

A worked example on demo data, with the request, the reply and the files written: [starting a RAID log from meeting minutes](examples/start-from-minutes.md). Read it when you want to see the expected output; the names and dates in it are made up.
