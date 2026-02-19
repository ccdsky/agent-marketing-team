---
status: pending
priority: p2
issue_id: "020"
tags: [code-review, market-research, phase4, human-ai-boundary, ambiguity]
---

# Market Research Phase 4 "Human Leads, AI Assists" Framing Creates Mandatory/Optional Conflict

## Problem Statement

`market-research/SKILL.md` Phase 4 is labeled "Primary Research Support — Human Leads, AI Assists." The prose clearly says this phase requires human action (scheduling interviews, conducting surveys, facilitating focus groups). However, the output template for Phase 4 includes required sections (Interview Guide, Survey Draft, Participant Screener) that an AI agent must produce regardless of whether a human is available to execute the research.

An agent reading Phase 4 will produce an interview guide as a required deliverable, but the actual primary research it's designed to guide will never happen if no human follows up. The output looks complete (guide is written) but the research phase is incomplete (no interviews conducted).

## Findings

**market-research/SKILL.md Phase 4 output template includes:**
> "Interview Guide: [8-12 questions]"
> "Survey Draft: [link or content]"
> "Participant Screener: [criteria]"

These are instruments for human execution of research — the agent produces the tools, a human must use them. But the research deliverable format presents these alongside actual findings (from Phases 1-3), implying equal completeness.

**The confusion:** A Campaign Lead reading the research package will see Phase 4 "complete" (instruments written) and may proceed to Sprint 2 without knowing that primary research interviews were never conducted.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Clearly mark Phase 4 as "instruments only" with explicit human action required (Recommended)

Add to Phase 4 output:

```
## Phase 4: Primary Research Instruments
**Status: INSTRUMENTS READY — Human execution required**

The following guides are ready for you to use. Primary research findings will be incomplete
until interviews/surveys are conducted.

**To complete this phase:** Schedule 3-5 interviews using the guide below and add findings
to the research package before Sprint 2 begins.

[Interview Guide, Survey Draft, Participant Screener below]
```

Also update Executive Summary in output to flag Phase 4 status: "Phase 4 instruments prepared — primary research pending."

**Pros:** Campaign Lead can accurately assess research completeness; human action is prompted explicitly
**Cons:** Makes "incomplete" state visible at Sprint 1 checkpoint — may slow campaigns
**Effort:** Small — add status labels to Phase 4 output template

### Option B: Move Phase 4 to a separate optional deliverable

Remove Phase 4 from the main research package and generate it as a separate `primary-research-instruments-[date].md` file. The main research deliverable covers Phases 1-3 only (all AI-executable).

**Pros:** Research package represents complete, executable work; instruments are clearly supplemental
**Cons:** May be overlooked as a separate file; Campaign Lead must know to check for it
**Effort:** Small

## Acceptance Criteria

- [ ] Phase 4 output is clearly labeled as instruments-only, not completed research
- [ ] Campaign Lead can determine from the research package whether primary research was conducted
- [ ] The Executive Summary accurately reflects research completeness across all phases

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
