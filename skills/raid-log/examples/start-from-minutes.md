# Example: start a RAID log from meeting minutes

**The setup.** Tuesday's weekly sync for a new onboarding launch left [minutes](../../meeting-minutes/examples/weekly-sync.md), a [decision log](../../../demo/after/DECISIONS.md) and an [action list](../../../demo/after/ACTIONS.md) in the folder. The [transcript](../../../demo/weekly-sync-transcript.md) is there too. There is no RAID log yet.

**Tuesday 17 Nov, evening. Maya:** Start a RAID log for the onboarding launch from today's weekly sync.

---

Started `RAID.md` for the onboarding launch from today's sync (`meetings/2026-11-17-weekly-sync.md`). Six rows:

**Risks**
- **R-001** If onboarding goes to everyone in the week the pricing change lands, support gets both waves of tickets at once. Impact High, likelihood Low now that the launch is staged (D-001). Watching: the 2026-12-08 check before 100% is the mitigation. **Unowned.**
- **R-002** If nobody owns the help center articles, they are out of date when the new onboarding launches on 1 Dec. Med / Med. Mitigation: find an owner (A-006). **Unowned.**

**Issue**
- **I-001** Vendor quote stuck in legal since 2026-11-03. Owner Sam. Next step: you ask the legal lead for a review date today (A-002). Impact Med (check): the minutes' summary calls it a risk to the 1 Dec date, but nobody in the call said what the quote holds up.

**Dependencies**
- **DP-001** Billing (Ana) ships the new price IDs by 2026-11-27, or the 1 Dec launch is at risk. Owner: you. This is the item closest to the launch date.
- **DP-002** Finance says whether new prices show on the pricing page at launch or after. Leo can't finish the copy without it. Needed by 2026-11-24 (check): that's when you said you'd bring the answer, not a date Leo gave.

**Assumption**
- **AS-001** QA on the new onboarding finishes on Thursday 2026-11-19 (Leo). Owner Leo, check that day.

The billing IDs are logged once, as a dependency, not again as a risk. Impact and likelihood are my first read, so correct any you score differently.

**One question:** who owns R-001 and R-002? Priya would fit R-001, since it's her queue. R-002 can stay unowned until A-006 finds someone for the articles. And for I-001: what does the vendor quote hold up? If it blocks the 1 Dec launch, its impact goes to High.

---

**The file:** `RAID.md`

```markdown
# RAID log - New onboarding launch
Last reviewed: 2026-11-17

## Risks
| ID | Risk | Impact | Likelihood | Owner | Mitigation | Status | Raised | Source |
|---|---|---|---|---|---|---|---|---|
| R-001 | If onboarding goes to everyone in the week the pricing change lands, support gets both waves of tickets at once | High | Low | ? | Staged launch (D-001): 10% of new sign-ups on 2026-12-01, everyone on 2026-12-15; numbers checked on 2026-12-08 before going to 100% | Watching | 2026-11-17 | meetings/2026-11-17-weekly-sync.md |
| R-002 | If nobody owns the help center articles for the new onboarding, they are out of date when it launches on 2026-12-01 | Med | Med | ? | Find an owner for the articles (A-006, by 2026-11-24 (check)) | Open | 2026-11-17 | meetings/2026-11-17-weekly-sync.md |

## Assumptions
| ID | Assumption | Owner | Check by | Status | Source |
|---|---|---|---|---|---|
| AS-001 | QA on the new onboarding finishes on 2026-11-19 | Leo | 2026-11-19 | Open | weekly-sync-transcript.md |

## Issues
| ID | Issue | Impact | Owner | Next step | Status | Raised | Source |
|---|---|---|---|---|---|---|---|
| I-001 | Vendor quote stuck in legal review since 2026-11-03 | Med (check) | Sam | Maya asks the legal lead for a review date on 2026-11-17 (A-002); Sam keeps 2026-11-25 as the date (A-003) | Open | 2026-11-17 | meetings/2026-11-17-weekly-sync.md |

## Dependencies
| ID | Dependency | On whom | Needed by | Owner | Status | Source |
|---|---|---|---|---|---|---|
| DP-001 | Billing ships the new price IDs; without them the 2026-12-01 launch is at risk | Billing (Ana) | 2026-11-27 | Maya | Open | meetings/2026-11-17-weekly-sync.md |
| DP-002 | Finance says whether the new prices show on the pricing page at launch or after; Leo can't finish the pricing-page copy without it | Finance | 2026-11-24 (check) | Maya | Open | meetings/2026-11-17-weekly-sync.md |
```

---

**What to notice**

- Six real rows, not fifteen generic ones. Each traces back to something said in the call.
- The mitigation for R-001 is a decision with a date (the staged launch), not «monitor closely».
- An impact nobody stated is marked `(check)` and asked about, not guessed.
- Rows nobody owns say `?`, and the owners go into one grouped question.

Next in the demo project: [Friday, logging a decision from notes](../../decision-log/examples/log-and-ask.md).
