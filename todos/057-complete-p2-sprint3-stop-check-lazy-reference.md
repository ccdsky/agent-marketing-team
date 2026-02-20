---
status: pending
priority: p2
issue_id: "057"
tags: [code-review, delegation, stop-check, campaign-lead]
---

# Sprint 3 STOP CHECK Uses "Same as Sprint 2" Lazy Reference

## Problem Statement

The Sprint 3 Kickoff Protocol STOP CHECK reads "Same as Sprint 2 — if you find yourself writing content or creating files in specialist-owned directories, STOP and spawn the appropriate specialist." An LLM resolving "same as Sprint 2" must scroll back through the document to find the Sprint 2 STOP CHECK text. In a long file this is a context hazard. The lazy reference also introduces subtle risk: if Sprint 2's STOP CHECK is ever updated, Sprint 3's would silently become out of sync.

## Findings

**Sprint 2 STOP CHECK (correct):**
```
STOP CHECK: If you find yourself reading a skill file, writing a draft, or creating a file in `drafts/` or `edited/` — STOP. You are violating the delegation model. Spawn the appropriate specialist instead.
```

**Sprint 3 STOP CHECK (current):**
```
STOP CHECK: Same as Sprint 2 — if you find yourself writing content or creating files in specialist-owned directories, STOP and spawn the appropriate specialist.
```

**File:** `.claude/agents/campaign-lead.md`, Sprint 3 Kickoff Protocol, final line
**Identified by:** code-simplicity-reviewer

## Proposed Solution

Replace Sprint 3 STOP CHECK with the identical text from Sprint 2:

```
**STOP CHECK:** If you find yourself reading a skill file, writing a draft, or creating a file in `drafts/` or `edited/` — STOP. You are violating the delegation model. Spawn the appropriate specialist instead.
```

**Effort:** Trivial
**Risk:** None

## Acceptance Criteria

- [ ] Sprint 3 STOP CHECK contains identical text to Sprint 2 (no forward/backward reference)

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by code-simplicity-reviewer.
