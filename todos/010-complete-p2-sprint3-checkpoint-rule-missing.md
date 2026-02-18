---
status: pending
priority: p2
issue_id: "010"
tags: [code-review, CLAUDE.md, sprint-model, behavioral-directive]
---

# CLAUDE.md Trim Removed "No Sprint 3 Checkpoint" Behavioral Directive

## Problem Statement

The trimmed CLAUDE.md summarizes the sprint model as:
```
Sprint 1: strategy (checkpoint) → Sprint 2: drafts (checkpoint) → Sprint 3: ship.
```

The critical "no Sprint 3 checkpoint" rule is missing from CLAUDE.md. TEAM.md carries it, and sprint-planning.md states it, but CLAUDE.md is the first file loaded in every conversation. An agent that only scans CLAUDE.md before starting a campaign could present an unnecessary Sprint 3 checkpoint to the user.

The behavioral directive "Sprint 3 has no checkpoint — execute approved direction" is operationally important enough to survive in the routing document.

## Proposed Solution

Add one line to CLAUDE.md's sprint model summary:
```
**Sprint model** — Sprint 1: strategy (checkpoint) → Sprint 2: drafts (checkpoint) → Sprint 3: ship (no checkpoint — execute approved direction).
```

**Effort:** Trivial — 1 line edit in CLAUDE.md

## Acceptance Criteria

- [ ] CLAUDE.md explicitly states Sprint 3 has no checkpoint
- [ ] Behavioral directive is not hidden in a secondary file

## Work Log

- 2026-02-18: Identified by architecture-strategist during PR review
