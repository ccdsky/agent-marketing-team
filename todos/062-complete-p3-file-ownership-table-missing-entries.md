---
status: pending
priority: p3
issue_id: "062"
tags: [code-review, file-ownership, documentation-consistency]
---

# File Ownership Table Missing Entries: knowledge/archive/, strategy/, and Ambiguous analytics/ Path

## Problem Statement

Three gaps in file ownership documentation across campaign-lead.md and TEAM.md:

1. `knowledge/archive/` — Retrospective step 5 writes to this directory, but it does not appear in TEAM.md's ownership table or the campaign-lead.md self-check table. Owner should be Campaign Lead (after retrospective).

2. `output/campaigns/[slug]/strategy/` — referenced in research-specialist.md as the output location for positioning angles, but not in TEAM.md's directory structure (lines 23-31), TEAM.md's ownership table, or campaign-lead.md's self-check table. This is an undeclared directory with an undeclared owner.

3. `analytics/` in the self-check table is ambiguous — it could mean `output/campaigns/[slug]/analytics/` (campaign-level tracking plan) or `knowledge/feedback/analytics/` (post-campaign analytics, per TEAM.md's ownership table). Distribution Specialist uses both paths for different purposes.

## Findings

**TEAM.md ownership table (line 20):** Lists `knowledge/feedback/analytics/` — post-campaign knowledge base
**Campaign dir structure (TEAM.md lines 23-31):** Shows `analytics/` as campaign-level subdirectory
**distribution-specialist.md:** Uses both paths for different outputs
**campaign-lead.md self-check table (line 337):** Lists `analytics/` without path qualification

**File:** `.claude/agents/TEAM.md` lines 14-31; `.claude/agents/campaign-lead.md` self-check table
**Identified by:** architecture-strategist, agent-native-reviewer

## Proposed Solution

Update TEAM.md ownership table to add:
- `knowledge/archive/` → Campaign Lead (after retrospective)
- `output/campaigns/[slug]/strategy/` → Research Specialist

Update campaign-lead.md self-check table (if kept) to split `analytics/`:
- `output/campaigns/[slug]/analytics/` → Distribution Specialist (campaign tracking)
- `knowledge/feedback/analytics/` → Distribution Specialist (post-campaign knowledge base)

Or redirect research-specialist.md strategy/ output to `knowledge/research/` where Research Specialist ownership is already established, eliminating the undeclared directory.

**Effort:** Small
**Risk:** Low

## Acceptance Criteria

- [ ] `knowledge/archive/` appears in TEAM.md ownership table with Campaign Lead as owner
- [ ] `strategy/` directory either documented in ownership tables or output path redirected to `knowledge/research/`
- [ ] `analytics/` path qualified in all ownership tables to remove ambiguity

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist.
