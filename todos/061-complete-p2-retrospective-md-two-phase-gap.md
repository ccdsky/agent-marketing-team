---
status: pending
priority: p2
issue_id: "061"
tags: [code-review, retrospective, documentation-consistency]
---

# retrospective.md Evidence Gathering References Analytics as Prerequisite (Two-Phase Gap)

## Problem Statement

`campaign-lead.md` now mandates the retrospective runs after Sprint 3 completes, before the pre-launch summary. But `retrospective.md`'s Step 1 evidence gathering (lines 19-28) lists "Distribution Specialist's Week 1 analytics report" as a prerequisite. An agent reading `retrospective.md` directly sees analytics as required input and may conclude the retrospective must wait for post-launch data — reproducing the exact failure the PR was designed to fix through a different path.

`campaign-lead.md` lines 457-458 acknowledge this with a note: "The retrospective can be revisited and updated when Week 1 analytics arrive." But this note lives only in campaign-lead.md. retrospective.md is the canonical reference for retrospective execution and should reflect the two-phase model.

## Findings

**retrospective.md Step 1 evidence list (lines 22-26):**
```
- Task completion times vs estimates
- Quality Gate scores from each asset
- Distribution Specialist's Week 1 analytics report: `knowledge/feedback/analytics/[campaign-slug]-retrospective-[date].md`
- Any escalations or blockers that occurred
- Sprint 1 checkpoint: what did user approve vs revise?
- Sprint 2 checkpoint: what feedback was given?
```

Analytics report is listed as one of six evidence items with no indication it's deferred.

**File:** `.claude/workflows/retrospective.md`, lines 19-28
**Identified by:** architecture-strategist

## Proposed Solution

Add a note to Step 1 of retrospective.md clarifying the two-phase model:

```
**Note on timing:** When running the retrospective immediately after Sprint 3 (the standard flow), the Week 1 analytics report will not yet exist. Proceed with the remaining evidence items. Leave a placeholder in the retrospective file for analytics and revisit Step 1 + Question 1 when the analytics report becomes available (typically 1 week post-launch).
```

**Effort:** Trivial
**Risk:** None

## Acceptance Criteria

- [ ] retrospective.md Step 1 evidence list notes that analytics evidence is deferred in post-Sprint-3 runs
- [ ] retrospective.md makes clear the retro is valid and complete without analytics (can be revisited)
- [ ] campaign-lead.md note at lines 457-458 aligns with the retrospective.md update (no contradiction)

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist.
