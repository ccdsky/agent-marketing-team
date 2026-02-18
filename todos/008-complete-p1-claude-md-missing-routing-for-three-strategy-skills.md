---
status: complete
priority: p1
issue_id: "008"
tags: [code-review, blocking, routing, claude-md, agent-native]
---

# CLAUDE.md Missing Routing Rules for Three Strategy Skills

## Problem Statement

`CLAUDE.md` defines routing rules for the 5 agent roles and lists all 12 skills in the Quick Reference, but provides no routing table entries for three of the five new strategy skills:
- `/positioning-angles` — no routing rule
- `/expert-review` — no routing rule  
- `/lead-magnet-strategy` — no routing rule

When a user directly requests "run positioning angles on this research" or "expert review this landing page", there is no routing path defined. The agent will default to an ad-hoc response rather than activating the correct skill via the correct agent.

## Findings

**CLAUDE.md routing table** has entries for:
- Campaign Lead (campaigns, multi-asset)
- Research Specialist (research, market research, keyword research, market-research skill)
- Creative Specialist (write, draft, create, content)
- Quality Gate (review, edit, feedback)
- Distribution Specialist (publish, format, analytics)

The skills list in CLAUDE.md mentions all 12 skills but the routing section does not specify which agent executes `/positioning-angles`, `/expert-review`, or `/lead-magnet-strategy` when directly requested.

**Note:** `/keyword-research` routes to Research Specialist (explicitly mentioned). `/market-research` also routes to Research Specialist. These two are covered.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Add strategy skill keywords to existing agent routing rules (Recommended)

Add to Research Specialist routing keywords:
> `positioning-angles, positioning gaps, differentiation angles, positioning framework`

Add to Creative Specialist routing keywords:
> `expert review, expert panel, lead magnet strategy, lead magnet concept`

This routes:
- positioning-angles → Research Specialist (it uses competitive analysis data)
- expert-review → Creative Specialist (it reviews creative assets)
- lead-magnet-strategy → Creative Specialist (it produces concept briefs, not research packages)

**Pros:** Uses existing routing structure; no new agent needed; routes to logical owners
**Cons:** Requires deciding which agent "owns" each new skill (positioning-angles ownership is debated — see todo 009)
**Effort:** Small — add keyword rows to routing table

### Option B: Add a "Strategy Skills" section to routing

Add a new routing section:
```
### Strategy Skills (Direct Invocation)

| Skill | Route to | When |
|-------|----------|------|
| /positioning-angles | Research Specialist | "Run positioning angles", "Find differentiation angles" |
| /expert-review | Creative Specialist | "Expert review this", "Get expert feedback on" |
| /lead-magnet-strategy | Creative Specialist | "Lead magnet strategy", "Design lead magnet concept" |
```

**Pros:** Clear, scannable; separate from agent routing table
**Cons:** Adds section length to CLAUDE.md
**Effort:** Small

## Acceptance Criteria

- [ ] Direct invocation of `/positioning-angles` routes to a defined agent
- [ ] Direct invocation of `/expert-review` routes to a defined agent  
- [ ] Direct invocation of `/lead-magnet-strategy` routes to a defined agent
- [ ] All 5 strategy skills have a defined routing path in CLAUDE.md

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
