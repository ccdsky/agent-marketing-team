---
status: pending
priority: p2
issue_id: "011"
tags: [code-review, templates, simplicity, asset-plan]
---

# Campaign Templates Over-Specify Agent Owners and Sprints

## Problem Statement

All three campaign templates pre-populate the "Campaign Asset Plan" table with hardcoded owner and sprint assignments:
```
| Sales / landing page | Creative Specialist | Sprint 2 | Research |
| Pre-launch email sequence | Creative Specialist | Sprint 2 | Research |
```

This creates false precision. Campaign Lead already reads `sprint-planning.md` and `campaign-lead.md` to determine who owns what in which sprint. If a campaign deviates at all from the template's assumptions (which every real campaign does), an agent must override a table that appears authoritative.

The template is meant to scaffold decision-making, but hardcoding decisions that agents already know makes the table a liability when reality diverges from the template.

## Proposed Solution

Convert Owner and Sprint columns to blank placeholders in all three templates:
```
| Asset | Owner | Sprint | Depends On |
|-------|-------|--------|-----------|
| Lead magnet content | | | Research |
| Landing page | | | Research + Lead magnet concept |
```

Leave Asset and Depends On pre-filled — these are genuinely useful structural guidance.

**Effort:** Small — 3 template files, ~10 lines each to update

## Acceptance Criteria

- [ ] Asset plan tables in all 3 templates have blank Owner and Sprint columns
- [ ] Asset and Depends On columns remain pre-filled with useful content

## Work Log

- 2026-02-18: Identified by simplicity-reviewer during PR review
