---
status: pending
priority: p3
issue_id: "049"
tags: [code-review, quality-gate, verbosity, duplication, editorial]
---

# quality-gate.md Has Multiple Redundant Sections — ~160 Lines That Don't Add Operational Value

## Problem Statement

`quality-gate.md` is the longest agent file at ~630+ lines. Several sections duplicate content already expressed by the rubric, TEAM.md, or other sections within the same file: "Good vs Bad Feedback Examples," "Common Editorial Issues," "File Ownership" standalone section, "Serial Editing" elaboration, and "Sprint-Specific Review Standards" (which duplicates "Approval Thresholds").

## Findings

**Redundant sections:**

1. **"Good vs Bad Feedback Examples"** (~8 lines) — training examples for humans, not operational for agents
2. **"Common Editorial Issues"** (~62 lines) — five issues with Symptoms/Fix subsections. All five are already listed under Voice Fidelity, Craft Quality, and Clarity rubric sections in the same file.
3. **"File Ownership"** standalone section (~30 lines) — says "write to edited/, not drafts/." Already stated in Step 7A and in TEAM.md's File Ownership table.
4. **"Serial Editing"** section (~25 lines) — explains why serial is important (3 reasons) and restates the 5-step workflow already in the main workflow. The rule "claim ONE at a time" is already at line 35.
5. **"Sprint-Specific Review Standards"** (~50 lines) — covers same question as "Approval Thresholds" (how strict per sprint). Two sections answering the same question.

**Total estimated removable: ~175 lines**

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Delete redundant sections, merge Sprint-Specific into Approval Thresholds

- Delete Good vs Bad Feedback Examples
- Delete Common Editorial Issues (rubric already covers it)
- Delete standalone File Ownership section
- Reduce Serial Editing to one sentence appended to the CRITICAL note at line 35: "Edit in order: lead magnet → landing page → email sequence → social."
- Merge Sprint-Specific Review Standards into Approval Thresholds (add 2 sentences per sprint: "Focus on: X. Don't focus on: Y.")

**Effort:** Medium — edit quality-gate.md, verify rubric covers everything removed

## Acceptance Criteria

- [ ] "Common Editorial Issues" section removed — rubric sections cover the same issues
- [ ] "Serial Editing" section removed — rule preserved as one sentence in the CRITICAL note
- [ ] "Sprint-Specific Review Standards" merged into "Approval Thresholds"
- [ ] quality-gate.md is shorter without losing any unique operational content

## Work Log

- 2026-02-19: Identified during v1.3 code review by code-simplicity-reviewer
