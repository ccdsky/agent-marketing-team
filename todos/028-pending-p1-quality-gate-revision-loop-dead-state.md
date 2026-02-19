---
status: pending
priority: p1
issue_id: "028"
tags: [code-review, quality-gate, revision-loop, creative-specialist, coordination]
---

# Quality Gate Revision Loop Creates Dead State — Creative Specialist Cannot Find Feedback

## Problem Statement

`quality-gate.md` Step 7B creates a revision task for the Creative Specialist, but the revision task contains no reference to where the feedback actually lives. The Creative Specialist claims the revision task, calls `TaskGet` on it, and finds no feedback — because the feedback is stored on the QG editing task, not the revision task. The link between the two tasks is never established.

Additionally, `TaskUpdate(status="pending")` on the QG editing task is semantically wrong — it implies the task is unclaimed and available for another agent to grab.

## Findings

**quality-gate.md Step 7B creates:**
```
TaskCreate(
  subject="[S2] Revise [asset] — QG feedback round [N]",
  description="Revisions needed. See editorial feedback in QG task metadata."
)
```

"QG task metadata" is undefined — which QG task? The Creative Specialist has no way to know the editing task ID without it being passed explicitly. In a campaign with multiple assets in parallel revision, this is completely ambiguous.

Then:
```
TaskUpdate(taskId="[ID]", status="pending", ...)
```

Setting the completed editing task back to `pending` makes it reclaimable by any agent.

**Identified by:** architecture-strategist, agent-native-reviewer

## Proposed Solutions

### Option A: Pass editing task ID in revision task description (Recommended)

```
TaskCreate(
  subject="[S2] Revise [asset] — QG feedback round [N]",
  description="QG review complete. Retrieve feedback: TaskGet(taskId='[EDITING-TASK-ID]') → read metadata fields: voice, clarity, craft, positioning, action_items.",
  metadata={"blocked_asset": "[asset]", "revision_round": N}
)
```

Set QG editing task to `status="completed"` (not pending) with `metadata={"revision_required": true}`.

**Effort:** Small — one edit to quality-gate.md Step 7B

### Option B: QG writes feedback to the revision task metadata directly

Quality Gate creates the revision task and immediately sets its metadata with the full feedback, so Creative Specialist only needs to read the revision task itself. No cross-task lookup needed.

**Effort:** Small — requires QG to duplicate feedback into two task metadata sets

## Acceptance Criteria

- [ ] Revision task description explicitly contains the editing task ID for Creative Specialist to call `TaskGet` on
- [ ] QG editing task is set to `status="completed"` (not pending) when revision is required
- [ ] A Creative Specialist claiming a revision task can retrieve the full action items without human help

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist and agent-native-reviewer
