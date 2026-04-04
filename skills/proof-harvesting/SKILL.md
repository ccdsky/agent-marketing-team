---
name: proof-harvesting
description: Extract, score (Specificity + Credibility + Relevance), and tag proof assets with Cialdini persuasion dimensions into a reusable proof library.
---

# Proof Harvesting Skill

## Purpose

Systematically extract, score, and organize proof assets from all available sources into a reusable proof library. Produces a structured inventory of testimonials, case studies, data points, and credentials — scored by strength and tagged by persuasion dimension — that feeds every content skill needing evidence.

Invoke when: Campaign Lead assigns proof collection as a Sprint 1 task, Research Specialist needs to inventory available evidence, or user requests "harvest proof for [company/campaign]."

---

## Methodology Sources

Cialdini (Influence) — 6 persuasion principles for proof classification: social proof, authority, consistency, liking, reciprocity, scarcity.

---

## Required Inputs

Before starting, always read:
- `context/business-profile.md` — What the proof should support (offers, claims, differentiators)
- `context/icp.md` — What outcomes and evidence the ICP values most
- Research package (if available): `knowledge/research/[relevant]-[date].md`
- Ask the user for access to: customer testimonials, case studies, sales decks, review site profiles, media mentions

---

## Framework

### Step 1: Inventory Available Proof

Audit all accessible proof sources. For each, extract specific assets.

**Source categories:**

| Category | What to extract | Where to look |
|----------|----------------|---------------|
| Customer Results | Quantified outcomes, before/after metrics | Case studies, testimonials page, sales decks |
| Testimonials | Quotes with attribution | Website, email replies, review sites (G2, Capterra) |
| Case Studies | Narrative with specifics | Published case studies, blog posts, sales materials |
| Data/Metrics | Usage stats, growth numbers, benchmarks | Product analytics, press releases, annual reports |
| Credentials | Expertise, experience, certifications | About page, team bios, LinkedIn profiles |
| Media/Press | Coverage, mentions, awards | Press page, Google News, industry publications |
| Community | User count, engagement metrics | Social profiles, community platforms, email list size |

**For each proof asset, capture:**
- **The proof:** Exact quote, number, or claim (verbatim — do not paraphrase)
- **Source:** Where it came from, with URL if possible
- **Attribution:** Who said it — name, title, company (anonymous proof scores lower)
- **Date:** When — proof decays; recent is stronger than old
- **Context:** What was being discussed when this proof was generated

### Step 2: Score Each Proof Asset

Rate each asset on three dimensions (1-5 each):

| Dimension | 1 (weak) | 3 (moderate) | 5 (strong) |
|-----------|----------|-------------|------------|
| **Specificity** | "Great product" | "Saved us time on reporting" | "Reduced CAC by 40% in 6 weeks" |
| **Credibility** | Anonymous | First name only | Full name, title, named company |
| **Relevance** | Tangential outcome | Related to ICP need | Directly addresses ICP's #1 pain point |

**Score = Specificity + Credibility + Relevance (max 15)**

**Minimum threshold:** 9+ to include in proof library. Below 9 → note in gaps section but don't include in main library.

**Cialdini Persuasion Tags (assign 1-2 per asset):**
- **Social Proof** — numbers, adoption stats, "people like you" evidence ("500+ teams use...")
- **Authority** — credentials, expertise, endorsements from respected figures ("Featured in Forbes...")
- **Consistency** — arcs showing commitment → effort → result ("After 3 months of using X, we saw Y")
- **Liking** — relatability, shared identity with ICP ("As a fellow engineer, I...")
- **Reciprocity** — value already given (free content, tools, community contributions)
- **Scarcity** — genuine capacity limits, time-bound availability (only tag if real — never manufacture)

### Step 3: Identify Proof Gaps

Map proof inventory against content needs:

| Content Need | Required Proof Type | Available? | Gap? |
|-------------|-------------------|------------|------|
| Landing page hero (above fold) | Strongest single result (Score 13+) | | |
| Landing page Section 4 (Proof Block) | 2+ types from `/landing-page` hierarchy | | |
| Email sequence proof email | Case study arc (before → after) | | |
| Blog post credibility | Author credentials + supporting data | | |
| Ad creative / `/ad-angles` proof dimension | One-line social proof stat | | |
| Objection handling (FAQ) | Proof that counters top 3 ICP objections | | |

**For each gap:**
- Can we get this proof? From whom? (Name the specific customer, team member, or source)
- What would we need to ask them?
- What's the best available substitute while we wait?

### Step 4: Organize Proof Library

Structure the output for downstream consumption by Creative Specialist:

**By strength tier:**
- **Tier 1 (Score 13-15):** Lead with these. Use in headlines, above-fold, and hero sections.
- **Tier 2 (Score 10-12):** Supporting proof. Use in proof sections, email body, and blog posts.
- **Tier 3 (Score 9):** Background proof. Use in FAQs, objection handling, and secondary mentions.

**By Cialdini dimension:** Ensures writers cover multiple persuasion angles, not just social proof repeatedly.

**By content need:** Pre-matched to specific skill sections so Creative Specialist can grab what they need without searching.

---

## Output Format

Save to: `knowledge/research/proof-library-[company]-[date].md`

```markdown
# Proof Library: [Company/Product]

**Date:** [YYYY-MM-DD]
**Campaign:** [slug if applicable]
**Sources audited:** [list of sources checked]
**Feeds into:** `/landing-page` Section 4, `/email-sequence` proof emails, `/ad-angles` proof dimension

---

## Tier 1 Proof (Score 13-15) — Lead With These

### [Proof Asset Name]

**Proof:** "[Exact quote or data point]"
**Source:** [Where from, URL]
**Attribution:** [Name, Title, Company]
**Date:** [YYYY-MM-DD]
**Score:** Specificity [X/5] + Credibility [X/5] + Relevance [X/5] = **[Total/15]**
**Cialdini tags:** [Social Proof / Authority / Consistency / etc.]
**Best use:** [Landing page hero / Email proof email / Ad creative]

[Repeat for each Tier 1 asset]

---

## Tier 2 Proof (Score 10-12) — Supporting Evidence

[Same format as Tier 1]

---

## Tier 3 Proof (Score 9) — Background / FAQ

[Same format]

---

## Proof by Cialdini Dimension

### Social Proof
- [Asset name] — [one-line summary] (Tier [X])

### Authority
- [Asset name] — [one-line summary] (Tier [X])

### Consistency
- [Asset name] — [one-line summary] (Tier [X])

[Continue for Liking, Reciprocity, Scarcity — only include dimensions that have assets]

---

## Proof Gap Analysis

| Content Need | Required | Available | Gap | Remediation |
|-------------|----------|-----------|-----|-------------|
| Landing page hero | Score 13+ result | [Yes/No] | [Description] | [Who to ask, what to request] |
| Email proof email | Case study arc | [Yes/No] | [Description] | [Who to ask] |
[...]

---

## Below Threshold (Score < 9)

| Proof | Score | Why below threshold | Could upgrade if... |
|-------|-------|--------------------|--------------------|
| [Description] | [X/15] | [What's weak] | [What would improve it] |
```

---

## Quality Gate

Before marking complete:

- [ ] All accessible proof sources audited (not just the obvious ones — check sales decks, support emails, review sites)
- [ ] Every asset scored on Specificity + Credibility + Relevance with specific rationale
- [ ] Every asset tagged with 1-2 Cialdini persuasion dimensions
- [ ] Proof gaps identified for each content type in the gap analysis matrix
- [ ] Gap remediation plan included (who to ask, what to request, timeline)
- [ ] No proof asset included below threshold (score < 9) in main library — below-threshold assets noted separately
- [ ] Cross-references use `/skill-name` notation: `/landing-page`, `/email-sequence`, `/ad-angles`
