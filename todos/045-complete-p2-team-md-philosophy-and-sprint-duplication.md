---
status: pending
priority: p2
issue_id: "045"
tags: [code-review, TEAM.md, verbosity, duplication, token-cost]
---

# TEAM.md Philosophy Sections Are Non-Operational — ~100 Lines Loaded Before Every Agent Task

## Problem Statement

`TEAM.md` is read by every agent before every task. It contains ~100 lines of philosophy, orientation, and marketing rationale that do not affect agent behavior: "We Are a Marketing Team," "The Three-Layer Stack (Vibe Marketing)," "The Vibe Marketing Insight," "The Marketing Team Mindset," and a complete duplicate of the sprint model that lives more authoritatively in `campaign-lead.md`. These add token cost to every agent task without changing any decision.

## Findings

**Sections that change no agent behavior:**

1. `## We Are a Marketing Team, Not a Content Team` (~12 lines) — philosophical framing
2. `## The Three-Layer Stack (Vibe Marketing)` with ASCII diagram (~18 lines) — human orientation
3. `## The Vibe Marketing Insight: Options + Taste = Winners` (~8 lines) — marketing philosophy
4. `## The Marketing Team Mindset` (~10 lines) — cultural principles restated from CLAUDE.md
5. Sprint 1/2/3 detailed descriptions (~35 lines) — duplicates campaign-lead.md which is the canonical home
6. "Traditional handoff model (old)" comparison block — historical documentation
7. "Benefits:" bulleted list under Task-Based Coordination — marketing bullets

**Total:** ~100 lines loaded by every agent on every task.

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Strip to operational content only (Recommended)

Remove sections 1-4 entirely. Replace sprint descriptions (section 5) with one line:
> "Campaigns run in three sprints: Sprint 1 (strategy, checkpoint), Sprint 2 (drafts, checkpoint), Sprint 3 (ship, no checkpoint). Details in `.claude/agents/campaign-lead.md`."

Remove historical comparison and benefits bullets.

Result: TEAM.md shrinks from ~360 lines to ~240 operational lines.

**Effort:** Medium — edit TEAM.md, verify no operational content is removed

## Acceptance Criteria

- [ ] TEAM.md contains only operational instructions agents use at runtime
- [ ] No agent behavior changes as a result of the removals
- [ ] Philosophy/orientation content is either moved to README.md or deleted

## Work Log

- 2026-02-19: Identified during v1.3 code review by code-simplicity-reviewer
