---
name: lead-magnet
description: Create high-value opt-in content (checklists, guides, templates, frameworks) with Schwartz awareness-appropriate framing.
---

# Lead Magnet Skill

## When to Use

Create high-value opt-in content that generates email subscribers by delivering a specific, immediate outcome. Lead magnets succeed when they solve one concrete problem so well that the reader tells others about it.

Invoke when: Campaign needs a lead generation asset — checklist, guide, template, framework, mini-course, or swipe file.

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Voice and tone
- `context/icp.md` — The specific pain point this lead magnet solves and the ICP's language
- `context/business-profile.md` — How this lead magnet connects to the paid offering
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md`
- Lead magnet concept (if available): from `/lead-magnet-strategy` output
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`

---

## Framework

### Step 1: Validate the Concept

Before writing any content, validate:

**Audience awareness check:**
Lead magnets serve people who are **Problem Aware or Solution Aware** — they feel the pain but haven't committed to a solution (or are comparing solutions). This determines your framing:

| Schwartz Awareness Level | Lead Magnet Framing |
|----------------|-------------------|
| Problem Aware | "Here's why this problem is worse than you think" — the lead magnet reveals the scope of the problem and positions your approach as the path forward |
| Solution Aware | "Here's how to evaluate solutions" — the lead magnet helps them compare approaches and naturally favors your mechanism |

Lead magnets should **not** target Unaware audiences (they don't know they have the problem yet — use blog posts) or Most Aware audiences (they already want your product — use a direct offer).

**Value density test:**
"Can someone implement this and get a result in under 30 minutes?"

If no → too broad. Narrow the scope.
If yes → proceed.

**Title test:** Must have all three — specific outcome + target audience + timeframe/specificity.

**Connection to paid offering:** Define how the lead magnet bridges to the next step before writing.

### Step 2: Choose the Format

| Format | Best For | Time to Create | ICP Appreciation |
|--------|----------|----------------|-----------------|
| **Checklist** | Process-oriented ICPs, quick wins | Low | "I can use this today" |
| **Cheat sheet / reference** | Complex topics, repeated use | Low | "I'll keep this open while I work" |
| **Template** | When readers need to produce something | Medium | "This saved me hours" |
| **Framework / model** | Positioning, strategy | Medium | "This changed how I think about X" |
| **Mini-guide** | Education-oriented ICPs | Medium-High | "I learned something I didn't know" |
| **Swipe file** | Copywriting, examples, inspiration | Low-Medium | "I can steal these directly" |
| **Mini-course (3-5 emails)** | Complex skills, behavior change | High | "This actually helped me do the thing" |
| **Calculator / assessment** | Data-driven ICPs | High | "It showed me where I stand" |

### Step 3: Write the Lead Magnet

#### Cover / Title Slide
- Lead magnet title (use the validated title from Step 1)
- Subtitle: One sentence describing the specific outcome
- Author name
- Optional: "Brought to you by [Business Name]"

#### Introduction (50-100 words max)
- Who this is for (name the ICP specifically)
- What they'll be able to do after using this
- How to use it
- Skip the backstory — they opted in, they want the content

#### Core Content

Write the content matching the chosen format. Each section must deliver value — no filler.

#### Next Step (Internal CTA)

Connect to the logical next step without hard-selling. One line, soft bridge.

### Step 4: Voice Pass

Verify against `voice-dna.md` and `icp.md`. The share test: would the reader send this to a colleague?

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/lead-magnet-[title-slug]-draft.md`

*This single file contains both the lead magnet content and the delivery email template. No separate delivery email file is created.*

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/lead-magnet-[title-slug]-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

**File format:**
```markdown
# Lead Magnet Draft: [Title]

**Format:** [checklist | template | guide | framework | swipe file | mini-course]
**Validated title:** [Final title]
**Target ICP:** [Who this is for]
**Core outcome:** [What they can do after this]
**Connection to paid offering:** [How this leads to next step]

---

## Lead Magnet Content

[Full content, formatted for the chosen format]

---

## Delivery Email Content

**Subject:** [Your [lead magnet title] is here]
**Preview text:** [Here's what you asked for + one-line tease]

Body:
[Short delivery email — 100 words max, just deliver the goods]

[CTA: Download/Access link]

---

## Self-Assessment

- Value density (can they get a result in 30 min?): [Yes/Borderline/No]
- Title specificity: [1-10]
- Voice match: [1-10]
- Natural connection to paid offering: [1-10]
- "Would they share this?" test: [Yes/No — why]
```

---

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Format:** Checklist
**Validated title:** The CI/CD Migration Checklist for Mid-Market Engineering Teams

---

**File:** `output/campaigns/acme-cicd-launch/drafts/lead-magnet-cicd-checklist-draft.md`

```
## Lead Magnet Content

# The CI/CD Migration Checklist for Mid-Market Engineering Teams

**Who this is for:** Engineering leads and DevOps-curious CTOs at companies
with 15-50 engineers who are outgrowing their current pipeline setup.

**What you'll have after this:** A phase-by-phase migration plan you can
present to your team this week — with the 4 steps most guides skip.

**How to use it:** Check off what you've done. Focus on the unchecked boxes.
Phase 3 is where most migrations stall.

---

### Phase 1: Current State Audit

- [ ] Document all active pipelines and their owners
- [ ] List every custom plugin or script your pipeline depends on
- [ ] Identify which pipelines run on a schedule vs. triggered by commits

[Phase 2: Environment parity — 8 items]
[Phase 3: Rollback validation — 5 items (the section most teams skip)]
[Phase 4: Cutover and monitoring — 6 items]

---

## Next Step (Bridge to Offer)

If you're in Phase 2 or later and want a second set of eyes on your
migration plan, Acme CI/CD offers a free 30-minute pipeline audit for
mid-market teams.

We'll look at your current setup and tell you exactly where the risk is
before you migrate — not after.

[Book your free audit → link]
```

---

## Quality Checklist

Before marking complete:

- [ ] Title passes the specificity test (outcome + audience + timeframe)
- [ ] Value density test passed (implementable in <30 minutes)
- [ ] Format chosen matches ICP consumption preference (icp.md Content Preferences)
- [ ] Introduction is under 100 words and skips backstory
- [ ] Every section delivers value — no filler
- [ ] Next step CTA connects to the logical paid offering
- [ ] Language matches ICP vocabulary throughout
- [ ] Voice matches voice-dna.md (read-aloud test)
- [ ] Delivery email template written
- [ ] "Would they share this?" self-test passed
- [ ] Self-assessment complete
- [ ] File saved to correct output path
