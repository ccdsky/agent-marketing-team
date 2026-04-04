---
name: blog-post
description: Write SEO-optimized articles with Schwartz awareness-matched intros, keyword integration, and conversion CTAs.
---

# Blog Post Skill

## Purpose

Write SEO-optimized articles that rank for target keywords and convert readers into leads or subscribers. Produces complete, publication-ready blog posts with all SEO elements.

Invoke when: Campaign needs content marketing assets, SEO content, or thought leadership articles.

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Voice and tone
- `context/icp.md` — Reader profile, questions they ask, language they use
- `context/business-profile.md` — Content pillars, offerings to connect to
- Campaign brief (if applicable): `output/campaigns/[slug]/campaign-brief.md`
- Keyword research (if available): from research package in `knowledge/research/`
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`

---

## Framework

### Step 1: Define the Article

Clarify before writing:
- **Primary keyword:** The main search term this article targets
- **Secondary keywords:** 2-4 related terms to include naturally
- **Search intent:** Informational | Navigational | Commercial | Transactional
- **Reader's question:** The specific question this article answers
- **Funnel stage:** Awareness (top) | Consideration (middle) | Decision (bottom)
- **Awareness-stage mapping:** Match funnel stage to messaging approach:

  | Funnel Stage | Schwartz Awareness Level | Masterson Lead Type | Intro Strategy |
  |-------------|-------------------------|--------------------|----|
  | Awareness (top) | Unaware or Problem Aware | Story Lead or Problem-Agitation Lead | Open with shared experience or pain point — reader should recognize their situation |
  | Consideration (mid) | Solution Aware | Solution/Mechanism Lead | Open with mechanism differentiation — "Most approaches fail because..." |
  | Decision (bottom) | Product Aware or Most Aware | Proof Lead or Direct Offer Lead | Open with evidence or results — reader needs confirmation, not education |

  This determines your opening paragraph strategy — not just the CTA.
- **CTA:** What should the reader do after reading?

### Step 2: Plan the Structure

Before writing body copy, map the outline:

```
Title: [Primary keyword + compelling angle]
Meta description: [150-160 chars summarizing the article]

H1: [= or close to Title]
Intro: Hook + why this matters + what they'll learn (150-200 words)

H2: [Main section 1 — covers first major point]
  H3: [Subsection if needed]

H2: [Main section 2]
H2: [Main section 3]
...
H2: [FAQ section — 3-5 questions using secondary keywords]

Conclusion: Recap + actionable next step + CTA
```

**Rule:** H2 headings should read as answers to questions the reader has.

### Step 3: Write the Article

#### Title Options (write 3, choose strongest)
**Formulas:**
- How-to: "How to [achieve outcome] in [timeframe]"
- List: "[Number] [Adjective] Ways to [Achieve Goal]"
- Question: "Why Does [Common Problem] Happen? (And How to Fix It)"
- Power word: "The [Adjective] Guide to [Topic]"

**Title rules:**
- Include primary keyword near the front
- Under 60 characters (prevents truncation in SERPs)
- Specific beats vague

#### Meta Description (150-160 characters)
- Include primary keyword
- Include a benefit or hook
- End with implicit or explicit CTA
- Not truncated — test the length

#### Introduction (150-200 words)
Structure:
1. Hook — stat, story, or bold claim that creates urgency
2. Empathy — show you understand the reader's situation
3. Promise — what they'll learn or be able to do
4. Brief credibility signal (optional)

Avoid: "In this article, we will explore..." — readers already know that.

#### Body Sections (300-500 words each)
Each H2 section:
1. State the point clearly in the first sentence
2. Explain with examples, data, or story
3. Give the reader something actionable
4. Transition naturally to the next section

**Formatting rules:**
- Short paragraphs (2-4 sentences max)
- Bullet lists for 3+ parallel items
- Bold key phrases (not random words)
- Include at least one concrete example per H2

#### FAQ Section
3-5 questions using secondary keywords and common ICP questions. Answers: 50-150 words each, direct and specific.

#### Conclusion (100-150 words)
1. Recap the key insight (not a list of everything covered)
2. Actionable next step — what to do right now
3. CTA — connect to the campaign goal

### Step 4: SEO Elements

- **Keyword density:** Primary keyword appears 2-3x per 1000 words (natural, not forced)
- **Internal links:** 2-3 links to related content on the same site (if available)
- **External links:** 1-2 authoritative sources for factual claims
- **Image alt text:** Descriptive, includes keyword where natural
- **Featured snippet target:** If applicable, format one section as a direct answer to the primary question

### Step 5: Voice and ICP Pass

Read against voice-dna.md. The article should sound like the owner wrote it — not like SEO content. Replace any generic phrases with authentic voice patterns.

Verify ICP fit: Would the target reader find this genuinely useful? Does it treat them as intelligent adults?

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/blog-[topic-slug]-draft.md`

For standalone posts (Simple Mode): Return output inline. Do not create a file unless the user asks.

**File format:**
```markdown
# Blog Post Draft: [Title]

**Primary keyword:** [keyword]
**Secondary keywords:** [kw1], [kw2], [kw3]
**Target word count:** [X] words
**Funnel stage:** [awareness|consideration|decision]
**CTA:** [what the reader should do]

---

## SEO Elements

**Meta title:** [60 chars max]
**Meta description:** [150-160 chars]
**Featured snippet target:** [Yes/No — which section]

---

## Full Article

[Complete article ready for publication]

---

## Self-Assessment

- Voice match: [1-10]
- SEO optimization: [1-10]
- Reader value (would they bookmark this?): [1-10]
- CTA integration: [1-10]
- Estimated word count: [X]
```

---

## Quality Checklist

Before marking complete:

- [ ] Primary keyword in title, H1, first paragraph, and meta description
- [ ] Title under 60 characters
- [ ] Meta description 150-160 characters with keyword and benefit
- [ ] Introduction hooks the reader in first 2 sentences
- [ ] Each H2 section is actionable and specific
- [ ] FAQ section targets secondary keywords
- [ ] At least one concrete example or story in the body
- [ ] Internal links included (if applicable)
- [ ] No "SEO-ese" language — reads like a person wrote it
- [ ] Voice matches voice-dna.md (read-aloud test on intro and conclusion)
- [ ] CTA connects to campaign goal
- [ ] Self-assessment complete
- [ ] File saved to correct output path
