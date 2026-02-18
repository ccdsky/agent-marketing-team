---
status: pending
priority: p3
issue_id: "013"
tags: [code-review, creative-specialist, skills, v2.0]
---

# /positioning-angles v1.1 Constraint Not Reflected in creative-specialist.md Skill List

## Problem Statement

`campaign-lead.md` was patched with a v1.1 note for the positioning-angles task. But `creative-specialist.md`'s skill list (entries 8-12) still lists `/positioning-angles`, `/keyword-research`, `/market-research`, `/expert-review`, and `/lead-magnet-strategy` as available skills without any v1.1 constraint annotation.

An agent reading the Creative Specialist's skill list would believe all 12 skills are ready to invoke.

Note: This overlaps with todo #007 (Research Specialist). Together they cover the same root cause: v2.0 skills are described as if they exist in v1.1.

## Fix

In `creative-specialist.md` skill list entries 8-12, add a status line:
```
**Status (v1.1):** Not yet implemented. Do not invoke. Generate inline from research.
```

**Effort:** Small — ~5 lines in creative-specialist.md

## Work Log

- 2026-02-18: Identified by architecture-strategist during PR review
