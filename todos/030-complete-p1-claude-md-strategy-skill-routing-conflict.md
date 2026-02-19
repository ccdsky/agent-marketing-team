---
status: pending
priority: p1
issue_id: "030"
tags: [code-review, routing, CLAUDE.md, research-specialist, creative-specialist, strategy-skills]
---

# CLAUDE.md Strategy Skill Routing Conflict Between Research Specialist and Creative Specialist

## Problem Statement

`CLAUDE.md` routing rules assign "positioning angles" and "differentiation angles" to the Research Specialist, and "lead magnet strategy" to the Creative Specialist. But skill files indicate the opposite for positioning angles and an ambiguous split for lead magnet strategy. In Simple Mode, a request like "generate positioning angles for my product" has two agents with competing claims and no resolution rule.

## Findings

**CLAUDE.md Research Specialist keywords:**
> "positioning angles, differentiation angles, competitive positioning"

**CLAUDE.md Creative Specialist keywords:**
> "lead magnet strategy, lead magnet concept"

**positioning-angles/SKILL.md** invocation note:
> "Invoke when: Research Specialist executes this as part of Sprint 1 strategy phase"

**research-specialist.md** (line 409) explicitly lists positioning-angles as a strategy skill it owns.

**creative-specialist.md** (line 89) also lists:
> "Lead magnet strategy (concept brief) → `Read(file_path=".claude/skills/lead-magnet-strategy/SKILL.md")`"

In Campaign Mode, task assignment resolves ownership. In Simple Mode, the routing is ambiguous. There is also no precedence rule for when a single request matches multiple agent keyword sets.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Consolidate — all strategy skills route to Research Specialist (Recommended)

Routing rule: strategy skills (positioning-angles, market-research, keyword-research, lead-magnet-strategy, expert-review) → Research Specialist. Content creation skills → Creative Specialist.

Update CLAUDE.md to:
- Add `lead-magnet-strategy, lead-magnet concept` to Research Specialist keywords
- Remove `lead-magnet strategy, lead-magnet concept` from Creative Specialist keywords
- Add a precedence note: "Multi-keyword requests: Campaign Lead takes precedence. Strategy-only requests: Research Specialist. Content creation: Creative Specialist."

**Effort:** Small — routing table edit in CLAUDE.md

### Option B: Add disambiguation note per routing block

Keep current assignment but add a note under each block clarifying that overlap requests go to Campaign Lead:

> "If request involves both strategy and content creation, route to Campaign Lead."

**Effort:** Trivial — 1 line per routing block

## Acceptance Criteria

- [ ] A Simple Mode "generate positioning angles" request routes unambiguously to one agent
- [ ] A Simple Mode "create a lead magnet strategy" request routes unambiguously to one agent
- [ ] CLAUDE.md includes a precedence rule for multi-keyword requests

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
