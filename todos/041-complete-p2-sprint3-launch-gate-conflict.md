---
status: pending
priority: p2
issue_id: "041"
tags: [code-review, sprint3, campaign-lead, TEAM.md, checkpoint, publish]
---

# Sprint 3 Launch Gate Conflict — TEAM.md and campaign-lead.md Contradict Each Other

## Problem Statement

`TEAM.md` Sprint Model says Sprint 3 requires "no checkpoint — execute approved direction." `campaign-lead.md` Quality Gates section says Sprint 3 → Launch requires "✅ User gives final launch approval." These directly contradict. At the most consequential moment (actual publish), agents will either publish without checking in (following TEAM.md) or stall waiting for an undefined approval signal (following campaign-lead.md).

## Findings

**TEAM.md Sprint Model:**
> "Sprint 3: ship (no checkpoint — execute approved direction)"

**campaign-lead.md Quality Gates section (lines 426-429):**
```
Sprint 3 → Launch:
- ✅ All assets pass editorial review
- ✅ Platform formatting correct
- ✅ Analytics tracking configured
- ✅ User gives final launch approval
```

Distribution Specialist has no instruction for how to surface "ready to launch" or how to receive the "go" signal. The approval mechanism is undefined.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Add one lightweight pre-publish gate — resolve both documents (Recommended)

Sprint 3 is not a full checkpoint, but publishing warrants one confirmation. The model:

**TEAM.md:** Change to "Sprint 3: execute approved direction. One pre-publish confirm before Distribution Specialist publishes — not a full strategy checkpoint."

**campaign-lead.md:** Replace "User gives final launch approval" with: "Campaign Lead surfaces a 'Ready to launch' summary to the user listing all assets and platforms. User replies 'go' to trigger Distribution Specialist's publishing tasks."

This preserves the "no strategy checkpoint" spirit while acknowledging publish is irreversible.

**Effort:** Small — edit one line in TEAM.md, one line in campaign-lead.md

### Option B: Remove launch approval from campaign-lead.md

Remove "User gives final launch approval" from the quality gates list. Sprint 3 executes without any gate. User must monitor proactively.

**Effort:** Trivial — delete one bullet

## Acceptance Criteria

- [ ] TEAM.md and campaign-lead.md agree on Sprint 3 gate behavior
- [ ] Distribution Specialist has a clear signal for when to publish (or no gate at all)
- [ ] The resolution is documented in one place and referenced in the other

## Work Log

- 2026-02-19: Identified during v1.3 code review by agent-native-reviewer
