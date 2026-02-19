---
status: pending
priority: p2
issue_id: "038"
tags: [code-review, CLAUDE.md, routing, precedence, multi-keyword]
---

# CLAUDE.md Routing Has No Precedence Rule — Multi-Keyword Requests Are Ambiguous

## Problem Statement

`CLAUDE.md` routing rules use keyword matching to direct requests to agents. When a single request matches multiple routing blocks (e.g., "Create a lead generation campaign with positioning angles" matches both Campaign Lead and Research Specialist), there is no rule for which agent takes precedence. In Campaign Mode, re-routing to individual specialists is also wrong — Campaign Lead should spawn them internally, not re-route.

## Findings

**CLAUDE.md routing blocks:**
- Campaign Lead: "campaign, marketing campaign, lead generation..."
- Research Specialist: "positioning angles, differentiation angles..."
- Creative Specialist: "lead magnet strategy..."

A request like "Create a lead generation campaign with positioning angles" matches Campaign Lead (campaign), Research Specialist (positioning angles), and potentially Creative Specialist (lead magnet). No precedence rule exists.

Additionally: if an LLM is already operating as Campaign Lead and encounters a sub-request that would normally route elsewhere, should it re-route or spawn internally? The routing section says nothing about this.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add precedence rule at top of Routing Rules section (Recommended)

```
## Routing Precedence

1. **Campaign Lead** — takes precedence for any multi-asset, sprint, or campaign request
2. **Individual specialists** — only for Simple Mode single-asset requests
3. **Never re-route mid-campaign** — Campaign Lead spawns specialists internally

Multi-keyword requests: if the request involves a campaign or multiple assets, always route to Campaign Lead regardless of other keywords present.
```

**Effort:** Small — add one block at top of Routing Rules in CLAUDE.md

## Acceptance Criteria

- [ ] CLAUDE.md includes a routing precedence rule for multi-keyword requests
- [ ] Campaign Lead takes precedence over specialist routing for campaign-scale requests
- [ ] The difference between Simple Mode routing and Campaign Mode internal spawning is explicit

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
