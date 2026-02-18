---
status: pending
priority: p2
issue_id: "007"
tags: [code-review, research-specialist, skills, v2.0]
---

# Research Specialist References Non-Existent v2.0 Skills as Invocable

## Problem Statement

`research-specialist.md` lines 486-499 instructs the Research Specialist to invoke `/keyword-research` and `/market-research` skills. These skills are explicitly deferred to v2.0 (per IMPLEMENTATION-SUMMARY.md). The agent file has no conditional — it instructs invocation as if the skills exist.

When a Campaign Lead creates a research task for keyword research or market research, the Research Specialist will attempt to invoke a non-existent skill and produce unpredictable output.

Note: The same issue exists for creative-specialist.md's skill list (which lists skills 8-12 without v1.1 constraints), but the campaign-lead.md patch already addressed positioning-angles. The remaining 4 strategy skills need the same treatment in research-specialist.md.

## Findings

- `research-specialist.md` lines 486-499: `/keyword-research` and `/market-research` invocation
- IMPLEMENTATION-SUMMARY.md: these are explicitly v2.0 skills
- `creative-specialist.md` skill list 8-12: lists v2.0 skills without v1.1 annotation

**Identified by:** agent-native-reviewer

## Proposed Solution

Add a note in `research-specialist.md` wherever `/keyword-research` and `/market-research` are referenced:
```
Note: /keyword-research and /market-research skills are not yet implemented (v2.0).
Execute using the inline methods described in this file's "Research Types and Methods" section.
```

Also annotate `creative-specialist.md`'s skill list entries 8-12 (positioning-angles, keyword-research, market-research, expert-review, lead-magnet-strategy) with:
```
**Status:** Not yet implemented — v2.0. Do not attempt to invoke.
```

**Effort:** Small — 2 files, ~5 lines each

## Acceptance Criteria

- [ ] research-specialist.md does not instruct invocation of unimplemented skills
- [ ] creative-specialist.md skill list 8-12 clearly marked as v2.0/not yet implemented
- [ ] Agents can still execute research inline without a skill file

## Work Log

- 2026-02-18: Identified by agent-native-reviewer during PR review
