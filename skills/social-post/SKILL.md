---
name: social-post
description: Write platform-optimized social posts (LinkedIn, Twitter/X, Substack Notes) with Schwartz traffic-source awareness matching.
---

# Social Post Skill

## When to Use

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

Apply the hook from Step 2 and write natively for the platform. Key constraints:
- **LinkedIn:** First 2 lines must stand alone (before "see more"). 150-300 words. 3-5 hashtags at end.
- **Twitter/X:** 280 chars/tweet. Threads: 3-8 tweets, no hashtags. Each tweet must stand alone.
- **Substack Notes:** 150-500 words. More personal than LinkedIn. Questions perform well.

For detailed platform formatting, see `agents/references/platform-formats.md`.

### Step 4: Voice Pass

Verify against `voice-dna.md` and `icp.md`. The share test: would the ICP tag someone or save this?

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/social-[platform]-[topic]-draft.md`

For standalone posts (Simple Mode): Return output inline. Do not create a file unless the user asks.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/social-[platform]-[topic]-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

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

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Platform:** LinkedIn
**Goal:** Lead generation (drive checklist opt-in)
**Hook type:** Specific result

---

**File:** `output/campaigns/acme-cicd-launch/drafts/social-linkedin-cicd-draft.md`

```
## Draft

We cut our deploy incidents by 60% in 6 weeks.

Not by hiring a DevOps engineer. Not by rewriting our pipeline from scratch.

By fixing the one thing nobody puts in their CI/CD runbook.

Here's the thing about mid-market engineering teams (20-50 engineers): you
graduate past the point where Jenkins "just works," but you're not big enough
to justify a dedicated platform engineer to maintain it.

So you inherit a CI/CD setup that works 90% of the time.

That other 10% costs you 3-4 hours per incident, a Friday afternoon on
call, and one engineer who quietly starts job hunting because they're tired
of being paged.

The fix we found: rollback validation as a standing monthly drill.

Not a runbook checkbox. An actual drill — deploy something, roll it back,
time it, fix what broke. Repeat monthly.

Teams that do this cut incident resolution from 40+ minutes to under 8.

If you're evaluating CI/CD options for a growing team, I put together a
migration checklist that makes rollback validation step one (not step nine).

Link in comments.

#devops #cicd #engineeringteams
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
