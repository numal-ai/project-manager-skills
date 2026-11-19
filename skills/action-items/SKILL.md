---
name: action-items
description: Track action items across meetings and chats - pull who-does-what-by-when out of notes, threads or emails into one action list (ACTIONS.md), show what is overdue or due this week by person, draft short follow-ups to owners, and, when a tracker like Jira, Linear, Asana, Trello or GitHub Issues is connected, turn action items into tickets that carry the meeting context, only after the user confirms. Use it whenever the user says action items, to-dos from a meeting, "who owns what", "what's overdue", "follow up on...", a follow-up email after a meeting, "turn these notes into tasks or tickets", or wants an action item tracker or template.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Action items

Most of what a meeting decides is lost between the meeting and the tracker:

- the owner wasn't named;
- the date was «soon»;
- the ticket was created by someone who wasn't there and doesn't know why it matters.

This skill keeps one list with a real owner and date for every item, and carries the «why» into the ticket.

The list lives in `ACTIONS.md` in the working folder.

## Format

```markdown
# Action items

| ID | Action | Owner | Due | Status | Source | Tracker |
|---|---|---|---|---|---|---|
| A-031 | Write the rollout note for support | Priya | 2026-11-19 | Open | meetings/2026-11-17-weekly-sync.md | — |
| A-029 | Get the vendor quote approved by legal | Sam | 2026-11-25 | Blocked | meetings/2026-11-10-weekly-sync.md | LIN-477 |
```

- **Action:** starts with a verb and names a result someone can check. «Send the rollout note to support», not «rollout note».
- **Owner:** one person. «Team» or «we» means nobody. If two people own an item, split it in two.
- **Due:** a date. «Soon» or «ASAP» isn't one: ask, or use the date of the next meeting and mark it `(check)`.
- **Status:** `Open`, `Blocked` (say on what, in the Action cell), `Done` or `Dropped`. When news changes the status, add when and where to the Action cell: «(done 2026-11-19, Maya's notes)». Never delete a row: dropped items tell you how much the team over-commits.
- **Source:** where the item came from. **Tracker:** the ticket key once there is one.

## What the user may ask for

### Capture items from text
1. Read the notes, thread or email.
2. Find the commitments: «I'll…», «can you… / sure», «X will send…», «let's have Y do…». News that someone now can do something («Leo can finish the copy now») isn't a commitment yet: ask whether to add it.
3. Write each one in the format above and show the list.
4. Ask about items with no owner or no date in one grouped question, not item by item.
5. Add the confirmed items with the next free IDs.

### Show what's due
Group by person:
- overdue first, with the number of days;
- then due in the next 7 days;
- then blocked, with what each item is waiting on.

End with the counts, for example «7 open, 2 overdue, 1 blocked». Keep it to one screen.

### Draft follow-ups
For each owner with overdue items, write one short, friendly message covering all their items. If nothing is overdue, say so. Offer a heads-up only where the user's notes hold news the owner may not have heard yet.

```
Hi Sam - quick check on the vendor quote (from the 10 Nov sync, due 25 Nov). Still waiting on legal? If a new date is easier, just tell me and I'll update the list.
```

- Send nothing yourself. Show the drafts and send only the ones the user approves, through a tool that is actually connected.
- Never write follow-ups that shame people or go over their heads to their manager unless the user asks for that.

### Turn items into tracker tickets
When a tracker tool is connected through MCP or a CLI (Jira, Linear, Asana, Trello, ClickUp, GitHub Issues, Yandex Tracker or similar):
1. **Look first, read-only.** Search the tracker for existing tickets on the same work, so you don't create duplicates.
2. **Show the plan:** for each item, create a new ticket or comment on an existing one.
   - **Title:** the action.
   - **Assignee:** the owner, matched to a tracker user. If the match is unclear, ask.
   - **Due date.**
   - **Description:** what was decided and why, in one or two sentences, plus the meeting date and the minutes link. This context is what makes a ticket useful to the person who wasn't in the room.
3. **Create or update only what the user approves.** Tickets notify people, so never do it silently.
4. **Write the ticket keys into the Tracker column.** When a ticket is done in the tracker, the matching row becomes `Done` at the next review.

### Weekly clean-up
Mark items done in the tracker as `Done` here. List items that have been open for more than 3 weeks with no movement and ask: drop, re-date or reassign? A list full of zombie items stops being read.

## Rules

- **Don't invent owners or dates.** A wrong owner means the wrong person gets chased and the real owner thinks it's handled.
- **One list per team or project folder.** If the user keeps several, ask which one to use. Never merge lists silently.
- **Private items stay out.** Commitments from 1:1 notes (`one-on-ones/`) don't go into the shared list unless the user says so.

## Example

A worked example on demo data, with the request, the reply and the files written: [updating the action list from the week's notes](examples/friday-update.md). Read it when you want to see the expected output; the names and dates in it are made up.
