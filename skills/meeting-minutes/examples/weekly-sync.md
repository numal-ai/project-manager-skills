# Example: minutes from a weekly sync transcript

**The setup.** Maya Okafor, a PM, runs the weekly sync for a new onboarding launch. The team: Leo Park (engineering lead), Priya Shah (support lead) and Sam Lee (engineer). Here is the [32-minute transcript](../../../demo/weekly-sync-transcript.md). The folder is empty.

**Tuesday 17 Nov, after the call. Maya:** Write minutes from this transcript.

---

**The minutes:** `meetings/2026-11-17-weekly-sync.md`

```markdown
# Weekly sync - 2026-11-17

**Attendees:** Maya Okafor, Leo Park, Priya Shah, Sam Lee · **Source:** weekly-sync-transcript.md

## Summary
The onboarding launch is now staged: 10% of new sign-ups on 1 Dec, everyone on 15 Dec, so support isn't hit by onboarding and pricing in the same week. Pricing-page timing waits on finance. Two risks to the 1 Dec date: billing price IDs and the vendor quote in legal.

## Decisions
- **D-001 Accepted:** Launch the new onboarding to 10% of new sign-ups on 2026-12-01 and to everyone on 2026-12-15. Decided by Maya, Leo, Priya. Why: avoid both waves of support tickets in pricing week. Revisit 2026-12-08, before going to 100%.
- **D-002 Not accepted:** Move the whole launch to January. Why not: sales already promised December to two accounts.

## Action items
| ID | Action | Owner | Due | Status |
|---|---|---|---|---|
| A-001 | Write the rollout note for support | Priya | 2026-11-19 | Open |
| A-002 | Ask the legal lead for a review date on the vendor quote | Maya | 2026-11-17 | Open |
| A-003 | Get the vendor quote approved by legal | Sam | 2026-11-25 | Blocked (in legal since 2026-11-03) |
| A-004 | Confirm with finance whether new prices show at launch or after | Maya | 2026-11-24 | Open |
| A-005 | Talk to Ana about the billing price IDs | Maya | 2026-11-24 (check) | Open |
| A-006 | Find an owner for the help center articles on the new onboarding | ? | 2026-11-24 (check) | Open |

## Risks and issues
- **Risk:** If billing doesn't ship the new price IDs by 2026-11-27, the 1 Dec launch slips - owner Maya.
- **Issue:** Vendor quote has been in legal review since 2026-11-03 - next step: Maya asks the legal lead today.

## Open questions
- Who updates the help center articles for the new onboarding? - no owner yet ("figure out offline"); tracked as A-006.

## Discussed, no outcome
- Do new prices show on the pricing page at launch or after? - waits on finance (A-004). Leo can't finish the copy without it. Goes on the next agenda.
```

**The recap message,** drafted and not sent:

> Weekly sync, 17 Nov: onboarding goes to 10% of new sign-ups on 1 Dec, everyone on 15 Dec (January was ruled out). Next: Priya - support rollout note by Thu; Maya - legal lead today, finance on pricing timing and Ana on price IDs by next sync; Sam - vendor quote by 25 Nov. Open: who updates help center articles? Minutes: meetings/2026-11-17-weekly-sync.md

The same run started the [decision log](../../../demo/after/DECISIONS.md) and the [action list](../../../demo/after/ACTIONS.md), which every other skill reads.

---

**What to notice**

- January was proposed and turned down. That's recorded as D-002 with the reason, because «why not January?» is the question people ask a month later.
- «Let's figure that out offline» didn't become a fake owner. A-006 has `?` and the help center question stays open.
- Dates the transcript didn't pin down are marked `(check)`, not guessed.
- The pricing-page question had no outcome, so it's listed as such and goes on the next agenda.

Next in the demo project: [a RAID log from the same minutes](../../raid-log/examples/start-from-minutes.md), or [Wednesday's morning brief](../../morning-brief/examples/launch-week-brief.md).
