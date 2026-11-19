# Example: an async standup summary

**The setup.** The onboarding launch team posts async updates in Slack. Here is [Wednesday's thread](../../../demo/standup-2026-11-18.md). The folder holds Tuesday's [minutes](../../../demo/after/meetings/2026-11-17-weekly-sync.md) and [action list](../../../demo/after/ACTIONS.md). Slack isn't connected, so the PM pastes the thread.

**Wednesday 18 Nov, 10:15. Maya:** Summarise today's standup thread.

---

# Standup - 2026-11-18 (Wed)

## Blocked (2)
- **Sam** - vendor quote still in legal since 3 Nov (15 days); pinged legal yesterday, no reply (A-003). Unblock: Maya to ask the legal lead for a review date (A-002, was due 17 Nov).
- **Leo** - can't finish the pricing page copy until he knows whether new prices show at launch or after. Unblock: Maya, with the answer from finance (A-004).

## Today
- **Leo** - pricing page copy, as far as he can; SSO sign-up edge case from QA (not a blocker yet).
- **Priya** - support rollout note (A-001, due Thu).
- **Sam** - event tracking for the 10% rollout.

## Done since last standup
- Leo - step-3 layout bug fixed; Sam's PR reviewed.
- Priya - support macros for the new flow (check)

## No update
- None. Leo, Priya and Sam all posted.

---

Both blockers wait on you: the legal lead (A-002) and finance (A-004).

- Priya's macros are marked (check): her update doesn't say whether they're finished.
- Quiet blockers weren't checked: this is the first summary in `standups/`, and there's no tracker or `RAID.md` to compare against.
- Team taken from the 17 Nov sync attendees, since there's no `TEAM.md`.

Saved to `standups/2026-11-18.md`. Slack isn't connected, so I can't post it to #onboarding-standup. The summary above is ready to paste.

---

**What to notice**

- Five messages became two blockers, each with a name on both sides: who is blocked and who can unblock.
- The skill links each blocker to the action list (A-002, A-003, A-004), so the PM sees that both blockers are hers.
- «Progressed» isn't «done»: an unclear item is marked `(check)`, not counted as finished.
- Leo's SSO edge case isn't a blocker yet, so it stays in his «Today» line.

Next in the demo project: [the 1:1 prep with Sam](../../one-on-one/examples/prep-with-sam.md).
