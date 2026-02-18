---
status: pending
priority: p3
issue_id: "033"
tags: [code-review, simplicity, campaign-lead, templates, duplication]
---

# campaign-lead.md Campaign Templates Section Duplicates the templates/ Directory

## Problem Statement

`campaign-lead.md` lines 363-402 contains three inline campaign type summaries (Lead Generation, Product Launch, Content Marketing Sprint) with assets, timelines, and token budgets. These three campaign types each have a dedicated template file in `.claude/templates/`.

The inline summaries restate and partially contradict the template files (e.g., different asset lists, older sprint assignments). Campaign Lead loads both the inline summary and potentially reads the template file — loading the same information twice.

## Proposed Solution

Replace the inline Campaign Templates section in `campaign-lead.md` with a reference:

```markdown
## Campaign Templates

Three campaign templates are available. Read the appropriate template when starting:
- **Lead generation:** `.claude/templates/lead-gen-campaign.md`
- **Product launch:** `.claude/templates/product-launch.md`
- **Content sprint:** `.claude/templates/content-sprint.md`

Copy the template to `output/campaigns/[slug]/campaign-brief.md` and fill it in.
```

**Effort:** Small — replace ~40 lines in campaign-lead.md with 6-line reference block

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
