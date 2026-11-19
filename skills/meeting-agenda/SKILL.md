---
name: meeting-agenda
description: Build a meeting agenda from what is actually open - overdue and due action items, decisions due to be revisited, open risks, questions left from the last meeting - plus the topics people asked to add, each with an owner, a time box and the outcome it needs. Covers weekly team syncs, staff meetings, project status meetings, planning, client calls and project kickoff meetings. Use it whenever the user asks for an agenda, a meeting agenda template, a project kickoff template or a steering committee agenda, asks "what should we cover", "prep me for the sync" or "plan the kickoff", or shares a meeting invite and wants it to be useful.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Meeting agenda

A good agenda is a list of outcomes, not topics. «Pricing» wastes 20 minutes. «Decide whether the price change ships with onboarding or after it» gets decided. Build the agenda from what is open in the team's record first, then what people asked to add. That way nothing quietly drops between meetings.

## What you need

- **The meeting:** name, date, length, attendees. If the length isn't given, take it from the Meetings table of the team charter in `TEAM.md`, with what the meeting is for. Without one, assume 30 minutes for a weekly sync and 60 minutes for a kickoff, and say so.
- **Topics people asked for:** from the user, the invite or chat.
- **The record in the working folder, when it exists:**
  - the last minutes of this meeting series in `meetings/`: their sections «Open questions», «Discussed, no outcome» and «Risks and issues»;
  - `ACTIONS.md`: items owned by attendees or by nobody (`?`) that are `Open` and due on or before the meeting day, plus every `Blocked` item whatever its date;
  - `DECISIONS.md`: decisions whose Revisit date falls on or before the meeting day;
  - `RAID.md`: high-impact risks that aren't `Closed`, open issues, dependencies needed within two weeks. If a newer decision or note already settles a row, leave it off and offer to update `RAID.md`.
  - `CHANGES.md`: change requests still `Pending` whose decider (the Decided by column) is in the meeting. Each becomes a Decide item with the options from the request.
  - `PROJECT.md`: milestones in the next two weeks, so the agenda checks they are still on track.
- **Who chairs:** the user, unless they say otherwise.
- **Dates marked `(check)`:** read them as the date given, and say on the agenda that the date is unconfirmed.
- **Connected tools, read-only:** blocked or overdue tickets in the tracker, the calendar invite, the chat thread where topics were proposed.

## Steps

1. **Collect the candidates** from everything above. For each one, note where it came from (for example «A-029, blocked for 2 weeks»). People trust an agenda more when they can see why an item is on it.

2. **Write each candidate as an outcome**, in one of three kinds:
   - **Decide:** a choice the group has to make. «Decide whether…» / «Choose between…».
   - **Unblock:** someone is stuck and needs something from someone in the room.
   - **Inform:** news people need. Keep it short, or move it to the async list.

   Edge cases:
   - **A topic someone asked for without saying what they need:** infer the kind from the wording. If it's unclear, use Inform marked `(check)` and suggest the requester say what they need.
   - **An overdue action with no blocker** doesn't need meeting time. Put it under «Async instead»: the owner posts a new date.
   - **An item whose purpose is to find an owner** («who updates the help center?») is a Decide item led by the chair.
   - **A blocker nobody in the room can remove** (another team, legal, a vendor) is Inform: the owner reports, and the chair takes the ask outside.

3. **Order the items:** Decide first, then Unblock, then Inform. Decisions need fresh heads. Updates can be read.

4. **Give each item an owner** (who leads it), **a time box**, and **the prep needed** (a doc to read, numbers to bring).

5. **Fit the meeting length.** Leave about 10% as buffer.
   - What doesn't fit goes to «Async instead»: things to settle in a message instead of meeting time.
   - What can wait goes to «Parking lot».

6. **Save the agenda**, if you can write files, to `meetings/YYYY-MM-DD-<short-name>-agenda.md`.
   - Offer to share it with the attendees, and do that only after the user says yes.
   - Without file access, return the agenda as text.

## Agenda format

```markdown
# <Meeting> - <YYYY-MM-DD>, <length>

**Goal:** <one sentence: what must be true when the meeting ends>

**Attendees:** ... · **Pre-read:** <links, if any>

| # | Outcome needed | Kind | Lead | Time | Prep | Why it's here |
|---|---|---|---|---|---|---|
| 1 | Decide whether the price change ships with onboarding or after it | Decide | Maya | 10 min | Finance answer (A-004) | Raised in last sync, no outcome |
| 2 | Unblock the vendor quote: legal review date | Unblock | Sam | 5 min | - | A-029 blocked on legal for 2 weeks |
| 3 | Revisit D-009: weekly release train | Decide | Leo | 5 min | Release stats since October | Revisit date 2026-11-24 |
| 4 | Launch metrics, week 1 | Inform | Priya | 5 min | Dashboard link | Requested by Maya |

**Async instead:** <item - who posts it, by when, and where if a channel is known>
**Parking lot:** <items that can wait>
**Still open, not on this agenda:** <open questions from last time that didn't make the list - skip the ones already above>
```

## Kickoff meetings

When the meeting starts a project, a client engagement or a new team, use this order. Skip a part only if it is already settled in writing.

1. **Why this project:** the goal and how we'll know it worked, as one or two measurable outcomes.
2. **Scope:** what's in and, just as important, what's out.
3. **Who decides what:** owner, approvers, who must be consulted, who is kept informed. Write down the names.
4. **Timeline:** milestones and the first deliverable.
5. **Known risks, assumptions, dependencies.** Seed `RAID.md` with them.
6. **How we work:** meeting cadence, channel, tracker, where decisions are recorded.
7. **Next steps:** owners and dates. These become the first rows of `ACTIONS.md`.

After the kickoff, the `project-charter` skill turns the minutes into `PROJECT.md`: goal, success measures, scope in and out, milestones and who decides.

## Rules

- **Never put more on the agenda than fits.** An agenda that runs over teaches people to ignore it. It's better to push items to async openly.
- **Every item has a lead.** An item with nobody to lead it is a sign it isn't ready. Move it to the parking lot and say so.
- **An open decision that keeps coming back gets flagged.** If its revisit date has passed twice, note «third time on the agenda». Repeated deferral is information the manager wants.
- **Don't invent urgency.** If the record is empty and nobody proposed topics, say so and suggest a shorter meeting, or skipping it.

## Example

A worked example on demo data, with the request, the reply and the files written: [the next weekly sync's agenda, built from a week of records](examples/next-sync-agenda.md). Read it when you want to see the expected output; the names and dates in it are made up.
