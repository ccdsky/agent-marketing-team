---
status: pending
priority: p3
issue_id: "025"
tags: [code-review, expert-review, escalation, error-handling]
---

# Expert Review Has No Escalation Path When Fewer Than 3 Experts Complete Successfully

## Problem Statement

`expert-review/SKILL.md` spawns 5 expert subagents in parallel (Step 2) and synthesizes all 5 responses (Step 5). If one or more subagents fail to return (timeout, error, truncation), the synthesis step has no instruction on how to proceed with partial results. Proceeding with fewer than 5 experts silently changes the weighted score. Waiting indefinitely blocks the creative workflow.

## Findings

**expert-review/SKILL.md Step 5:**
> "Collect scores from all 5 experts and apply weights table"

No handling for:
- Expert subagent returns empty or malformed response
- Expert subagent times out
- 2 of 5 experts return (is 40% response rate sufficient to synthesize?)

There is no minimum viable response threshold defined.

## Proposed Solutions

### Option A: Define minimum threshold with graceful degradation (Recommended)

Add to Step 5:

```
## Synthesis (Step 5)

**If all 5 expert responses received:** Apply full weights table.

**If 3-4 responses received:** Normalize weights across responding experts (proportionally) and note
"[N]/5 experts responded" in synthesis. Flag as REDUCED CONFIDENCE review.

**If fewer than 3 responses received:** Do not synthesize. Note: "Expert review incomplete — 
[N]/5 experts responded. Proceeding with Creative Specialist self-assessment only."
Flag task with metadata: {"expert_review_status": "incomplete", "experts_responded": N}
```

**Effort:** Small — add conditional logic to Step 5

## Acceptance Criteria

- [ ] expert-review/SKILL.md defines behavior when fewer than 5 experts respond
- [ ] A minimum viable response threshold (e.g., 3 of 5) is specified
- [ ] Partial review results are labeled as such in output

## Work Log

- 2026-02-18: Identified during v1.2 PR review
