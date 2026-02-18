---
status: pending
priority: p2
issue_id: "014"
tags: [code-review, duplication, market-research, keyword-research, audience-behavior]
---

# Audience Behavior Map Duplicated in Market Research and Keyword Research

## Problem Statement

`market-research/SKILL.md` Phase 2c produces an "Audience Behavior Map" covering channel preferences, content consumption patterns, and watering holes. `keyword-research/SKILL.md` Step 3 instructs agents to "map audience behavior" covering the same dimensions (channels, content formats, community sources). When a campaign runs both skills, agents execute this work twice with no mechanism to skip the duplicate.

In a campaign, market-research always precedes keyword-research. The audience behavior data from market-research is available when keyword-research starts — but keyword-research has no instruction to check for and reuse existing audience behavior output.

## Findings

**market-research/SKILL.md Phase 2c output:**
> "Audience Behavior Map: where they consume content, formats they prefer, communities they trust"

**keyword-research/SKILL.md Step 3:**
> "Map audience behavior: channels, content formats, community sources"

These are equivalent work products. No cross-reference exists in either skill to avoid duplication.

**campaign flow:** market-research → positioning-angles → keyword-research
By the time keyword-research runs, audience behavior data exists in `knowledge/research/market-research-[topic]-[date].md`

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Add pre-check to keyword-research Step 3 (Recommended)

Update keyword-research/SKILL.md Step 3 to:

```
## Step 3: Audience Behavior Mapping

**If market-research output exists for this campaign:** Read the Audience Behavior Map from
`knowledge/research/market-research-[topic]-[date].md` Phase 2c. Skip re-execution of this step.
Extract: channels, content formats, community sources → proceed to Step 4.

**If no prior market-research:** Execute audience behavior mapping [existing Step 3 content].
```

**Pros:** Eliminates redundant work; uses higher-quality research from dedicated market-research skill
**Cons:** Requires keyword-research agent to know where to find market-research output (soluble with standard path pattern)
**Effort:** Small — add conditional check to Step 3

### Option B: Remove audience behavior from keyword-research, declare it a market-research dependency

Note in keyword-research/SKILL.md: "Requires market-research output. Run market-research first. Audience behavior data is consumed from market-research Phase 2c output."

**Pros:** Clean dependency declaration; simplifies keyword-research
**Cons:** Breaks keyword-research as a standalone skill (can't run without prior market-research)
**Effort:** Small

## Acceptance Criteria

- [ ] keyword-research/SKILL.md Step 3 checks for existing audience behavior data before re-executing
- [ ] A campaign running both skills does not produce duplicate audience behavior analysis
- [ ] Standalone keyword-research (no prior market-research) still has a path through Step 3

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
