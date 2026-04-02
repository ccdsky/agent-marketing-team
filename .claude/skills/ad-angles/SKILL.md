# Ad-Angle Multiplication Skill

## Purpose

Multiply a single approved positioning angle into 10-15 distinct creative variants for ads, social posts, email subjects, and content hooks. Each variant targets a different buyer psychology dimension and awareness stage, producing a ready-to-use angle library for Sprint 2 content creation.

Invoke when: Campaign Lead assigns angle multiplication after Sprint 1 checkpoint, Research Specialist needs to expand an approved angle, or user requests "multiply angles for [positioning angle]" or "generate ad angles for [campaign]."

**Different from `/positioning-angles`:** That skill generates 5-8 *strategic* angles scored by defensibility. This skill takes one *approved* angle and expands it into 10-15 *creative* variants tagged by dimension and channel.

---

## Methodology Sources

Cialdini (Influence) — 6 persuasion principles mapped to angle dimensions. Dixon/Adamson (Challenger Sale) — teach-tailor-take-control for contrarian angles. Schwartz — 5 awareness stages for angle targeting.

---

## Required Inputs

Before starting, always read:
- Approved positioning angle from Sprint 1: `output/campaigns/[slug]/strategy/positioning-angles-[date].md`
- Mechanism from `/positioning-angles` Step 3.5 output
- `context/icp.md` — Pain points, language, objections
- `context/voice-dna.md` — Voice and tone
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`

---

## Framework

### Step 1: Load the Core Angle

Extract from the approved positioning angle:
- **The positioning statement** (one sentence)
- **The mechanism** (from Step 3.5 — Failure → Shift → Result)
- **The primary ICP pain point** it addresses
- **The strongest available proof** (from proof library if available)

### Step 2: Multiply Across 6 Dimensions

Generate 2-3 hooks per dimension. Each must feel genuinely different — not a rewrite with synonyms. Target 12-18 raw angles, cull to 10-15.

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

For each of the 10-15 surviving angles, create a structured entry:

| # | Dimension | Hook (15 words max) | Awareness Stage | Best Channel | Proof Needed |
|---|-----------|---------------------|-----------------|-------------|-------------|
| 1 | Pain | "..." | Problem Aware | LinkedIn ad | None |
| 2 | Proof | "..." | Product Aware | Email subject | Case study |

**Awareness stage tagging:**
- Pain angles → typically target Unaware or Problem Aware
- Desire angles → Problem Aware or Solution Aware
- Proof angles → Product Aware
- Identity angles → Solution Aware (tribal differentiation)
- Contrarian angles → Unaware or Problem Aware (pattern interrupt)
- Urgency angles → Most Aware (close the deal)

**Channel tagging:**
- **LinkedIn post/ad** — works for all dimensions, 1-2 sentence hook
- **Email subject line** — under 50 chars, curiosity or benefit
- **Blog post title** — SEO-friendly, specific
- **Ad creative** — visual hook + 1 line, scroll-stop test
- **Landing page headline** — above-fold, clarity over cleverness

### Step 4: Quality Filter

Remove any angle that:
- Feels like a synonym rewrite of another angle (collapse them)
- Can't be written as a headline in under 15 words
- Fails the scroll-stop test: would you pause your feed for this?
- Uses urgency without a genuine deadline or scarcity
- Makes a claim the proof library can't support

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/strategy/ad-angles-[date].md`

For standalone use: `output/drafts/ad-angles-[topic]-[date].md`

```markdown
# Ad-Angle Library: [Campaign Name]

**Date:** [YYYY-MM-DD]
**Core positioning angle:** [The approved angle this expands]
**Mechanism:** [Named mechanism from Step 3.5]
**Campaign:** [slug if applicable]

---

## Core Angle Summary

**Positioning statement:** [One sentence]
**Primary ICP pain:** [From icp.md]
**Strongest proof:** [Best available evidence]

---

## Angle Library

| # | Dimension | Hook | Awareness Stage | Best Channel | Proof Needed |
|---|-----------|------|-----------------|-------------|-------------|
| 1 | Pain | [hook text] | [stage] | [channel] | [proof or None] |
| 2 | Pain | [hook text] | [stage] | [channel] | [proof or None] |
| 3 | Desire | [hook text] | [stage] | [channel] | [proof or None] |
[... 10-15 total]

---

## Angles by Dimension

### Pain ([N] angles)
1. **"[Hook]"** — [1-sentence expansion, why it works for this ICP]

### Desire ([N] angles)
[same format]

### Proof ([N] angles)
[same format]

### Identity ([N] angles)
[same format]

### Contrarian ([N] angles)
[same format]

### Urgency ([N] angles)
[same format]

---

## Dimension Coverage

| Dimension | Count | Awareness Stages Covered |
|-----------|-------|------------------------|
| Pain | [N] | [stages] |
| Desire | [N] | [stages] |
| Proof | [N] | [stages] |
| Identity | [N] | [stages] |
| Contrarian | [N] | [stages] |
| Urgency | [N] | [stages] |
| **Total** | **[N]** | |

---

## Usage Notes for Creative Specialist

- [Which angles to prioritize for which asset types]
- [Any angles that need additional proof before use]
- [Suggested A/B test pairings]
```

---

## Quality Gate

Before marking complete:

- [ ] 10-15 distinct angles (not rewrites of each other)
- [ ] All 6 dimensions represented (minimum 1 angle per dimension)
- [ ] Each angle tagged with awareness stage and best channel
- [ ] Proof-dependent angles have proof assets identified (or flagged as gaps)
- [ ] Urgency angles use genuine scarcity only (no manufactured deadlines)
- [ ] Every hook passes the 15-word headline test
- [ ] No angle makes a claim the proof library can't support
