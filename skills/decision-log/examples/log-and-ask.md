# Example: log a decision, then ask the log questions

**The setup.** The folder has the [decision log](../../../demo/after/DECISIONS.md) from Tuesday's weekly sync, with D-001 (staged launch) and D-002 (January turned down). On Thursday the PM met finance and wrote it in [her notes](../../../demo/updates-2026-11-20.md).

## 1. Log a decision

**Friday 20 Nov. Maya:** Log the pricing-page decision from my notes.

---

Logged as **D-003** in `DECISIONS.md`:

> **D-003 Accepted (2026-11-19):** Put the new prices on the pricing page only after the new onboarding reaches 100% of new sign-ups, so not before 2026-12-15. Decided by you and Dana Ruiz (finance lead). Why: one change at a time for support. No revisit date. Source: your notes, 2026-11-20.

Nothing is replaced: the 17 Nov sync parked this question without an outcome, so there was no earlier decision on it. It answers your finance action (A-004) and unblocks Leo's pricing-page copy. I haven't touched `ACTIONS.md`.

One link to keep in mind: D-003 waits on D-001's 100% date. If the 2026-12-08 revisit holds back the full rollout, the new prices wait too.

---

## 2. Ask why

**Maya:** Why did we pick a staged launch?

---

**D-001**, decided 2026-11-17 by you, Leo and Priya (`meetings/2026-11-17-weekly-sync.md`): the new onboarding goes to 10% of new sign-ups on 2026-12-01 and to everyone on 2026-12-15.

**Why:** to avoid both waves of support tickets in pricing week. Launching to everyone on 1 Dec, the week the pricing change lands, would have hit support with onboarding and pricing tickets at once.

**Considered and turned down:** moving the whole launch to January (D-002, not accepted). Sales had already promised December to two accounts.

**Revisit:** 2026-12-08, a look at the numbers before going to 100%.

Since then, D-003 (19 Nov) keeps the new prices off the pricing page until onboarding is at 100%, for the same reason: one change at a time for support.

---

## 3. Ask what's due

**Maya:** Which decisions are due for a revisit?

---

**None right now.** No revisit date has passed or falls in the next 7 days (through 2026-11-27).

The next one is **D-001** (staged launch) on **2026-12-08**: check the numbers before going to 100%. D-003 (pricing page) moves with it, because the new prices wait for 100%.

One more thing: D-003 has no follow-up on the action list. Nobody is down for finishing the pricing-page copy or for putting the new prices live after 15 Dec.

---

**The file:** `DECISIONS.md`

```markdown
# Decision log

| ID | Date | Decision | Status | Decided by | Why | Revisit | Source |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-11-17 | Launch the new onboarding to 10% of new sign-ups on 2026-12-01 and to everyone on 2026-12-15 | Accepted | Maya, Leo, Priya | Avoid both waves of support tickets in pricing week | 2026-12-08 | meetings/2026-11-17-weekly-sync.md |
| D-002 | 2026-11-17 | Move the whole launch to January | Not accepted | Maya | Sales already promised December to two accounts | — | meetings/2026-11-17-weekly-sync.md |
| D-003 | 2026-11-19 | Put the new prices on the pricing page only after the new onboarding reaches 100% of new sign-ups, so not before 2026-12-15 | Accepted | Maya, Dana Ruiz (finance lead) | One change at a time for support | — | Maya's notes, 2026-11-20 |
```

---

**What to notice**

- The decision is dated the day it was made (19 Nov), not the day it was logged.
- «Why did we…?» comes back with the source, the reason, and what was turned down. The turned-down option is often the most useful part.
- The log noticed that D-003 depends on D-001's date, and that nobody owns its follow-up.

Next in the demo project: [the action list, updated from the same notes](../../action-items/examples/friday-update.md).
