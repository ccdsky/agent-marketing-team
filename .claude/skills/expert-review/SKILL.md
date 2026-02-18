# Expert Review Skill

## Purpose

Spawn 3-5 specialized review agents to analyze a draft marketing asset from different expert perspectives simultaneously. Synthesizes parallel feedback into a prioritized revision list with specific changes and estimated impact.

Invoke when: A Sprint 2 draft is complete and ready for multi-perspective review before the Quality Gate sees it, or when the user requests "expert review" on a specific asset.

---

## Why Multi-Agent Review

B2B marketing assets must satisfy multiple stakeholders — end user, manager, executive, procurement — and survive committee review. A single reviewer catches single-perspective issues. Multi-agent review catches cross-audience problems before they reach real buyers.

**When NOT to use this skill:**
- Sprint 1 sketches or outlines (too early — wait for full drafts)
- Simple social posts or short-form content (overhead not worth it)
- When the brief is still unclear (fix the brief first)

**Timing:** Run after Creative Specialist produces a full draft. Expert review feeds revision guidance back to Creative Specialist before Quality Gate final approval.

---

## Required Inputs

Before starting:
- Draft asset file path (e.g., `output/campaigns/[slug]/drafts/landing-page-draft.md`)
- Asset type (landing page, lead magnet, email sequence, blog post, social post)
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md`
- `context/icp.md` — Who the asset targets
- `context/voice-dna.md` — Voice standard to evaluate against

---

## Framework

### Step 1: Determine Asset Type and Select Expert Panel

Based on the asset type, select the appropriate 3-5 expert panel:

**For Landing Pages:**
1. **Conversion Copywriter** — CTA strength, objection handling, urgency
2. **CLOSURE Framework Auditor** — Credibility, Lure, Objection handling, Social proof, Usability, Result
3. **ICP Relevance Reviewer** — Speaks to their pain? Uses their language?
4. **Voice Matcher** — Matches voice-dna.md throughout?
5. **B2B Buyer Psychology Reviewer** — Addresses career risk, reduces switching anxiety, maps to JTBD forces

**For Lead Magnets:**
1. **Hormozi Value Equation Scorer** — Dream Outcome × Perceived Likelihood / Time Delay × Effort
2. **Bridge Reviewer** — Does solving the narrow problem reveal the next problem your core offer solves?
3. **Completeness Reviewer** — Complete solution to a narrow problem, or a teaser?
4. **Exposure Ninja Three Pillars Checker** — Relevancy, Perceived Value, True to Your Word
5. **B2B Applicability Reviewer** — Implementable by the ICP in their business context?

**For Email Sequences:**
1. **Sequence Arc Reviewer** — Does the narrative build coherently across emails?
2. **Subject Line Specialist** — Open rate optimization for each email
3. **CTA Reviewer** — One clear action per email? Appropriate ask for sequence position?
4. **Unsubscribe Risk Reviewer** — Which emails might trigger opt-outs and why?
5. **B2B Buying Cycle Aligner** — Does timing match how B2B buyers actually evaluate solutions?

**For Blog Posts:**
1. **SEO Structure Reviewer** — Headers, keyword placement, search intent alignment
2. **ICP Value Reviewer** — Would the ICP actually read this? Share it? Act on it?
3. **Credibility Reviewer** — Is every claim supported? Are sources authoritative?
4. **Voice Matcher** — Matches voice-dna.md?
5. **CTA Reviewer** — Does the post have a clear next step that connects to the funnel?

**For Lead Magnet Strategy (concept briefs, not finished content):**
1. **Bridge Tester** — Is the bridge from lead magnet to core offer clear and natural?
2. **Value Equation Scorer** — Hormozi: Dream Outcome × Perceived Likelihood / Time Delay × Effort
3. **Format Fit Reviewer** — Is the chosen format best for this ICP and this specific promise?
4. **Naming Reviewer** — Do the 3 headline options pass the specificity test?
5. **Distribution Realism Reviewer** — Is the distribution plan actually executable?

### Step 2: Spawn Expert Agents in Parallel

Use the Task tool to spawn each expert simultaneously. Each expert receives:
- The draft asset
- Their specific evaluation framework/criteria
- The ICP profile
- A standardized output format

**Expert agent prompt template:**

```
You are a [Expert Role] evaluating a B2B marketing asset.

Asset type: [type]
Asset path: [path — read this file]

Your evaluation framework: [specific criteria for this expert]

ICP: Read context/icp.md for the target buyer profile.
Voice standard: Read context/voice-dna.md for voice expectations.

Evaluate the asset against your framework. Be specific and honest.

Output format:
## [Expert Name] Review

### Strengths (what works)
- [Specific strength with line/section reference]

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

### Step 3: Collect and Synthesize Parallel Feedback

After all expert agents complete, synthesize their findings:

**1. Consensus strengths** — What do multiple experts agree is working? (These are safe — don't change them)

**2. Consensus issues** — What do multiple experts flag? (Highest priority — fix these first)

**3. Conflicting opinions** — Where do experts disagree? (Requires judgment — see synthesis rule below)

**Synthesis rule for conflicts:** When experts disagree, favor the expert whose lens aligns most directly with the asset's primary job. Landing page? Favor conversion copywriter. Lead magnet? Favor Hormozi bridge reviewer. Email sequence? Favor sequence arc reviewer.

**4. Scoring summary** — Aggregate expert scores with weights:

| Asset Type | Score Weights |
|-----------|---------------|
| Landing page | Conversion Copywriter 30% + ICP Relevance 25% + Voice 20% + CLOSURE 15% + B2B Psychology 10% |
| Lead magnet | Bridge 30% + Value Equation 25% + B2B Applicability 20% + Completeness 15% + Three Pillars 10% |
| Email sequence | Arc 30% + Subject Lines 20% + CTAs 20% + B2B Cycle 20% + Unsub Risk 10% |

### Step 4: Build Prioritized Revision List

Produce a revision list the Creative Specialist can execute:

- **Must fix before Quality Gate** (consensus issues, HIGH priority from any expert)
- **Should fix if possible** (single-expert issues with clear impact)
- **Nice to have** (LOW priority, subjective preferences)

Each revision item: specific change + section/line reference + expected impact.

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/reviews/expert-review-[asset-type]-[date].md`

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
[...]

**Weighted score:** [X/10]

---

## Consensus Strengths (Don't change these)

- [Strength — cited by [X] experts]
- [...]

---

## Must Fix Before Quality Gate

### Issue 1: [Short title]

**Flagged by:** [Expert names]
**Location:** [Section/line]
**Problem:** [What's wrong and why it matters]
**Suggested fix:** [Specific change to make]
**Expected impact:** [What fixing this will change]

[Continue for all must-fix items]

---

## Should Fix (High Impact, Single Expert)

### Issue [N]: [Short title]
[same structure]

---

## Nice to Have (Low Priority)

- [Brief note — section — expert]
- [...]

---

## Conflicting Opinions

| Topic | Expert A says | Expert B says | Recommendation |
|-------|--------------|---------------|----------------|
| [Topic] | [View] | [View] | [Which to follow and why] |

---

## Creative Specialist Revision Checklist

- [ ] [Must fix 1]
- [ ] [Must fix 2]
- [ ] [Must fix 3]
[...]
- [ ] [Should fix 1]
[...]

**Route to Quality Gate when:** All must-fix items are checked off.
```

---

## Quality Checklist

Before marking complete:

- [ ] Asset type determined before selecting expert panel
- [ ] Correct expert panel for asset type (not generic reviewers)
- [ ] All 3-5 experts spawned in parallel (not sequentially — use Task tool)
- [ ] Each expert received specific framework criteria, not vague instructions
- [ ] Consensus strengths identified (what NOT to change)
- [ ] Consensus issues distinguished from single-expert opinions
- [ ] Conflicts resolved with clear recommendation and rationale
- [ ] Weighted aggregate score calculated
- [ ] Revision list prioritized: must-fix / should-fix / nice-to-have
- [ ] Creative Specialist revision checklist written with checkboxes
- [ ] Clear routing instruction: "Route to Quality Gate when all must-fix items complete"
- [ ] Output saved to correct path
