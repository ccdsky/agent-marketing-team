---
status: pending
priority: p2
issue_id: "027"
tags: [code-review, simplicity, duplication, escalation]
---

# Escalation Format Is Duplicated Six Times Across Agent Files (~120 Lines)

## Problem Statement

The escalation format block (Situation / Options / Recommendation / Decision Needed) appears in:
1. `TEAM.md` lines 156-165 (brief version)
2. `CLAUDE.md` "Escalation Protocol" section
3. `campaign-lead.md` lines 482-505 (full markdown format block)
4. `research-specialist.md` lines 469-477 (abbreviated)
5. `creative-specialist.md` lines 437-451
6. `quality-gate.md` lines 641-661
7. `distribution-specialist.md` lines 852-879

Each file also lists its own "when to escalate" triggers, which is agent-specific and should stay. The escalation format itself is not agent-specific and should appear once.

## Proposed Solution

Move the canonical escalation format to `TEAM.md` under "Escalation Protocol." Each agent file reduces to:

```markdown
## When to Escalate

Escalate to Campaign Lead (or to the user if you are Campaign Lead) when:
- [Agent-specific trigger 1]
- [Agent-specific trigger 2]

Use the **Escalation Format** defined in TEAM.md.
```

**Effort:** Small-Medium — edit 5 agent files + CLAUDE.md, expand TEAM.md

## Acceptance Criteria

- [ ] Escalation markdown format exists once in TEAM.md
- [ ] Each agent file only specifies its unique escalation triggers
- [ ] No duplication of the Situation/Options/Recommendation/Decision format

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
