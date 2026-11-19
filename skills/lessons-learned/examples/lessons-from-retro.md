# Example: lessons from a retro and a launch review, and what came of a decision

**The setup.** The launch is done. The folder still holds the records from launch week: the [decision log](../../../demo/after/DECISIONS.md) with D-001 (the staged launch), the sprint retro from 16 November in `retros/`, and the actions and RAID log as of 20 November. There is no `LESSONS.md` yet. Today the team held a launch review, and the PM attaches [her notes](../../../demo/launch-review-2026-12-18.md).

**Friday 18 Dec. Maya:** Here are my notes from today's launch review. Add the lessons from it and from the sprint retro. And what came of our decision to stage the launch?

---

## What came of D-001, the staged launch

- **It worked.** 10% of new sign-ups got the new onboarding on 1 Dec. Tickets in the first week rose 12%, with no extra shift. On 8 Dec the 10% group was at 38% first invoices within 7 days (31% before), so everyone got it on 15 Dec as planned.
- **Cost:** Northfield Dental and Juniper Studio had to be switched on by hand on 1 Dec.
- **Surprises:** staging also saved the 1 Dec date when billing's price IDs came three days late, because the 10% group stayed on the old prices. But the full rollout (15 Dec) and the new prices (16 Dec) still landed in the same week. Tickets rose 20% that week, mostly pricing questions, and the macros handled most of them.

Sources: your launch review notes, D-001, D-003. The lesson in it is L-001 below.

Nothing to look at again: the decision is carried out. The next check is the 45% target at the end of January, as Elena asked.

## Lessons added

`LESSONS.md` is new, with five lessons from today's review and the 16 Nov sprint retro. They are in the file below.

Left out:
- Pair reviews on risky flows: already a team practice (D-006), with nothing measured to put in «Because».
- Juniper Studio typing in their clients by hand while bulk import moved to January: your notes don't say what we'd do differently. If you know, I'll add it as a lesson.

The folder is behind your notes: A-003, A-006, I-001, DP-001, R-001 and R-002 are still open there, and the 1 Dec and 15 Dec milestones in `PROJECT.md` still say Planned. Want me to bring them up to date?

---

**`LESSONS.md`**

```markdown
# Lessons learned

| ID | When this happens | Do this | Because | Tags | Status | Source |
|---|---|---|---|---|---|---|
| L-001 | A launch lands close to another change that brings support tickets, such as a price change | Roll out to a small share of new sign-ups first, check the numbers on a set date before going to everyone, and have the support macros ready before the other change goes live | At 10%, first-week tickets rose only 12% and first invoices reached 38% against 31%. When the new prices followed a day after the full rollout, tickets rose 20% and the macros handled most of them | launch, support, schedule | Active | D-001; Maya's launch review notes, 2026-12-18 |
| L-002 | A project's dates touch other teams' work (a price change, billing, a legal review) | At kickoff, ask each of those teams for their dates. After that, keep a standing item in the weekly sync for dates and answers needed from other teams | The team learned by accident, three weeks before launch, that the pricing change could land in launch week, and the launch had to be re-planned (D-001) | launch, dependencies, planning | Active | retros/2026-11-16-onboarding-sprint.md; Maya's launch review notes, 2026-12-18 |
| L-003 | Work waits on another team's review or delivery | The day the wait starts, name a person on that team and a date to answer by. If that date is less than a week before yours, plan a way to go ahead without it | The vendor quote sat in legal for three weeks with no date. Billing's price IDs came three days late, and 1 Dec held only because the 10% group stayed on the old prices | vendor, dependencies, schedule | Active | retros/2026-11-16-onboarding-sprint.md; Maya's launch review notes, 2026-12-18 |
| L-004 | A launch changes what customers see | Name an owner for the help center articles at kickoff, with a date before launch to update them by | The need was raised at kickoff, but the articles got an owner five days before launch. Two were out of date on launch day | launch, support, planning | Active | meetings/2026-10-05-kickoff-notes.md; Maya's launch review notes, 2026-12-18 |
| L-005 | A sign-up flow has an SSO path | Run the SSO test cases in the first week of the sprint | SSO QA came late again, and an SSO bug reached staging | launch, quality, planning | Active | retros/2026-11-16-onboarding-sprint.md |
```

---

**What to notice**

- «What came of the decision» answers with numbers and sources, and names what it cost and what surprised people, not just «it worked».
- Every lesson is an action someone can take next time, with no names and no blame. «Sam was slow with legal» became L-003, a rule about any wait on another team.
- Findings with no practice behind them were left out and said so, rather than padded into lessons.
- The skill noticed that other records are stale, and offered to update them instead of editing them on the side.
- The next project's charter and RAID log can pull these lessons back in: L-002 and L-004 are kickoff questions.

[Back to all skills](../../../README.md#the-skills)
