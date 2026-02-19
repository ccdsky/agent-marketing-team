---
status: pending
priority: p2
issue_id: "011"
tags: [code-review, architecture, lead-magnet-strategy, file-paths, domain-ownership]
---

# Lead Magnet Strategy Standalone Output Path Writes to Research Specialist Domain

## Problem Statement

`lead-magnet-strategy/SKILL.md` defines two output paths depending on context:
- Campaign mode: `output/campaigns/[slug]/strategy/lead-magnet-concept-[date].md` ✓
- Standalone mode: `knowledge/research/lead-magnet-concept-[date].md` ✗

The standalone path writes to `knowledge/research/` which is the Research Specialist's domain (market research, competitor analysis, keyword research packages all live there). Lead magnet strategy is a creative concept brief, not a research package. Writing it to `knowledge/research/` creates category confusion and pollutes the research corpus with strategy output.

## Findings

**lead-magnet-strategy/SKILL.md standalone output path:**
> "Standalone (no campaign): save to `knowledge/research/lead-magnet-concept-[date].md`"

**knowledge/research/ directory purpose** (from knowledge/README.md):
> "Research packages: market intelligence created by Research Specialist"

Lead magnet strategy output is a creative concept brief with hook, mechanism, name options, Value Equation score, and delivery plan — not market intelligence.

**Identified by:** architecture-strategist, code-simplicity-reviewer

## Proposed Solutions

### Option A: Route standalone output to output/drafts/ (Recommended)

Update standalone path to:
> `output/drafts/lead-magnet-concept-[date].md`

This matches how creative-specialist.md handles simple mode output:
> "Simple Mode (no active campaign): use `output/drafts/[YYYY-MM-DD]-[asset-type].md`"

**Pros:** Consistent with simple mode conventions; doesn't pollute research corpus; logical for concept briefs
**Cons:** None
**Effort:** Small — change one path in lead-magnet-strategy/SKILL.md

### Option B: Add knowledge/strategy/ subdirectory

Create `knowledge/strategy/` for strategy briefs (positioning angles, lead magnet concepts) separate from `knowledge/research/`.

**Pros:** Clear separation of research vs. strategy artifacts
**Cons:** Adds directory complexity; strategy briefs are campaign-specific, not reusable knowledge assets
**Effort:** Small but adds structure overhead

## Acceptance Criteria

- [ ] Standalone lead magnet strategy output does not write to `knowledge/research/`
- [ ] Standalone path is consistent with how other standalone creative outputs are saved
- [ ] `knowledge/research/` remains exclusively for Research Specialist deliverables

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
