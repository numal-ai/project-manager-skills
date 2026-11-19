# Example: a change request from Sales, then the decision

**The setup.** It's Friday of launch week. The folder has the [charter](../../project-charter/examples/charter-from-kickoff.md) in `PROJECT.md`: bulk import is on the «Out» list, and Elena Brooks approves changes to scope and dates. It also has the decision log with D-001 (10% of new sign-ups on 1 Dec, everyone on 15 Dec), the RAID log and the Friday status report. Last night the sales lead sent the PM [an email](../../../demo/sales-request-2026-11-19.md) with two asks. No tracker is connected.

## 1. Write the change request

**Friday 20 Nov, morning. Maya:** Marco sent this last night. Write a change request.

---

I logged Marco's email as two change requests in `CHANGES.md`, both Pending and both for Elena to decide (PROJECT.md: she approves scope and date changes). They are two different asks with very different costs, so each gets its own row.

**CR-001 Promised accounts on 1 December.** Northfield Dental and Juniper Studio get the new onboarding from 1 Dec, switched on by hand, instead of depending on the 10% sample.
- It's a change because it bends D-001 and turns a sales promise into part of the plan. No new feature, and no milestone moves as far as anyone has said.
- The catch: both accounts sign up in the first week of December, after 1 Dec, so the switch has to work for accounts that don't exist yet. How, and how long it takes, is Leo's to say (check).
- Options: switch them on as asked; ask them to sign up from 15 Dec, when everyone gets it; or keep the sample as it is and likely miss the promise.

**CR-002 Bulk import on 1 December.** Bulk import is on the charter's «Out» list, and Elena said «Import is out» at kickoff.
- «Maybe a week of work» is Leo in passing, through Marco, so I kept it as (check). There are 6 working days before 1 Dec, and QA finished yesterday: a week of build leaves no time to test it.
- Options: build it for 1 Dec, which puts the date at risk; load the two accounts' client lists for them once, with no import feature (needs Leo's estimate); or defer it to after 15 Dec.

Before Elena decides, two answers from Leo are missing: how to switch on accounts that sign up after 1 Dec, and what a one-off load of their client lists would take.

Next step, your pick:
- Your Friday update to Elena says «Nothing needed this week». I can put these two decisions there instead.
- Or I draft a short note to Elena with both requests. Nothing is sent until you say yes to the text.

The 24 Nov sync agenda is not the place for them: Elena isn't in that meeting.

---

## 2. Record the decision

**Maya:** Elena looked at it this afternoon. The two accounts get switched on by hand on December 1. Bulk import moves to January. Record it.

---

Recorded Elena's call in `CHANGES.md` and `DECISIONS.md`:
- **CR-001 Approved** as asked: D-007. D-001 stays as it is: 10% on 1 Dec, everyone on 15 Dec.
- **CR-002 Deferred** to January 2027, no day set: D-008. Bulk import is not in the 1 Dec release.

Did Elena give a reason for either call? The Why cells in D-007 and D-008 stay empty until you tell me.

The plan needs these updates. One yes covers all of them:

`PROJECT.md`
1. The 1 Dec milestone becomes «10% of new sign-ups, plus Northfield Dental and Juniper Studio switched on by hand», source D-001, D-007.
2. «Out» list: «bulk import for existing accounts (moved to January 2027, CR-002)».
3. New open question: bulk import in January, in this project or a new one, who builds it, and on what date? Ask Elena.
4. Change history: one line each for D-007 and D-008.

`ACTIONS.md`
5. A-010: switch both accounts on by hand for 1 Dec, in a way that works for accounts that sign up after 1 Dec; get their sign-up emails from Marco. Owner Leo (check), due 30 Nov (check).

`RAID.md`
6. New R-003: if the hand switch doesn't work for accounts that sign up after 1 Dec, both land on the old flow and the December promise is missed. Impact High, likelihood Med (both check), owner Leo (check), mitigation A-010.

No tracker is connected, so nothing changes there.

Make these 6 updates?

**Maya:** Yes.

Done. Who should hear about it:
- **Leo:** A-010 is new work before 1 Dec, and only he can say how to switch on accounts that don't exist yet.
- **Priya:** two named accounts on the new flow in week one.
- **Marco:** the hand switch on 1 Dec is confirmed, and bulk import moves to January, so he has to tell both accounts. He also needs to send Leo their sign-up emails.

I can draft a message to each of them. Nothing goes out unless you say yes to the text.

---

**`CHANGES.md`** (the CR-001 section is left out here; it has the same headings)

```markdown
# Change log

| ID | Raised | Change | Asked by | Impact | Status | Decided by | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| CR-001 | 2026-11-19 | Give Northfield Dental and Juniper Studio, the two accounts Sales promised December, the new onboarding from 2026-12-01, switched on by hand instead of depending on the 10% sample | Marco Diaz | No milestone moves, as far as anyone has said; the switch must work for accounts that sign up after 2026-12-01 (check with Leo) | Approved | Elena Brooks | D-007 | Marco's email, 2026-11-19 |
| CR-002 | 2026-11-19 | Add bulk import of existing clients to the 2026-12-01 release, for Northfield Dental and Juniper Studio (about 400 clients each) | Marco Diaz | Deferred to January 2027 (check). As asked: moves bulk import from Out to In; about a week of work (check) plus QA with 6 working days left; puts 2026-12-01 at risk | Deferred | Elena Brooks | D-008 | Marco's email, 2026-11-19 |

## CR-002 Bulk import on 1 December

**What changes:** bulk import of existing clients moves from the charter's «Out» list to «In» for the 2026-12-01 release.
**Why it was asked:** the two accounts won't type in about 400 clients each by hand (Marco's email).
**If we don't change:** both accounts start in December without their clients loaded.
**Impact:**
- Scope: «bulk import» moves from Out to In (PROJECT.md). Elena kept it out at kickoff (meetings/2026-10-05-kickoff-notes.md).
- Dates: «maybe a week of work» is Leo in passing, via Marco (check with Leo). QA finished 2026-11-19; 6 working days remain before 2026-12-01, so there is no time to test it.
- Money: none named.
- People: Leo's engineers and the QA contractor; most likely at the cost of the pricing-page work (check with Leo).
- Risks: import code lands after QA, days before launch, for the two accounts Sales cares most about.
- Earlier decisions: changes the charter's «Out» list, agreed by Elena on 2026-10-07.
**Options:**
1. Accept as asked: build it for 2026-12-01. Costs: about a week plus QA (check); puts the date at risk.
2. Accept in part: load the two accounts' client lists once, from a file they send; no feature. Costs: needs an estimate from Leo (check).
3. Defer to after 2026-12-15. Costs: both accounts start without their clients loaded; Marco tells them.
**Who decides:** Elena Brooks (approves changes to scope, dates and budget, PROJECT.md)
**Decision:** Deferred by Elena Brooks on 2026-11-20, option 3: January 2027, no day set (D-008).
```

---

**What to notice**

- One email, two asks, two rows. They had very different costs, and Elena decided them differently.
- The estimate heard in passing («maybe a week») stayed `(check)` with the name of who can confirm it. No days were made up.
- The skill priced the change and laid out options. It never chose: Elena did, and her call became decision rows anyone can find later.
- After the decision, every update the plan needed came as one list with one yes, including the deferred import on the «Out» list.
- The next status report, agenda and brief will pick up `CHANGES.md` without being told.

Next in the demo project: [a RACI built from the same folder](../../raci-matrix/examples/raci-from-records.md).
