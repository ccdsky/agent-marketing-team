---
status: pending
priority: p3
issue_id: "064"
tags: [code-review, delegation, stop-check, campaign-lead]
---

# STOP CHECK Triggers on Writing, But Delegation Decision Happens at Task Claiming

## Problem Statement

The Sprint 2 and Sprint 3 STOP CHECKs trigger when Campaign Lead "finds itself reading a skill file, writing a draft, or creating a file." The v1.3 failure (campaign-evaluation.md, line 172) shows the delegation decision was made earlier: Campaign Lead's internal reasoning at the moment of *task claiming* was "Good — tasks are set up. Now let me read the skill files I'll need for drafting, and then claim and execute Task 5." The STOP CHECK triggers on reading a skill file (which is caught), but does not trigger on the upstream decision to claim a specialist-role task.

An agent that claims a task with subject keywords matching Creative Specialist, Quality Gate, or Distribution Specialist role keywords (draft, write, revise, edit, review, format, publish) is violating the delegation model before writing a single file. The STOP CHECK would be more effective if it also covered the task-claiming decision.

## Findings

**Current STOP CHECK (campaign-lead.md Sprint 2):**
```
STOP CHECK: If you find yourself reading a skill file, writing a draft, or creating a file in `drafts/` or `edited/` — STOP.
```

**TEAM.md role keyword filter (lines 148-154):**
| Role | Claim tasks containing these keywords |
| Creative Specialist | draft, write, revise, create, blog post, email sequence... |
| Quality Gate | edit, review, quality check, approve |
| Distribution Specialist | format, publish, distribution, analytics, performance |

Campaign Lead has no keywords in this table — it should never claim any task matching these keywords.

**File:** `.claude/agents/campaign-lead.md`, Sprint 2 STOP CHECK (line ~219), Sprint 3 STOP CHECK (line ~295)
**Identified by:** architecture-strategist

## Proposed Solution

Extend STOP CHECK to cover task claiming:

```
**STOP CHECK:** Before claiming any task, check its subject keywords. If the subject contains any of the following words, STOP — that task belongs to a specialist, not you: draft, write, revise, create, blog post, email, LinkedIn, newsletter, edit, review, quality check, format, publish, distribute, analytics.

If you find yourself reading a skill file, writing a draft, or creating a file in `drafts/`, `edited/`, or `ready/` — STOP. You are violating the delegation model. Spawn the appropriate specialist instead.
```

**Effort:** Small
**Risk:** Low — purely additive constraint

## Acceptance Criteria

- [ ] STOP CHECK explicitly covers the task-claiming decision point, not just file-writing
- [ ] Keyword list matches or references the TEAM.md Agent Protocol role-keyword filter table
- [ ] Both Sprint 2 and Sprint 3 STOP CHECKs updated consistently

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist.
