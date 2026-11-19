# Example: a stakeholder map and communication plan, then «who needs to hear?»

**The setup.** Friday of launch week. The folder has the [charter](../../project-charter/examples/charter-from-kickoff.md), the decision log, the action list, the RAID log, the minutes, the kickoff transcript and the Friday status report. There is no `TEAM.md`. The PM's own [notes from the week](../../../demo/updates-2026-11-20.md) and [calendar](../../../demo/calendar-2026-11-18.md) are outside the folder.

## 1. Map the stakeholders

**Friday 20 Nov. Maya:** Who are the stakeholders for the onboarding launch? Make a communication plan too.

---

Here's the stakeholder map with the communication plan under it, saved to `TEAM.md`. Interest and influence are my drafts, marked (check): those calls are yours.

**Gaps**
- **No update to Marco is on file since kickoff.** On 5 Oct he asked to be kept posted on the date, because he promised December to two accounts. That promise is why January was ruled out (D-002). Nothing on file says whether his two accounts are in the 10% on 1 Dec.
- **Elena and D-001.** The charter says date changes go to Elena. D-001 moved «everyone» from 1 Dec to 15 Dec, and the log doesn't name her. If she hasn't heard it from you yet, today's report is where she'd first read it.
- **Who already gets updates isn't on file.** The one report in `reports/` doesn't say who it went to.
- **Dana's pricing date now follows ours (D-003),** and she isn't on any regular update. I've put her on the stakeholder version of the Friday report.

I can also draft today's stakeholder version of the report for Marco and Dana.

---

## 2. Who needs to hear

**Maya:** Billing just told me the price IDs may come on the 30th, not the 27th. Who needs to hear about this?

---

One correction first: billing had planned the IDs for Thu 26 Nov, and Fri 27 Nov is the date we need them by (DP-001). So Mon 30 Nov would be three days past our date and the day before the 1 Dec launch.

Whether 1 Dec moves depends on one answer from Leo: does the 10% launch still need the new price IDs, now that the new prices don't go live before 15 Dec (D-003)?

**Tell now**
1. **Leo**, with Priya and Sam seeing it: he needs to answer the question above, and if the launch does need the IDs, say the latest date that still holds 1 Dec. Quickest: a post in the team channel today.
2. **Elena**: she approves date changes. She needs to know that 1 Dec may be at risk, and that you'll know once Leo answers. Quickest: today's status report, if it hasn't gone out yet. Its «Green, one day of margin» line is now out of date.

**Tell only if 1 Dec moves**
3. **Marco**: his two accounts were promised December. Everyone still gets the new onboarding on 15 Dec, so the promise holds unless that date moves too.
4. **Priya**: the rollout note she sent support says 1 Dec.
5. **Dana**: only if 15 Dec moves, since her pricing page follows it.

**Ask, not tell: Ana.** Is 30 Nov firm or a maybe, and can the IDs come any sooner?

Drafts, not sent:

> **Team channel:** @Leo Billing says the new price IDs may come on Mon 30 Nov instead of Thu 26 Nov. We need them by 27 Nov for the 1 Dec launch (DP-001). Does the 10% launch on 1 Dec still need the new price IDs, now that the new prices don't go live before 15 Dec (D-003)? If yes, what's the latest date that still holds 1 Dec? An answer before Tuesday's sync would help.

> **To Elena:** Heads-up: billing says the new price IDs may come on 30 Nov, not 26 Nov. We need them by 27 Nov, so the 1 Dec launch to 10% of new sign-ups may be at risk. Leo is checking whether the launch still needs them, since the new prices wait until after 15 Dec. I'll know by Tuesday. If 1 Dec has to move, I'll bring it to you before anything changes. Nothing needed from you now.

Nothing goes out until you say yes to the text.

---

**`TEAM.md`**

```markdown
# Team

## Stakeholders

| Person | Role | Interest | Influence | What they need | How and how often | Made by | Source |
|---|---|---|---|---|---|---|---|
| Elena Brooks | VP Product, sponsor; approves changes to scope, dates and budget | High (check) | High (check) | A one-page update on Fridays; any change to scope or the date comes to her | Status report, weekly, Friday; a personal note before any date or scope change is final | status-report, executive version; note from Maya | meetings/2026-10-05-kickoff-notes.md; PROJECT.md |
| Marco Diaz | Sales lead | High (check) | Med (check) | When the two accounts promised December get the new onboarding; word on any date change | Status report, weekly, Friday, plus a note on any date change | status-report, stakeholder version; note from Maya | meetings/2026-10-05-kickoff-notes.md; D-002 |
| Dana Ruiz | Finance lead; owns the pricing change | High (check) | Med (check) | The date the new onboarding reaches everyone: the new prices follow it (D-003) | Status report, weekly, Friday, plus a note if 15 Dec moves | status-report, stakeholder version; note from Maya | D-003; Maya's notes, 2026-11-20 |
| Leo Park | Engineering lead | High (check) | High (check) | The new price IDs a few days before launch; other teams' dates and answers early (D-004) | Weekly sync, Tuesday 10:00, and the recap after it | meeting-minutes recap | meetings/2026-10-05-kickoff-notes.md; retros/2026-11-16-onboarding-sprint.md |
| Priya Shah | Support lead | High (check) | Med (check) | The flow two weeks before launch; an owner for the help center articles; not two waves of tickets in one week (D-001) | Weekly sync, Tuesday 10:00, and the recap after it | meeting-minutes recap | meetings/2026-10-05-kickoff-notes.md; meetings/2026-11-17-weekly-sync.md |
| Sam Lee | Engineer; owns the vendor quote approval | Med (check) | Low (check) | A legal review date and a named legal contact (A-003, A-008) | Weekly sync, Tuesday 10:00, and the recap after it | meeting-minutes recap | meetings/2026-11-17-weekly-sync.md |
| Ana | Billing; ships the new price IDs | Low (check) | High (check) | The date we need the IDs (27 Nov) and early word if it changes | A personal note only when that date changes | note from Maya | RAID.md DP-001; Maya's notes, 2026-11-20 |
| Nina Shaw | Legal lead; reviews the vendor quote | Low (check) | High (check) | The date approval is needed (25 Nov) | Through Sam until approval; a note only if the date changes | Sam; note from Maya | A-003, A-008; Maya's notes, 2026-11-20 |

### Communication plan
- **Weekly, Tuesday 10:00:** weekly sync with Leo, Priya and Sam, with the standing item «dates and answers we need from other teams» (D-004).
- **After each weekly sync:** recap in the team channel (meeting-minutes). This is the team's written weekly update.
- **Weekly, Friday:** status report. Executive version → Elena. Stakeholder version → Marco, Dana.
- **At milestones:** before 1 Dec, Marco hears whether his two accounts are in; before the 8 Dec numbers check, Elena sees the numbers, and Marco and Dana hear the outcome the same day; on 15 Dec, Dana hears the pricing page can follow.
- **On a date or scope change:** a personal note from Maya before the next report. Elena first, before it is final; then Marco, Dana (if 15 Dec moves) and Priya.
- **Other teams:** Ana and Nina hear from us only when the date we need moves.
```

---

**What to notice**

- Interest and influence go in as drafts marked `(check)`. People are described by what they said and asked for, with sources, never by labels. Leo's remark at kickoff that Ana's team is «slammed» stayed out of her row: she might read it.
- The plan reuses updates that already exist (the Friday report, the sync recap) instead of adding channels.
- The gaps are facts with sources: Marco asked to be kept posted and has heard nothing on file.
- «Who needs to hear?» separated news that may not happen: who to tell now, who only if the date really moves, and whom to ask instead of tell.
- The messages are drafted in the reply, and nothing is sent without a yes.

Next in the demo project: [the Tuesday after, a how-we-work talk becomes the team charter](../../team-charter/examples/charter-from-session.md).
