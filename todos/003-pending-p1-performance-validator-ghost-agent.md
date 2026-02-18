---
status: pending
priority: p1
issue_id: "003"
tags: [code-review, architecture, TEAM.md, agent-definition]
---

# "Performance Validator" Ghost Agent in TEAM.md

## Problem Statement

`.claude/agents/TEAM.md` line 120 (file ownership table) assigns the analytics phase to a "Performance Validator":

```
| Analysis | Performance Validator | knowledge/feedback/analytics/ | Campaign Lead |
```

And line 130:
```
└── analytics/   (Performance Validator)
```

This agent has no definition file, appears in no routing rule in CLAUDE.md, and is never mentioned in campaign-lead.md, sprint-planning.md, or any template. Every other file assigns analytics responsibility to the Distribution Specialist.

An agent reading TEAM.md receives a false picture of the team's composition. If an agent tries to route analytics work to "Performance Validator," it will find no definition to follow.

## Findings

- `.claude/agents/TEAM.md` lines 120 and 130: only two locations referencing this ghost agent
- CLAUDE.md routing: Distribution Specialist owns analytics
- campaign-lead.md Sprint 3 tasks: Distribution Specialist runs analytics
- sprint-planning.md: Distribution Specialist runs performance reporting
- All three campaign templates: Distribution Specialist owns analytics
- retrospective.md Step 1: references Distribution Specialist's analytics report

**Identified by:** architecture-strategist

## Proposed Solution

Replace "Performance Validator" with "Distribution Specialist" in both locations in TEAM.md. This is a one-line fix in two places.

**Effort:** Small — 2 line edits in TEAM.md

## Acceptance Criteria

- [ ] TEAM.md file ownership table shows Distribution Specialist for Analytics phase
- [ ] No file in the repository references "Performance Validator"

## Work Log

- 2026-02-18: Identified by architecture-strategist during PR review
