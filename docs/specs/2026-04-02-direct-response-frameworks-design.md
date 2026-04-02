# Direct-Response Frameworks Integration

**Date:** 2026-04-02
**Status:** Design — awaiting approval
**Scope:** Enrich 4 existing skills + create 2 new skills with direct-response marketing theory

---

## Problem

The marketing team's skills encode strong structural frameworks (Dunford positioning, Hormozi value equation, Laja messaging tests) but lack foundational direct-response theory that determines *how to talk to buyers based on where they are in their awareness journey*. Specifically:

1. **No awareness-stage diagnosis.** Skills use "cold/warm/hot traffic" — a media-buying concept — instead of Schwartz's 5-stage buyer awareness model, which determines *messaging approach*.
2. **Mechanism is named but not built.** Positioning-angles lists "mechanism-based" as an angle type but doesn't teach how to construct a mechanism.
3. **No angle multiplication.** Positioning-angles produces 5-8 strategic angles. There's no process for expanding a chosen angle into 10-15 creative variants for actual content.
4. **No proof harvesting.** Landing-page has a proof hierarchy for *writing* proof sections, but no process for *collecting and organizing* proof assets before writing.

---

## Source Material

### Primary: advertising-skills repo (realkimbarrett/advertising-skills)
- Schwartz Awareness Mapper — 5-stage diagnostic with messaging rules per stage
- Mechanism Builder — Failure→Shift→Result structure, 4 mechanism types, naming rules
- Ad-Angle Multiplier — 6 dimensions (Pain, Desire, Proof, Identity, Contrarian, Urgency), 10-15 angles
- Proof Harvester — planned but not implemented in repo

### Supplementary: Book frameworks
- **Cialdini (Influence)** — 6 persuasion principles: reciprocity, commitment/consistency, social proof, authority, liking, scarcity. Applied to proof scoring and angle dimensions.
- **Masterson & Forde (Great Leads)** — 6 lead types matched to awareness stages: Direct Offer, Promise, Solution, Problem-Agitation, Secret, Story.
- **Thiel (Zero to One)** — "Secret" test for mechanism strength and category-creation potential.
- **Kahneman (Thinking, Fast and Slow)** — System 1/System 2 dual-process check: mechanisms must satisfy both intuitive and logical evaluation.
- **Dixon & Adamson (Challenger Sale)** — Teach-tailor-take-control framework for contrarian angles.
- **Cialdini + Kahneman combined** — Persuasion layer for quality checks across skills.

---

## Design

### Part 1: Enrich Landing Page Skill

**File:** `.claude/skills/landing-page/SKILL.md`

#### 1a. Replace Traffic Source with Awareness Diagnosis (Step 1)

Remove the current `Traffic source: cold | warm | hot` field. Replace with:

```
Buyer Awareness Stage: [Diagnose before writing]

Stage Diagnosis:
- Unaware      → They don't know they have the problem
- Problem Aware → They feel the pain but don't know solutions exist
- Solution Aware → They know solutions exist, evaluating approaches
- Product Aware  → They know your product, not yet convinced
- Most Aware     → They know and trust you, need the right offer

Matching Lead Type (Masterson/Forde):
- Unaware       → Story Lead or Secret Lead (pattern interrupt, curiosity)
- Problem Aware  → Problem-Agitation Lead (deepen pain, name it)
- Solution Aware → Solution/Mechanism Lead (why THIS approach works)
- Product Aware  → Promise Lead or Proof Lead (results, evidence)
- Most Aware     → Direct Offer Lead (price, terms, urgency)

Messaging Rules by Stage:
- Unaware: Never mention the product above the fold. Lead with story or
  shared experience. Goal: make them realize they have a problem.
- Problem Aware: Agitate before solving. Don't present the solution in
  Section 1. Goal: deepen the pain until they want a solution.
- Solution Aware: Lead with mechanism differentiation. "Most solutions
  fail because..." Goal: position your approach as structurally different.
- Product Aware: Lead with proof. Testimonials, case studies, specific
  results. Goal: remove doubt with evidence.
- Most Aware: Lead with offer. Price, guarantee, urgency. Skip the
  education. Goal: make the decision easy.
```

#### 1b. Enhance Solution Bridge (Section 3)

Add Kahneman dual-process check after the existing mechanism guidance:

```
Mechanism Credibility Check (Kahneman):
- System 1 (intuitive): Does the mechanism "feel right" on first read?
  Test: could you explain it to a friend in one sentence and get a nod?
- System 2 (analytical): Does it hold up to logical scrutiny?
  Test: if someone asks "why does that work?" can you answer specifically?
- If it passes System 1 but fails System 2 → it's a gimmick, revise
- If it passes System 2 but fails System 1 → it's too complex, simplify
```

#### 1c. Enhance Proof Block (Section 4)

Add Cialdini's persuasion dimensions to the existing proof hierarchy:

```
Proof Persuasion Dimensions (Cialdini):
When selecting and arranging proof, ensure coverage across:
- Social Proof: "People like you chose this" (user counts, adoption data)
- Authority: "Experts endorse this" (credentials, endorsements, media)
- Consistency: "The journey works" (case study arcs: commitment → result)

Arrange proof to satisfy both System 1 (emotional testimonial story)
and System 2 (specific numbers and outcomes) in sequence.
```

#### 1d. Update Output Format

In the output template metadata, replace `Traffic source assumption: [cold|warm|hot]` with:

```
**Awareness stage:** [Unaware|Problem Aware|Solution Aware|Product Aware|Most Aware]
**Lead type used:** [Story|Secret|Problem-Agitation|Solution/Mechanism|Promise|Proof|Direct Offer]
```

---

### Part 2: Enrich Email Sequence Skill

**File:** `.claude/skills/email-sequence/SKILL.md`

#### 2a. Add Awareness-Stage Arc to Step 1

After the existing "Sequence arc" section, add:

```
Awareness-Stage Arc:
Map each email to an awareness-stage transition. The subscriber enters
at one stage and should exit at the next:

Lead magnet delivery example:
  Email 1: Problem Aware → Solution Aware
    (Deliver the lead magnet. Name the mechanism. "Here's why this works.")
  Email 2: Solution Aware → Solution Aware (deeper)
    (Expand the mechanism. Share a non-obvious insight.)
  Email 3: Solution Aware → Product Aware
    (Introduce your specific approach. Case study or proof.)
  Email 4: Product Aware → Most Aware
    (Handle top objection. More proof. Build certainty.)
  Email 5: Most Aware → Convert
    (Clear offer. Genuine urgency if available. One CTA.)

Rule: Never skip more than one awareness stage per email.
If subscribers enter at Unaware, you need more emails (add 1-2 at
the start for story/problem-agitation before introducing solutions).

Each email's subject line and opening hook should match the Masterson
lead type for its TARGET awareness stage (the stage you're moving
the reader toward, not where they start).
```

---

### Part 3: Enrich Blog Post Skill

**File:** `.claude/skills/blog-post/SKILL.md`

#### 3a. Map Funnel Stage to Awareness and Lead Type (Step 1)

After the existing "Funnel stage" field, add:

```
Awareness-Stage Mapping:
- Awareness (top-of-funnel) = Unaware or Problem Aware
  → Use Story Lead or Problem-Agitation Lead for intro
  → Goal: reader recognizes they have the problem
- Consideration (mid-funnel) = Solution Aware
  → Use Solution/Mechanism Lead for intro
  → Goal: reader understands why your approach is different
- Decision (bottom-funnel) = Product Aware or Most Aware
  → Use Proof Lead or Direct Offer Lead for intro
  → Goal: reader has enough evidence to act

This determines your opening paragraph strategy — not just the CTA.
```

---

### Part 4: Enrich Positioning Angles Skill

**File:** `.claude/skills/positioning-angles/SKILL.md`

#### 4a. New Step 3.5: Build the Mechanism

Insert between Step 3 (Map Attributes to Customer Value) and Step 4 (Generate Angles):

```
### Step 3.5: Build the Mechanism

The mechanism is the "why this works" story that makes positioning
believable and defensible. Every strong positioning angle has a
mechanism underneath it — build it explicitly before generating angles.

**Structure — Failure → Shift → Result:**

1. THE FAILURE — Why what they tried before didn't work
   "Most [solutions] fail because they [common approach flaw]"
   Source this from icp.md pain points and research package.

2. THE SHIFT — What's different about your approach
   "We discovered that [insight/method/framework] changes the equation"
   Source this from business-profile.md unique attributes (Step 2 output).

3. THE RESULT — What becomes possible
   "[Specific outcome] because [mechanism removes the old bottleneck]"
   Source this from Step 3's attribute-to-value mapping.

**Four Mechanism Types (choose the strongest fit):**

| Type | Pattern | Best when... |
|------|---------|-------------|
| Process | "Instead of X, we do Y, which means Z" | Your method is genuinely different |
| Discovery | "We found that [non-obvious truth], which is why [result]" | You have a proprietary insight |
| System | "Our [Named System] works because [addresses root cause]" | You have a structured framework |
| Timing | "Until [recent change], this wasn't possible. Now [capability]" | A market shift enables your approach |

**Naming Rules:**
- 2-4 words. Memorable. Ownable.
- Should feel proprietary without being jargon.
- Test: if a competitor could use this exact name, it's not specific enough.
- Examples: "Awareness Matching System", "Offer Compression Method",
  "Revenue Signal Engine"

**Thiel's "Secret" Test:**
- Does this mechanism encode a non-obvious truth about the market?
- Is it something you believe that most competitors would disagree with?
- If yes → this is a strong candidate for category creation.
  Flag it and consider a Category Creation angle in Step 4.

**Kahneman Dual-Process Litmus Test:**
- System 1: "I haven't heard it explained like that before" → you're close
- System 2: "That actually makes sense why mine didn't work" → you've got it
- Must pass both. Intuition without logic is a gimmick.
  Logic without intuition won't be remembered.

**Output:** One mechanism per unique attribute cluster from Step 3.
Tag each with its type. Carry forward into Step 4 — every angle
should reference or build on a mechanism, not just the
"mechanism-based" angle type.
```

#### 4b. Add Category Creation Angle Type (Step 4)

Add to the existing angle types list:

```
- **Category creation:** "[Product] is the first [new category] for [ICP]"
  Prerequisite: Step 3.5 mechanism passes Thiel's "secret" test.
  The mechanism defines the category — the category name should make
  the mechanism's insight self-evident.
  Reference: Play Bigger (already in methodology sources).
```

#### 4c. Update Methodology Sources

Add to the existing sources line:

```
Thiel (Zero to One) — "secret" test for mechanism strength and category creation.
Masterson/Forde (Great Leads) — lead type selection by awareness stage.
Kahneman (Thinking, Fast and Slow) — dual-process mechanism credibility test.
```

---

### Part 5: New Skill — Ad-Angle Multiplication

**File:** `.claude/skills/ad-angles/SKILL.md`

**Purpose:** Multiply a single approved positioning angle into 10-15 distinct creative variants for ads, social posts, email subjects, and content hooks. Runs in Sprint 2 after the positioning angle is approved at Sprint 1 checkpoint.

**Different from positioning-angles:** Positioning-angles generates *strategic* angles (5-8, scored by defensibility). Ad-angles generates *creative* variants of one chosen angle (10-15, tagged by dimension and channel).

```
## Required Inputs

Before starting, always read:
- Approved positioning angle from Sprint 1:
  `output/campaigns/[slug]/strategy/positioning-angles-[date].md`
- Mechanism from positioning-angles Step 3.5 output
- `context/icp.md` — Pain points, language, objections
- `context/voice-dna.md` — Voice and tone
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`

## Framework

### Step 1: Load the Core Angle

Extract from the approved positioning angle:
- The positioning statement (one sentence)
- The mechanism (from Step 3.5)
- The primary ICP pain point it addresses
- The strongest available proof

### Step 2: Multiply Across 6 Dimensions

Generate 2-3 hooks per dimension. Each must feel genuinely different —
not a rewrite with synonyms. Target 12-18 raw angles, cull to 10-15.

**PAIN — Lead with what hurts**
"Tired of [specific frustration from icp.md]?"
"Every [ICP role] knows the feeling of [pain moment]"
Source: icp.md pain points. Use their exact language.

**DESIRE — Lead with what they want**
"[Specific result] in [timeframe]"
"What if [desired state] was your default?"
Source: icp.md desired outcomes.

**PROOF — Lead with evidence** (Cialdini: social proof + authority)
"[Customer name] went from [before] to [after] in [time]"
"[Number] [ICP roles] already [achieved outcome]"
Source: proof library. Only use verified proof assets.

**IDENTITY — Lead with who they are** (Cialdini: commitment + liking)
"Built for [identity group] who [shared belief]"
"If you're the kind of [role] who [behavior], this is for you"
Source: icp.md identity markers and tribal language.

**CONTRARIAN — Lead with what's wrong** (Challenger Sale: teach, tailor, take control)
"Why [common advice] is actually hurting your [outcome]"
"[Industry consensus] is wrong. Here's what works instead."
Source: mechanism's FAILURE component. Challenge the status quo.

**URGENCY — Lead with timing** (Cialdini: scarcity — ONLY if genuine)
"[Market shift] means [window of opportunity]"
"Before [deadline/change], you could still [action]"
Source: real market timing. Never manufacture fake urgency.

### Step 3: Tag Each Angle

For each of the 10-15 surviving angles:

| # | Dimension | Hook (≤15 words) | Awareness Stage | Best Channel | Proof Needed |
|---|-----------|-------------------|-----------------|-------------|-------------|
| 1 | Pain | "..." | Problem Aware | LinkedIn ad | None |
| 2 | Proof | "..." | Product Aware | Email subject | Case study |
[...]

**Awareness stage tagging:**
- Pain angles → typically target Unaware or Problem Aware
- Desire angles → Problem Aware or Solution Aware
- Proof angles → Product Aware
- Identity angles → Solution Aware (tribal differentiation)
- Contrarian angles → Unaware or Problem Aware (pattern interrupt)
- Urgency angles → Most Aware (close the deal)

**Channel tagging:**
- LinkedIn post/ad — works for all dimensions, 1-2 sentence hook
- Email subject line — under 50 chars, curiosity or benefit
- Blog post title — SEO-friendly, specific
- Ad creative — visual hook + 1 line, scroll-stop test
- Landing page headline — above-fold, clarity over cleverness

### Step 4: Quality Filter

Remove any angle that:
- Feels like a synonym rewrite of another angle (collapse them)
- Can't be written as a headline in under 15 words
- Fails the scroll-stop test: would you pause your feed for this?
- Uses urgency without a genuine deadline or scarcity
- Makes a claim the proof library can't support

## Output Format

Save to: `output/campaigns/[slug]/strategy/ad-angles-[date].md`
For standalone: `output/drafts/ad-angles-[topic]-[date].md`

## Quality Gate

Before marking complete:
- [ ] 10-15 distinct angles (not rewrites of each other)
- [ ] All 6 dimensions represented (minimum 1 angle per dimension)
- [ ] Each angle tagged with awareness stage and best channel
- [ ] Proof-dependent angles have proof assets identified
- [ ] Urgency angles use genuine scarcity only (no manufactured deadlines)
- [ ] Every hook passes the 15-word headline test
```

---

### Part 6: New Skill — Proof Harvesting

**File:** `.claude/skills/proof-harvesting/SKILL.md`

**Purpose:** Systematically extract, score, and organize proof assets from all available sources into a reusable proof library. Runs during Sprint 1 alongside research, or as a standalone skill. Output feeds every content skill that needs proof (landing-page Section 4, email sequences, blog posts, ad-angles).

```
## Required Inputs

Before starting, always read:
- `context/business-profile.md` — What proof should support
- `context/icp.md` — What outcomes and evidence the ICP values
- Research package (if available): `knowledge/research/[relevant]-[date].md`
- Existing customer stories, testimonials, case studies (ask user for sources)

## Framework

### Step 1: Inventory Available Proof

Audit all accessible proof sources. For each, extract specific assets:

**Source Categories:**

| Category | What to extract | Where to look |
|----------|----------------|---------------|
| Customer Results | Quantified outcomes, before/after | Case studies, testimonials page, sales decks |
| Testimonials | Quotes with attribution | Website, email replies, review sites |
| Case Studies | Narrative with specifics | Published case studies, blog posts |
| Data/Metrics | Usage stats, growth, benchmarks | Product analytics, press releases |
| Credentials | Expertise, experience, certs | About page, team bios, LinkedIn |
| Media/Press | Coverage, mentions, awards | Press page, Google News |
| Community | User count, engagement metrics | Social profiles, community platforms |

**For each proof asset, capture:**
- The proof (exact quote, number, or claim)
- Source (where it came from, with URL if possible)
- Attribution (who said it — name, title, company)
- Date (when — proof decays; recent > old)
- Context (what was being discussed)

### Step 2: Score Each Proof Asset

**Three scoring dimensions:**

| Dimension | 1 (weak) | 3 (moderate) | 5 (strong) |
|-----------|----------|-------------|------------|
| Specificity | "Great product" | "Saved us time" | "Reduced CAC by 40% in 6 weeks" |
| Credibility | Anonymous | First name only | Full name, title, named company |
| Relevance | Tangential outcome | Related to ICP need | Directly addresses ICP's #1 pain |

**Score = Specificity + Credibility + Relevance (max 15)**
Minimum threshold: 9+ to include in proof library.

**Cialdini Persuasion Tags (assign 1-2 per asset):**
- **Social Proof** — numbers, adoption, "people like you" evidence
- **Authority** — credentials, expertise, endorsements from respected figures
- **Consistency** — arcs showing commitment → effort → result
- **Liking** — relatability, shared identity with ICP
- **Reciprocity** — value already given (free content, tools, community)
- **Scarcity** — genuine capacity limits, time-bound availability

### Step 3: Identify Proof Gaps

Map proof inventory against content needs:

| Content Need | Required Proof Type | Available? | Gap? |
|-------------|-------------------|------------|------|
| Landing page hero (above fold) | Strongest single result | ? | ? |
| Landing page Section 4 | 2+ proof types from hierarchy | ? | ? |
| Email sequence proof email | Case study arc (before→after) | ? | ? |
| Blog post credibility | Author credentials + data | ? | ? |
| Ad creative | One-line social proof stat | ? | ? |
| Objection handling | Proof that counters top 3 objections | ? | ? |

For each gap:
- Can we get this proof? From whom?
- What would we need to ask the customer/team?
- Interim substitute (what's the best available alternative?)

### Step 4: Organize Proof Library

Structure the output so Creative Specialist can grab what they need:

**By strength tier:**
- Tier 1 (Score 13-15): Lead with these. Use in headlines and above-fold.
- Tier 2 (Score 10-12): Supporting proof. Use in proof sections and emails.
- Tier 3 (Score 9): Background proof. Use in FAQs and objection handling.

**By Cialdini dimension:** So writers can ensure they're covering
multiple persuasion angles, not just repeating social proof.

**By content need:** Pre-matched to specific skill sections so
Creative Specialist doesn't have to search.

## Output Format

Save to: `knowledge/research/proof-library-[company]-[date].md`

## Quality Gate

Before marking complete:
- [ ] All accessible proof sources audited (not just the obvious ones)
- [ ] Every asset scored on Specificity + Credibility + Relevance
- [ ] Every asset tagged with 1-2 Cialdini persuasion dimensions
- [ ] Proof gaps identified for each content type
- [ ] Gap remediation plan included (who to ask, what to request)
- [ ] No proof asset included below threshold (score < 9)
```

---

### Part 7: Integration Points

#### Research Specialist Agent Update

**File:** `.claude/agents/research-specialist.md`

Add to "Research Skill Integration" section:

```
- **Ad-angle multiplication:** Read `.claude/skills/ad-angles/SKILL.md` —
  Multiplies approved positioning into 10-15 creative variants across
  6 dimensions. Run after Sprint 1 checkpoint when angle is approved.
- **Proof harvesting:** Read `.claude/skills/proof-harvesting/SKILL.md` —
  Systematic proof extraction and scoring. Run during Sprint 1 alongside
  market research. Output feeds all content skills.
```

Add "proof harvesting" and "ad angles" to the task keyword filter.

#### Creative Specialist Agent Update

**File:** `.claude/agents/creative-specialist.md`

Add to skill list in "Step 5: Read Appropriate Content Skill":

```
- Ad angles → `Read(file_path=".claude/skills/ad-angles/SKILL.md")`
```

Add to "Step 4: Load Context & Research":

```
Read(file_path="knowledge/research/proof-library-[company]-[date].md")  # if available
```

#### Campaign Lead Agent Update

**File:** `.claude/agents/campaign-lead.md`

Add proof harvesting as a Sprint 1 task in campaign brief template alongside market research and positioning angles.

#### CLAUDE.md Routing Update

**File:** `CLAUDE.md`

Add to Research Specialist keywords: `proof harvesting, proof inventory, proof audit`
Add to Research Specialist keywords: `ad angles, angle multiplication, creative angles`
Add new skill entries to Available Skills section.

---

## What's NOT Changing

- **Market research skill** — already strong, no overlap with these frameworks
- **Lead magnet strategy skill** — Hormozi/Exposure Ninja frameworks are complete
- **Expert review skill** — evaluates quality, doesn't need awareness theory
- **Quality Gate agent** — scoring rubric is independent of these frameworks
- **Distribution Specialist agent** — operates downstream of content creation
- **Sprint model and task coordination** — workflow structure stays the same
- **Newsletter, social-post, repurpose skills** — lightweight by design, don't need enrichment

---

## Implementation Order

1. **Positioning angles** (Step 3.5 mechanism building) — foundational, other changes reference it
2. **Landing page** (awareness diagnosis, proof enhancement) — highest-impact content skill
3. **Email sequence** (awareness arc) — second-highest impact
4. **Blog post** (awareness-matched intros) — smallest change
5. **New skill: proof-harvesting** — Sprint 1 input, needed before content skills run
6. **New skill: ad-angles** — Sprint 2 input, depends on positioning-angles output
7. **Agent updates** (research-specialist, creative-specialist, campaign-lead) — wiring
8. **CLAUDE.md routing** — final step, registers everything

---

## Success Criteria

After implementation:
- Running `/landing-page` prompts for awareness stage diagnosis before writing
- Running `/positioning-angles` produces a named mechanism with Failure→Shift→Result structure
- Running `/ad-angles` on an approved angle produces 10-15 tagged creative variants
- Running `/proof-harvesting` produces a scored, organized proof library
- Email sequences show awareness-stage transitions per email
- Blog post intros match their funnel stage to a Masterson lead type
