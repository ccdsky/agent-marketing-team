---
status: pending
priority: p2
issue_id: "024"
tags: [code-review, simplicity, duplication, agent-protocol, self-claiming]
---

# Self-Claiming Workflow Is Duplicated Six Times Across the System (~200 Lines)

## Problem Statement

The self-claiming protocol (TaskList → claim → execute → complete) appears in:
1. `research-specialist.md` lines 32-88 (full workflow, ~56 lines)
2. `creative-specialist.md` lines 34-67 (same steps, ~34 lines)
3. `quality-gate.md` lines 31-80 (same steps, ~50 lines)
4. `distribution-specialist.md` lines 33-119 (same steps, ~86 lines)
5. `sprint-planning.md` lines 189-199 (restated, ~10 lines)
6. `CLAUDE.md` "Quick Start → For Agents" section (~8 lines)

The only meaningful differences between the agent files are:
- Which task keywords to look for
- Whether to claim serially (quality-gate) or can claim multiple (others)

Everything else — the tool calls, the "don't claim if dependencies unclear" check, the TaskUpdate syntax — is word-for-word identical.

This is ~200 lines of duplication that every agent loads in full. When this protocol changes (e.g., if task tool semantics shift), it must be updated in 6 places.

## Proposed Solution

Move the canonical self-claiming protocol to `TEAM.md` under "Agent Protocol." Each agent file is then reduced to:

```markdown
## Self-Claiming Workflow

Follow the **Agent Protocol** in `.claude/agents/TEAM.md`.

**This agent's task keywords:** [write, draft, create, content]

**Claiming behavior:** Standard (can claim multiple tasks simultaneously)
```

Quality Gate adds: "Claiming behavior: Serial only — complete one editing task before claiming the next."

**Effort:** Medium — edit 4 agent files + sprint-planning + CLAUDE.md, expand TEAM.md

## Acceptance Criteria

- [ ] Self-claiming protocol exists once in TEAM.md
- [ ] Each agent file references TEAM.md for the protocol and only specifies its unique keywords/constraints
- [ ] No duplication of TaskList/TaskUpdate/TaskGet syntax across agent files

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
