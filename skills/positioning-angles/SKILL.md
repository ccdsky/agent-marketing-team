---
name: positioning-angles
description: Generate 5-8 scored B2B positioning angles with mechanism construction (Failure-Shift-Result), Thiel secret test, and Kahneman dual-process credibility check.
---

# Positioning Angles Skill

## When to Use

Generate 5-8 differentiated B2B positioning angles scored by defensibility, ICP resonance, and provability. Turns research into strategic positioning options the Campaign Lead uses to direct Sprint 2 content creation. Invoke when Campaign Lead assigns positioning work in Sprint 1, or user requests "generate positioning angles for [product/company]."

---

## Required Inputs

Before starting, always read:
- `context/voice-dna.md` — Owner's voice and positioning instincts
- `context/icp.md` — Target buyer's pain points, current alternatives, decision language
- `context/business-profile.md` — Unique attributes, proof points, offer details
- Research package: `knowledge/research/[relevant]-[date].md` (if available — run `/market-research` first if not)
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if this is for a specific campaign)

---

## Procedure

1. **Map the real competitive landscape.** Dunford's core question: "What would the buyer do if this product didn't exist?" Document primary competitive alternative (often status quo, spreadsheets, or "do nothing"), secondary alternatives (2-3), and why buyers switch from each.

2. **Extract unique attributes.** List what the product can truthfully claim that real competitive alternatives cannot — not features, but capabilities, approaches, outcomes, or philosophies. Filtering rule: if a competitor could claim the same thing tomorrow, it's not unique.

3. **Map attributes to customer value.** For each unique attribute: the outcome it delivers (not the feature), who values it most (ICP role), and in what context it matters most.

4. **Build the mechanism.** Every strong positioning angle needs a "why this works" story. Structure: Failure (why prior solutions failed) → Shift (what's different about your approach) → Result (what becomes possible). Choose mechanism type: Process, Discovery, System, or Timing. Name it (2-4 words, ownable). Apply Thiel's "secret" test and Kahneman dual-process litmus test. For all four mechanism type patterns, naming rules, and test criteria, see `references/methodology.md`.

5. **Generate 5-8 positioning angles.** Types: Against a specific alternative, For a specific context, Mechanism-based, Outcome-based, Against the status quo, Category creation (requires mechanism passing Thiel's test). Angles must be mutually exclusive — collapse if two feel similar. For full angle type patterns, see `references/methodology.md`.

6. **Score each angle** on Defensibility / ICP Resonance / Provability (1-5 each, max 15). Minimum threshold: 9+. Tag each dimension score [E] evidence-based or [I] inferred — no bare scores. For full scoring guide, see `references/methodology.md`.

7. **Apply Laja's 4-layer test to top 2-3 angles:** Clarity, Relevance, Value, Differentiation. Fail any layer → flag for revision. For detailed layer criteria, see `references/methodology.md`.

---

## Output

Save to: `output/campaigns/[campaign-slug]/strategy/positioning-angles-[date].md`
For standalone research: `knowledge/research/positioning-angles-[company]-[date].md`

Required sections: Competitive Landscape, Qualifying Angles (score ≥ 9, ranked), Below Threshold table, Recommended Direction, Handoff Notes for Campaign Lead.

For full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/strategy/positioning-angles-[YYYY-MM-DD].md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "campaign-lead"
})
```

**Sprint 1 Checkpoint:** Do not proceed to Sprint 2 asset creation. Present top-scoring recommendation + 2-3 alternatives + one open validation question. Human approves angle, then asset creation begins.

---

## Example

**Scenario:** Positioning angles for Acme CI/CD — a CI/CD platform for mid-market engineering teams.

**Competitive Landscape:**
- Primary alternative: Self-managed Jenkins (most common — team is already paying ops cost)
- Secondary: GitHub Actions (included with GitHub, low friction to try)
- Key switching trigger: After a major Jenkins outage or failed upgrade derails a sprint

**Mechanism (Discovery type):**
- Failure: Jenkins teams spend 15-25% of DevOps capacity on pipeline maintenance instead of shipping
- Shift: Acme discovered that pipeline reliability is an infrastructure problem, not a configuration problem
- Result: Teams reclaim DevOps hours permanently because managed infrastructure removes the root cause
- Named: "Pipeline Ownership Shift"
- Thiel test: Most CI tools say "we're faster" — Acme is saying "the configuration model is the problem." Competitors would disagree. Strong candidate.

**Top Qualifying Angle:**

**Angle 1: Against the Status Quo — Score: 13/15**
Positioning statement: "Stop maintaining CI infrastructure. Acme handles pipeline reliability so mid-market engineering teams ship faster without a dedicated DevOps hire."
Against: Self-managed Jenkins
Mechanism: Pipeline Ownership Shift
Scores: Defensibility 4/5 [E] | ICP Resonance 5/5 [E] | Provability 4/5 [I]
Laja test: Clarity ✓ | Relevance ✓ | Value ✓ | Differentiation ✓

---

## Quality Gate

Before marking complete:

- [ ] Competitive landscape includes "do nothing" / status quo alternative (not just named vendors)
- [ ] Every unique attribute filtered: "could a competitor claim this tomorrow?" — if yes, remove
- [ ] All scores tagged [E] evidence-based or [I] inferred — no bare scores
- [ ] Top 2-3 angles passed Laja's 4-layer test (Clarity / Relevance / Value / Differentiation)
- [ ] Any [I]-tagged scores flagged for validation in Handoff Notes
