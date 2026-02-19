---
status: pending
priority: p2
issue_id: "042"
tags: [code-review, TEAM.md, self-claiming, role-filter, campaign-mode, coordination]
---

# Self-Claiming Protocol Has No Role Filter — Agents Could Claim Wrong Task Types

## Problem Statement

`TEAM.md` Agent Protocol tells agents to claim tasks with "status pending, owner empty, blockedBy empty" — but does not tell agents to filter by their role. In Campaign Mode with multiple specialist subagents active simultaneously, a Creative Specialist could claim a research task or editing task if the task subject doesn't contain one of its expected keywords.

## Findings

**TEAM.md Agent Protocol Step 1:**
> "Check for tasks: TaskList(). Look for status: pending, owner: empty, blockedBy: empty."

No role filtering. The task keyword lists exist in individual agent files, but the canonical Agent Protocol in TEAM.md doesn't reference them.

**creative-specialist.md** documents task keywords: "write, draft, create, content, expert review, lead magnet strategy"

But if Campaign Lead creates a task with a subject like "Lead magnet concept brief" (which a Research Specialist should own), and Creative Specialist runs TaskList() and finds no pending tasks with "write/draft/create," it may still claim adjacent tasks.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Add role keyword filter to Agent Protocol in TEAM.md (Recommended)

After the TaskList step, add:

```
**Before claiming, verify the task matches your role keywords:**
- Research Specialist: "research", "competitor", "customer language", "positioning", "keyword", "market"
- Creative Specialist: "draft", "write", "revise", "expert review", "lead magnet strategy"
- Quality Gate: "quality gate", "editorial", "review", "edit"
- Distribution Specialist: "format", "publish", "distribution", "analytics", "performance"

If no unclaimed task matches your role keywords:
→ Do not claim any task.
→ Escalate: "No available tasks for [role]. TaskList shows: [pending tasks]."
```

**Effort:** Small — add one section to TEAM.md Agent Protocol

## Acceptance Criteria

- [ ] TEAM.md Agent Protocol includes role-keyword filtering before claiming
- [ ] Each agent file's task keywords list is treated as the filter set
- [ ] An agent with no matching tasks escalates rather than claiming an inappropriate task

## Work Log

- 2026-02-19: Identified during v1.3 code review by agent-native-reviewer
