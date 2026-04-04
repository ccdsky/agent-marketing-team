---
name: landing-page
description: Write direct-response landing pages with Schwartz awareness diagnosis, Masterson lead types, and proof-driven conversion sections.
---

# Landing Page Skill

## Purpose

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

**Headline formula options:**
- `[Specific outcome] without [biggest fear]`
- `How [ICP] can [achieve goal] in [timeframe]`
- `The [ICP's] guide to [desired transformation]`
- `Stop [painful thing]. Start [desired thing].`

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

**Mechanism Credibility Check (Kahneman):**
- System 1 (intuitive): Does the mechanism "feel right" on first read? Test: could you explain it to a friend in one sentence and get a nod?
- System 2 (analytical): Does it hold up to logical scrutiny? Test: if someone asks "why does that work?" can you answer specifically?
- If it passes System 1 but fails System 2 → it's a gimmick, revise
- If it passes System 2 but fails System 1 → it's too complex, simplify

#### Section 4: Proof Block

Back up the promise with evidence. Use whatever proof exists:

**Hierarchy of proof (use the strongest available):**
1. Specific customer results with numbers ("helped X achieve Y in Z weeks")
2. Testimonials with full name and specific outcomes
3. Case studies or before/after stories
4. Social proof numbers (subscribers, customers, revenue)
5. Media logos or expert endorsements
6. Your own credentials (years of experience, past results)

**Write proof as stories, not praise.** "John reduced his CAC by 40% in 6 weeks" beats "Amazing product!"

**Proof Persuasion Dimensions (Cialdini):**
When selecting and arranging proof, ensure coverage across multiple persuasion principles:
- **Social Proof:** "People like you chose this" — user counts, adoption stats, industry logos
- **Authority:** "Experts endorse this" — credentials, endorsements, media mentions
- **Consistency:** "The journey works" — case study arcs showing commitment → effort → result

Arrange proof to satisfy both System 1 (emotional testimonial story) and System 2 (specific numbers and outcomes) in sequence.

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
