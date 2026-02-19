---
status: pending
priority: p3
issue_id: "048"
tags: [code-review, verbosity, duplication, research-specialist, creative-specialist, distribution-specialist]
---

# Agent Files Contain Non-Operational Boilerplate — Anti-Patterns, Parallel Workflow, Communicating Sections

## Problem Statement

`research-specialist.md`, `creative-specialist.md`, and `distribution-specialist.md` each contain sections that are documentation for human readers, not operational instructions for agents. These sections increase file length without changing any agent decision: anti-patterns lists (restate the quality checklist in negative form), parallel workflow sections (explain that parallel is faster than serial), and "Communicating with Other Agents" example messages (illustrate what TEAM.md already defines).

## Findings

**research-specialist.md:**
- "Research Anti-Patterns (Avoid These)" (~25 lines) — restates quality checklist in ❌/✅ form
- "Parallel Research Coordination" (~22 lines) — explains that parallel is faster (obvious from task model)
- "Communicating with Other Agents" (~10 lines) — illustrative, already in TEAM.md
- "Example Workflow" steps 1, 2, 4, 5 (~25 lines) — TEAM.md protocol repeated verbatim

**creative-specialist.md:**
- "Content Creation Anti-Patterns (Avoid These)" (~25 lines) — restates quality checklist
- "Parallel Writing Workflow" (~28 lines) — "Writer 1 claims X, Writer 2 claims Y" is implied by the task model
- "Communicating with Other Agents" (~20 lines) — trim to unique content only

**distribution-specialist.md:**
- "Communicating with Other Agents" (~47 lines) — contains full example task comment messages that add no operational constraint

**Total estimated removable content: ~200 lines**

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Delete non-operational sections entirely (Recommended)

- Delete all anti-patterns sections (checklists already encode the same constraints)
- Delete parallel workflow/coordination sections (agents don't need to be told parallel is faster)
- Trim "Communicating with Other Agents" to unique content only (revision task creation in QG is unique; example messages in DS are not)
- Delete Example Workflow steps 1, 2, 4, 5 in research-specialist.md

**Effort:** Medium — requires careful review of each section for any hidden operational content

## Acceptance Criteria

- [ ] No section exists solely to explain why the agent should do something (the what is sufficient)
- [ ] Anti-patterns sections removed — quality checklists cover the same ground
- [ ] Parallel workflow explanation sections removed
- [ ] "Communicating with Other Agents" sections retain only unique operational instructions

## Work Log

- 2026-02-19: Identified during v1.3 code review by code-simplicity-reviewer
