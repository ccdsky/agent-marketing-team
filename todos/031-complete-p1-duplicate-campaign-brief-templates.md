---
status: pending
priority: p1
issue_id: "031"
tags: [code-review, campaign-lead, campaign-brief, templates, contradictory-instructions]
---

# Duplicate Campaign Brief Templates Create Contradictory Instructions for Campaign Lead

## Problem Statement

`campaign-lead.md` contains a full inline campaign brief template in its Campaign Kickoff Workflow (Step 5) AND a Campaign Templates section that references separate template files in `.claude/templates/`. An agent following the workflow sequentially will fill in the inline template first, then reach the templates section and be told to copy a different template. Two different templates for the same artifact.

## Findings

**campaign-lead.md Campaign Kickoff Workflow Step 5** contains a full inline `campaign-brief.md` template with all fields.

**campaign-lead.md Campaign Templates section** (lines 355-363) says:
> "Three templates are available — read the relevant one before creating a campaign brief:
> - Lead generation: `.claude/templates/lead-gen-campaign.md`
> - Product launch: `.claude/templates/product-launch.md`
> - Content sprint: `.claude/templates/content-sprint.md`"

The instruction says to "copy the template to `output/campaigns/[slug]/campaign-brief.md`."

An agent following the workflow encounters Step 5's inline template first, fills it in, then reads the templates section and discovers it should have used a different template. This creates conflicting instructions about how to produce the canonical campaign brief.

Additionally: the `.claude/templates/` directory may not exist (the review found no `templates/` directory in the codebase).

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Remove inline template from Step 5, reference template files (Recommended)

Remove the inline brief template from the Campaign Kickoff Workflow Step 5. Replace with:
> "Read the relevant campaign template from `.claude/templates/` and copy it to `output/campaigns/[slug]/campaign-brief.md`. Fill in the template fields using what you've learned in steps 1-4."

Create the `.claude/templates/` files or confirm they exist.

**Effort:** Small — edit Step 5 + verify/create template files

### Option B: Remove Campaign Templates section, keep inline template

If the templates directory doesn't exist, remove the Campaign Templates section. The inline template in Step 5 becomes the single source of truth.

**Effort:** Trivial — delete one section

## Acceptance Criteria

- [ ] Campaign Lead has exactly ONE path to produce a campaign brief, not two
- [ ] The template referenced actually exists in the codebase
- [ ] An agent following the kickoff workflow produces a campaign brief without contradictory instructions

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
