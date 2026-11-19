# The shared folder

The seventeen skills read and write plain Markdown files in one folder, so each skill can pick up where another left off. Minutes add decisions and action items. The agenda, standup and status report read them, and the morning brief shows what is waiting on you. The charter, the change log and the lessons register give every other skill the project's scope, what changed and what past projects learned.

You don't need to set anything up. The first time a skill wants to keep a record, it asks once, then creates only the files it uses.

```
your-team-folder/
├── PROJECT.md          project charter: goal, success measures, scope in and out, milestones, who decides
├── DECISIONS.md        decision log: what was decided, by whom, why, when to revisit
├── ACTIONS.md          action items: who does what by when
├── RAID.md             risks, assumptions, issues, dependencies
├── CHANGES.md          change log: requested changes to scope, dates or budget, and what was decided
├── LESSONS.md          lessons register: in situation X, do Y, because Z
├── TEAM.md             optional: people and who reports to whom, meetings, team charter, RACI, stakeholders
├── meetings/           one file per meeting: 2026-11-17-weekly-sync.md (+ -agenda.md)
├── one-on-ones/        private: one running file per person: sam-lee.md
├── skip-levels/        private: one file per person you meet a level down, plus one per round of themes
├── onboarding/         one page per new team member, made from the team charter
├── standups/           2026-11-17.md
├── retros/             2026-11-13-sprint-12.md
└── reports/            2026-11-20-onboarding-status.md
```

## Rules every skill follows

- **Nothing is invented.** Every decision, action and risk must trace back to something someone said or wrote. If something is unclear, it goes under open questions instead of being guessed. Uncertain items are marked `(check)`.
- **Rows are never deleted.** A row's status changes instead (`Done`, `Dropped`, `Closed`, `Replaced by D-014`). The history is the point.
- **IDs are stable.** `D-001` for decisions, `A-001` for action items, `R-` / `AS-` / `I-` / `DP-` for RAID, `CR-001` for change requests, `L-001` for lessons. New rows take the next free number.
- **Dates are ISO** (`2026-11-17`). Relative dates such as «by Friday» are turned into dates, counted from the meeting date. A date nobody has given yet («next sprint») stays in the text, and the date cell says `(check)`.
- **No owner is written `?`.** An item nobody has taken keeps `?` in its Owner cell until someone does, in every file.
- **Source is where to look it up:** a path in the folder, a link, or, for material outside the folder, a short name and date («Maya's notes, 2026-11-20»).
- **Other people are never contacted silently.** Creating tracker tickets, sending recaps or posting to chat happens only after you say yes to a list of exactly what will be sent.
- **One yes per batch.** A run gathers everything that needs your yes into one list with one question at the top. Most runs ask for none or one. A row shows its own state, so nothing needs a separate confirmation to be read.
- **The plan itself is yours.** Dates, budget, scope and who is on the team change only when a person with the right to decide says so. A skill prepares the change (`change-control` writes the request and its impact) and records the decision in DECISIONS.md.
- **1:1 and skip-level notes stay private.** Nothing from `one-on-ones/` or `skip-levels/` is copied into shared files unless you ask. What leaves a skip-level leaves as a theme, without names.
- **No file access?** In a plain chat, a skill returns each block with the file it belongs to, so you can paste it yourself.

## File formats

### DECISIONS.md

```markdown
# Decision log

| ID | Date | Decision | Status | Decided by | Why | Revisit | Source |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-11-17 | Launch the new onboarding to 10% of sign-ups first | Accepted | Maya, Leo | Limits risk before the pricing change | 2026-12-01 | meetings/2026-11-17-weekly-sync.md |
| D-002 | 2026-11-17 | Move the launch to January | Not accepted | Maya | Sales already promised December | — | meetings/2026-11-17-weekly-sync.md |
```

Status is one of `Accepted`, `Not accepted` (a proposal that was declined or set aside), or `Replaced by D-0xx`.

### ACTIONS.md

```markdown
# Action items

| ID | Action | Owner | Due | Status | Source | Tracker |
|---|---|---|---|---|---|---|
| A-001 | Send the rollout note to support | Priya | 2026-11-20 | Open | meetings/2026-11-17-weekly-sync.md | — |
```

Status is one of `Open`, `Blocked`, `Done` or `Dropped`. The Tracker column holds the ticket key once a ticket exists, for example `LIN-482`.

### RAID.md

Four tables:

- **Risks:** ID, Risk, Impact, Likelihood, Owner, Mitigation, Status, Raised, Source.
- **Assumptions:** ID, Assumption, Owner, Check by, Status, Source.
- **Issues:** ID, Issue, Impact, Owner, Next step, Status, Raised, Source.
- **Dependencies:** ID, Dependency, On whom, Needed by, Owner, Status, Source.

Impact and likelihood are `High`, `Med` or `Low`. Status is `Open`, `Watching` or `Closed`. The `raid-log` skill holds the full format.

### PROJECT.md

The project charter, one per folder. The `project-charter` skill writes it, and every other skill reads it for the goal, the scope and who decides.

```markdown
# Project charter: New onboarding launch

Status: Agreed by Elena Brooks on 2026-10-07 · Updated: 2026-10-07 · Source: meetings/2026-10-05-kickoff.md

## Goal
New customers send their first invoice within a week of signing up.

## Success measures
| Measure | Now | Target | By | Source |
|---|---|---|---|---|
| Sign-ups who send a first invoice within 7 days | 31% | 45% | 2027-01-31 | meetings/2026-10-05-kickoff.md |

## Scope
**In:** the new sign-up flow, the invoice template picker, the support macros.
**Out:** pricing changes, the mobile app, bulk import for existing accounts.

## Milestones
| Milestone | Date | Status | Source |
|---|---|---|---|
| Rollout to 10% of new sign-ups | 2026-12-01 | Planned | D-001 |

## Who decides
Sponsor: Elena Brooks. Approves changes to scope, dates and budget: Elena Brooks. Runs the project: Maya Okafor.

## Budget frame
Not named at kickoff (check).

## Open questions
- Does the target count trial accounts? Ask Elena.

## Change history
- (none yet)
```

- **Success measures** have a number and a date. A goal nobody put a number on stays in the Goal section, and the measure is listed under open questions.
- **Scope** keeps both lists. «Out» is what stops the same request from coming back every week.
- **Milestones** link to the decision that set the date, when there is one.
- **Assumptions and risks** named at kickoff go to RAID.md, not here. The charter stays short.
- **Status** is `Draft` until the sponsor agrees it. Once agreed, it changes only through an approved change request or a decision. A line under `## Change history` shows when and why.

### CHANGES.md

The change log: every requested change to scope, dates or budget, from the request to the decision.

```markdown
# Change log

| ID | Raised | Change | Asked by | Impact | Status | Decided by | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| CR-002 | 2026-11-19 | Add bulk import of existing clients to the 2026-12-01 release, for the two accounts Sales promised December | Marco Diaz | About a week of work plus QA, with 6 working days left (check with Leo); puts 2026-12-01 at risk | Pending | Elena Brooks | — | Marco's email, 2026-11-19 |

## CR-002 Bulk import on 1 December

**What changes:** …
**Why it was asked:** …
**If we don't change:** …
**Impact:** scope, dates, money, people, risks, each with a source or `(check)`.
**Options:** accept, accept in part, defer, each with what it costs.
**Who decides:** Elena Brooks (approves scope changes, PROJECT.md).
```

Status is one of `Pending`, `Approved`, `Rejected`, `Deferred` or `Withdrawn`. A change approved in part is `Approved`, and the decision row says which part. **Decided by** is filled in from the start with who has the right to decide, so the agenda knows whom to put the item to. **Decision** holds the `D-0xx` row once the call is made.

### LESSONS.md

The lessons register: what past work taught, written so the next project can use it.

```markdown
# Lessons learned

| ID | When this happens | Do this | Because | Tags | Status | Source |
|---|---|---|---|---|---|---|
| L-001 | A launch lands in the same week as a pricing change | Roll out in steps and keep a week between the launch and the price change | Support tickets doubled when both landed together (check) | launch, support, schedule | Active | retros/2026-12-19-onboarding-launch.md |
```

- A lesson is advice someone can act on, not a feeling. «Communication was bad» is not a lesson. «Post the rollout plan to support two weeks before launch» is.
- No names and no blame. The lesson is about the situation.
- Status is `Active`, `Replaced by L-0xx` or `Retired` (no longer true).
- **Source** can be a retro, a closeout, an incident review, or a decision whose result is now known (`D-001`).

### TEAM.md (optional)

Who is who, so owners get matched correctly, and who reports to whom:

```markdown
# Team

## People
| Name | Role | Team | Reports to | Also called |
|---|---|---|---|---|
| Maya Okafor | Project manager, activation team lead | Activation | Elena Brooks | — |
| Sam Lee | Engineer | Activation | Maya Okafor | Sam |
```

Recurring meetings, the team charter, the RACI and the stakeholder map are sections of the same file. Each skill keeps its own section:

```markdown
## Team charter: Activation team

Status: Agreed by the team on 2026-12-01 · Next review: 2027-02-08 · Source: meetings/2026-11-24-working-agreements.md

### Purpose
We get new customers from sign-up to their first invoice.

### What we own
**Ours:** the sign-up flow, activation, the first-invoice experience.
**Not ours:** billing; pricing (finance); the help center (support, told two weeks before the flow changes).

### How we decide
- Small calls: whoever does the work.
- Anything that moves a date or the scope: Maya, who takes it to Elena (PROJECT.md).
- Still stuck after the sync: Maya and Leo decide, and everyone goes with it.

### Working agreements
| Agreement | Since | Decision | Review |
|---|---|---|---|
| First look at a code review within one working day | 2026-11-24 | D-010 | 2027-02-08 |
| Waiting more than two working days on another team: post it in the team channel | 2026-11-24 | D-011 | 2027-02-08 |

### Meetings
| Meeting | When | Length | What for |
|---|---|---|---|
| Weekly sync | Tuesday 10:00 | 30 min | Decisions, blockers, dates from other teams |

### How we know it works
- Reviews get a first look within a day.

### Open questions
- Who is on call during the launch weeks?
```

The `team-charter` skill keeps this section. Every working agreement is also a row in `DECISIONS.md`, so the retro can check it and a change replaces it like any other decision.

```markdown
## RACI

| Work | Maya Okafor | Leo Park | Priya Shah | Elena Brooks | Source |
|---|---|---|---|---|---|
| Rollout dates and steps | R | C | C | A | meetings/2026-10-05-kickoff.md |
| Support macros | I | — | A, R | — | meetings/2026-11-17-weekly-sync.md |

R does the work · A owns the result and signs off, one per row · C is asked before · I is told after.

## Stakeholders

| Person | Role | Interest | Influence | What they need | How and how often | Made by | Source |
|---|---|---|---|---|---|---|---|
| Elena Brooks | VP Product, sponsor | High | High | Date risk early, one page | Status report, weekly, Friday | status-report | meetings/2026-10-05-kickoff.md |
```

`raci-matrix` keeps the RACI section and `stakeholder-map` keeps the Stakeholders section. Other skills read them: the decision log checks who has the A, change control knows whom to ask, and the status report knows who gets which update.

### skip-levels/ (private)

Notes from meetings with the people who report to your direct reports. The `skip-level-meeting` skill keeps them:

- `skip-levels/<first-last>.md`: one running file per person, newest meeting on top. The prep for a meeting is replaced by the write-up: what you asked, what they raised, what you committed to, and what they agreed may be shared.
- `skip-levels/<YYYY-MM>-<lead-first-last>-team.md`: one file per round with a lead's team: the themes (raised by two or more people, written without names), what to take back to the lead, your commitments, and what went into shared records after the lead heard the themes.

Nothing from this folder goes into shared files or to the lead without your yes, and then only as themes without names.
