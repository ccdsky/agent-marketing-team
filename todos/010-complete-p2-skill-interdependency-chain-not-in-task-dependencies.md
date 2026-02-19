---
status: pending
priority: p2
issue_id: "010"
tags: [code-review, architecture, task-coordination, skill-dependencies, campaign-lead]
---

# Skill Interdependency Chain Not Expressed at Task Level in Campaign Lead

## Problem Statement

The five strategy skills have a logical execution order:
1. `market-research` → produces landscape and JTBD data
2. `keyword-research` → uses ICP problems (informed by market-research)
3. `positioning-angles` → requires market-research output to map competitive landscape
4. `lead-magnet-strategy` → requires positioning angle to design bridge concept
5. `expert-review` → requires a completed asset to review

This dependency chain exists at the skill level (each skill's "Before You Start" section) but is not expressed in Campaign Lead's task breakdown. Tasks could be claimed out of order, producing positioning angles before market research completes, or running keyword research without JTBD data.

## Findings

**Campaign Lead sprint 1 example tasks:**
- Task [1]: market research
- Task [2]: competitor analysis  
- Task [3]: positioning angles (reads research packages from [1] and [2])
- Task [4]: keyword research

No `blockedBy` relationships are shown between these tasks. An agent could claim Task [4] (keyword research) before Task [1] completes, producing keyword clusters without the JTBD context that makes keyword research meaningful.

**market-research/SKILL.md** says "read ICP profile before starting" — but doesn't reference keyword-research as a downstream consumer that needs this data first.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add explicit blockedBy to Campaign Lead sprint task examples (Recommended)

Update the Campaign Lead Sprint 1 example to show `addBlockedBy` relationships:

```
TaskCreate(
  subject="[S1] Keyword research for [topic]",
  description="...",
  blockedBy=["[market-research task ID]"]  # needs JTBD data first
)

TaskCreate(
  subject="[S1] Positioning angles for [topic]",
  description="...",
  blockedBy=["[market-research task ID]", "[competitor-analysis task ID]"]
)
```

**Pros:** Enforces correct execution order; prevents out-of-order claiming; matches how TaskCreate/addBlockedBy actually works
**Cons:** Campaign Lead must know task IDs at creation time (they do — they create tasks sequentially)
**Effort:** Small — add blockedBy to example task creation calls in campaign-lead.md

### Option B: Document the dependency chain in a separate section

Add to campaign-lead.md: "Strategy Skill Execution Order" section explaining which skills must complete before others can start, without changing example task templates.

**Pros:** Educational; agents can use judgment
**Cons:** Less reliable than enforced task-level dependencies; agents may skip or misread
**Effort:** Trivial

## Acceptance Criteria

- [ ] Campaign Lead Sprint 1 example tasks include `addBlockedBy` relationships between strategy skill tasks
- [ ] positioning-angles task is blocked until market-research and competitor-analysis tasks complete
- [ ] keyword-research task is blocked until market-research task completes

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
