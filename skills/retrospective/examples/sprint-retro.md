# Example: a sprint retro, from plan to write-up

**The setup.** The onboarding team's two-week sprint ended on Fri 13 Nov. The PM has [her notes for the retro](../../../demo/retro-notes-2026-11-16.md): a few facts and five anonymous notes from the team board. This example starts in an empty folder.

## 1. Before the retro

**Monday 16 Nov, 09:00. Maya:** Plan our sprint retro for today at 14:00, 45 min. Here are the notes.

---

**Retro plan: sprint 2026-11-02 to 2026-11-13**
Mon 16 Nov, 14:00-14:45 · Maya, Leo, Priya, Sam · Start / Stop / Continue

**Format: Start / Stop / Continue.** It's a routine sprint retro with 45 minutes, and this format gets to actions fastest. Nothing in the notes says morale is off, so there's no need for Mad / Sad / Glad.

| Time | Block | Min |
|---|---|---|
| 14:00 | Check-in | 5 |
| 14:05 | Last retro's actions, then what happened | 5 |
| 14:10 | Input: Start / Stop / Continue | 15 |
| 14:25 | Group, merge, vote | 10 |
| 14:35 | Actions: owner, date, check | 10 |

**1. Check-in (5 min)**
"One word for how this sprint felt, and one sentence on why."

**2. Last retro's actions**
No earlier retro is on file, so there's nothing to tick off. Take one minute to ask the room whether anything was agreed last time. One board note says "QA on SSO came late **again**", so the SSO point may be a repeat.

**What happened** (read out, no discussion yet)
- Sprint goal met: new onboarding code complete on Fri 13 Nov.
- 11 of 13 planned stories done. Both left over are on the pricing page.
- The vendor quote went to legal on 3 Nov and was still there at sprint end, 10 days later.
- On 10 Nov the team learned that the pricing change and the onboarding launch could land in the same week.
- One bug reached staging: SSO sign-ups skipped step 2.

**3. Input (15 min)**
8 minutes of silent writing, then each person reads theirs out. The 5 notes already on the board stay up; people add to them.
- **Start:** What would have told us the pricing date before 10 Nov? What would have got the pricing-page answer, or the vendor quote out of legal, sooner?
- **Stop:** What do we keep doing that pushes SSO QA to the end of the sprint?
- **Continue:** What got onboarding code complete on time that we want next sprint too?

**4. Group and vote (10 min)**
Merge duplicates and count each group. Everyone gets 3 dots. Keep the top 2 or 3 themes: ten actions means none get done.

**5. Actions (10 min)**
Each theme gets an action with one owner, a date, and a check you can see by the next retro.

**For you, not the room:** 3 of the 5 board notes are about dates and answers from other teams arriving late (the pricing date, who to chase in legal, the pricing-page answer). Expect that to be the biggest group, and keep time for the SSO repeat too.

Saved the plan to `retros/2026-11-16-onboarding-sprint.md`. After the retro, tell me what came out and I'll write it up in the same file.

---

## 2. After the retro

**Monday 16 Nov, 15:00. Maya:** Here's what came out of the retro. The top-voted theme was "we hear about other teams' dates and answers too late" (pricing date, legal, the pricing-page answer). Agreed: Maya adds a standing "dates and answers we need from other teams" item to the weekly sync, starting 2026-11-17. Sam finds a named contact in legal for vendor reviews by 2026-11-20. Leo moves SSO test cases to the first week of each sprint, starting with the next sprint. Keep doing pair reviews on risky flows. Write it up.

---

Written up in `retros/2026-11-16-onboarding-sprint.md`, plus `ACTIONS.md` (A-001 to A-003) and `DECISIONS.md` (D-001 to D-003).

**Top theme:** we hear about other teams' dates and answers too late. It was the top vote, and 3 of the 5 board notes were about it.

| ID | Action | Owner | Due | Check |
|---|---|---|---|---|
| A-001 | Standing "dates and answers we need from other teams" item in the weekly sync | Maya | 2026-11-17 | On every weekly sync agenda from 2026-11-17; by the next retro, no other team's date or answer was learned by accident (proposed) |
| A-002 | Find a named contact in legal for vendor reviews | Sam | 2026-11-20 | The team knows the name by 2026-11-20 (proposed) |
| A-003 | Move SSO test cases to the first week of each sprint, starting with the next sprint | Leo | (check) | SSO cases run in week 1 of the next sprint; no SSO bug reaches staging that sprint (proposed) |

The other two themes: SSO QA came late again (A-003 covers it), and pair reviews on risky flows stay (D-003).

**To confirm:**
1. When does the next sprint start? A-003 has no date until I know.
2. The checks are my proposal, not something the team set in the room. Change any that don't fit.
3. Your message didn't include vote counts or the notes added in the room, so the counts are from the 5 notes on the board before the retro.

The next retro opens with A-001 to A-003. Nothing was sent to anyone. Want a short recap for the team channel?

---

**The file:** `retros/2026-11-16-onboarding-sprint.md`

```markdown
# Retro - Sprint 2026-11-02 to 2026-11-13
Format: Start / Stop / Continue · 2026-11-16, 45 min · Maya, Leo, Priya, Sam

## Last retro's actions
- None on file: this is the first retro in `retros/`.

## What happened
- Sprint goal met: new onboarding code complete on 2026-11-13
- 11 of 13 planned stories done; the 2 left over are both on the pricing page
- Vendor quote went to legal on 2026-11-03 and was still there at sprint end (10 days)
- On 2026-11-10 the team learned the pricing change and the onboarding launch could land in the same week
- One bug reached staging: SSO sign-ups skipped step 2

## Themes
1. **We hear about other teams' dates and answers too late** (3 notes; top-voted) - "We learned about the pricing date by accident in a channel."
2. **SSO QA comes late** (1 note, raised before) - "QA on SSO came late again."
3. **Keep: pair reviews on risky flows** (1 note) - "Pair reviews on the onboarding flow caught a lot early."

## Actions
| ID | Action | Owner | Due | Check |
|---|---|---|---|---|
| A-001 | Add a standing "dates and answers we need from other teams" item to the weekly sync | Maya | 2026-11-17 | On every weekly sync agenda from 2026-11-17; by the next retro, no other team's date or answer was learned by accident (proposed) |
| A-002 | Find a named contact in legal for vendor reviews | Sam | 2026-11-20 | The team knows the name by 2026-11-20 (proposed) |
| A-003 | Move SSO test cases to the first week of each sprint, starting with the next sprint | Leo | (check) | SSO cases run in week 1 of the next sprint; no SSO bug reaches staging that sprint (proposed) |

## Decisions
- D-001 The weekly sync has a standing item: dates and answers we need from other teams (from 2026-11-17)
- D-002 SSO test cases run in the first week of each sprint (from the next sprint)
- D-003 Keep pair reviews on risky flows

## Open questions
- When does the next sprint start? A-003 is due at the end of its first week.
- Note counts are from the 5 notes on the board before the retro; notes added in the room and vote counts weren't recorded.
- The checks were drafted after the retro, not set in the room: confirm or change them.
```

**What to notice**

- The plan starts from facts, not from «what went wrong?», so nobody has to defend themselves.
- The board notes are quoted, never attributed.
- Three agreed items became three actions with owners. The theme the team wants to keep became a decision, not a fake action.
- What the skill couldn't know (the next sprint's date, the votes) is a question, not a guess.
