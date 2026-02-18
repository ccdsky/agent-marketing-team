---
status: pending
priority: p2
issue_id: "019"
tags: [code-review, lead-magnet-strategy, email-sequence, skill-overlap, scope-creep]
---

# Lead Magnet Strategy Step 7 Prescribes Email Sequence Arc, Preempting Email Sequence Skill

## Problem Statement

`lead-magnet-strategy/SKILL.md` Step 7 (Nurture Bridge) defines a specific 4-email nurture sequence arc: delivery email, quick win, deeper value, and conversion email. This pre-empts `email-sequence/SKILL.md` by prescribing the sequence structure at the concept brief stage, before the Creative Specialist has had a chance to design the email arc using the full email sequence skill and research context.

When Creative Specialist later runs `/email-sequence`, they inherit a constrained brief that has already decided arc structure, reducing the email sequence skill to execution of a pre-decided plan rather than informed design.

## Findings

**lead-magnet-strategy/SKILL.md Step 7:**
> "Define nurture bridge: Email 1 (delivery + quick win), Email 2 (value deepening), Email 3 (case study/social proof), Email 4 (conversion pitch)"

This is a fixed 4-email arc, not a flexible recommendation. The email-sequence skill covers variable-length sequences (3-7 emails), different goals (onboarding, nurture, re-engagement), and different structural frameworks based on audience and offer.

**email-sequence/SKILL.md** — has its own arc design methodology that considers audience temperature, sequence goal, and conversion pathway. A concept brief that has already fixed the arc to 4 emails removes these design decisions.

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Replace arc prescription with delivery mechanism guidance only (Recommended)

Change Step 7 to define only the lead magnet delivery mechanics, not the full sequence arc:

```
## Step 7: Delivery & First-Touch Design

Define immediate post-signup experience:
- Delivery method: Email with download link / Instant web access / PDF attachment
- First touch subject line: [draft subject for delivery email]
- Quick win moment: What value does the subscriber get in the first 5 minutes?

Note: Full nurture sequence arc is designed by Creative Specialist using /email-sequence skill,
informed by this concept brief.
```

**Pros:** Preserves email sequence skill's design space; concept brief stays at concept level
**Cons:** Removes nurture planning from concept brief — Campaign Lead has less to present at Sprint 1 checkpoint
**Effort:** Small

### Option B: Reframe Step 7 as "Nurture Goals" rather than "Nurture Arc"

Replace the specific 4-email arc with outcome goals:
> "Nurture goals: deliver quick win, build credibility, handle top objection, convert to [offer]. Email-sequence skill designs the arc to meet these goals."

**Pros:** Sets context for email-sequence skill without over-prescribing structure; still useful at Sprint 1 checkpoint
**Cons:** More ambiguous — "goals" could still be interpreted as prescribing sequence
**Effort:** Trivial

## Acceptance Criteria

- [ ] lead-magnet-strategy/SKILL.md Step 7 does not prescribe specific email count or arc structure
- [ ] The concept brief defines delivery mechanics and nurture goals without constraining email-sequence design
- [ ] email-sequence/SKILL.md retains full arc design authority

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
