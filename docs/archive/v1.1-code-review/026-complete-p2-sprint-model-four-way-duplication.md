---
status: pending
priority: p2
issue_id: "026"
tags: [code-review, simplicity, duplication, sprint-model]
---

# Sprint Model Is Fully Described in Four Separate Places (~150 Lines)

## Problem Statement

The three-sprint structure (Plan & Sketch → Refine & Deepen → Execute & Ship) with its goals, durations, and deliverables appears in:
1. `TEAM.md` "Sprint Model: Iterative Validation" (lines 57-93) — full description
2. `CLAUDE.md` "Sprint model" core principles — summary plus example flow
3. `campaign-lead.md` — Sprint 1, 2, 3 preamble sections before task breakdowns
4. `sprint-planning.md` — entire workflow file for the same three sprints

Campaign Lead reads campaign-lead.md (its own definition) and may read sprint-planning.md. TEAM.md is read at activation. CLAUDE.md is always loaded. This means the sprint model is loaded 3-4 times into context for every campaign session.

## Proposed Solution

- `TEAM.md` — Keep as canonical home of sprint philosophy (one time)
- `sprint-planning.md` — Keep as executable workflow with task names (one time)
- `campaign-lead.md` — Remove sprint preamble text; keep only task breakdown tables. Add: "Sprint structure: see TEAM.md. Task templates: see sprint-planning.md."
- `CLAUDE.md` — Reduce to one-line reference: "Sprint model: see TEAM.md"

**Effort:** Medium — targeted removals in campaign-lead.md and CLAUDE.md

## Acceptance Criteria

- [ ] Sprint model philosophy appears once (TEAM.md)
- [ ] Executable sprint task templates appear once (sprint-planning.md)
- [ ] campaign-lead.md does not restate sprint goals/durations
- [ ] CLAUDE.md references rather than restates the sprint model

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
