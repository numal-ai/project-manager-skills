# Example: a RACI built from the folder, then «who decides…?»

**The setup.** Friday of launch week. The folder has the [charter](../../project-charter/examples/charter-from-kickoff.md) in `PROJECT.md`, the decision log, the action list, the RAID log, the minutes, the kickoff transcript and the sprint retro. There is no `TEAM.md`, so nobody has written down who is who.

## 1. Build the RACI

**Friday 20 Nov. Maya:** Build a RACI for the onboarding launch.

---

Here's the RACI for the onboarding launch, saved to `TEAM.md`. There was no team list, so the people come from the kickoff, the 17 Nov sync, the retro and D-003.

**What the checks found**
- **Three rows have no A:** help center articles, pricing-page copy and the vendor contract. They are marked «(no A yet)». Help center articles have no R either, so nobody is doing them (A-006, R-002).
- **The log and the charter disagree on dates.** The charter says date changes go to Elena. D-001 moved «everyone» from 1 Dec to 15 Dec, and the log says you, Leo and Priya decided it. Elena isn't named. I kept Elena as the A because the charter names her.
- **D-003 has two deciders,** you and Dana. Pricing is finance's project, so Dana gets the A (check) and you the R.
- Nobody holds most of the As. No row has four or more Cs, and everyone on the team has a letter. You do the work on 6 of the 10 rows, mostly chasing other teams.

**Questions**
1. Did Elena sign off D-001? If not, does she confirm it now, or should the RACI make you the A for rollout steps? Moving the A would also go in `DECISIONS.md`.
2. Who updates the help center articles, and who signs them off? It's item 1 on the 24 Nov agenda.
3. Who signs off the pricing-page copy before it goes live: Leo, you or Dana?
4. Who signs the checklist-tool vendor contract once legal clears it: Sam, you or Elena?
5. On when the new prices show: is Dana the A with you as R, or is it your call?

Until you answer, these stay in the file as `(check)` cells and «(no A yet)» rows.

---

## 2. Ask who decides

**Maya:** Who decides whether the new prices show on the pricing page at launch?

---

Dana Ruiz (finance lead) has the last word: she is the A on «When new prices show on the pricing page», and you're the R. Her A is still `(check)`, because D-003 lists you both.

It's already decided. Under D-003 (19 Nov), the new prices go on the pricing page only after the new onboarding reaches 100% of new sign-ups, so not before 15 Dec.

- **Ask first (C):** nobody is listed.
- **Tell after (I):** Leo, who needs the answer for the pricing-page copy, and Elena (check).

To change it, start with Dana. A change would reopen D-003.

---

**`TEAM.md`**

```markdown
# Team

## RACI

| Work | Maya Okafor | Leo Park | Priya Shah | Sam Lee | Elena Brooks | Dana Ruiz | Marco Diaz | Source |
|---|---|---|---|---|---|---|---|---|
| Scope and budget | R | — | — | — | A | — | — | PROJECT.md, meetings/2026-10-05-kickoff-notes.md |
| Launch dates and rollout steps | R | C | C | — | A | — | I | PROJECT.md, D-001, D-002 |
| Build and QA: sign-up flow, template picker, SSO tests | — | A, R (check) | — | — | — | — | — | meetings/2026-10-05-kickoff-notes.md, A-009, D-005 |
| Support readiness: support plan, macros, rollout note | — | — | A, R (check) | — | — | — | — | meetings/2026-10-05-kickoff-notes.md, A-001 |
| Help center articles (no A yet) | — | — | C (check) | — | — | — | — | A-006, meetings/2026-11-24-weekly-sync-agenda.md |
| When new prices show on the pricing page | R | I | — | — | I (check) | A (check) | — | D-003, A-004 |
| Pricing-page copy (no A yet) | — | R | — | — | — | — | — | meetings/2026-11-17-weekly-sync.md |
| Billing price IDs from Ana's team | A, R (check) | C (check) | — | — | — | — | — | A-005, RAID.md DP-001 |
| Vendor contract for the checklist tool (no A yet) | R | — | — | R | — | — | — | A-002, A-003, A-008 |
| Running the project: weekly sync, decision log, Friday status | A, R | C (check) | C (check) | C (check) | I | — | — | PROJECT.md, A-007, D-004 |

R does the work · A owns the result and signs off, one per row · C is asked before · I is told after.
```

---

**What to notice**

- Every letter traces back to the record: who owns the actions, who made the decisions, who the charter names. Guesses are marked `(check)`.
- The gaps went into the file, not only into the chat: three rows say «(no A yet)».
- Where the decision log and the charter disagree, the skill kept the charter's A and asked, rather than quietly picking one.
- «Who decides?» came back with the A, the decision already made, and who to start with if it needs to change.

Next in the demo project: [the stakeholder map and communication plan](../../stakeholder-map/examples/communication-plan.md).
