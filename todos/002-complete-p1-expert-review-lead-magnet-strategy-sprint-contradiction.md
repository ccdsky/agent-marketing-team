---
status: complete
priority: p1
issue_id: "002"
tags: [code-review, blocking, expert-review, lead-magnet-strategy, sprint-model]
---

# Expert Review "When NOT to Use" Contradicts Lead Magnet Strategy Sprint Timing

## Problem Statement

`expert-review/SKILL.md` lists "Sprint 1 sketches — too early for detailed expert critique" as a case when NOT to use expert review. However, `lead-magnet-strategy/SKILL.md` produces a concept brief that is explicitly a Sprint 1 deliverable. If a Creative Specialist runs lead-magnet-strategy in Sprint 1 and then tries to run expert review per their workflow (Step 8), the expert-review skill's own gate will block them.

This creates an impossible situation: the creative-specialist.md says "run expert review for Sprint 2 drafts" but lead-magnet-strategy produces a strategy brief (not a draft), making the correct sprint ambiguous.

## Findings

**expert-review/SKILL.md — "When NOT to use" section:**
> "Sprint 1 sketches — the asset isn't developed enough for meaningful expert critique"

**lead-magnet-strategy/SKILL.md — output described as:**
> "concept brief" created during Sprint 1 positioning phase

**creative-specialist.md — Step 8:**
> "For Sprint 2 drafts, run expert review before marking complete"

The conflict: lead-magnet-strategy output is a concept brief (strategy), not a draft, but expert review's panel for lead magnets assumes a developed asset exists ("review the hook, mechanism, and delivery of this lead magnet").

**Identified by:** architecture-strategist, code-simplicity-reviewer

## Proposed Solutions

### Option A: Clarify timing in lead-magnet-strategy (Recommended)

Add a note in lead-magnet-strategy/SKILL.md Step 9 (Quality Gate) explicitly stating: expert review applies after a full draft exists (Sprint 2), not at concept brief stage. The concept brief itself is reviewed against the Value Equation score and Three Pillars criteria only.

**Pros:** Preserves expert-review's gate logic; clarifies when concept brief "graduates" to needing expert review
**Cons:** Requires agent to understand distinction between concept brief review and asset draft review
**Effort:** Small

### Option B: Add a "concept brief" expert panel to expert-review/SKILL.md

Create a fifth panel type for lead magnet concept briefs with criteria appropriate to strategy-stage evaluation (feasibility, ICP fit, differentiation) rather than asset-quality criteria.

**Pros:** Complete solution; explicit path for every asset type
**Cons:** Adds complexity to already-large skill; concept briefs may not need 5-expert review
**Effort:** Medium

### Option C: Remove lead magnet from expert-review and keep all evaluation in lead-magnet-strategy

The lead-magnet-strategy skill already has its own quality gates (Value Equation >= 6.25, Three Pillars, name tests). Remove lead magnet from expert-review's panel list or note it as Sprint 2 only.

**Pros:** Simplest; removes contradiction; each skill owns its phase
**Cons:** Sprint 2 lead magnet drafts still need expert review — this only solves Sprint 1 contradiction
**Effort:** Small

## Acceptance Criteria

- [ ] The sprint timing for expert review of lead magnet strategy output is unambiguous
- [ ] An agent can determine without guessing whether to run expert review on a concept brief
- [ ] expert-review/SKILL.md and lead-magnet-strategy/SKILL.md are internally consistent

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist
