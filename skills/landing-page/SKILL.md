---
name: landing-page
description: Write direct-response landing pages with Schwartz awareness diagnosis, Masterson lead types, and proof-driven conversion sections.
---

# Landing Page Skill

## When to Use

Write a direct-response landing page that converts visitors into leads or customers. This skill produces a complete landing page draft — from above-fold headline through CTA — optimized for the specific campaign goal.

Invoke when: Campaign Lead assigns a landing page task, or user requests "write a landing page for [product/lead magnet]."

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Voice and tone for all copy
- `context/icp.md` — Who the page targets (pain points, language, objections)
- `context/business-profile.md` — Offer details, proof points, differentiators
- Research package: `knowledge/research/[relevant]-[date].md` (if available)
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md`

---

## Framework

### Step 1: Define the Conversion Goal

Clarify before writing:
- **What are we offering?** (lead magnet, product, service, trial)
- **One conversion action:** email signup | purchase | book a call | download
- **Buyer Awareness Stage (Schwartz):** Diagnose before writing — determines your entire messaging approach

  | Schwartz Awareness Stage | The buyer... | Lead Type (Masterson/Forde) |
  |-------|-------------|---------------------------|
  | **Unaware** | Doesn't know they have the problem | Story Lead or Secret Lead |
  | **Problem Aware** | Feels the pain, doesn't know solutions exist | Problem-Agitation Lead |
  | **Solution Aware** | Knows solutions exist, evaluating approaches | Solution/Mechanism Lead |
  | **Product Aware** | Knows your product, not yet convinced | Promise Lead or Proof Lead |
  | **Most Aware** | Knows and trusts you, needs the right offer | Direct Offer Lead |

  **Messaging rules by stage:**
  - Unaware: Never mention the product above the fold. Lead with story or shared experience. Goal: make them realize they have a problem.
  - Problem Aware: Agitate before solving. Don't present the solution in Section 1. Goal: deepen the pain until they want a solution.
  - Solution Aware: Lead with mechanism differentiation. "Most solutions fail because..." Goal: position your approach as structurally different.
  - Product Aware: Lead with proof. Testimonials, case studies, specific results. Goal: remove doubt with evidence.
  - Most Aware: Lead with offer. Price, guarantee, urgency. Skip the education. Goal: make the decision easy.

- **Primary objection to overcome:** (from icp.md — what makes them hesitate?)

### Step 2: Build the 7-Section Structure

Write sections in this order. Each section has one job.

#### Section 1: Above the Fold (The Hook)

The only part most visitors see. Must do all of these:
- Address the ICP's situation or pain directly
- Make a specific, believable promise
- Create enough curiosity or clarity to scroll

**Headline formula options (top 2):**
- `[Specific outcome] without [biggest fear]`
- `How [ICP] can [achieve goal] in [timeframe]`

*(See `skills/landing-page/references/headline-formulas.md` for full list)*

**Subheadline:** 1-2 sentences that expand the headline and clarify who this is for.

**Above-fold CTA:** Action button, visible without scrolling. Label = the outcome, not the action.
- Bad: "Submit" or "Sign up"
- Good: "Get the free guide" or "Start my trial"

#### Section 2: Problem Agitation

Name the pain the ICP is experiencing. Show you understand their world better than they've articulated it.

**Structure:**
1. Describe the symptom they notice
2. Name the real underlying problem
3. Show the emotional cost (frustration, anxiety, lost opportunities)

**Length:** 3-5 short paragraphs or a short bulleted list of pain points.

**Voice rule:** Use their exact language from `icp.md` Language Patterns section.

#### Section 3: Solution Bridge

Transition from problem to solution. Don't hard-sell yet — position the solution as the natural answer to the pain.

**Structure:**
1. "There's a better way" or "What if..." opening
2. Name your solution and its core mechanism
3. Explain WHY it works (the unique mechanism)
4. One-sentence promise: what they'll have/be able to do

**Mechanism Credibility Check:** Can you explain it in one sentence and get a nod (System 1)? Can you defend it when challenged (System 2)? If it only passes one — revise.

#### Section 4: Proof Block

Back up the promise with evidence. Use whatever proof exists:

**Hierarchy of proof (use the strongest available — top 2):**
1. Specific customer results with numbers ("helped X achieve Y in Z weeks")
2. Testimonials with full name and specific outcomes

*(See `skills/landing-page/references/proof-hierarchy.md` for full 6-tier list)*

**Write proof as stories, not praise.** "John reduced his CAC by 40% in 6 weeks" beats "Amazing product!"

Cover at least two Cialdini dimensions (Social Proof, Authority, Consistency). Mix System 1 proof (emotional story) with System 2 proof (specific numbers) in sequence.

#### Section 5: Offer Stack / What You Get

For lead magnets or products: list exactly what's included.

**Format:**
```
What you get:
- [Deliverable 1]: [specific benefit in 1 line]
- [Deliverable 2]: [specific benefit in 1 line]
- [Bonus or unique element]
```

For services: describe the process and what they receive at each stage.

#### Section 6: Objection Handling (FAQ)

Address the top 3-5 objections from `icp.md`. Format as questions + honest answers.

Common objection categories:
- Time ("I don't have time for this")
- Trust ("Will this actually work for me?")
- Fit ("Is this right for my situation?")
- Risk ("What if it doesn't work?")

Write answers the owner would actually give — not marketing-speak.

#### Section 7: Closing CTA

Restate the offer and the single action. Urgency if genuine (limited spots, deadline). No fake urgency.

**Structure:**
```
[Restate the transformation]
[Restate what they get]
[Primary CTA button]
[Risk reversal if applicable: guarantee, free trial, no credit card]
```

### Step 3: Voice Pass

Read entire page against `voice-dna.md`. Replace any generic marketing language with owner's actual voice patterns. The page should read like the owner wrote every word.

### Step 4: ICP Fit Check

Verify against `icp.md`:
- Every section speaks to this specific person's situation
- Pain points use their exact language
- Objections are their real objections (not generic)
- The promise maps to their actual desired outcome

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/landing-page-draft.md`

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/landing-page-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

**File format:**
```markdown
# Landing Page Draft: [Campaign Name]

**Conversion goal:** [one action]
**Target ICP segment:** [from icp.md]
**Awareness stage:** [Unaware|Problem Aware|Solution Aware|Product Aware|Most Aware]
**Lead type used:** [Story|Secret|Problem-Agitation|Solution/Mechanism|Promise|Proof|Direct Offer]

---

## Above the Fold

### Headline
[Headline]

### Subheadline
[Subheadline]

### CTA Button
[Button label]

---

## Section 2: Problem Agitation

[Copy]

---

## Section 3: Solution Bridge

[Copy]

---

## Section 4: Proof Block

[Copy]

---

## Section 5: Offer Stack

[Copy]

---

## Section 6: FAQ / Objection Handling

[Copy]

---

## Section 7: Closing CTA

[Copy]

---

## Self-Assessment

- Voice match: [1-10] — [note on where it's weakest]
- Headline strength: [1-10]
- Proof quality: [1-10]
- Objection coverage: [1-10]
- Overall conversion readiness: [1-10]
- Key weaknesses for Quality Gate to focus on: [notes]
```

---

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Conversion goal:** Email opt-in for lead magnet (CI/CD Migration Checklist)
**Awareness stage:** Problem Aware
**Lead type:** Problem-Agitation

---

**File:** `output/campaigns/acme-cicd-launch/drafts/landing-page-draft.md`

```
## Above the Fold

### Headline
Ship faster without breaking prod — even with a 20-person eng team.

### Subheadline
Acme CI/CD gives mid-market teams the deployment pipeline that enterprise
teams spend months building. No DevOps hire required.

### CTA Button
Get the free migration checklist

---

## Section 2: Problem Agitation

Your Jenkins setup made sense at 5 engineers.

Now you have 20. Every deployment is a coin flip. Someone broke the shared
pipeline last Tuesday. The post-mortem was 3 hours. Nothing changed.

The problem isn't your team — it's that Jenkins was designed for teams with
a dedicated DevOps engineer to babysit it. You don't have that.

Meanwhile your competitors ship on Fridays. You don't.

---

## Section 3: Solution Bridge
[Introduce Acme CI/CD — the mechanism: pre-configured pipelines for
common mid-market stacks, zero-config branch protection, one-click rollback]

## Section 4: Proof Block
[3 customer stories with deployment frequency and incident metrics]

## Section 5: Offer Stack
[What's in the Migration Checklist — 4 deliverables]

## Section 6: FAQ
[Top 3 objections: "We're too customized for this", "Migration risk",
"Cost vs. hiring a DevOps engineer"]

## Section 7: Closing CTA
[Restate: Ship on Fridays again. Get the checklist.]
```

---

## Quality Checklist

Before marking complete:

- [ ] Headline addresses ICP's real pain or desire (not generic benefit)
- [ ] "Problem agitation" uses language from icp.md Language Patterns
- [ ] Solution section explains the mechanism, not just the outcome
- [ ] At least 2 forms of proof present (testimonials, data, case study)
- [ ] Objection handling covers top 3 objections from icp.md
- [ ] One and only one conversion action (no competing CTAs)
- [ ] Voice matches voice-dna.md throughout (read-aloud test)
- [ ] No corporate speak, no hype, no empty promises
- [ ] Self-assessment completed with honest scores
- [ ] File saved to correct output path
