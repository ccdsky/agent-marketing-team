---
status: pending
priority: p1
issue_id: "004"
tags: [code-review, architecture, file-paths, output-convention]
---

# Standalone Content Path Split Across Three Inconsistent Conventions

## Problem Statement

When a user requests simple content (no active campaign), three different files specify three different output paths:

1. `creative-specialist.md` patch (Step 6): `output/drafts/[YYYY-MM-DD]-[asset-type].md`
2. `social-post/SKILL.md` line 136: `output/campaigns/standalone/drafts/social-[platform]-[topic]-[date].md`
3. `newsletter/SKILL.md` line 145: `output/campaigns/standalone/drafts/newsletter-[YYYY-MM-DD]-[topic].md`

Other SKILL.md files (landing-page, email-sequence, blog-post, lead-magnet, repurpose) only specify campaign-mode paths and are silent about standalone mode.

Additionally, `output/campaigns/standalone/` has no `.gitkeep` scaffolding and is excluded by `.gitignore` (the entire `output/` tree is gitignored), so it will never exist on a fresh clone.

## Findings

- `creative-specialist.md` Step 6: `output/drafts/` path
- `social-post/SKILL.md` line 136: `output/campaigns/standalone/drafts/` path
- `newsletter/SKILL.md` line 145: `output/campaigns/standalone/drafts/` path
- `output/` is in `.gitignore` — no scaffolded path persists across clones
- All 5 remaining SKILL.md files: silent on standalone path

**Identified by:** architecture-strategist + agent-native-reviewer

## Proposed Solution

Pick one convention and apply it everywhere. The simplest consistent choice:

**For simple mode: return output inline only.** The `creative-specialist.md` Step 6 patch already states this as the first option: "Return output inline. Do not create a file unless the user asks for one."

Update `social-post/SKILL.md` and `newsletter/SKILL.md` Output Format sections to match:
- In simple mode → output inline, no file
- In campaign mode → `output/campaigns/[slug]/drafts/[asset-name]-draft.md`

Remove the `output/campaigns/standalone/` references from both SKILL.md files. They reference a path that won't exist, and the creative-specialist.md step already establishes the inline convention.

**Effort:** Small — 2 SKILL.md output sections to update, remove ~3 lines each

## Acceptance Criteria

- [ ] All SKILL.md files agree on standalone output behavior (inline)
- [ ] No SKILL.md file references `output/campaigns/standalone/`
- [ ] `creative-specialist.md` standalone convention matches all SKILL.md files

## Work Log

- 2026-02-18: Identified by architecture-strategist + agent-native-reviewer during PR review
