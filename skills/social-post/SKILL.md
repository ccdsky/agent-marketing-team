---
name: social-post
description: Write platform-optimized social posts (LinkedIn, Twitter/X, Substack Notes) with Schwartz traffic-source awareness matching.
---

# Social Post Skill

## Purpose

Write platform-optimized social posts (LinkedIn, Twitter/X, Substack Notes) that match your voice, engage your ICP, and drive the campaign goal.

Invoke this skill when creating any social content — standalone posts, campaign teasers, repurposed insights, or engagement posts.

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Your voice patterns and anti-patterns
- `context/icp.md` — Who you're speaking to and what language resonates
- `context/business-profile.md` — What you offer and your content pillars
- Campaign brief (if part of a campaign): `output/campaigns/[slug]/campaign-brief.md`
- Past learnings (if any): search `knowledge/learnings/` for relevant patterns

---

## Framework

### Step 1: Clarify the Goal

Before writing, answer:
- **Platform:** LinkedIn | Twitter/X | Substack Notes
- **Goal:** Awareness | Lead generation | Engagement | Traffic
- **Core idea:** One sentence — what insight, story, or hook is this post about?
- **CTA:** What do you want them to do after reading?
- **Audience awareness level:** Who sees this post — and what do they already know?

  | Traffic Source | Schwartz Awareness Level | Hook Strategy |
  |---------------|-------------------------|---------------|
  | Organic feed (followers) | Product/Most Aware | Lead with insight or proof — they know you. Skip introductions. |
  | Organic feed (non-followers, algorithm reach) | Unaware/Problem Aware | Lead with story, contrarian take, or pain — they don't know you yet. Hook must stand alone. |
  | Paid promotion / boosted | Unaware | Pattern interrupt — assume they've never heard of you. Curiosity or bold claim. |
  | Shared / reposted | Problem/Solution Aware | The sharer's credibility carries you. Lead with the mechanism or result. |

  When in doubt, assume the audience is **Problem Aware** — they feel the pain but haven't found you yet. This is the most common state for organic reach on LinkedIn and Twitter/X.

### Step 2: Choose a Hook Pattern

Pick one hook type based on the post goal:

| Hook Type | Pattern | Best For |
|-----------|---------|---------|
| **Contrarian** | "Everyone says X. Here's why that's wrong." | Thought leadership |
| **Insight reveal** | "I spent [time] learning [topic]. Here's what matters:" | Value-dense posts |
| **Story opener** | "Two years ago, I [did X]. Here's what happened:" | Brand building |
| **Specific result** | "[Specific outcome] in [specific timeframe]. Here's how:" | Lead gen |
| **Question** | "Why do [most people] fail at [topic]?" | Engagement |
| **Number** | "5 things I wish I knew about [topic]:" | Shareability |

### Step 3: Write Platform-Specific Draft

Write the full post following the platform structure below. Don't self-censor during drafting — revise in Step 4.

#### LinkedIn

**Structure:**
```
[Hook — 1-2 lines, stops the scroll]

[Bridge — 1 line connecting hook to content]

[Body — 3-7 lines, short paragraphs, one idea per paragraph]

[Proof or example — specific, concrete]

[CTA — soft ask or invitation]

[Hashtags — 3-5 relevant, placed after CTA]
```

**Rules:**
- First 2 lines must stand alone (they appear before "see more")
- Max 3 lines per paragraph (white space is your friend)
- No bullet lists in first 2 lines
- Emojis: use sparingly, only if authentic to your voice
- Length: 150-300 words optimal (can go to 600 for high-value long-form)

#### Twitter/X

**Structure (thread):**
```
Tweet 1: [Hook — the single most compelling point]
Tweet 2-8: [One idea per tweet, builds on previous]
Tweet N: [Summary or CTA]
```

**Structure (single tweet):**
```
[Hook] [Core insight]. [CTA or question?]
```

**Rules:**
- 280 chars per tweet
- Threads: 3-8 tweets optimal
- No hashtags in thread (kills engagement on X)
- Add one hashtag max at very end if needed
- Conversational, punchy, direct

#### Substack Notes

**Structure:**
```
[Hook or observation — 1-2 sentences]

[Insight or story — 3-5 sentences]

[Question or invitation to respond]
```

**Rules:**
- 150-500 words
- More personal, less polished than LinkedIn
- Can share article excerpts with commentary
- Questions perform well

### Step 4: Voice and ICP Pass

**Voice check** — Read aloud against `voice-dna.md`. Ask:
- Does this sound like the owner's actual speech patterns?
- Are there any phrases the voice-dna marks as anti-patterns?
- Is the tone calibrated correctly for this platform?
- Does it avoid the "AI writing" tells (excessive hedging, generic advice)?

**ICP check** — Verify against `icp.md`:
- Does this address a real pain point or aspiration of the ICP?
- Is the language they'd recognize (not jargon they don't use)?
- Would they share this? Tag someone? Save it?

Rewrite any lines that don't pass both checks.

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/social-[platform]-[topic]-draft.md`

For standalone posts (Simple Mode): Return output inline. Do not create a file unless the user asks.

**File format:**
```markdown
# Social Post: [Platform] — [Topic]

**Campaign:** [campaign name or "standalone"]
**Goal:** [awareness|leads|engagement|traffic]
**Date target:** [date or "flexible"]

---

## Draft

[Full post text, ready to copy-paste]

---

## Self-Assessment

- Voice match: [1-10]
- ICP relevance: [1-10]
- Hook strength: [1-10]
- Notes: [anything to flag for review]
```

---

## Quality Checklist

Before marking complete:

- [ ] Hook stops the scroll in first 2 lines
- [ ] Voice matches `voice-dna.md` patterns (read aloud test)
- [ ] No anti-patterns from voice-dna.md present
- [ ] ICP would recognize this as relevant to their situation
- [ ] Platform format followed (LinkedIn vs Twitter vs Notes)
- [ ] CTA is clear but not desperate
- [ ] No corporate speak or generic AI phrasing
- [ ] Self-assessment scores recorded
- [ ] File saved to correct output path
