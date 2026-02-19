# Positioning Angles Skill

## Purpose

Generate 5-8 differentiated B2B positioning angles scored by defensibility, ICP resonance, and provability. This skill turns research into strategic positioning options the Campaign Lead uses to direct Sprint 2 content creation.

Invoke when: Campaign Lead assigns positioning work in Sprint 1, or user requests "generate positioning angles for [product/company]."

---

## Methodology Sources

Dunford (Obviously Awesome) — 5-component positioning model. Laja (Wynter) — 4-layer messaging test. Walker (Refine Labs) — demand creation vs. capture. Play Bigger — category design.

---

## Required Inputs

Before starting, always read:
- `context/voice-dna.md` — Owner's voice and positioning instincts
- `context/icp.md` — Target buyer's pain points, current alternatives, decision language
- `context/business-profile.md` — Unique attributes, proof points, offer details
- Research package: `knowledge/research/[relevant]-[date].md` (if available — run `/market-research` first if not)
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if this is for a specific campaign)

---

## Framework

### Step 1: Map the Real Competitive Landscape

**Dunford's core question:** "What would the buyer do if this product didn't exist?"

The real competition is rarely another vendor. In B2B, it's often:
- "Do nothing / keep the status quo"
- An internal spreadsheet or manual process
- A generalist tool (Excel, Notion, Slack)
- Hiring someone instead of buying software

Document:
- **Primary competitive alternative** (most common — ask business-profile.md)
- **Secondary alternatives** (2-3 other paths buyers consider)
- **Why buyers switch** from each alternative (from icp.md pain points)

### Step 2: Extract Unique Attributes

List what the product can truthfully claim that the real competitive alternatives cannot. Not features — capabilities, approaches, outcomes, or philosophies.

**Filtering rule:** If a competitor could claim the same thing tomorrow, it's not a unique attribute. Push until you find what's structurally or philosophically distinctive.

Examples of strong unique attributes:
- Built for a specific workflow that generic tools ignore
- Delivers a specific outcome 10x faster by a specific mechanism
- Trained on a proprietary data set competitors don't have
- Founder-led expertise from a specific domain
- Integration or compatibility that matters to the ICP

### Step 3: Map Attributes to Customer Value

For each unique attribute, identify:
- **The outcome it delivers** (not the feature — the result the ICP cares about)
- **Who values it most** (which ICP role — individual contributor, manager, executive?)
- **In what context** (what situation makes this matter most?)

This produces the raw material for positioning angles.

### Step 4: Generate 5-8 Positioning Angles

Each angle is a different way of framing the product's position relative to the competitive landscape. Angles should be mutually exclusive — if two angles feel similar, collapse them.

**Angle types to consider:**

- **Against a specific alternative:** "Unlike [alternative], [product] does [X] so buyers can [outcome]"
- **For a specific context:** "The [product] for [specific situation/trigger]"
- **Category creation:** "[Product] is the first [new category name] for [ICP]"
- **Mechanism-based:** "The only [product type] that works by [unique mechanism]"
- **Outcome-based:** "The [ICP]'s fastest path to [specific outcome]"
- **Against the status quo:** "Stop [painful workaround]. [Product] handles [X] automatically"

### Step 5: Score Each Angle

Score each angle on three dimensions (1-5 each):

| Dimension | What it measures | Scoring guide |
|-----------|------------------|---------------|
| **Defensibility** | Can competitors copy this in 6 months? | 5 = structural/IP advantage; 1 = easily copied |
| **ICP Resonance** | Does the target ICP actually care about this? | 5 = directly addresses primary pain; 1 = tangential |
| **Provability** | Can we demonstrate this with evidence? | 5 = specific data/case studies; 1 = claim only |

**Total score = Defensibility + ICP Resonance + Provability (max 15)**

Minimum threshold to include in output: 9+. Angles below 9 are noted but not recommended.

**Evidence tagging (required):** For each dimension score, tag the evidence source:
- **[E]** Evidence-based — score directly supported by research package data (quotes, competitor analysis, customer interviews)
- **[I]** Inferred — score based on ICP profile interpretation or general market knowledge without specific evidence

Example: `Defensibility 4/5 [E] — based on competitor analysis showing no one else uses this mechanism`
vs. `ICP Resonance 3/5 [I] — inferred from ICP role profile; not validated in customer interviews`

Scores with [I] tags should be treated as hypotheses, not facts. Flag them in the output for validation.

### Step 6: Apply Laja's 4-Layer Test to Top Angles

For the top 2-3 scoring angles, evaluate:

1. **Clarity** — Can a buyer understand this in one reading without context?
2. **Relevance** — Does this speak to a problem they're actively experiencing?
3. **Value** — Is the outcome worth caring about from their perspective?
4. **Differentiation** — Could a competitor claim the same thing? If yes, back to Step 4.

Flag any angle that fails one of these layers — it needs revision before use.

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/strategy/positioning-angles-[date].md`

For standalone research: `knowledge/research/positioning-angles-[company]-[date].md`

```markdown
# Positioning Angles: [Company/Product]

**Date:** [YYYY-MM-DD]
**Research basis:** [what research was used]
**ICP focus:** [primary target from icp.md]

---

## Competitive Landscape

**Primary competitive alternative:** [what most buyers do instead]
**Secondary alternatives:** [2-3 others]
**Key switching trigger:** [what makes buyers look for alternatives]

---

## Qualifying Angles (Score ≥ 9, ranked highest to lowest)

### Angle 1: [Short name] — Score: [X/15]

**Positioning statement:** [One sentence framing]
**Against:** [What alternative this beats]
**Unique mechanism:** [Why it works / what makes it structurally different]
**Target context:** [When/where this resonates most]

**Scores:** Defensibility [X/5] [E/I] | ICP Resonance [X/5] [E/I] | Provability [X/5] [E/I]

**Laja test (top 3 angles only):** Clarity ✓/✗ | Relevance ✓/✗ | Value ✓/✗ | Differentiation ✓/✗

**Evidence available:** [testimonials, data, case studies that support this]

**Use for:** [which asset types / campaigns this angle fits]

---

### Angle 2: [Short name] — Score: [X/15]
[same structure]

---

### Angle 3: [Short name] — Score: [X/15]
[same structure]

[Continue for all remaining qualifying angles, score descending]

---

## Below Threshold (Score <9)

| Angle | Score | Why not recommended |
|-------|-------|---------------------|
| [Name] | [X/15] | [brief note] |

---

## Recommended Direction

**Primary angle:** [Angle name — highest total score that passes Laja test]
**Secondary angle:** [Angle name — use for different ICP segments or channels]
**Category play:** [If applicable — new category name to test]

**Rationale:** [2-3 sentences on why these lead, what evidence supports them, what to watch]

---

## Handoff Notes for Campaign Lead

- [Key context the Campaign Lead needs to brief Creative Specialist]
- [Any angles that need primary research to validate]
- [Channels where specific angles will land best — based on ICP audience hangouts]
```

---

## Sprint 1 Checkpoint

**Do not proceed to Sprint 2 asset creation.** This output presents options — the human selects the direction.

When handing off to Campaign Lead, include:
- Top-scoring recommendation and why it leads
- The 2-3 alternative angles and what trade-offs each represents
- One open validation question (typically: which [I]-tagged assumption needs primary research most urgently?)

Campaign Lead presents at Sprint 1 checkpoint. Human approves angle. Then asset creation begins.

---

## Quality Gate

Before marking complete:

- [ ] Competitive landscape includes "do nothing" / status quo alternative (not just named vendors)
- [ ] Every unique attribute filtered: "could a competitor claim this tomorrow?" — if yes, remove
- [ ] All scores tagged [E] evidence-based or [I] inferred — no bare scores
- [ ] Top 2-3 angles passed Laja's 4-layer test (Clarity / Relevance / Value / Differentiation)
- [ ] Any [I]-tagged scores flagged for validation in Handoff Notes
