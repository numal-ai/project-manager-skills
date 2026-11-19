# Example: a team charter from a how-we-work talk, then a page for the new engineer

**The setup.** Tuesday after launch week. Tess Moreno joined the team yesterday and asked how the team works, so after the weekly sync the team took twenty minutes to talk it through. Maya pastes [the transcript](../../../demo/working-agreements-2026-11-24.md). The folder has the [project charter](../../project-charter/examples/charter-from-kickoff.md) in `PROJECT.md`, the decision log up to D-008, the action list, the RAID log, the sprint retro, and a `TEAM.md` with the [RACI](../../raci-matrix/examples/raci-from-records.md) and the [stakeholder map](../../stakeholder-map/examples/communication-plan.md). No chat is connected.

## 1. Write the charter

**Tuesday 24 Nov, 11:00. Maya:** Here's the transcript of our how-we-work talk after the sync. Write up our team charter.

---

The charter is at the top of `TEAM.md`, marked **Draft** until the team has seen it. I saved the transcript to `meetings/2026-11-24-working-agreements.md` and logged the new agreements as D-009 to D-013.

**Left out on purpose**
- Sam's «let's just be nice in reviews»: everyone agreed, but it doesn't say what anyone does. If there's a real problem behind it, the retro can turn it into a behaviour.
- Slack after six: you parked it, so it's an open question, not a rule.

**Already decided, so reused, not logged again:** pair reviews (D-006), SSO tests in week 1 (D-005) and the standing sync item (D-004), all from the 16 Nov retro.

**Please check (the (check) marks)**
- **Dates I worked out.** Retros every other Monday from 16 Nov give 30 Nov as the next one. «February» became the first retro in February, 8 Feb. The Wednesday trial ends 23 Dec, so it's reviewed at the 28 Dec retro, which is Christmas week.
- **«Ours».** Nobody listed it today. I took it from the project scope.
- **Standup.** Nobody said what goes in it. One line from the team would do.
- **Retro length.** The 45 minutes come from the 16 Nov retro.

**Two records today's talk may have settled.** Say yes and I'll update both:
1. Priya said the help center is support's. That would close A-006 (owner Priya), and set the RACI row «Help center articles» to Priya as A. R-002 then gets her as owner.
2. Tess isn't in `TEAM.md`. I'd add a People table with her in it.

**For the team channel.** Not posted. Say yes to the text, or paste it yourself:

> Our team charter from today's talk (draft, tell me what I got wrong):
> • What we're for: getting new customers from sign-up to their first invoice.
> • Not ours: billing (Ana's team), pricing (finance), help center (support). Support hears about a flow change two weeks before it ships.
> • Who decides: small calls, whoever does the work. Dates or scope go to Maya, who takes them to Elena. Still stuck after the sync? Maya and Leo decide, and we all go with it.
> • Reviews: first look within one working day; say so in the PR if it's big.
> • Waiting on another team for more than two working days? Post it here. After a week, Maya goes to their lead.
> • No meetings on Wednesday mornings: a one-month trial, checked at the retro.
> • Still open: who's on call in the launch weeks (Leo is checking December).
> Full charter: TEAM.md. We look at the whole thing again in February.

Once the team is OK with it, tell me and the status becomes «Agreed by the team on …».

---

## 2. A page for the newcomer

**Maya, 15:00:** Tess asked for something short she can keep open in her first weeks. Make it.

---

Here's Tess's page, saved as `onboarding/tess-moreno.md`. It says the charter is still a draft. Two blanks first: what goes in the standup, and whether the next retro is 30 Nov. «Whom to ask» comes from the RACI and the stakeholder list, not from today's talk, so please skim it. Nothing has gone to Tess; say yes to the text and I'll get it ready.

> # Welcome to the activation team, Tess
> For your first weeks · 2026-11-24 · From the team charter in TEAM.md (draft), DECISIONS.md and the RACI
>
> **What we do:** we get new customers from sign-up to their first invoice. Right now that's the new onboarding launch.
> **What we don't:** billing (Ana's team), pricing (finance), the help center (support; they hear about a flow change two weeks ahead).
> **What you can just decide:** small calls in your own work. Dates or scope: Maya. Stuck after the sync: Maya and Leo decide.
> **How we work:** first look at a review within a working day, so chase after that; risky flows get a pair review; waiting on another team two working days, post it in the channel; Wednesday mornings are meeting-free until 23 Dec.
> **Your meetings:** weekly sync Tuesday 10:00; async standup before 10:00; retro every other Monday.
> **Whom to ask:** code and reviews, Leo · priorities and dates, Maya · support and the help center, Priya.
> **Decisions to know:** staged launch, 10% on 1 Dec and everyone on 15 Dec (D-001) · two Sales accounts switched on by hand on 1 Dec (D-007) · bulk import moved to January (D-008) · new prices not before 15 Dec (D-003).
> **Not settled yet:** who's on call in the launch weeks.

---

**`TEAM.md`** (the RACI and Stakeholders sections below it are unchanged)

```markdown
# Team

## Team charter: Activation team

Status: Draft · Next review: 2027-02-08 (check) · Source: meetings/2026-11-24-working-agreements.md

### Purpose
We get new customers from sign-up to their first invoice.

### What we own
**Ours:** the way from sign-up to a customer's first invoice; today, the new sign-up flow and the template picker (PROJECT.md) (check).
**Not ours:** billing (Ana's team); pricing (finance, Dana Ruiz); the help center (support, Priya Shah).

### How we decide
- Small calls: whoever does the work (D-013).
- Anything that moves a date or the scope: Maya, who takes it to Elena Brooks (PROJECT.md).
- Still stuck after the sync: Maya and Leo decide, and everyone goes with it (D-013).
- Who does and signs off each piece of the onboarding launch: the RACI below.

### Working agreements
| Agreement | Since | Decision | Review |
|---|---|---|---|
| First look at a code review within one working day; if it's big, say so in the PR | 2026-11-24 | D-010 | 2027-02-08 (check) |
| Pair reviews on risky flows | 2026-11-16 | D-006 | — |
| SSO test cases run in the first week of each sprint | 2026-11-16 | D-005 | Next retro |
| Support hears about a flow change two weeks before it ships (with support) | 2026-11-24 | D-009 | 2027-02-08 (check) |
| Waiting on another team more than two working days: post it in the team channel; after a week, Maya asks that team's lead | 2026-11-24 | D-011 | 2027-02-08 (check) |
| No meetings on Wednesday mornings, as a one-month trial (to 2026-12-23) | 2026-11-24 | D-012 | 2026-12-28 (check) |

### Meetings
| Meeting | When | Length | What for |
|---|---|---|---|
| Weekly sync | Tuesday 10:00 | 30 min | Decisions, blockers, the dates and answers we need from other teams (D-004) |
| Standup | Async in the team channel, before 10:00 | — | (check) |
| Retro | Every two weeks, Monday; next 2026-11-30 (check) | 45 min (check) | What to keep and change; agreements due for review |

### How we know it works
- Reviews get a first look within a day.
- Nobody learns another team's date by accident.

### Open questions
- Who is on call during the launch weeks? Support needs a name to page (A-011).
- Slack after six: a rule or not? To the retro if it comes up.
- Who tells support about a flow change: whoever makes it, or Maya?
```

**`DECISIONS.md`** (new rows; Source for each is `meetings/2026-11-24-working-agreements.md`)

```markdown
| D-009 | 2026-11-24 | Support hears about a flow change two weeks before it ships | Accepted | Team, Priya Shah (support) | Otherwise the help center articles are wrong on day one | 2027-02-08 (check) | … |
| D-010 | 2026-11-24 | First look at a code review within one working day; if it's big, say so in the PR | Accepted | Team | People know when to chase a review and can plan for big ones | 2027-02-08 (check) | … |
| D-011 | 2026-11-24 | Waiting on another team more than two working days: post it in the team channel; after a week, Maya asks that team's lead | Accepted | Team | The vendor quote waited three weeks in legal and nobody chased it until the retro | 2027-02-08 (check) | … |
| D-012 | 2026-11-24 | No meetings on Wednesday mornings, as a one-month trial (2026-11-25 to 2026-12-23) | Accepted | Team | Leo never gets a long block of time | 2026-12-28 (check) | … |
| D-013 | 2026-11-24 | Small calls: whoever does the work. Still stuck after the sync: Maya and Leo decide, and everyone goes with it | Accepted | Team | Tess asked what she can decide on her own | 2027-02-08 (check) | … |
```

**`ACTIONS.md`** (new row)

```markdown
| A-011 | Look at who's around in December and name who is on call during the launch weeks | Leo | ? | Open | meetings/2026-11-24-working-agreements.md | — |
```

---

**What to notice**

- Every line comes from the talk or the records. Gaps are marked `(check)` or listed as open questions, never filled with a plausible rule.
- Agreements the team already made in the retro were reused by their IDs. Only the new ones got decision rows, so the retro can check them like any other decision.
- A value («be nice in reviews») and a parked topic («Slack after six») stayed out of the agreements, and the reply says why.
- Rough dates («February», «a month») became real dates, each marked `(check)`.
- Records the talk may have settled elsewhere, such as the help center owner, came back as one question instead of quiet edits.
- Nothing went to the team or to Tess without a yes to the text.

Next in the demo project: [the VP's skip-levels with two engineers, a week after the launch](../../skip-level-meeting/examples/round-with-themes.md).
