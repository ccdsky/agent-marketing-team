---
name: blog-post
description: Write SEO-optimized articles with Schwartz awareness-matched intros, keyword integration, and conversion CTAs.
---

# Blog Post Skill

## When to Use

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

Write 3 title options (under 60 chars, primary keyword near front). Include meta description (150-160 chars).

Apply the **Masterson Lead Type from Step 1** to the introduction — this is the most important structural decision. The intro strategy differs completely by funnel stage.

**Structure:** H2 sections (each answering a reader question) → FAQ section (3-5 Qs using secondary keywords) → Conclusion with CTA.

### Step 4: Voice Pass

Verify against `voice-dna.md` and `icp.md`. The article should sound like the owner, not SEO content.

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/blog-[topic-slug]-draft.md`

For standalone posts (Simple Mode): Return output inline. Do not create a file unless the user asks.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/blog-[topic-slug]-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

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

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Primary keyword:** replace Jenkins mid-market
**Funnel stage:** Consideration (Solution Aware readers comparing options)

---

**File:** `output/campaigns/acme-cicd-launch/drafts/blog-replace-jenkins-draft.md`

```
## SEO Elements

**Meta title:** Why Mid-Market Teams Are Ditching Jenkins (58 chars)
**Meta description:** Jenkins made sense at 5 engineers. At 20+, it becomes a
full-time job to maintain. Here's what mid-market teams are switching to —
and why. (156 chars)

---

## Full Article

# Why Mid-Market Teams Are Ditching Jenkins

You didn't hire a DevOps engineer. You inherited a Jenkins setup.

That works fine when three engineers share one pipeline. It stops working when
you have 20 engineers, 4 product lines, and a Friday deploy that broke prod
last month.

Jenkins was designed for teams with a dedicated pipeline engineer. If that's
not you, you're spending engineering hours maintaining infrastructure instead
of shipping product.

## The Real Cost of "Free" CI/CD

Most teams calculate Jenkins cost as $0 (open source, self-hosted). The real
cost is 5-10 engineer-hours per week in maintenance, incident response, and
plugin compatibility fixes...

## What Mid-Market Teams Actually Need

[H2: Pipeline speed that scales with team size]
[H2: Branch protection without custom scripting]
[H2: Rollback that works on the first try]

## How Teams Are Making the Switch

[Case study: 60% reduction in deploy incidents, 3-week migration]

## FAQ

**Q: We have too much custom pipeline logic to switch.**
[Answer: 150 words]

**Q: How long does migration actually take?**
[Answer: 150 words]

## Conclusion

[Recap + CTA: Download the CI/CD Migration Checklist]
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
