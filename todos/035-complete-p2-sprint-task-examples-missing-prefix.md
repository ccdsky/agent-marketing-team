---
status: pending
priority: p2
issue_id: "035"
tags: [code-review, campaign-lead, sprint-prefix, task-naming, sprint-detection]
---

# Sprint Task Breakdown Examples Missing [S1]/[S2]/[S3] Prefixes — Breaks Downstream Sprint Detection

## Problem Statement

`campaign-lead.md` Sprint 1 task breakdown examples use number-only prefixes like `[1]`, `[2]`, `[3]` rather than the `[S1]`, `[S2]`, `[S3]` convention defined in `sprint-planning.md`. Since `creative-specialist.md` and `quality-gate.md` detect sprint context from the `[S1]`/`[S2]`/`[S3]` task title prefix to determine behavior (draft depth, review thresholds), tasks created without the prefix cause agents to fall through sprint-detection logic.

## Findings

**campaign-lead.md Sprint 1 breakdown examples** use:
```
[1] Market research (Research Specialist, 4h)
[2] Positioning angles (Research Specialist, 2h)
...
```

**sprint-planning.md** defines the convention:
```
TaskCreate("[S1] Market research — ...")
```

**creative-specialist.md** (line 236):
> "Determine your sprint from the task title. All tasks are prefixed [S1], [S2], or [S3]."

**quality-gate.md** (line 580):
> "Determine sprint context from task title prefix [S1]/[S2]/[S3]"

The inline task breakdown in campaign-lead.md is the most likely pattern to be copied when agents create tasks. It must model the correct convention.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Update all task breakdown examples to use [S1]/[S2]/[S3] prefix (Recommended)

Update every task in the Sprint 1, 2, and 3 task breakdown tables to use `[S1]`, `[S2]`, `[S3]` prefixes:

```
[S1] Market research (Research Specialist, 4h) - BLOCKED_BY: none
[S1] Positioning angles (Research Specialist, 2h) - BLOCKED_BY: [research]
```

**Effort:** Small — find/replace in campaign-lead.md task breakdown tables

## Acceptance Criteria

- [ ] Every task in campaign-lead.md's sprint breakdown examples uses `[S1]`/`[S2]`/`[S3]` prefix
- [ ] The convention is consistent between campaign-lead.md examples and sprint-planning.md task creation calls
- [ ] A Creative Specialist or Quality Gate claiming a task can determine sprint from the task title prefix

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
