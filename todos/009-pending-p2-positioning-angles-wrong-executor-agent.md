---
status: pending
priority: p2
issue_id: "009"
tags: [code-review, architecture, positioning-angles, campaign-lead, role-clarity]
---

# Positioning Angles Assigned to Campaign Lead Contradicts Coordinator Role

## Problem Statement

The Campaign Lead's Sprint 1 example task assigns positioning angles work to Campaign Lead itself. The Campaign Lead role definition explicitly states "You coordinate. Specialists execute." — Campaign Lead should not be doing research or analysis work. Positioning angles requires reading research packages, mapping competitive landscape, and scoring differentiation dimensions — this is Research Specialist work.

This assignment creates a precedent for Campaign Lead doing substantive specialist work, which breaks the coordination model and creates token overhead on the coordinator agent.

## Findings

**campaign-lead.md Sprint 1 example:**
> Task [3]: Campaign Lead reads research packages and produces positioning angles using `.claude/skills/positioning-angles/SKILL.md`

**campaign-lead.md role definition:**
> "You coordinate. Specialists execute. You do not write content, conduct research, or create assets directly."

Positioning angles execution requires:
- Reading and synthesizing research packages (Research Specialist domain)
- Mapping competitor positioning (Research Specialist domain)
- Scoring differentiation dimensions (analytical work, Research Specialist domain)

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Route positioning-angles to Research Specialist (Recommended)

Update Campaign Lead Sprint 1 example task [3] to:
> "Research Specialist reads research packages and executes `/positioning-angles` skill. Deliverable: `output/campaigns/[slug]/strategy/positioning-angles-[date].md`"

Update Research Specialist's task keywords to include: `positioning angles, differentiation angles, competitive positioning`

**Pros:** Consistent with role definitions; Research Specialist already has the research context
**Cons:** None — Research Specialist naturally has all inputs needed for positioning angles
**Effort:** Small — update task assignment in campaign-lead.md + add keyword to research-specialist.md

### Option B: Create a "Strategy Specialist" role

Move both positioning and lead magnet strategy to a dedicated strategy agent between Research and Creative.

**Pros:** Clean separation of research vs. strategy vs. content
**Cons:** Adds a 6th agent; over-engineering for current scope; contradicts KISS principle
**Effort:** Large — new agent file, all routing updates

## Acceptance Criteria

- [ ] Campaign Lead Sprint 1 task list assigns positioning-angles to Research Specialist (or a specialist, not Campaign Lead)
- [ ] Research Specialist routing keywords include positioning angles
- [ ] Campaign Lead role definition remains "coordinate, not execute" with no counterexamples in sprint templates

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
