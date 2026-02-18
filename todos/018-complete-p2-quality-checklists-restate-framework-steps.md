---
status: pending
priority: p2
issue_id: "018"
tags: [code-review, duplication, quality-checklist, skill-structure, token-efficiency]
---

# Quality Checklists Largely Restate Framework Steps as Redundant Checkboxes

## Problem Statement

Each strategy skill ends with a "Quality Checklist" section that converts the skill's Framework steps into checkboxes. Since an agent following the Framework steps would have already satisfied each checklist item by definition, the checklists add 14-18 lines per skill without adding new gates. They're a summary of what was already done, not an independent quality check.

Combined with the Thought Leader Foundations overhead (todo 017), the non-operational sections of each skill add 25-30 lines of pure overhead.

## Findings

**Example from market-research/SKILL.md Quality Checklist:**
- [ ] Landscape research completed (this IS Phase 1 — agent just did it)
- [ ] Competitor analysis done (this IS Phase 2a — agent just did it)
- [ ] Customer language mined (this IS Phase 2b — agent just did it)
- [ ] Audience behavior mapped (this IS Phase 2c — agent just did it)

The only checklist items that add value are those covering output *quality* criteria not already explicit in the steps — for example, "All key findings have confidence levels assigned" (not stated in a specific step).

**Pattern across all 5 skills:** ~80% of checklist items are restatements of Framework steps.

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Reduce checklists to quality-only criteria not covered in Framework steps (Recommended)

For each skill, audit the checklist and keep only items that:
1. Check output quality, not step completion
2. Cover cross-cutting concerns (confidence levels, source citation, word count, etc.)
3. Provide a genuine gate that could fail even if all steps were followed

Example reduced market-research checklist:
```
## Quality Gate (Before Marking Complete)
- [ ] All key findings have confidence levels (HIGH/MEDIUM/LOW)
- [ ] Every claim has at least one source with URL
- [ ] Executive Summary is ≤5 bullets, all actionable
- [ ] Research questions from the brief are answered
```

**Pros:** Retains genuine quality gates; removes restatement overhead; ~10 lines saved per skill
**Cons:** Requires judgment to distinguish quality gates from step restatements
**Effort:** Small per skill (5 skills = medium total)

### Option B: Remove quality checklists entirely

Framework steps already contain in-step gates ("Do not proceed until..."). The Quality Checklist is redundant.

**Pros:** Maximum simplification
**Cons:** Loses the "before marking complete" verification moment
**Effort:** Trivial

## Acceptance Criteria

- [ ] Quality checklist items that duplicate Framework steps are removed or consolidated
- [ ] Remaining checklist items cover quality dimensions not explicitly checked in steps
- [ ] Each skill's quality checklist is ≤6 items

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
