---
status: pending
priority: p2
issue_id: "017"
tags: [code-review, token-efficiency, skill-structure, thought-leader-foundations]
---

# Thought Leader Foundations Sections Add ~75 Lines of Token Overhead Per Skill Invocation

## Problem Statement

Each of the 5 strategy skills includes a "Thought Leader Foundations" section (approximately 12-15 lines each) attributing methodological sources (Hormozi, Dunford, Fishkin, Laja, Ellis, etc.). These sections are purely documentary — the actual methodologies are operationalized in the Framework steps that follow. Agents reading SKILL.md files to execute tasks consume these sections as tokens but gain no additional execution guidance from them, since the same concepts appear in the step-by-step instructions.

Across 5 skills invoked in a typical Sprint 1, this adds ~75 lines of attribution text to context on every campaign execution.

## Findings

**Example from positioning-angles/SKILL.md:**
> "## Thought Leader Foundations
> April Dunford — Obviously Awesome: Five-component positioning model (competitive alternatives, unique attributes, value for buyers, target customer characteristics, market category)
> Peep Laja — Conversion XL: Four-layer messaging hierarchy (category claim, POD, proof, resonance test)
> Chris Walker — Refine Labs: Demand creation vs. demand capture distinction (dark funnel, brand-to-demand)
> [8 more lines]"

This section appears in all 5 strategy skills. The concepts are then re-explained in the Framework section with actual instructions. The attribution section is not referenced by any step.

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Move Thought Leader Foundations to a single reference file (Recommended)

Create `.claude/skills/METHODOLOGY-SOURCES.md` as a reference document containing all thought leader attributions in one place.

In each skill's Thought Leader Foundations section, replace with:
> "**Methodology sources:** April Dunford, Peep Laja, Chris Walker (see `.claude/skills/METHODOLOGY-SOURCES.md`)"

One line per skill instead of 12-15. The reference file is consulted only if someone wants to understand the sources.

**Pros:** Reduces per-skill invocation token cost by ~12 lines; preserves attribution for documentation purposes
**Cons:** Breaks inline readability of each skill — reader must follow a reference
**Effort:** Small — create reference file, update 5 skill headers

### Option B: Remove Thought Leader Foundations entirely

The framework steps already implement the methodologies — attribution is implicit in the instructions. Remove the sections as non-operational.

**Pros:** Maximum token reduction
**Cons:** Loses educational value; harder to understand why specific steps exist
**Effort:** Small

### Option C: Keep but truncate to one-line citations

Reduce each entry to: "Dunford positioning model, Laja messaging hierarchy, Walker demand creation (see also: Obviously Awesome, CXL, Refine Labs)"

Reduces from ~15 lines to 2-3 lines per skill.

**Pros:** Minimal change; retains attribution; significant token reduction
**Cons:** Still some overhead on each invocation
**Effort:** Trivial

## Acceptance Criteria

- [ ] Thought Leader Foundations sections are either consolidated, truncated, or replaced with references
- [ ] Each skill's context load is reduced by at least 10 lines compared to current state
- [ ] Attribution to source thinkers is preserved in some form

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
