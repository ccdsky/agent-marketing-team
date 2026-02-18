---
status: pending
priority: p1
issue_id: "005"
tags: [code-review, architecture, task-ownership, expert-review]
---

# Expert Review Task Ownership Ambiguous

## Problem Statement

`campaign-lead.md` Sprint 2 task breakdown lists expert review tasks as owned by Creative Specialist:
```
[11] Expert review: Lead magnet (Creative Specialist, 1h) - BLOCKED_BY: [8]
```

`sprint-planning.md` Sprint 2 task list creates expert review tasks with no owner:
```
TaskCreate: "Expert review — Lead magnet"
TaskCreate: "Expert review — Landing page"
```

Then immediately lists a separate Quality Gate task — suggesting expert review may belong to Quality Gate, Campaign Lead, or be a different kind of task entirely.

`creative-specialist.md` Step 8 ("Optional: Run Expert Review") confirms this is a Creative Specialist responsibility. But sprint-planning.md's unnamed tasks mean any agent scanning TaskList will see unclaimed "Expert review" tasks with no owner indication.

## Findings

- `campaign-lead.md` lines 235-244: expert review = Creative Specialist
- `sprint-planning.md` lines 91-93: expert review = no owner assigned
- `creative-specialist.md` Step 8: expert review is Creative Specialist's optional step
- `quality-gate.md`: no mention of expert review as its responsibility

**Identified by:** architecture-strategist

## Proposed Solution

Add owner to TaskCreate calls in sprint-planning.md, matching what campaign-lead.md already defines:
```
TaskCreate: "Expert review — Lead magnet"
→
TaskCreate: "Expert review — Lead magnet (Creative Specialist runs Task tool)"
```

Or add a note in sprint-planning.md:
```
**Note:** Expert review tasks are claimed and executed by the Creative Specialist using the Task tool to spawn subagents. They are NOT Quality Gate tasks.
```

**Effort:** Small — 3-line clarification in sprint-planning.md

## Acceptance Criteria

- [ ] sprint-planning.md expert review tasks indicate Creative Specialist ownership
- [ ] No ambiguity between expert review (Creative Specialist, Task tool subagents) and Quality Gate review (editorial rubric)

## Work Log

- 2026-02-18: Identified by architecture-strategist during PR review
