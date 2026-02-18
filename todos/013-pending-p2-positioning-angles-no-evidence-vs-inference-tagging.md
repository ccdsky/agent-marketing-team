---
status: pending
priority: p2
issue_id: "013"
tags: [code-review, positioning-angles, fabrication, evidence-tagging, scoring-integrity]
---

# Positioning Angles Scoring Has No Evidence vs. Inference Distinction

## Problem Statement

`positioning-angles/SKILL.md` produces scores for each angle on Defensibility, Resonance, and Provability (max 15 points per angle). There is no instruction to distinguish between scores based on actual research evidence vs. scores generated from training-prior inference. A score of "Resonance: 8/5" looks identical whether it's grounded in customer interview data or fabricated from the agent's general knowledge about SaaS buyers.

Decision-makers selecting a positioning angle based on a 14/15 score may not realize that score was manufactured, not measured.

## Findings

**positioning-angles/SKILL.md Step 5 scoring:**
> "Score each angle: Defensibility (1-5), Resonance (1-5), Provability (1-5)"

No instruction to:
- Tag which inputs came from the research package vs. agent inference
- Flag scores as HIGH/MEDIUM/LOW confidence
- Note when Resonance score lacks customer validation data

The market-research skill correctly uses confidence levels (HIGH/MEDIUM/LOW). The positioning-angles skill, which consumes research output, does not carry this confidence tracking forward.

**Identified by:** architecture-strategist, code-simplicity-reviewer

## Proposed Solutions

### Option A: Add confidence tagging to scoring template (Recommended)

Update Step 5 to require agents to tag each score with its evidence source:

```
**Angle: [Name]**
- Defensibility: 4/5 [HIGH — based on 3 competitor analysis findings]
- Resonance: 3/5 [MEDIUM — inferred from ICP profile, not validated in interviews]
- Provability: 5/5 [HIGH — 3 customer case studies available]
- **Total: 12/15** [HIGH confidence overall]
```

Define the tagging convention:
- HIGH: Score based on specific evidence from research package
- MEDIUM: Score based on ICP profile interpretation or industry patterns
- LOW: Score based on agent inference without specific evidence

**Pros:** Decision-makers can see which scores are data-backed; preserves value of high-confidence scores
**Cons:** Adds scoring complexity; agents must self-assess their own evidence quality
**Effort:** Small — add tagging template to Step 5

### Option B: Add a "Research Gaps" section to output

After scoring, require an explicit section listing which scoring dimensions lacked specific research evidence.

**Pros:** Simpler than per-score tagging; highlights data gaps for future research
**Cons:** Less granular — can't see which specific scores are inferred vs. evidence-based
**Effort:** Small

## Acceptance Criteria

- [ ] Positioning angles output includes evidence source or confidence level for each scored dimension
- [ ] A reviewer reading the output can distinguish data-backed scores from inferred scores
- [ ] The scoring template in Step 5 includes tagging syntax

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
