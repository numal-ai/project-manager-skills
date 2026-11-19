---
name: morning-brief
description: A morning brief for a manager - one page of what needs you today - decisions waiting on you, overdue and due-today action items, today's meetings and what each needs from you, risks that changed, decisions due to be revisited, and anything blocked on you. Built from the folder's decision log, action list and RAID log plus any connected calendar, tracker, email or chat tools, all read-only. Use it whenever the user says "morning brief", "daily brief", "brief me", "what's on my plate", "what needs me today", "start my day", "catch me up", or opens a work session at the start of the day.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Morning brief

A manager starts the day with too many inboxes: chat, email, tracker, calendar, meeting notes. The brief answers one question — «what needs me today, and in what order?» — on one screen. It doesn't summarise everything that happened. It filters for what is the manager's to do, decide or unblock.

## Sources

Read every source, never write to one.

- **The working folder:**
  - `ACTIONS.md`: items owned by the user that are due today or overdue, plus items owned by others that are blocked on the user;
  - `DECISIONS.md`: decisions with a Revisit date of today or earlier;
  - `CHANGES.md`: change requests still `Pending` that the user decides, or that wait on a number the user owes;
  - `RAID.md`: High risks that are new or changed, and dependencies due this week;
  - the latest minutes in `meetings/`: open questions addressed to the user or with no owner, and, if there is no `RAID.md`, the risks the minutes list;
  - `one-on-ones/` and `skip-levels/`: open agreements and commitments the user owns, for today's 1:1s and skip-levels.
- **Connected tools, if available:**
  - **calendar:** today's meetings;
  - **tracker:** tickets assigned to the user, plus reviews and approvals waiting on them;
  - **email and chat:** direct questions to the user since yesterday evening that are still unanswered.
- **Who the user is:** take their name from `TEAM.md`, the calendar owner or the minutes; ask once only if none of these says. You need it to match «owned by you».

If only some sources are available, build the brief from those. Say in one line what wasn't checked («Calendar not connected»).

## Steps

1. **Collect the candidates.** Keep the source and link of each one.

2. **Keep only what needs the user,** in one of three kinds:
   - **Decide:** a choice or approval waiting on them, even when someone else is waiting for it.
   - **Do:** their own items due today or overdue.
   - **Unblock:** someone is waiting on them for something other than a decision: an ask, a review, an introduction.

   Each item goes in one place. If the user's own overdue item is what blocks someone, list it once, under Unblock, and mention the item there.

   «For your information» items stay out, except a High risk that changed. Leaving things out is the point of a brief.

3. **Prepare today's meetings.** For each meeting give one line: what it needs from the user (a decision, a number, an answer), and the open items related to it. Meetings that need nothing from the user share one last line, «Also today: 15:00 Design review», so none looks missed.

4. **Order the brief:**
   - **Decide** first: other people's work waits on these;
   - then **Unblock**;
   - then **Do**, with overdue items first.

   Inside each kind, order by how long it has been waiting.

5. **Cap the brief.** If there are more than about 10 items, show the top 10. Add «+N more» with the rule used to pick the top 10.

6. **Reply with the brief.** Save it to `briefs/YYYY-MM-DD.md` only if the user asks for a history.

## Brief format

```markdown
# Wednesday 18 Nov - 6 things need you

## Decide (2)
- **Price change timing** - with onboarding or after? Leo needs it to finish the pricing page (raised 17 Nov, no outcome). → 10:00 sync
- **Revisit D-011, December support hours** - revisit date is today.

## Unblock (2)
- **Sam** - vendor quote stuck in legal 8 days (A-029). Ask legal lead for a date.
- **Priya** - waiting on your review of the support note (LIN-482, 1 day).

## Do (2)
- Investor update draft - due today.
- Overdue: confirm conference budget with finance for Sam (from 1:1, due 20 Nov? (check))

## Today's meetings
- 10:00 Weekly sync - decide price change timing (see above).
- 15:00 1:1 Sam - follow up on the on-call rotation proposal.

Not checked: email (not connected).
```

## Rules

- **Read-only.** The brief reads tools and never replies, moves tickets or accepts invites. Offer the follow-up action, and do it only when the user says so.
- **Nothing invented.** Every line points to its source: a file row, a ticket, a message. If a due date is unclear, mark it `(check)`.
- **Private stays private.** Items from 1:1 and skip-level notes appear in the user's own brief, but never in anything shared.
- **Same shape every day.** The user learns where to look, so a busy day looks busy at a glance. Keep the heading of an empty kind, with one line under it: «Nothing due today».

## Example

A worked example on demo data, with the request, the reply and the files written: [a morning brief in launch week](examples/launch-week-brief.md). Read it when you want to see the expected output; the names and dates in it are made up.
