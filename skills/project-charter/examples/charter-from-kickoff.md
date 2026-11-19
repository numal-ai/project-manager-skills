# Example: a project charter from the kickoff

**The setup.** The folder is empty: the project starts today. The PM attaches the [kickoff transcript](../../../demo/kickoff-notes-2026-10-05.md). The VP of Product, the PM, the engineering, support and sales leads were in the room.

**Monday 5 Oct, evening. Maya:** Here's the transcript from today's kickoff. Write the project charter.

---

I wrote the charter from the kickoff transcript and saved it as `PROJECT.md`, status Draft. Four things weren't settled in the room, so they are open questions at the bottom, three of them for Elena.

I also started the records the rest of the project will use. Owners marked `?` and dates marked (check) stay open until you tell me who or when:

`RAID.md`
- R-001 If support gets the flow later than 2026-11-17 (two weeks before launch), the macros aren't ready for 1 December. Impact Med, likelihood Med. Owner `?`.
- R-002 If the launch slips past December, Sales breaks the promise Marco made to two accounts. Impact High, likelihood Med. Owner: you.
- AS-001 Design is final this week, so code complete holds on 2026-11-13 (Leo's condition). Check by 2026-10-09. Owner `?`.
- DP-001 Billing (Ana) ships the new price IDs a few days before launch (check the exact date). Owner `?`.
- DP-002 Legal approves the vendor contract for the checklist tool. Legal hasn't seen it yet. Needed by (check). Owner `?`.

`DECISIONS.md`
- D-001 Not accepted: add bulk import to this project. Decided by Elena. No reason was given, so Why stays empty.
- D-002 Accepted: launch on 2026-12-01. Decided by Elena and you.
- D-003 Accepted: no new hires; QA is paid from the contractor budget you already have. Decided by Elena.

`ACTIONS.md`
- A-001 Priya: draft the support plan, by 2026-10-20.
- A-002 Leo: estimate QA properly, by Friday 2026-10-09.
- A-003 Elena: find out how finance counts trials for the 45% target. Due (check).
- A-004 Elena: find out how much is left in the contractor budget. Due (check).
- A-005 You: send the charter to Elena, by Wednesday 2026-10-07.
- A-006 You: a one-page update to Elena every Friday, the first on 2026-10-09.

Tell me if any of these is wrong and I'll fix it.

**Note to Elena** (draft, not sent):

> Hi Elena,
>
> Here is the draft charter for the new onboarding, from today's kickoff. It has what we agreed: new customers sending a first invoice in their first week, from about 31% to 45% by the end of January; launch on 1 December; bulk import, the mobile app and pricing out; and any change to the scope or the launch date comes to you.
>
> Three things I need from you before it's final:
> 1. Does the 45% count trial sign-ups, or paying customers only?
> 2. How much is left in the contractor budget for QA?
> 3. If QA needs more than that, who approves it?
>
> If the rest looks right, a short reply is enough and I'll mark the charter agreed.
>
> Maya

Send this to Elena as written?

---

**`PROJECT.md`**

```markdown
# Project charter: New onboarding

Status: Draft · Updated: 2026-10-05 · Source: Kickoff transcript, 2026-10-05

## Goal
More new customers send their first invoice in their first week after signing up.

## Success measures
| Measure | Now | Target | By | Source |
|---|---|---|---|---|
| New customers who send a first invoice in their first week | about 31% | 45% | 2027-01-31 | Kickoff transcript, 2026-10-05 |

## Scope
**In:** the new sign-up flow, the template picker for the first invoice, what support needs for it: macros and the help center.
**Out:** bulk import (D-001), the mobile app, pricing (finance's project).

## Milestones
| Milestone | Date | Status | Source |
|---|---|---|---|
| Code complete | 2026-11-13 | Planned | Leo Park, if design is final this week (AS-001) |
| QA done | (check) | Planned | «A week or so» after code complete; Leo estimates by 2026-10-09 (A-002) |
| Launch | 2026-12-01 | Planned | D-002 |

## Who decides
Sponsor: Elena Brooks (VP Product). Approves changes to scope and the launch date: Elena Brooks. Approves budget changes: not said (check). Runs the project: Maya Okafor.

## Budget frame
No new hires; QA is paid from the contractor budget the team already has (D-003). How much is left in it: not named (check).

## Open questions
- Does the 45% target count trial sign-ups, or paying customers only? Ask Elena Brooks.
- How much is left in the contractor budget for QA? Ask Elena Brooks.
- Who approves budget changes if QA needs more than what is left? Ask Elena Brooks.
- Who owns the help center articles? Priya Shah raised it and nobody took it. Settle at the next Tuesday sync.

## Change history
- (none yet)
```

---

**What to notice**

- Every number and date is the speakers' own. «A week or so» of QA stayed vague and became an action for Leo, not a made-up date.
- What the room didn't settle is a question with a name next to it, not a guess. Nobody said who approves budget changes, so the charter says so.
- The «Out» list carries the argument from the room: bulk import was asked for and turned down, and that is now a decision row anyone can find.
- The kickoff seeded the RAID log, the decision log and the action list in the same run, so the next skill has something to read.
- Writing to the folder needed no question. The only yes asked for is the one that reaches another person: the note to the sponsor.

Next in the demo project: [six weeks later, the sprint retro](../../retrospective/examples/sprint-retro.md).
