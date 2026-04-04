# Expert Review — Extended Reference

## Expert Panel Definitions — All Asset Types

### Landing Pages
1. **Conversion Copywriter** — CTA strength, objection handling, urgency
   - Scored dimensions: Headline strength, benefit clarity, objection handling, CTA strength, social proof
2. **CLOSURE Framework Auditor** — Credibility, Lure, Objection handling, Social proof, Usability, Result
3. **ICP Relevance Reviewer** — Speaks to their pain? Uses their language?
4. **Voice Matcher** — Matches voice-dna.md throughout?
5. **B2B Buyer Psychology Reviewer** — Addresses career risk, reduces switching anxiety, maps to JTBD forces

### Lead Magnets
1. **Hormozi Value Equation Scorer** — Dream Outcome × Perceived Likelihood / Time Delay × Effort
2. **Bridge Reviewer** — Does solving the narrow problem reveal the next problem your core offer solves?
3. **Completeness Reviewer** — Complete solution to a narrow problem, or a teaser?
4. **Exposure Ninja Three Pillars Checker** — Relevancy, Perceived Value, True to Your Word
5. **B2B Applicability Reviewer** — Implementable by the ICP in their business context?

### Email Sequences
1. **Sequence Arc Reviewer** — Does the narrative build coherently across emails?
2. **Subject Line Specialist** — Open rate optimization for each email
3. **CTA Reviewer** — One clear action per email? Appropriate ask for sequence position?
4. **Unsubscribe Risk Reviewer** — Which emails might trigger opt-outs and why?
5. **B2B Buying Cycle Aligner** — Does timing match how B2B buyers actually evaluate solutions?

### Blog Posts
1. **SEO Structure Reviewer** — Headers, keyword placement, search intent alignment
2. **ICP Value Reviewer** — Would the ICP actually read this? Share it? Act on it?
3. **Credibility Reviewer** — Is every claim supported? Are sources authoritative?
4. **Voice Matcher** — Matches voice-dna.md?
5. **CTA Reviewer** — Does the post have a clear next step that connects to the funnel?

### Lead Magnet Strategy (concept briefs, not finished content)
1. **Bridge Tester** — Is the bridge from lead magnet to core offer clear and natural?
2. **Value Equation Scorer** — Hormozi: Dream Outcome × Perceived Likelihood / Time Delay × Effort
3. **Format Fit Reviewer** — Is the chosen format best for this ICP and this specific promise?
4. **Naming Reviewer** — Do the 3 headline options pass the specificity test?
5. **Distribution Realism Reviewer** — Is the distribution plan actually executable?

---

## Expert Agent Prompt Template

When building the prompt for each expert, replace `[your specific evaluation criteria]` with 4-6 scored dimensions from the expert's role description.

```
You are a [Expert Role from panel] evaluating a B2B marketing [asset type].

Read the asset: [asset file path]
Read the ICP profile: context/icp.md
Read the voice standard: context/voice-dna.md

Your evaluation criteria:
[List 4-6 specific scored dimensions for this expert]

Evaluate the asset against your criteria. Be specific and honest. Reference specific sections.

Output format:
## [Expert Name] Review

### Strengths (what works)
- [Specific strength with section reference]

### Issues (what needs fixing)
- [Specific issue + why it matters + suggested fix]
  Priority: HIGH / MEDIUM / LOW
  Estimated impact: [what fixing this will change]

### Score: [X/10]

### Top 3 must-fix items:
1. [Most critical]
2. [Second]
3. [Third]
```

---

## Score Weighting Tables

| Asset Type | Weights |
|-----------|---------|
| Landing page | Conversion Copywriter 30% + ICP Relevance 25% + Voice 20% + CLOSURE 15% + B2B Psychology 10% |
| Lead magnet | Bridge 30% + Value Equation 25% + B2B Applicability 20% + Completeness 15% + Three Pillars 10% |
| Email sequence | Arc 30% + Subject Lines 20% + CTAs 20% + B2B Cycle 20% + Unsub Risk 10% |
| Blog post | SEO Structure 25% + ICP Value 25% + Credibility 20% + Voice 20% + CTA 10% |

---

## Partial Response Handling

| Experts Responded | Action |
|-------------------|--------|
| 5/5 | Apply full weights table |
| 3-4/5 | Normalize weights proportionally across responding experts. Label: "REDUCED CONFIDENCE — [N]/5 experts responded." |
| <3/5 | Do not synthesize. Note: "Expert review incomplete — [N]/5 experts responded. Proceeding with self-assessment only." Set task metadata: `{"expert_review_status": "incomplete", "experts_responded": N}` |

---

## Synthesis Rules

**Conflict resolution:** When experts disagree, favor the expert whose lens aligns most directly with the asset's primary job:
- Landing page → favor Conversion Copywriter
- Lead magnet → favor Hormozi Bridge Reviewer
- Email sequence → favor Sequence Arc Reviewer
- Blog post → favor ICP Value Reviewer

---

## Full Output Template

```markdown
# Expert Review: [Asset Type] — [Campaign Name]

**Date:** [YYYY-MM-DD]
**Asset reviewed:** [path to draft]
**Expert panel:** [list of 3-5 experts used]

---

## Aggregate Score: [X/10]

| Expert | Score | Primary finding |
|--------|-------|-----------------|
| [Expert 1] | [X/10] | [One-line summary] |

**Weighted score:** [X/10]

---

## Consensus Strengths (Don't change these)

- [Strength — cited by [X] experts]

---

## Must Fix Before Quality Gate

### Issue 1: [Short title]

**Flagged by:** [Expert names]
**Location:** [Section/line]
**Problem:** [What's wrong and why it matters]
**Suggested fix:** [Specific change to make]
**Expected impact:** [What fixing this will change]

---

## Should Fix (High Impact, Single Expert)

### Issue [N]: [Short title]
[same structure]

---

## Nice to Have (Low Priority)

- [Brief note — section — expert]

---

## Conflicting Opinions

| Topic | Expert A says | Expert B says | Recommendation |
|-------|--------------|---------------|----------------|
| [Topic] | [View] | [View] | [Which to follow and why] |

---

## Creative Specialist Revision Checklist

- [ ] [Must fix 1]
- [ ] [Must fix 2]
- [ ] [Should fix 1]

**Route to Quality Gate when:** All must-fix items are checked off.
```
