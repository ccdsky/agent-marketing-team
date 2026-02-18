---
status: pending
priority: p3
issue_id: "024"
tags: [code-review, positioning-angles, lead-magnet-strategy, sprint-checkpoints, human-in-loop]
---

# Strategy Skills Lack "Options, Not Decisions" Note — Could Bypass Sprint 1 Checkpoint

## Problem Statement

`positioning-angles/SKILL.md` and `lead-magnet-strategy/SKILL.md` produce strategy recommendations without explicitly noting that these are options for the human to choose from, not decisions the agent makes. An agent completing positioning angles may select an angle itself and proceed, bypassing the Sprint 1 checkpoint where the human approves the strategic direction.

The sprint model depends on human approval at Sprint 1 to validate strategic direction before asset creation begins. If strategy skills produce "the answer" rather than "options for review," the checkpoint becomes ceremonial rather than functional.

## Findings

**positioning-angles/SKILL.md** Step 6:
> "Present top angle to Campaign Lead as recommended positioning"

"Recommended" implies a decision has been made. Campaign Lead should present this to the human for approval, not implement it.

**lead-magnet-strategy/SKILL.md** Step 9:
> "Select highest-scoring concept. This is your lead magnet direction."

"This is your direction" implies the decision is final. It should read "Present for Sprint 1 checkpoint approval."

Both skills lack an explicit: "Do not proceed to asset creation without human approval of this strategic direction."

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add "Present for Approval" gate at end of each strategy skill (Recommended)

Add to the end of both positioning-angles and lead-magnet-strategy:

```
## Sprint 1 Checkpoint

**Do not proceed to Sprint 2 asset creation.** Present this output to Campaign Lead with:
- Top recommendation and rationale
- Alternative options and why they scored lower
- One open question for the human to resolve

Campaign Lead presents at Sprint 1 checkpoint. Human approves direction. Then asset creation begins.
```

**Effort:** Small — add final section to 2 skills

## Acceptance Criteria

- [ ] positioning-angles/SKILL.md explicitly states output requires human approval before asset creation
- [ ] lead-magnet-strategy/SKILL.md explicitly states output requires Sprint 1 checkpoint approval
- [ ] The language is "options/recommendation" not "decision/direction"

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
