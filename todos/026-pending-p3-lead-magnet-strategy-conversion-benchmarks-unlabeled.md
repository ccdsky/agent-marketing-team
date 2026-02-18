---
status: pending
priority: p3
issue_id: "026"
tags: [code-review, lead-magnet-strategy, distribution-channel, fabrication, estimates]
---

# Lead Magnet Strategy Distribution Channel "Estimated Conversion" Column Unlabeled as Benchmarks

## Problem Statement

`lead-magnet-strategy/SKILL.md` Step 8 (Distribution Channel Plan) includes an "Estimated Conversion" column in the distribution channel table. These conversion rate estimates are drawn from the agent's training data benchmarks, not from actual campaign data or the user's specific context. They are presented in the table without any label indicating they are estimates rather than measured rates.

This is a smaller version of the same issue in keyword-research (todo 006): fabricated numbers presented as data.

## Findings

**lead-magnet-strategy/SKILL.md Step 8 output:**
```
| Channel | Estimated Conversion |
|---------|---------------------|
| LinkedIn | 2-4% |
| Email to list | 8-12% |
```

These are industry benchmark ranges, not the user's actual conversion rates. Presented without caveat, they may be used as targets or baselines in performance reporting.

## Proposed Solutions

### Option A: Label column as "Benchmark Range" with caveat (Recommended)

Change column header to "Benchmark Range (est.)" and add footnote:
> "*Industry benchmarks from training data. Replace with your actual conversion rates after first campaign."

**Effort:** Trivial — header rename + one footnote line

## Acceptance Criteria

- [ ] Distribution channel table column clearly indicates estimates are benchmarks, not measured
- [ ] A note prompts the user to replace with actual data after first campaign

## Work Log

- 2026-02-18: Identified during v1.2 PR review
