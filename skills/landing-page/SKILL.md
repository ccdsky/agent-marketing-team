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

### Step 1: Diagnose Awareness Stage (Schwartz)

Diagnose before writing — this determines your entire messaging approach:

| Schwartz Stage | Lead Type (Masterson) | Above-Fold Rule |
|-------|-------------|---------------------------|
| **Unaware** | Story / Secret Lead | Never mention product. Lead with story. |
| **Problem Aware** | Problem-Agitation Lead | Agitate before solving. No solution in Section 1. |
| **Solution Aware** | Solution/Mechanism Lead | Lead with mechanism differentiation. |
| **Product Aware** | Promise / Proof Lead | Lead with proof — testimonials, case studies, results. |
| **Most Aware** | Direct Offer Lead | Lead with offer. Skip education. |

Also define: **One conversion action** and **primary objection to overcome** (from icp.md).

### Step 2: Build the 7-Section Structure

Write sections in this order. Each section has one job.

#### Section 1: Above the Fold (The Hook)

Headline + subheadline + CTA button. Apply the Lead Type from Step 1. CTA label = the outcome, not the action.

*(See `skills/landing-page/references/headline-formulas.md` for formula options)*

#### Section 2: Problem Agitation

Use exact language from `icp.md` Language Patterns section. 3-5 short paragraphs.

#### Section 3: Solution Bridge

Name the solution and its core mechanism. Explain WHY it works.

**Mechanism Credibility Check:** Must pass both — intuitive nod (System 1) AND defensible when challenged (System 2). If it only passes one, revise.

#### Section 4: Proof Block

Cover at least **two Cialdini dimensions** (Social Proof, Authority, Consistency, Liking, Reciprocity, Scarcity). Mix System 1 proof (emotional story) with System 2 proof (specific numbers) in sequence. *(See `references/proof-hierarchy.md` for the 6-tier list)*

#### Section 5: Offer Stack / What You Get

List exactly what's included with one-line benefit per item.

#### Section 6: Objection Handling (FAQ)

Address top 3-5 objections from `icp.md` as questions + answers.

#### Section 7: Closing CTA

Restate transformation + offer + single CTA + risk reversal (if applicable).

### Step 3: Voice and ICP Pass

Verify against `voice-dna.md` (voice match) and `icp.md` (pain points use their exact language, objections are real).

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
