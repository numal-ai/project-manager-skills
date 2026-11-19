# Example: prep for a skip-level, two write-ups, and what to take back to the lead

**The setup.** The day the new onboarding went out to 10% of new sign-ups. Elena Brooks, VP Product, is meeting two engineers from Maya Okafor's team: Sam Lee, and Tess Moreno, who joined a week ago. Elena's folder has the shared records of the launch: the decision log (with her own calls on the [change requests](../../change-control/examples/scope-change-request.md), D-007 and D-008), the action list, the RAID log, the minutes, the retro, and `TEAM.md` with the people and the [team charter](../../team-charter/examples/charter-from-session.md). It also has `one-on-ones/maya-okafor.md`, her private 1:1 notes with Maya. The skill doesn't open that file.

## 1. Prep

**Tuesday 1 Dec, 17:00. Elena:** Prep my skip-level with Sam tomorrow.

---

Here's your prep for Sam. It's your first skip-level with him, so nothing is open from last time. Saved privately in `skip-levels/sam-lee.md`.

**Context** (from the shared records)
- The launch is staged: 10% of new sign-ups from 1 Dec, numbers on 8 Dec, everyone from 15 Dec (D-001). The records don't show yet whether today's 10% went out as planned.
- Sam owns the legal approval of the vendor quote (A-003). It has been in legal since 3 Nov; the review was set for 24 Nov. `ACTIONS.md` still says blocked, with no update since.
- On 24 Nov the team wrote down how it works, for Tess. Sam asked for the rule on waiting for other teams, after legal took three weeks with nobody chasing: post it after two working days, and after a week Maya goes to that team's lead (D-011). Also a first look at a review within a working day (D-010).
- The 16 Nov retro's top theme was hearing other teams' dates too late (D-004).
- Your calls of 20 Nov: the two December accounts switched on by hand (D-007); bulk import moved to January 2027, no day set (D-008).

**Questions** (first skip-level, the day after the launch, two weeks after your scope change)
1. «What does a good week look like for you?»
2. «What slowed you down most?» Let him bring up legal or not.
3. «What's still unclear?» After the import move and the by-hand switch.
4. «What should I know about the team that I probably don't?»

**What he may ask you**
- Bulk import: January 2027, no day yet. You can share that. Who works on it is Maya's call, so don't promise it.
- On-call in the launch weeks: still an open question in the team charter. Leo's and Maya's to answer.
- The vendor quote, if it's still stuck: D-011 has Maya go to legal's lead. Point him to Maya.

**Before the meeting:** does Maya know you're meeting Sam tomorrow? If she doesn't, tell her today.

---

## 2. Write up both, and what to take back

**Thursday 3 Dec, 16:00. Elena:** Maya knew, she told the team last week. Here are [my notes from both](../../../demo/skip-level-notes-2026-12-03.md). Write them up, and what do I take back to Maya?

---

Both are written up, privately: Sam's meeting replaces his prep in `skip-levels/sam-lee.md`, Tess is in a new `skip-levels/tess-moreno.md`, and the round is in `skip-levels/2026-12-maya-okafor-team.md`.

Two things I didn't write down:
- **The reason for Tess's January request.** It's about her health, so her file only says she'll sort her January hours with Maya. You said yes to her, so Maya should hear it from you first.
- **What you asked.** Your notes don't say, so that line reads «(not in the notes)».

**To take back to Maya** (a draft for your next 1:1; nothing is sent)

1. **Decisions reach the team late or second-hand.** A change was heard from another team before anyone inside told the team, and a decision already made was found by searching old threads. It was also the top theme of the 16 Nov retro (D-004). Part of it is yours: the January import move was your decision (D-008), and the team heard it from outside.
2. **Template picker reviews wait days, because only one person knows that code.** On 24 Nov the team agreed to a first look within a working day (D-010). This one is for Maya and Leo to solve.
3. **Sam wants to lead the bulk import work in January.** He said you can tell Maya, and he'll raise it with her himself. It's her call, so don't promise him anything.
4. **Tess would like to sit in on a few support calls** to see where customers get stuck. She said yes to you raising it.
5. **What you'll do yourself:**
   - Tell Sam by Fri 4 Dec whether the two January hires are confirmed. If the answer affects Maya's team, tell Maya first.
   - Raise Tess's support-calls idea with Maya. I put Fri 4 Dec, since your notes give no date. When is your next 1:1 with her?
   - Proposed: when you decide a date or scope change, agree with Maya when the team hears it, so they hear it before other teams do. Say if you want this on your list.

**Stays private:** how Sam felt about the October design work (he said not for sharing), what he said about Maya's time, and Tess's worry about on-call. One person said each, and nobody gave permission. On-call has been an open question in the team charter since 24 Nov, when Priya raised it. If you ask Maya about it, ask it as that.

**Anonymity is weak here.** Maya's team is three people and you met two, so «two people said it» means both. That's why the themes give only general examples.

**Shared files:** nothing from this round goes in yet. Both themes need to reach Maya first, and neither Sam nor Tess agreed to a risk going into `RAID.md`.

---

## 3. «Put whatever should go into the shared files»

**Elena, 16:30:** Looks good. Put whatever should go into the shared files there.

---

Nothing goes into the shared files today, so I haven't changed any.
- **The themes go to Maya first.** `DECISIONS.md`, `ACTIONS.md` and `RAID.md` are her team's records. If the themes showed up there before you'd talked, she'd find out from her own log that you went around her.
- **`RAID.md` needs consent.** The single-reviewer point is a real risk, but neither Sam nor Tess agreed to it going in.
- **Your promises to Sam and Tess stay private.**

After your 1:1, whatever Maya wants on the team's record goes in as she words it, without names. I've noted your OK in the round file, and your new habit is on your list.

---

**`skip-levels/sam-lee.md`**

```markdown
# Skip-level - Sam Lee (Engineer, reports to Maya Okafor) · with Elena Brooks

## 2026-12-02
**Lead knew:** yes
**I asked about:** (not in the notes)
**They raised:**
- The 10% launch on 1 Dec went fine, a quiet day; he's proud of it.
- Heard from Marco, before Maya told the team, that bulk import moves to January: «felt like we were the last to know».
- His template picker PR waited 3 days for Leo; Leo is the only one who knows that code.
- Wants to lead the bulk import work in January.
- Asked whether the two January hires are confirmed.
- Said Maya is great but stretched thin, in meetings all day, and decisions come through late.
- Felt a bit passed over when Leo took the template picker design in October. Not for sharing.
**I committed to:**
- [ ] Elena: tell Sam whether the two January hires are confirmed, by 2026-12-04 (tell Maya first if it affects her team)
**May be shared:** the wish to lead the January import work, with Maya (Sam said yes). Not the October design work. Not what he said about Maya's time.
**Feeds themes:** 1, 2
```

**`skip-levels/tess-moreno.md`**

```markdown
# Skip-level - Tess Moreno (Engineer, joined 2026-11-23, reports to Maya Okafor) · with Elena Brooks

## 2026-12-03
**Lead knew:** yes
**I asked about:** (not in the notes)
**They raised:**
- Ten days in. The team is friendly; the how-we-work page helped a lot.
- Found the decision on when the new prices go live (D-003) by searching old threads; nobody told her. «Where do decisions live?»
- Her first PR waited two days; only Leo can review template picker code.
- Worried about on-call in the launch weeks; she has never done it here. Doesn't want it to sound like complaining.
- Would like to sit in on a few support calls, to see where customers get stuck.
**I committed to:**
- [ ] Elena: raise sitting in on support calls with Maya, by 2026-12-04 (check)
- Agreed: Tess sorts her January hours with Maya. Tell Maya first.
**May be shared:** the support-calls wish, with Maya (Tess said «yes please»). Not the on-call worry.
**Feeds themes:** 1, 2
```

**`skip-levels/2026-12-maya-okafor-team.md`**

```markdown
# Skip-level round - Maya Okafor's team, December 2026

Met: Sam Lee (2026-12-02), Tess Moreno (2026-12-03). Not met yet: Leo Park.

Anonymity is weak: the team is three people and Maya knows whom you met, so «two people» means both. The examples stay general.

## Themes (raised by two or more people, no names)
1. Decisions reach the team late or second-hand. A change was heard from another team before anyone inside told the team; a decision already made was found by searching old threads. Same top theme as the 16 Nov retro (D-004).
2. Template picker reviews wait days, because one person knows that code. The team agreed to a first look within one working day on 24 Nov (D-010).

## To take back to Maya
- Theme 1. Part of it is mine: the January import move was my decision (D-008), and the team heard it from outside.
- Theme 2. Hers and Leo's to solve.
- Shared with permission: Sam wants to lead the bulk import work in January. Her call; nothing promised to him.
- Shared with permission: Tess would like to sit in on a few support calls.

## My commitments
- [ ] Tell one person whether the two January hires are confirmed, by 2026-12-04; Maya first if it touches her team
- [ ] Raise one person's support-calls idea with Maya, by 2026-12-04 (check)
- [ ] When I decide a date or scope change, agree with Maya when the team hears it (from 2026-12-03; check at the next round)

## Stays private
- One person's feeling about how design work was handed out in October (not for sharing).
- One person's view of how the lead's time is spread.
- One person's worry about on-call in the launch weeks.

## Shared records
- 2026-12-03: nothing written. Maya hears the themes first; nobody agreed to a RAID entry.
```

---

**What to notice**

- The prep came only from shared records. Elena's private 1:1 notes with Maya stayed closed, so nothing Maya said in confidence shaped the questions.
- A theme needs two people. Everything one person said stayed in their file, even when it echoed a theme.
- Items people agreed to share went to Maya with their names, because that's what they agreed. Everything else left as a theme without names, with a warning that anonymity is weak on a team of three.
- A theme that landed on Elena's own decision was said plainly.
- The health detail behind a request was left out. The commitment it led to was kept, with «tell Maya first».
- «Put it in the shared files» got an empty list with the reasons: the lead hears the themes first, and a risk needs the person's consent.

Next in the demo project: [a month later, the lessons from the launch](../../lessons-learned/examples/lessons-from-retro.md).
