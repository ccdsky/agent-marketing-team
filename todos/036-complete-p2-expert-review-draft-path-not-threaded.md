---
status: pending
priority: p2
issue_id: "036"
tags: [code-review, expert-review, campaign-lead, creative-specialist, metadata, task-threading]
---

# Expert Review Tasks Don't Specify How to Retrieve the Draft Path — "Provided in Context" Is Undefined

## Problem Statement

`campaign-lead.md` Sprint 2 expert review tasks include no instruction for how the reviewing agent finds the draft file. `expert-review/SKILL.md` says the asset path is "provided in context" for campaign mode but never defines what "context" means operationally — the agent must call `TaskGet` on the upstream drafting task to find the deliverable path, but this step is absent from both files.

## Findings

**campaign-lead.md Sprint 2 task 11:**
> "Expert review: Lead magnet (Creative Specialist, 1h) — BLOCKED_BY: [8]"

No instruction to retrieve the draft path from task 8's metadata.

**expert-review/SKILL.md Required Inputs:**
> "Called by Creative Specialist (campaign mode): Asset path and type are provided in context."

"Provided in context" is underspecified. In practice, "context" means the TaskGet metadata of the upstream drafting task — but the agent spawned to run expert review is a fresh subagent that doesn't have this in its conversation context unless it is explicitly told to look.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Embed draft task ID in expert review task description (Recommended)

Campaign Lead creates expert review tasks with the upstream drafting task ID:

```
TaskCreate(
  subject="[S2] Expert review — lead magnet",
  description="Run expert review on lead magnet draft. Read draft path: TaskGet('[DRAFTING-TASK-ID]').metadata['deliverable']. Asset type: lead-magnet.",
  metadata={"drafting_task_id": "[DRAFTING-TASK-ID]"}
)
```

Also update `expert-review/SKILL.md` Required Inputs for campaign mode:
> "Called by Creative Specialist (campaign mode): Read draft path from `TaskGet([drafting-task-ID]).metadata['deliverable']`. The drafting task ID is in this task's description."

**Effort:** Small — update sprint task creation in campaign-lead.md + one line in expert-review/SKILL.md

## Acceptance Criteria

- [ ] Expert review task description contains the upstream drafting task ID
- [ ] expert-review/SKILL.md defines how to retrieve the draft path in campaign mode (not just "provided in context")
- [ ] A fresh subagent spawned for expert review can find the file to review without human help

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
