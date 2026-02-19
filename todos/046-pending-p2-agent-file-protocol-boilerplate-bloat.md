---
status: pending
priority: p2
issue_id: "046"
tags: [code-review, creative-specialist, quality-gate, TEAM.md, protocol-duplication, verbosity]
---

# Agent Files Restate TaskList/TaskUpdate Protocol — ~150 Lines of Boilerplate Already in TEAM.md

## Problem Statement

`creative-specialist.md` (9-step self-claiming workflow, ~120 lines) and `quality-gate.md` (~30 lines of steps 3-4) both fully restate the TaskList → claim → load context → execute → complete protocol that already lives canonically in TEAM.md's Agent Protocol. These sections are read on every content creation and editorial task, diluting the genuinely unique content (skill mapping, serial editing rule, metadata fields) with protocol boilerplate.

## Findings

**creative-specialist.md Self-Claiming steps 1-4 and step 9** (~80 lines) restate:
- TaskList filtering (TEAM.md steps 1-2)
- TaskUpdate claim (TEAM.md step 3)
- Read context files (TEAM.md step 4)
- TaskUpdate completion (TEAM.md step 5)

**Unique content** not in TEAM.md: skill-to-asset mapping list (step 5), output path rules (step 6), self-assessment requirement (step 7), expert review trigger (step 8).

**quality-gate.md** steps 3-4 restate TaskUpdate claim and file loading — same TEAM.md content.

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Replace boilerplate steps with TEAM.md reference + unique content only (Recommended)

**creative-specialist.md:**
```
## Self-Claiming Workflow

Follow **Agent Protocol** in `.claude/agents/TEAM.md`.

Additionally for creative tasks:

**Step 5: Choose your skill**
[skill mapping table — keep as-is]

**Step 6: Output paths**
[file path rules — keep as-is]

**Step 7: Self-assess**
[self-assessment requirement — keep as-is]

**Step 8: Expert review**
[expert review trigger — keep as-is]
```

**quality-gate.md:** Steps 3-4 become a one-line reference: "Follow TEAM.md Agent Protocol steps 3-4 for claiming and context loading."

**Effort:** Medium — requires careful review of each step to separate unique from boilerplate

## Acceptance Criteria

- [ ] creative-specialist.md self-claiming section is ≤40 lines (from ~120)
- [ ] quality-gate.md boilerplate steps reference TEAM.md
- [ ] No unique operational content is lost — only TEAM.md duplicates are removed
- [ ] Both files still function as standalone agent prompts after the edit

## Work Log

- 2026-02-19: Identified during v1.3 code review by code-simplicity-reviewer
