---
status: pending
priority: p3
issue_id: "022"
tags: [code-review, expert-review, skill-structure, consistency]
---

# Expert Review Skill Structure Has Non-Standard "Why Multi-Agent Review" Section

## Problem Statement

`expert-review/SKILL.md` includes a "Why Multi-Agent Review" section that explains the rationale for parallel expert spawning. No other skill file includes a rationale section. This section is non-operational (agents don't need to understand why multi-agent review works, only how to execute it) and adds 8 lines that distinguish this skill's structure from all others.

Similarly, the "When NOT to use" section contains bullets that belong more naturally in the "Purpose" or opening context section.

## Findings

**expert-review/SKILL.md non-standard sections:**
1. "Why Multi-Agent Review" — explains cognitive separation rationale (non-operational, 8 lines)
2. "When NOT to use" — placement after "Purpose" before "Framework" is awkward; Sprint 1 timing guidance belongs with Framework Step 1 (when to invoke)

All other skills: Purpose → Thought Leader Foundations → Framework Steps → Output Format → Quality Checklist

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Remove "Why Multi-Agent Review", fold "When NOT to use" into Step 1 (Recommended)

- Remove "Why Multi-Agent Review" section entirely (rationale is implicit in the approach)
- Move "When NOT to use" criteria to Step 1 as "Invocation Check" before proceeding

**Effort:** Small — restructure top of file

## Acceptance Criteria

- [ ] expert-review/SKILL.md matches structural pattern of other skills
- [ ] No non-operational rationale sections precede the Framework steps

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
