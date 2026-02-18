# Positioning Angles Skill

## Purpose

Generate 5-8 differentiated B2B positioning angles scored by defensibility, ICP resonance, and provability. This skill turns research into strategic positioning options the Campaign Lead uses to direct Sprint 2 content creation.

Invoke when: Campaign Lead assigns positioning work in Sprint 1, or user requests "generate positioning angles for [product/company]."

---

## Thought Leader Foundations

This skill is grounded in proven B2B positioning methodology:

**April Dunford (Obviously Awesome):** Positioning is context, not messaging. Her 5-component framework: Competitive Alternatives → Unique Attributes → Value (for customers) → Target Customers → Market Category. Most B2B companies position against the wrong competitor — always ask what buyers would do *without* the product.

**Peep Laja (Wynter):** 4-layer messaging test: Clarity → Relevance → Value → Differentiation. 78% of B2B buyers have a shortlist before talking to sales — positioning must work before human contact. In mature markets, find a different consideration set rather than competing on "better."

**Chris Walker (Refine Labs):** Demand creation vs. demand capture. Most B2B positioning focuses on capture (people already searching) while ignoring creation (making people aware they have a problem). Dark social — Slack, DMs, podcasts — often drives B2B decisions more than trackable channels.

**Play Bigger (Category Design):** Category creation as positioning strategy. The category king captures 76% of the economics — being second is not a strategy. Only viable for genuinely novel products; most B2B companies should position within an existing category with a distinctive twist.

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

## Recommended Angles (Score 12-15)

### Angle 1: [Short name]

**Positioning statement:** [One sentence framing]
**Against:** [What alternative this beats]
**Unique mechanism:** [Why it works / what makes it structurally different]
**Target context:** [When/where this resonates most]

**Scores:** Defensibility [X/5] | ICP Resonance [X/5] | Provability [X/5] | **Total: [X/15]**

**Laja test:** Clarity ✓/✗ | Relevance ✓/✗ | Value ✓/✗ | Differentiation ✓/✗

**Evidence available:** [testimonials, data, case studies that support this]

**Use for:** [which asset types / campaigns this angle fits]

---

### Angle 2: [Short name]
[same structure]

---

## Strong Contenders (Score 9-11)

### Angle 3: [Short name]
[same structure — shortened, no Laja test]

[Continue for remaining 9+ angles]

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

## Quality Checklist

Before marking complete:

- [ ] Real competitive landscape mapped (not just named competitors — includes "do nothing")
- [ ] Unique attributes are truly unique (filtered: competitors can't claim the same tomorrow)
- [ ] Every attribute mapped to an ICP outcome, not just a feature
- [ ] Minimum 5 angles generated with distinct framings
- [ ] All angles scored on all three dimensions (Defensibility, Resonance, Provability)
- [ ] Top angles passed Laja's 4-layer test (or flagged for revision)
- [ ] At least one angle with score 12+ identified
- [ ] Recommended direction section complete with rationale
- [ ] Output saved to correct path
- [ ] Handoff notes written for Campaign Lead
