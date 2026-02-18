---
status: pending
priority: p3
issue_id: "027"
tags: [code-review, market-research, confidence-levels, evidence-quality]
---

# Market Research Confidence Levels Not Standardized by Source Type

## Problem Statement

`market-research/SKILL.md` uses HIGH/MEDIUM/LOW confidence levels for key findings, which is good. However, confidence assignment is left to agent judgment without a source-type baseline. A G2 review quote and an agent inference about market trends should have different default confidence floors, but the skill doesn't specify this. Agents may assign HIGH confidence to inferred findings or MEDIUM confidence to direct customer quotes, creating inconsistent evidence quality signaling.

## Findings

**market-research/SKILL.md confidence levels:**
> "Assign HIGH/MEDIUM/LOW confidence based on evidence quality"

No guidance on what constitutes each level. Two commonly confused cases:
- Direct customer quote from a review site → should be HIGH by default
- Agent inference from market patterns → should be MEDIUM or LOW by default
- Secondary source (analyst report) → should be MEDIUM by default

Without source-type defaults, confidence assignment is arbitrary.

## Proposed Solutions

### Option A: Add source-type confidence baseline table (Recommended)

Add to market-research/SKILL.md, after the confidence level definitions:

```
**Default confidence by source type:**
| Source Type | Default Confidence | Override if... |
|-------------|-------------------|----------------|
| Direct customer quote (review, interview) | HIGH | Multiple sources corroborate |
| Competitor website copy | HIGH | Content is dated >1 year |
| Analyst report / research study | MEDIUM | Study is <6 months old → HIGH |
| Forum/Reddit discussion | MEDIUM | Single thread only → LOW |
| Agent inference from patterns | LOW | Corroborated by 2+ other sources → MEDIUM |
```

**Effort:** Small — add reference table to confidence level section

## Acceptance Criteria

- [ ] market-research/SKILL.md includes source-type baseline confidence table
- [ ] An agent can assign confidence without purely subjective judgment
- [ ] Direct customer quotes are consistently marked HIGH

## Work Log

- 2026-02-18: Identified during v1.2 PR review
