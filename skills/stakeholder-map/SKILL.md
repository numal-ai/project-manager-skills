---
name: stakeholder-map
description: Map project stakeholders and turn the map into a communication plan. It covers who they are, how much they care and how much sway they have, what each one needs to hear, through which channel and how often, and which update covers it. It keeps a stakeholder register in the shared folder, so status reports and recaps reach the right people. Use it whenever the user mentions a stakeholder map, stakeholder analysis, stakeholder register, a communication plan or communication plan template, a power-interest grid, "who needs to know about this", "who should get the update", keeping executives or a sponsor in the loop, or a stakeholder who was surprised by news.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# Stakeholder map and communication plan

Projects rarely fail because a stakeholder disagreed. More often a stakeholder heard bad news late, from someone else. A stakeholder map answers two questions. Who can help or hurt this project? What does each of them need to hear, how, and when? The answer to the second question is the communication plan.

The map lives in `TEAM.md` under `## Stakeholders`. If `TEAM.md` doesn't exist, create it with a `# Team` title and this section.

## Format

```markdown
## Stakeholders

| Person | Role | Interest | Influence | What they need | How and how often | Made by | Source |
|---|---|---|---|---|---|---|---|
| Elena Brooks | VP Product, sponsor | High | High | Date risk early, on one page | Status report, weekly, Friday | status-report, executive version | meetings/2026-10-05-kickoff.md |
| Marco Diaz | Sales lead | High | Med (check) | When the promised accounts get the new onboarding | Status report, weekly, plus a note on any date change | status-report, stakeholder version | meetings/2026-11-17-weekly-sync.md |

### Communication plan
- **Weekly, Friday:** status report. Executive version → Elena. Stakeholder version → Marco, Dana.
- **After each weekly sync:** recap in the team channel (meeting-minutes).
- **On a date or scope change:** a personal note to everyone with A or C on that area, before the next report.
```

- **Interest:** how much the outcome affects them. **Influence:** how much they can change it: budget, approval, people, a veto. Both are `High`, `Med` or `Low`. Both are judgments: the skill writes them into the file marked `(check)`, and the mark comes off when the user confirms.
- **What they need:** what this person needs from updates, in their terms: «date risk early», «what support has to do and when», «nothing until the price is final».
- **How and how often:** the channel and the rhythm: weekly status email, a line in the Friday report, a 1:1 every other week, only on change.
- **Made by:** the skill or person that produces it: `status-report` (team, stakeholder or executive version), the `meeting-minutes` recap, or a personal note from the user.

How the grid turns into a plan:
- **High influence, high interest:** involve them before decisions, with short, regular, personal updates.
- **High influence, low interest:** brief and rare, and never a surprise.
- **Low influence, high interest:** regular updates and a place to ask questions.
- **Low influence, low interest:** the general update is enough.
- **Med** counts as Low, unless the person approves something on the project.
- **The team itself** (people in the regular meetings) gets the meetings and their recap. The grid is for everyone else.

## What the user may ask for

### Map the stakeholders
Sources: `PROJECT.md` (sponsor and approvers), `TEAM.md`, meeting minutes (who was mentioned, who asked for what, who was worried), emails, and `reports/` (who already gets updates).
1. List the people and groups the project affects or depends on, inside and outside the team. Include the ones mentioned only in passing: «finance needs to know before the invoice change» means the finance lead.
2. For each person: role, a draft interest and influence marked `(check)`, what they asked for or worried about (with the source), and a suggested channel and rhythm.
3. Point out the gaps:
   - a high-influence person nobody updates;
   - someone getting three updates about the same thing;
   - an upcoming decision that affects someone who isn't on the list.
4. Show the table. A request to map the stakeholders is the yes to write it to `TEAM.md`, so don't ask first.

If the reports in `reports/` don't say who received them, say so once rather than guess who is already updated.

### Make the communication plan
From the map, write a short plan by rhythm: what goes out weekly, at milestones and on a change, to whom, and which skill drafts it. It goes under the table in the same section, in the same write.

### Who needs to hear about this?
For a decision, a change request or a date that slipped: list the people whose work, money or promises it touches. Use the map and the RACI section of `TEAM.md`: people with A and C on that area first, then those with I. Without a RACI, the approver named in `PROJECT.md` stands in for the A. For each, say what they need to know and the quickest fitting channel.

If the news may not happen («may come on the 30th»), split the list: **tell now** (the person whose answer settles it, and the person who decides) and **tell only if it happens**.

Draft the messages in the reply. Nothing is sent without the user's yes to the text, and nothing in the folder changes.

### Prepare for one stakeholder
Before a meeting or message to one person, write half a page:
- what they care about, from the map;
- what changed since they last heard: decisions, change requests and RAID rows since the date of the last report they received;
- what you need from them.

## Rules

- **The judgments are the user's.** Interest and influence are drafts. Write what people said or did, with a source, never a label like «difficult».
- **The register is shared.** Anyone with access to the folder can read `TEAM.md`, so write it as if the person will read their own row. Private impressions belong in the user's 1:1 notes, not here.
- **Fewer channels.** Add someone to an existing update before creating a new one.
- **Check it at each milestone.** Stakeholders change as the project moves.
- **Approvals per run:** one yes for the map and the plan. Any message needs its own yes to the text.

## Example

A worked example on demo data, with the request, the reply and the files written: [a stakeholder map and communication plan](examples/communication-plan.md). Read it when you want to see the expected output; the names and dates in it are made up.
