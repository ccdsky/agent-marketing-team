---
status: pending
priority: p2
issue_id: "021"
tags: [code-review, quality-gate, creative-specialist, revision-loop, workflow]
---

# Quality Gate Revision Request Has No Mechanism to Notify Creative Specialist

## Problem Statement

When Quality Gate requests revisions, it calls:
```
TaskUpdate(taskId="[ID]", status="pending")
```

This resets the Quality Gate's *editing* task to pending. But the Creative Specialist's original *writing* task is already marked `completed` — it is not reopened. There is no mechanism to:

1. Signal the Creative Specialist that revision is needed
2. Re-open the writing task for the Creative Specialist to find
3. Create a new revision task (no agent is specified to do this)

A Creative Specialist checking `TaskList()` for pending writing tasks would not see a completed task as needing attention. The Quality Gate's suggestion to "message Creative Specialist (or comment on their writing task)" (quality-gate.md line 188) is not executable — there is no messaging tool, and commenting on a completed task is not a notification mechanism.

The revision loop is architecturally undefined.

## Proposed Solution

**Option A (preferred):** When Quality Gate rejects a draft, it creates a new revision task:
```
TaskCreate("[S2] Revise — [asset] (QG revision request)")
```
with metadata containing the QG feedback. Creative Specialist picks up this new task from TaskList.

**Option B:** Quality Gate reopens the original writing task by setting it to pending:
```
TaskUpdate(taskId="[writing-task-id]", status="pending")
```
This requires the QG to know the writing task ID from the metadata it receives.

**Option C:** Campaign Lead is designated as the revision loop coordinator — QG notifies Campaign Lead, who creates the revision task.

**Effort:** Small — define the pattern in quality-gate.md and TEAM.md

## Acceptance Criteria

- [ ] quality-gate.md specifies the exact mechanism for requesting revisions (creates task or reopens task)
- [ ] Creative Specialist can discover revision requests via TaskList without checking comments on completed tasks
- [ ] Revision task naming follows [S2]/[S3] sprint prefix convention

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
