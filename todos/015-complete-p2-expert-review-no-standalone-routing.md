---
status: pending
priority: p2
issue_id: "015"
tags: [code-review, routing, expert-review, agent-native]
---

# Expert Review Skill Has No Defined Agent Owner for Standalone Invocation

## Problem Statement

When a user directly requests "expert review this landing page", there is no defined routing to an agent or a defined standalone invocation path. The expert-review skill is listed under Creative Specialist's skill set (Step 8), but it is also useful independently — a user may want to run expert review on an asset from a previous campaign or on content they wrote themselves. No routing rule covers this case, and the skill itself doesn't define who runs it.

## Findings

**CLAUDE.md routing table:** No entry for `/expert-review`

**creative-specialist.md:** Lists expert-review as Step 8 of creative workflow — assumes it's always called in context of asset creation, not standalone

**expert-review/SKILL.md:** No "Owner" or "Invoked by" section. First instruction is "Step 1: Receive asset file path" — assumes calling context always provides this, but standalone invocations need the agent to ask for it.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Add standalone invocation section to expert-review/SKILL.md + CLAUDE.md routing (Recommended)

Add to expert-review/SKILL.md at the top:

```
## Invocation

**Via creative-specialist (Campaign Mode):** Creative Specialist calls this after completing Sprint 2 draft.
Asset path is provided in context.

**Standalone (Direct Request):** Route to Creative Specialist. Creative Specialist asks:
1. "What's the path to the asset you want reviewed?" (or accepts pasted content)
2. "What asset type is it?" (landing page / lead magnet / email sequence / blog post)
Then proceeds to Step 1.
```

Add to CLAUDE.md Creative Specialist routing keywords: `expert review, expert panel, review this [asset type], get expert feedback`

**Pros:** Complete coverage; clear ownership; consistent with how other standalone skills work
**Cons:** Creative Specialist routing now covers both creation AND review — slight role blurring
**Effort:** Small

### Option B: Route expert review to Quality Gate

Quality Gate already does editorial review. Add expert-review as an optional pre-step Quality Gate can invoke.

**Pros:** Quality Gate is the review agent; logical ownership
**Cons:** Quality Gate's workflow is simple and focused; adding multi-agent Task spawning to Quality Gate increases complexity significantly
**Effort:** Medium

## Acceptance Criteria

- [ ] Standalone "expert review this [asset]" request has a defined routing path in CLAUDE.md
- [ ] expert-review/SKILL.md defines how to receive standalone invocation (get asset path, get asset type)
- [ ] The routing agent is clearly identified

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
