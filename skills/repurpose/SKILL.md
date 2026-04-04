---
name: repurpose
description: Adapt content for multiple platforms with Schwartz awareness-shift mapping — each platform gets a native hook matched to its audience's awareness level.
---

# Repurpose Skill

## When to Use

Adapt a piece of existing content for multiple platforms without losing the core insight — and without just copying and pasting. Good repurposing extracts the single best idea from a long piece and rebuilds it natively for the target platform.

Invoke when: A newsletter, blog post, or long-form piece needs to be adapted for social, or a talk/video transcript needs to become written content.

---

## Required Inputs

Before repurposing, read:
- `context/voice-dna.md` — Voice (especially platform-specific tone notes)
- `context/icp.md` — Who reads/watches on each target platform
- `context/business-profile.md` — Content pillars and brand consistency
- **The source content** — Read the full original piece
- **Brand guide** (optional): `context/brand-guide.md` — Platform-specific tone adjustments. Skip if file doesn't exist.

---

## Framework

### Step 1: Audit the Source Content

Read the full source piece and extract:

**Core idea audit:**
```
1. What is the single best insight in this piece?
2. What is the most surprising or counterintuitive point?
3. What concrete example or story is most illustrative?
4. What is the most actionable takeaway?
```

Pick **one** of these as the "repurposing anchor" for each platform. Different platforms can use different anchors from the same source piece.

**Do not** try to cram the whole piece into every platform. One piece → many native posts, each built around one extracted idea.

### Step 2: Map to Target Platforms

For each target platform, define:
- What format works natively (thread, post, short article, carousel)
- What the anchor idea is from the source
- What the platform-specific hook will be
- What the CTA should be (usually link back to original, or subscribe)
- **Audience awareness shift (Schwartz):** The target platform audience is likely at a *different* awareness level than the source audience. Adjust the opening accordingly:

  | Source → Target | Schwartz Awareness Shift | Adaptation |
  |----------------|----------------|------------|
  | Blog (SEO) → LinkedIn | Solution Aware → Problem Aware | The blog reader searched for this. The LinkedIn reader didn't. Lead with pain or story, not the solution. |
  | Blog (SEO) → Twitter thread | Solution Aware → Unaware | Thread must hook with curiosity or contrarian take. The reader has no context. |
  | Newsletter → LinkedIn | Most Aware → Problem Aware | Strip the insider context. The post must stand alone for people who don't subscribe. |
  | Newsletter → Blog | Most Aware → Solution Aware | Expand the insight into a full argument. Add evidence and structure the newsletter didn't need. |

  **Rule:** Never copy the source opening into the repurposed version. Every platform gets a native hook matched to its audience's awareness level.

| Platform | Native Format | Optimal Length | Best For |
|----------|--------------|----------------|---------|
| LinkedIn | Text post or article | 150-300 words | Insight + professional angle |
| Twitter/X | Thread | 3-8 tweets | Punchy breakdown of key points |
| Substack Notes | Short observation | 100-300 words | Personal, conversational |
| Instagram | Caption | 125-150 chars (first line) | Visual hook + story |
| YouTube description | Summary | 200-300 words | SEO + context |

### Step 3: Write Platform-Specific Versions

For each platform, rebuild natively around the anchor idea. Never copy the source opening. Never reference the original ("As I wrote in my newsletter...") — just deliver the value. For platform formatting constraints, see `agents/references/platform-formats.md`.

### Step 4: Voice Check

The derivative test: if someone saw this without context, would they know which piece it came from? If yes, rewrite to be more native. Verify against `voice-dna.md`.

---

## Output Format

Create one folder per repurpose project:
`output/campaigns/[slug]/drafts/repurposed/`

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[slug]/drafts/repurposed/repurpose-overview.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

Files:
```
repurposed/
├── repurpose-overview.md
├── linkedin-[topic-slug].md
├── twitter-thread-[topic-slug].md
├── substack-notes-[topic-slug].md
└── [other-platform]-[topic-slug].md
```

**Overview file format:**
```markdown
# Repurpose: [Source Piece Title]

**Source:** [Link or file path to original]
**Source type:** [newsletter | blog post | talk transcript | video]

## Core Ideas Extracted
1. [Insight 1]
2. [Insight 2]
3. [Story/example to anchor]

## Platform Map
| Platform | Anchor Idea | File | Status |
|----------|------------|------|--------|
| LinkedIn | [Insight N] | linkedin-[topic-slug].md | Draft |
| Twitter/X | [Insight N] | twitter-thread-[topic-slug].md | Draft |
| Substack Notes | [Insight N] | substack-notes-[topic-slug].md | Draft |
```

**Individual platform file format:**
```markdown
# [Platform] Version: [Topic]

**Source insight:** [which idea from source this is built on]
**Platform:** [LinkedIn | Twitter/X | Substack Notes]

---

## Draft

[Full post content, ready to copy-paste]

---

## Self-Assessment
- Native feel (doesn't look repurposed): [1-10]
- Voice match: [1-10]
- Hook strength: [1-10]
```

---

## Example

**Source:** Blog post — "Why Mid-Market Teams Are Ditching Jenkins"
**Source type:** Blog post (Solution Aware audience)
**Repurpose targets:** LinkedIn post + newsletter snippet

---

**File:** `output/campaigns/acme-cicd-launch/drafts/repurposed/repurpose-overview.md`

```
## Core Ideas Extracted
1. Jenkins maintenance cost = 5-10 eng-hours/week (the hidden tax)
2. Rollback drills cut incident resolution by 60-70%
3. Story: team cut deploy incidents 60% in 6 weeks without a DevOps hire

## Platform Map
| Platform  | Anchor Idea    | File                              | Status |
|-----------|----------------|-----------------------------------|--------|
| LinkedIn  | Idea #3 (story)| linkedin-ditching-jenkins.md      | Draft  |
| Newsletter| Idea #2 (drill)| newsletter-rollback-habit.md      | Draft  |
```

---

**LinkedIn version** (`linkedin-ditching-jenkins.md`):

Hook shifts from Solution Aware (blog reader searched this) → Problem Aware
(LinkedIn reader didn't). Lead with the pain story, not the mechanism.

```
We cut deploy incidents 60% in 6 weeks — no DevOps hire.

[Story-first body: what broke, what we changed, the monthly rollback drill]
[CTA: Full breakdown in comments — link to blog]
```

---

**Newsletter snippet** (`newsletter-rollback-habit.md`):

Hook shifts to insight reveal — subscribers are Most Aware, go deeper.

```
[Subject: The deploy that changed how I think about rollbacks]

[Open: the specific Monday morning incident — drop into the scene]
[Insight: rollback plans exist in runbooks; nobody drills them until it's
an emergency]
[Takeaway: monthly rollback drill as standing team ritual]
[CTA: I put the full framework in this week's blog post — link]
```

---

## Quality Checklist

Before marking complete:

- [ ] Source content fully read and audited
- [ ] Different anchor ideas used for different platforms (not the same point repeated)
- [ ] Each version is written natively for its platform
- [ ] None of the versions sound like they were obviously adapted from the original
- [ ] Hooks are platform-appropriate
- [ ] CTAs link back to original where appropriate
- [ ] Voice matches platform-specific tone from brand-guide.md (optional — skip if file doesn't exist)
- [ ] Overview file created with platform map
- [ ] All files saved to repurposed/ folder
- [ ] Self-assessment complete for each version
