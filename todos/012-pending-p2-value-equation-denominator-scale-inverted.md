---
status: pending
priority: p2
issue_id: "012"
tags: [code-review, logic-error, lead-magnet-strategy, value-equation, scoring]
---

# Value Equation Denominator Scoring Scale Is Inverted — Logic Error

## Problem Statement

`lead-magnet-strategy/SKILL.md` implements Hormozi's Value Equation: `Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)`. The scoring guide instructs: "Score Time Delay 1-10, where 10 = instant delivery". With this scale, instant delivery (Time Delay = 10) produces the *lowest* value score (divides by a large number), while slow delivery (Time Delay = 1) produces the *highest* value score. This is the opposite of the intended logic.

The same inversion may affect the Effort denominator if it follows the same 1-10 scale.

## Findings

**Hormozi's Value Equation intent:**
- Lower Time Delay = Higher Value (getting the result quickly is better)
- Lower Effort = Higher Value (easier path to outcome is better)

**The scoring error:**
- If Time Delay is scored 10 = instant, 1 = takes weeks: `10` in denominator → `Value / 10` (penalizes instant delivery)
- Correct scoring: 10 = slow delivery, 1 = instant, OR flip to numerator: `Value × (1/Time Delay)`

**Alternatively:** score as "perceived wait time" on 1-10 where 10 = very slow, 1 = instant. Then high scores (slow delivery) correctly decrease the Value fraction.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Invert scale description (Recommended)

Change Time Delay scoring to:
> "Score Time Delay 1-10 where 1 = instant delivery, 10 = weeks of waiting"

Change Effort scoring to:
> "Score Effort 1-10 where 1 = zero effort required, 10 = significant effort"

This preserves the Hormozi formula structure (divide by denominator) while making high scores indicate worse outcomes, correctly penalizing slow/effortful lead magnets.

**Pros:** Minimal change; preserves formula; semantically correct
**Cons:** Counter-intuitive scale (1 = good for denominator factors) — may need clear labeling
**Effort:** Small

### Option B: Move denominator factors to numerator as inverses

Rewrite formula as:
`Value = Dream Outcome × Perceived Likelihood × Speed × Ease`

Where Speed = (11 - Time Delay) and Ease = (11 - Effort), scored on intuitive scale (10 = great).

**Pros:** All factors scored intuitively (higher = better)
**Cons:** Departs from Hormozi's original formula notation; may confuse users familiar with the framework
**Effort:** Small

## Acceptance Criteria

- [ ] A lead magnet with instant delivery scores higher Value than one with delayed delivery, all else equal
- [ ] A lead magnet requiring zero effort scores higher Value than one requiring significant effort, all else equal
- [ ] The scoring guide text clearly communicates which end of the scale is "better"

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
