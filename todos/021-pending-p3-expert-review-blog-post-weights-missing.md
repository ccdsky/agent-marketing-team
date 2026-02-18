---
status: pending
priority: p3
issue_id: "021"
tags: [code-review, expert-review, blog-post, scoring-weights]
---

# Expert Review Synthesis Table Missing Blog Post Score Weights

## Problem Statement

`expert-review/SKILL.md` Step 5 includes scoring weight tables for three asset types (landing pages, lead magnets, email sequences) but omits blog posts. Blog post is one of the four defined panel types with a full 5-expert panel defined in Step 2. Without weights, an agent synthesizing blog post reviews must invent aggregation logic, producing inconsistent results.

## Findings

**expert-review/SKILL.md Step 5 synthesis table covers:**
- Landing pages: ✓ (Conversion Copywriter 30%, ICP Relevance 25%, Voice 20%, CLOSURE 15%, B2B Psychology 10%)
- Lead magnets: ✓
- Email sequences: ✓
- **Blog posts: ✗ (missing)**

The blog post expert panel is defined in Step 2 with 5 experts (SEO Strategist, Content Strategist, Subject Matter Expert, Conversion Copywriter, Reader Experience) but has no corresponding synthesis weights.

## Proposed Solutions

### Option A: Add blog post weights row to Step 5 table (Recommended)

Suggested weights for blog posts:
- SEO Strategist: 25% (primary goal: organic discoverability)
- Content Strategist: 25% (structure, narrative, ICP alignment)
- Subject Matter Expert: 20% (accuracy, depth, credibility)
- Conversion Copywriter: 20% (hook, CTA, conversion toward next step)
- Reader Experience: 10% (clarity, scannability, flow)

**Effort:** Small — add one row to the weights table

## Acceptance Criteria

- [ ] Step 5 synthesis table includes blog post weights
- [ ] Blog post weights sum to 100%
- [ ] An agent synthesizing blog post expert reviews has a complete aggregation formula

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
