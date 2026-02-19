---
status: pending
priority: p2
issue_id: "034"
tags: [code-review, quality-gate, self-claiming, task-protocol]
---

# Quality Gate Self-Claiming Workflow Jumps to Step 2 — Step 1 (TaskList) Is Missing

## Problem Statement

`quality-gate.md` Self-Claiming Workflow defers to TEAM.md for "Agent Protocol" and then lists steps 2-9. Step 1 (checking TaskList for available editing tasks) is absent from the numbered sequence. An agent reading quality-gate.md sequentially encounters "Step 2: Verify Draft is Complete" without a Step 1 explaining when and how to call TaskList.

## Findings

**quality-gate.md Self-Claiming Workflow:**
```
Follow **Agent Protocol** in `.claude/agents/TEAM.md`.

**Step 2: Verify Draft is Complete**
...
```

Step 1 is missing. TEAM.md's Agent Protocol Step 1 is "Check for tasks: TaskList()." But the Quality Gate file's unique requirement — checking for `metadata["ready_for"] == "quality-gate"` before claiming — belongs in Step 1, not buried in a reference to TEAM.md.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add Step 1 explicitly to quality-gate.md (Recommended)

```
**Step 1: Check for available editing tasks**
TaskList() — look for tasks with keywords: editing, quality gate, review, approve.
Status: pending. Owner: empty. blockedBy: empty.
Before claiming, verify: TaskGet(taskId).metadata["ready_for"] == "quality-gate"
```

This makes the section self-contained without requiring the agent to cross-reference TEAM.md for the first step.

**Effort:** Trivial — add 4 lines to quality-gate.md

## Acceptance Criteria

- [ ] quality-gate.md Self-Claiming Workflow begins at Step 1, not Step 2
- [ ] The unique QG pre-claim check (ready_for metadata) appears in Step 1
- [ ] An agent reading only quality-gate.md knows to call TaskList before any other step

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
