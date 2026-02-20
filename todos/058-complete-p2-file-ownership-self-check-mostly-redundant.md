---
status: pending
priority: p2
issue_id: "058"
tags: [code-review, verbosity, file-ownership, campaign-lead]
---

# File Ownership Self-Check Section Is Mostly Redundant

## Problem Statement

The File Ownership Self-Check section added to `campaign-lead.md` (~18 lines) duplicates constraints already expressed in three places: (1) the "YOU DO NOT" negative list at the header, (2) the Sprint 2 and Sprint 3 STOP CHECKs, and (3) TEAM.md's File Ownership Strategy table. The 3-question pre-write checklist assumes Campaign Lead will deliberate before a file write, but LLM agents follow the most recent instruction in context — the STOP CHECKs placed inside the sprint sections are closer to the decision point and more effective.

One fact in the section is non-redundant: the row asserting Campaign Lead owns `knowledge/learnings/` after the retrospective. This does not appear in TEAM.md's table and is worth preserving.

## Findings

**Redundant information in File Ownership Self-Check:**
- Directories `drafts/`, `edited/`, `ready/`, `knowledge/research/`, `analytics/` ownership → all in TEAM.md table
- "You cannot write to specialist directories" → already in YOU DO NOT list + STOP CHECKs
- 3-question pre-write checklist → STOP CHECKs serve this function closer to decision point

**Non-redundant information:**
- `knowledge/learnings/` — Campaign Lead (after retrospective) → not in TEAM.md table

**Also noted:** `knowledge/archive/` is missing from the table (retrospective step 5 writes there) and `analytics/` path is ambiguous (campaign-level `output/campaigns/[slug]/analytics/` vs. knowledge-base `knowledge/feedback/analytics/`).

**File:** `.claude/agents/campaign-lead.md`, File Ownership Self-Check section
**Identified by:** code-simplicity-reviewer, architecture-strategist

## Proposed Solutions

### Option A: Remove Section, Migrate Non-Redundant Fact (Recommended)

Delete the File Ownership Self-Check section entirely. Add one line to the retrospective mandatory steps:

```
4. Save learnings to `knowledge/learnings/campaigns/[category]/` with proper frontmatter (Campaign Lead writes this directory after retrospective)
```

Also add `knowledge/archive/` to TEAM.md's ownership table.

**Pros:** Removes ~18 lines of redundancy; retains the one new fact in context where it's needed
**Cons:** Table is removed — but table content is in TEAM.md

### Option B: Keep Section, Fix Gaps

Keep the section but remove the 3-question checklist, add the missing rows (`knowledge/archive/`, split `analytics/` into campaign-level and knowledge-base entries), and remove rows that duplicate TEAM.md verbatim.

**Pros:** Keeps quick-reference table visible to Campaign Lead
**Cons:** Still partially redundant; table maintenance burden

**Effort:** Small
**Risk:** Low

## Acceptance Criteria

- [ ] File Ownership Self-Check section either removed or stripped of redundant content
- [ ] `knowledge/learnings/` Campaign Lead ownership preserved in appropriate location
- [ ] `knowledge/archive/` ownership documented (Campaign Lead, after retrospective)
- [ ] `analytics/` path ambiguity resolved (see todo 062)

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by code-simplicity-reviewer and architecture-strategist.
