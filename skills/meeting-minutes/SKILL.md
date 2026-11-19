---
name: meeting-minutes
description: Turn a meeting transcript or rough notes into meeting minutes people can act on - decisions (accepted and not accepted), action items with owners and due dates, risks, open questions and a short recap message - and keep a running decision log (DECISIONS.md) and action list (ACTIONS.md) in the folder. Use it whenever the user pastes or points to a transcript, call notes or an export from Zoom, Google Meet, Teams, Granola, Otter, Fathom or tl;dv, or asks for minutes, a meeting summary, meeting notes, a recap or follow-up email, "what did we decide" or "who owns what", even if they never say "minutes".
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Meeting minutes

Minutes have two jobs:

- people who were in the meeting agree on what was decided and who does what next;
- people who missed it catch up in a minute.

Write for those two jobs: short, specific, and every line traceable to a person. A retelling of the conversation is not minutes, so leave the play-by-play out.

## What you need

- **The meeting itself:** a transcript (`.vtt`, `.srt`, `.txt`, `.docx`, `.md`), notes, or pasted text. If speaker names are missing, attribute a line only when the text makes it obvious. Otherwise write «someone» and add the item to open questions.
- **Meeting name, date and attendees.** Take them from the file or the text. If the date is unknown, use the file date or today, and say which one you used.
- **Optional context in the working folder:** earlier minutes in `meetings/`, `DECISIONS.md`, `ACTIONS.md`, `RAID.md`, and `TEAM.md` (who is who). Read them when they exist; they make the minutes much better.

## Steps

1. **Read the whole input once before writing anything.** Late parts of a meeting often reverse early ones («actually, let's not do that»).

2. **Pull out these items, each with its evidence in the text:**
   - **Decisions:** a choice the group made («let's go with», «agreed», «we won't», «final answer is»).
     - Mark each one `Accepted` or `Not accepted`. `Not accepted` covers a proposal that was turned down or an idea that was explicitly set aside.
     - A suggestion nobody agreed to is not a decision. Put it under «Discussed, no outcome».
     - If a decision changes or reverses one in `DECISIONS.md`, give the new decision its own row and set the old row's status to `Replaced by D-0xx`.
   - **Action items:** someone committed to do something, or was asked to and did not refuse.
     - Also count work the group agreed must happen even when nobody took it («someone needs to update the help center», «let's figure that out offline»). Write the owner as `?` and add the action to open questions: ownerless work is what gets dropped most often. A guessed owner is worse than an empty one, because the wrong person gets chased.
     - Ideas nobody agreed to go under «Discussed, no outcome», not into actions.
     - The owner is the person who said «I'll…» or who was asked by name.
     - Turn relative dates into dates counted from the meeting date. For a meeting on Tuesday 2026-11-17, «by Friday» becomes `2026-11-20`.
     - If no date was said and the next meeting date is known, use that date marked `(check)`. Otherwise write `—`. Never pick a date the meeting didn't imply.
     - A parked topic with a promise («I'll bring an answer next week») gives two items. The promise is an action. The topic goes under «Discussed, no outcome». A parked topic is not an issue.
     - «Let's look at the numbers again on 8 Dec» about a decision is that decision's Revisit date, not a separate action. It becomes an action only if someone is named to prepare something for it.
   - **Risks and issues:**
     - a risk is something that might go wrong;
     - an issue is something already going wrong.

     A missed deadline that hasn't arrived yet is a risk. Give a risk an owner only if someone took it on; otherwise use `?`.
   - **Open questions:** asked and not answered. Note who should answer, if anyone said.
   - **Updates to earlier action items:** if open items from `ACTIONS.md` came up, update them — done, blocked, or a new due date.

     If there is no `ACTIONS.md` yet but the meeting reports on earlier work («still with legal since the 3rd»), add that work as a new row with its current status (`Blocked`, `Open`), so it is tracked from now on.

3. **Write the minutes** in the format below. Keep names spelled as in the transcript or `TEAM.md`, and copy numbers and dates exactly.

4. **Leave out personal asides:** health, family, pay, performance, jokes about people. The user can ask for them to be put back. Minutes travel further than the room.

5. **Save the files, if you can write files:**
   - Save the minutes to `meetings/YYYY-MM-DD-<short-name>.md`.
   - Add the new decisions to `DECISIONS.md` and the new action items to `ACTIONS.md`, each with the next free ID. Update the status of rows that changed. Never delete a row.
   - Add new risks and issues to `RAID.md` if it exists. Otherwise keep them in the minutes only.
   - If someone asked to add work, move a milestone or spend more, and the meeting didn't settle it, list it under open questions as a possible change, and offer the `change-control` skill to write the change request.
   - If `DECISIONS.md` and `ACTIONS.md` don't exist and the user hasn't asked to keep records, ask once: «Keep a running decision log and action list in this folder?» Then create only those two files.
   - Without file access, put each block under a heading that names its file.

6. **Offer the next step in one line**, picked from these three, depending on what fits:
   - the recap message;
   - creating the action items in the tracker (only if a tracker tool is connected);
   - the agenda for the next meeting.

## Minutes format

```markdown
# <Meeting name> - <YYYY-MM-DD>

**Attendees:** Maya Okafor, Leo Park, Priya Shah · **Absent:** Sam Lee · **Source:** <file name or "notes">

## Summary
<Two or three sentences: what is different now because this meeting happened.>

## Decisions
- **D-014 Accepted:** <decision, as a full sentence>. Decided by <names>. Why: <reason given>. Revisit <date, if one was set>.
- **D-015 Not accepted:** <what was proposed>. Why not: <reason given>.

## Action items
| ID | Action | Owner | Due | Status |
|---|---|---|---|---|
| A-031 | <verb first: "Send the rollout note to support"> | Priya | 2026-11-20 | Open |
| A-032 | Get the vendor quote approved by legal | Sam | 2026-11-25 | Blocked (legal) |

## Updates to earlier items
- A-027 (Leo, landing page copy): done.
- A-029 (Sam, vendor quote): blocked, waiting on legal; new due date 2026-11-25.

## Risks and issues
- **Risk:** <what might go wrong> - owner <name>, <mitigation if one was discussed>.
- **Issue:** <what is going wrong now> - next step <...>.

## Open questions
- <question> - <who should answer, by when, if said>

## Discussed, no outcome
- <topic> - <where it stands>. Goes on the next agenda.
```

Leave out sections that would be empty. The exception is «Decisions» and «Action items»: if there were none, say so in one line. «No decisions were made» is useful to know.

## Writing rules

- **A decision is a full sentence a newcomer can understand.** «Launch the new onboarding to 10% of sign-ups on 1 Dec» — not «go with option B».
- **An action starts with a verb and names a result.** «Send the rollout note to support» — not «rollout note».
- **Keep each reason short and use the speaker's own words.** If no reason was given, write nothing rather than inventing one.
- **Mark what you are unsure of with `(check)`.** The reader fixes that faster than an error they can't see.

## Recap message

If the user asks for a recap, or accepts the offer, write a message for Slack or email of up to 120 words:

```
<Meeting>, <date>: decided <1-3 decisions>. Next: <owner> - <action> by <date>; ... Open: <question, if any>. Minutes: <link or file>.
```

No greeting and no «hope this helps».

Send it, or post it anywhere, only when the user says so, and only through a tool that is actually connected.

## Tracker tickets

When a tracker tool is connected (Jira, Linear, Asana, GitHub Issues, Trello or similar, through MCP or a CLI):

1. **Offer to turn the action items into tickets.** First show the exact list: title, assignee, due date, and a description holding the decision behind the action and the meeting date.
2. **Create the tickets only after the user says yes.** Tickets notify other people, so this is never a silent side effect.
3. **Write each ticket key into the Tracker column** of `ACTIONS.md`.
4. **If a matching ticket already exists, update it.** Add a comment with the new context instead of creating a duplicate.

## Register formats (create only when keeping records)

`DECISIONS.md`
```markdown
# Decision log

| ID | Date | Decision | Status | Decided by | Why | Revisit | Source |
|---|---|---|---|---|---|---|---|
```
Status is one of `Accepted`, `Not accepted` or `Replaced by D-0xx`. Source is the path of the minutes file.

`ACTIONS.md`
```markdown
# Action items

| ID | Action | Owner | Due | Status | Source | Tracker |
|---|---|---|---|---|---|---|
```
Status is one of `Open`, `Blocked`, `Done` or `Dropped`.

## Short worked case

Transcript excerpt:

> **Leo:** If we ship to everyone on the 1st and pricing changes the same week, support gets buried.
> **Maya:** Then 10% of new sign-ups first, everyone on the 15th. Leo, Priya, OK? Ok, done.
> **Priya:** I'll write the note for support by Thursday.
> **Leo:** Could we push it all to January? **Maya:** No, sales promised December.

Minutes lines (meeting on Tuesday 2026-11-17):

- **D-014 Accepted:** Launch the new onboarding to 10% of new sign-ups on 2026-12-01, and to everyone on 2026-12-15. Decided by Maya, Leo, Priya. Why: avoid overloading support in the week pricing changes.
- **D-015 Not accepted:** Move the launch to January. Why not: sales already promised December.
- `| A-031 | Write the rollout note for support | Priya | 2026-11-19 |` (Thursday)

## Example

A worked example on demo data, with the request, the reply and the files written: [minutes from a 32-minute weekly sync transcript](examples/weekly-sync.md). Read it when you want to see the expected output; the names and dates in it are made up.
