---
name: one-on-one
description: Prepare and keep 1:1 meetings (one-on-ones) - with someone who reports to you or with your own manager. Builds the agenda from the running 1:1 doc, last time's commitments and what happened since; suggests good questions for the situation; and after the meeting records notes, agreements and follow-ups in a private per-person file. Use it whenever the user mentions a 1:1, one on one, one-on-one meeting template, 1:1 questions, "prep my 1:1 with Sam", a career or feedback conversation, or wants to track what they agreed with someone.
license: MIT
metadata:
  author: Numal
  homepage: https://numal.ai
  collection: project-manager-skills
---

# One-on-one

A 1:1 belongs to the other person more than to the manager. It is the place to raise what doesn't fit in team meetings: how work feels, growth, friction, ideas. Status updates belong elsewhere.

The two things that make 1:1s work:

- **continuity:** last time's commitments are checked;
- **preparation:** both people bring topics.

This skill keeps both.

## The running doc

There is one file per person in `one-on-ones/<first-last>.md`, newest meeting on top:

```markdown
# 1:1 - Sam Lee (Engineer) · with Maya Okafor

## Standing topics
- Growth: wants to lead the next integration project (since 2026-09)

## 2026-11-17
**Their topics:** on-call load; conference budget
**My topics:** how the wait on legal is going; the on-call proposal
**Notes:** <short, factual>
**Agreed:**
- [ ] Maya: ask finance about the conference budget by 2026-11-20
- [ ] Sam: propose an on-call rotation change at the next team sync
**Follow up next time:** how the rotation proposal went

## 2026-11-03
...
```

**Privacy.** These notes are personal:

- keep them in `one-on-ones/`;
- never copy their content into shared files (`ACTIONS.md`, minutes, reports) unless the user asks;
- never post them anywhere.

If an agreement needs to be public, such as a team process change, suggest that the person raises it in the team meeting themselves.

## Before the meeting: prepare

1. **Read the person's file:**
   - open checkboxes from last time;
   - «Follow up next time»;
   - standing topics.
2. **Look at what happened since** in the shared files and connected tools. Asking for prep is permission to read them:
   - their items in `ACTIONS.md`;
   - decisions that affected their work;
   - wins worth naming;
   - tracker activity, read-only.

   Use this to ask better questions, not to turn the 1:1 into a status review.
3. **Draft the agenda:**
   - **Their topics first.** If they shared none, leave room and suggest asking them for topics a day before.
   - **Follow-ups:** each open agreement, checked off or re-dated.
   - **Your topics:** at most two. Feedback goes here, written down concretely: what happened, its effect, what you'd like instead.
   - **Two or three questions** that fit the moment (see below).
4. **Keep it short.** A 30-minute 1:1 has room for three or four topics.
5. **Save the prep** as the new dated section of the running doc: topics filled in, Notes and Agreed left as «—». After the meeting, fill the same section. The questions and the «since» context stay in your reply.

The rule on judgments below applies to prep too. If the user shares an impression («he sounded frustrated»), use it to frame a topic, keep it out of the file, and offer to record it.

## Questions by situation

Pick two or three. Don't run a questionnaire.

- **Regular check-in:** «What's taking more energy than it should right now?» · «What should I know that I don't?» · «Anything I could do differently that would help you?»
- **New in the role, first 90 days:** «What has surprised you?» · «Who has been most helpful?» · «What's still unclear about what good looks like?»
- **Growth and career:** «What do you want to be doing a year from now that you aren't doing now?» · «What skill would make the biggest difference?» · «What project would stretch you?»
- **After a hard week, an incident or a miss:** «How are you doing after last week?» · «What would you do differently?» · «What support was missing?» Look for learning, not blame.
- **With your own manager:** «What's your biggest priority this month, and how does my team help?» · «Where do you want me to take more ownership?» · «How do you see my team's work from outside?»

A skip-level, where you meet your report's reports, has its own skill: `skip-level-meeting` keeps those notes in `skip-levels/` and turns a round of them into themes without names.

## After the meeting: record

1. Turn the user's notes, or a transcript if they have one, into the dated section above:
   - their topics;
   - your topics;
   - short notes;
   - agreements as checkboxes with an owner and a date;
   - «Follow up next time».
2. Write facts and agreements. Leave out judgments about the person unless the user explicitly wants them recorded. These notes may be read later in a context nobody planned for.
3. Update «Standing topics» if a long-running theme came up: a growth goal, an ongoing concern.

## Rules

- **The other person's topics come first.** If the agenda is all manager topics, point that out, and draft a one-line message asking them for topics. Don't send it.
- **Agreements have owners and dates on both sides.** A 1:1 where only the report takes actions is a status meeting.
- **Never use 1:1 content in team settings without asking.** Trust in 1:1s takes months to build and one leak to lose.

## Example

A worked example on demo data, with the request, the reply and the files written: [1:1 prep with an engineer stuck waiting on legal](examples/prep-with-sam.md). Read it when you want to see the expected output; the names and dates in it are made up.
