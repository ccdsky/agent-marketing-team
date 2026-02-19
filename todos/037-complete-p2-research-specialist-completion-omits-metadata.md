---
status: pending
priority: p2
issue_id: "037"
tags: [code-review, research-specialist, metadata, task-completion, handoff]
---

# Research Specialist Completion Example Omits Metadata — Most-Copied Pattern Leaves Deliverable Undiscoverable

## Problem Statement

`research-specialist.md` "Example Research Workflow" Step 5 shows `TaskUpdate(taskId="2", status="completed")` with no metadata. The canonical TEAM.md Agent Protocol requires completion metadata with `deliverable` and `ready_for` fields. The example is the most likely pattern for agents to copy, and it models the wrong behavior — leaving `metadata["deliverable"]` unset breaks downstream discovery by Creative Specialist and Campaign Lead.

## Findings

**research-specialist.md Example Workflow Step 5:**
```python
TaskUpdate(
  taskId="2",
  status="completed"
)
```

**TEAM.md Agent Protocol Step 5 (canonical):**
```python
TaskUpdate(
  taskId="[ID]",
  status="completed",
  metadata={
    "deliverable": "[path to output file]",
    "ready_for": "campaign-lead"
  }
)
```

**research-specialist.md Completion Metadata** (lines 36-42) shows the correct format. But the concrete example that an agent is most likely to copy is the one in the workflow section, which is wrong.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Update the example to include full metadata (Recommended)

```python
TaskUpdate(
  taskId="2",
  status="completed",
  metadata={
    "deliverable": "knowledge/research/dev-cli-pain-points-2026-02-15.md",
    "key_findings": "1. Discoverability (83%) 2. Learning curve (67%) 3. Onboarding (54%)",
    "recommended_angle": "discovery engine",
    "ready_for": "campaign-lead"
  }
)
```

**Effort:** Trivial — replace one code block in research-specialist.md

## Acceptance Criteria

- [ ] The Example Research Workflow completion step includes full metadata in the code block
- [ ] The metadata fields match those defined in the "Completion Metadata" section of research-specialist.md
- [ ] A Campaign Lead or Creative Specialist calling `TaskGet` on a completed research task can find the deliverable path

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
