---
status: pending
priority: p1
issue_id: "029"
tags: [code-review, distribution-specialist, quality-gate, metadata, handoff]
---

# Distribution Specialist Has No Way to Identify the Editing Task ID for Approval Verification

## Problem Statement

`distribution-specialist.md` Self-Claiming Workflow Step 2 instructs the agent to verify QG approval by calling `TaskGet(taskId="[editing-task-ID]")` — but `[editing-task-ID]` is a placeholder with no resolution path. The publishing task that Distribution Specialist claims does not contain the upstream editing task ID. The agent cannot reach the QG approval metadata without it.

## Findings

**distribution-specialist.md Step 2:**
> "Check the editing task's metadata for Quality Gate's approval:
> `TaskGet(taskId="[editing-task-ID]")`"

When Distribution Specialist calls `TaskList()`, it finds a publishing task with `status: pending`. The publishing task has no reference to the editing task. The QG approval signal (`metadata["ready_for"] == "distribution-specialist"`) lives on the editing task.

The agent cannot programmatically find the editing task ID unless it is embedded somewhere in the publishing task.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Campaign Lead embeds editing task ID in publishing task description (Recommended)

When Campaign Lead creates publishing tasks in Sprint 3, include the editing task ID:

```
TaskCreate(
  subject="[S3] Format and publish — [asset]",
  description="Format and publish [asset]. Edited file path: TaskGet([EDITING-TASK-ID]).metadata['deliverable']. Verify QG approval in same metadata.",
  metadata={"editing_task_id": "[EDITING-TASK-ID]"}
)
```

**Effort:** Small — one update to Campaign Lead's Sprint 3 task creation workflow in campaign-lead.md and sprint-planning.md

### Option B: QG writes edited file path directly into the publishing task metadata

Quality Gate's completion step (Step 7A) updates the publishing task with the edited file path, so Distribution Specialist reads it from the task it already claimed.

```
# In quality-gate.md Step 7A:
TaskUpdate(taskId="[publishing-task-ID]", metadata={"edited_file": "[path]", "qg_approved": true})
```

**Effort:** Small — requires QG to know the publishing task ID (which Campaign Lead must pass in the editing task)

## Acceptance Criteria

- [ ] Distribution Specialist can retrieve the edited file path without knowing the editing task ID a priori
- [ ] QG approval is verifiable from the publishing task or its linked metadata
- [ ] The mechanism works in campaigns with multiple simultaneous assets

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
