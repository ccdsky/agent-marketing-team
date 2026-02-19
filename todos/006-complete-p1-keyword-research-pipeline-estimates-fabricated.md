---
status: complete
priority: p1
issue_id: "006"
tags: [code-review, blocking, keyword-research, fabrication, pipeline-estimates]
---

# Keyword Research Step 11 Pipeline Impact Estimates Are Fabricated Without Caveat

## Problem Statement

`keyword-research/SKILL.md` Step 11 instructs agents to calculate pipeline impact estimates (conversion rates, leads/month, pipeline value). These numbers require actual business data (current traffic, conversion rates, deal sizes) that agents do not have access to. Without caveat, an agent will generate plausible-looking numbers from training priors, presenting fabricated estimates as data. Decision-makers using this output to justify SEO investment will be misled.

## Findings

**keyword-research/SKILL.md Step 11:**
> "Estimate pipeline impact per target keyword cluster"
> Output includes: "Estimated monthly visits", "Conversion rate", "Leads/month", "Pipeline value"

None of these can be calculated without:
- Current site traffic baseline (not available from web search)
- Actual conversion rate history (requires analytics access)
- Average deal size (requires CRM data)
- Realistic click-through rates by position (requires live Ahrefs/GSC data)

Agents will fill these columns with industry benchmarks from training data and present them as estimates without labeling them as such. The visual presentation (a data table) implies measurement rather than assumption.

**Identified by:** agent-native-reviewer, architecture-strategist

## Proposed Solutions

### Option A: Label all estimates as benchmarks with explicit uncertainty (Recommended)

Update Step 11 to:
1. Require agents to label every number as "(benchmark estimate)" 
2. List the assumptions used (e.g., "assuming 2% conversion rate — replace with your actual rate")
3. Add a note: "These are illustrative estimates based on industry benchmarks. Replace with your actual conversion rates and deal sizes for accurate projections."

**Pros:** Preserves the value of the projection exercise while making uncertainty explicit
**Cons:** Output is less "clean" — but honest
**Effort:** Small — add framing language to Step 11

### Option B: Replace with input-output template requiring human data

Change Step 11 to a fill-in template:

```
## Pipeline Impact Estimates (Requires Your Data)

To estimate pipeline impact, provide:
- Your current organic conversion rate: ____%
- Average deal size: $____
- Target keyword cluster estimated monthly volume: ____

Pipeline estimate = Volume × CTR × Conversion Rate × Deal Size
```

**Pros:** Forces accurate data input; no fabrication risk
**Cons:** Step becomes a template rather than an automated estimate
**Effort:** Small

## Acceptance Criteria

- [ ] All pipeline estimates in Step 11 output are labeled as benchmark estimates with assumptions stated
- [ ] The output section includes a disclaimer that numbers require replacement with actual business data
- [ ] No table column presents a number as measured when it is estimated

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
