# Example: update the action list from the week's notes

**The setup.** Tuesday's weekly sync left six items in the [action list](../../../demo/after/ACTIONS.md). By Friday, the PM has [notes on what changed](../../../demo/updates-2026-11-20.md). No tracker or chat is connected.

**Friday 20 Nov. Maya:** Update the action list from my notes, tell me what's overdue, and draft the follow-ups.

---

Updated `ACTIONS.md` from your notes:

- **A-001** Write the rollout note for support (Priya): **Done**, sent 19 Nov.
- **A-002** Ask the legal lead for a review date (you): **Done**. Nina Shaw says legal reviews the quote on Tue 24 Nov.
- **A-003** Get the vendor quote approved (Sam): still **Blocked** on legal, now with the review date in the row. Due date stays 25 Nov.
- **A-004** Confirm price timing with finance (you): **Done** 19 Nov. The answer is logged as D-003.
- **A-005** Talk to Ana about the price IDs (you): **Done**. Billing plans the IDs for Thu 26 Nov.
- **A-006** Find an owner for the help center articles: no change, still nobody.

## What's due

**Nothing is overdue.** A-001 and A-002 had passed their dates, and both are done.

- **Sam:** A-003, blocked on legal (review Tue 24 Nov), due Wed 25 Nov.
- **No owner:** A-006, find someone for the help center articles, due Tue 24 Nov (check).
- **You, Priya, Leo:** nothing open.

**1 open, 0 overdue, 1 blocked**, 4 done since Tuesday.

## Follow-ups

None needed: nobody has an overdue item. One heads-up, since your notes have news Sam may not have heard yet:

```
Hi Sam - news on the vendor quote: Nina Shaw says legal will review it on Tue 24 Nov, the day before your 25 Nov date. If their review moves things, just tell me and I'll update the list.
```

No chat tool is connected, so nothing was sent. Copy it if you want it.

## One question

- **A-006:** who should own finding someone for the help center articles? It's due at Tuesday's sync and still has no owner.
- **New item?** Your notes say Leo can finish the pricing-page copy now. Should I add «Finish the pricing-page copy» for Leo, and by when?

Not for this list: billing's 26 Nov date (one day before the 27 Nov need) and QA finishing belong in `RAID.md` (DP-001, AS-001). Say if you want the RAID log updated too.

---

**The file:** `ACTIONS.md`

```markdown
# Action items

| ID | Action | Owner | Due | Status | Source | Tracker |
|---|---|---|---|---|---|---|
| A-001 | Write the rollout note for support (done 2026-11-19, Maya's notes) | Priya | 2026-11-19 | Done | meetings/2026-11-17-weekly-sync.md | — |
| A-002 | Ask the legal lead for a review date on the vendor quote (done 2026-11-17, Maya's notes: review set for 2026-11-24) | Maya | 2026-11-17 | Done | meetings/2026-11-17-weekly-sync.md | — |
| A-003 | Get the vendor quote approved by legal (blocked on legal: review set for 2026-11-24, Maya's notes) | Sam | 2026-11-25 | Blocked | meetings/2026-11-17-weekly-sync.md | — |
| A-004 | Confirm with finance whether new prices show at launch or after (done 2026-11-19, answer in D-003) | Maya | 2026-11-24 | Done | meetings/2026-11-17-weekly-sync.md | — |
| A-005 | Talk to Ana about the billing price IDs (done 2026-11-20, Maya's notes: IDs planned for 2026-11-26) | Maya | 2026-11-24 (check) | Done | meetings/2026-11-17-weekly-sync.md | — |
| A-006 | Find an owner for the help center articles on the new onboarding | ? | 2026-11-24 (check) | Open | meetings/2026-11-17-weekly-sync.md | — |
```

---

**What to notice**

- Rows changed status. None were deleted, and each says when and where the news came from.
- «Leo can finish the copy now» is news, not a promise, so it became a question, not a new row.
- Nothing was overdue, so there was nobody to chase. The one draft is news Sam may not have, and it wasn't sent.
- Dates and dependencies went to the RAID log, not the action list.

Next in the demo project: [the Friday status report](../../status-report/examples/friday-status.md).
