---
status: pending
priority: p3
issue_id: "051"
tags: [code-review, campaign-lead, file-size, structural-refactor, token-cost]
---

# campaign-lead.md Does Two Jobs at 516 Lines — Sprint Reference Content Inflates Read Cost

## Problem Statement

`campaign-lead.md` contains two conceptually distinct jobs: (1) Campaign Lead's orchestration protocol (kickoff, monitoring, escalation, retrospective), and (2) Sprint execution reference (task breakdowns, checkpoint formats, quality gates). The second job is loaded on every Campaign Lead invocation, including simple status checks and escalations where only the orchestration protocol is needed.

## Findings

**campaign-lead.md content (~516 lines):**
- Campaign Kickoff Workflow: ~40 lines (always needed)
- Sprint 1/2/3 task breakdowns with examples: ~190 lines (needed when creating tasks, not always)
- Sprint checkpoint presentation formats: ~60 lines (needed at checkpoints only)
- Progress Monitoring + Daily Status template: ~50 lines (needed when monitoring)
- Campaign Templates section: ~15 lines
- Failure Recovery Protocol: ~25 lines
- Quality Gates (3 checklists): ~30 lines
- Escalation scenarios: ~20 lines
- Campaign Retrospective with template: ~48 lines

**Core orchestration protocol** (~150 lines) is needed for every invocation. Sprint execution reference (~190 lines) is only needed when creating sprint tasks. An agent reading the full file before a monitoring check loads 3x more than needed.

Additionally, the sprint execution content duplicates sprint-planning.md, which exists specifically to hold this content.

**Identified by:** architecture-strategist, code-simplicity-reviewer

## Proposed Solutions

### Option A: Split into campaign-lead-core.md and absorb sprint details into sprint-planning.md

- `campaign-lead.md` (core, ~150 lines): responsibilities, kickoff, monitoring thresholds, escalation, retrospective trigger
- `sprint-planning.md` (absorb task breakdowns and checkpoint formats from campaign-lead.md)

Campaign Lead reads core always, loads sprint-planning.md only when creating sprint tasks.

**Effort:** Large — file restructure, must verify all cross-references

### Option B: Keep in one file but trim (Lower effort)

Remove the per-sprint task breakdowns (they duplicate sprint-planning.md), collapse monitoring to thresholds only, and remove the Daily Status template. Target: ~350 lines.

**Effort:** Medium — selective trimming without restructure

## Acceptance Criteria

- [ ] Core campaign orchestration instructions are accessible without loading sprint task breakdown content
- [ ] Sprint task breakdown content is not duplicated between campaign-lead.md and sprint-planning.md
- [ ] campaign-lead.md is under 350 lines (from 516) or split into two files

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist and code-simplicity-reviewer
