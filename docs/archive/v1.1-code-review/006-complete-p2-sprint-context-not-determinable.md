---
status: pending
priority: p2
issue_id: "006"
tags: [code-review, agent-coordination, sprint-model, task-naming]
---

# Sprint Context Not Determinable at Runtime

## Problem Statement

`creative-specialist.md` defines distinct behaviors per sprint:
- Sprint 1: sketches only, no expert review
- Sprint 2: full drafts, run expert review
- Sprint 3: polish pass, no new features

`quality-gate.md` has different approval thresholds per sprint:
- Sprint 2: 7/10 minimum
- Sprint 3: 8/10 minimum

But no agent has a reliable way to know which sprint it's in when claiming a task. TaskGet returns task details, but sprint membership is conveyed only if Campaign Lead includes it in the task title or description. sprint-planning.md shows task names like `"Draft — Lead magnet: [title]"` with no sprint prefix.

## Findings

- `creative-specialist.md`: sprint-specific behavior defined but not queryable
- `quality-gate.md`: sprint-specific thresholds defined but not queryable
- `sprint-planning.md`: task name templates have no sprint prefix
- `TaskUpdate` metadata could carry sprint but is inconsistently documented (see also todo #001)

**Identified by:** agent-native-reviewer + architecture-strategist

## Proposed Solution

Standardize task naming in `sprint-planning.md` to include sprint prefix:
```
TaskCreate: "[S2] Draft — Lead magnet: [title]"
TaskCreate: "[S3] Revise — Lead magnet (based on Sprint 2 feedback)"
```

Document this convention in sprint-planning.md:
```
**Task naming convention:** Prefix all tasks with [S1], [S2], or [S3] to indicate sprint.
```

Then update `creative-specialist.md` and `quality-gate.md` to check the task title prefix when determining sprint-specific behavior.

**Effort:** Small — naming convention + 2 agent file updates

## Acceptance Criteria

- [ ] sprint-planning.md task names include [S1]/[S2]/[S3] prefix
- [ ] creative-specialist.md checks sprint prefix to determine behavior
- [ ] quality-gate.md checks sprint prefix to determine approval threshold

## Work Log

- 2026-02-18: Identified by agent-native-reviewer + architecture-strategist during PR review
