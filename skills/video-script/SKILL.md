---
name: video-script
description: Write short-form video scripts (TikTok, Instagram Reels, YouTube Shorts) as timed shot tables with visual hooks, spoken word budgets, and explicit audio-track decisions.
---

# Video Script Skill

## When to Use

Write scripts for short-form vertical video (TikTok, Instagram Reels, YouTube Shorts). Video is a different asset class from social text posts: it has a time budget rather than a character budget, a visual hook rather than a written one, separate audio and on-screen-text tracks, and a shot structure.

Invoke this skill for any video asset — product demos, process/maker content, talking-head insights, or campaign teasers. For text posts, use `/social-post` instead.

---

## Required Inputs

Before writing, always read:
- `references/platform-formats.md` › Short-Form Video — the single source of truth for technical specs, duration caps, text-safe zones, and script constraints. **Cite it; never restate its numbers here or in drafts.**
- `context/voice-dna.md` — Your voice patterns and anti-patterns
- `context/icp.md` — Who you're speaking to and what language resonates
- **Named personas from the brief** — Load the primary and secondary persona dossiers named in the Campaign Brief's `Primary Persona(s)` / `Secondary Persona(s)` fields. **Skip if no personas are defined** — fall back to `context/icp.md` only.
- `context/business-profile.md` — What you offer
- Campaign brief (if part of a campaign): `output/campaigns/[slug]/campaign-brief.md`
- Past learnings (if any): search `knowledge/learnings/` for relevant patterns

---

## Framework

### Step 1: Clarify the Brief

- **Platform:** TikTok | Instagram Reels | YouTube Shorts (constraints differ — check the reference)
- **Duration target:** Use the proven range for the content type from `references/platform-formats.md` › Script Constraints
- **Goal:** Awareness | Lead generation | Follows | Traffic
- **Core idea:** One sentence — what does the viewer watch happen?
- **Audience awareness level:** Short-form discovery feeds (FYP, Reels tab, Shorts shelf) are almost entirely cold reach — assume **Unaware or Problem Aware**. The hook must stand alone with zero context about you. Only follower-targeted content (e.g., a Stories crosspost) may assume higher awareness.

### Step 2: Derive the Budgets

From the duration target and `references/platform-formats.md` › Script Constraints:

- **Spoken word budget** — scale the reference's words-per-duration rate to your target. Read the draft aloud; written pacing always overshoots.
- **Shot count** — plan 2-5 seconds per shot for demo/process content. A 20-second script is typically 5-7 shots.
- **Hook window** — the first shot must land inside the reference's hook window.

### Step 3: Design the Visual Hook

The hook is **visual and mid-action** — the thing is already happening in frame one. Never open with an introduction, a logo, or "hi everyone, today we're...".

| Hook Pattern | Frame One Shows | Best For |
|--------------|-----------------|----------|
| **Mid-process** | The most visually striking moment of the process, already underway | Maker/demo content |
| **Result-first** | The finished outcome, then "here's how" | Transformation content |
| **Pattern interrupt** | Something unexpected in an expected setting | Cold-reach awareness |
| **Problem close-up** | The pain, shown not described | Problem Aware audiences |

### Step 4: Decide the Audio Track

Make this an explicit choice, not a default:

- **Diegetic (process sound)** — the default per the reference; the payoff for maker/technical audiences
- **Voiceover** — only for narrative that visuals cannot carry; stays inside the word budget
- **Trending audio** — a deliberate reach play; forfeits process sound, so the visuals must carry everything

Technical detail (settings, materials, specs) goes in **on-screen text, not voiceover** — viewers absorb it visually while watching the action.

### Step 5: Write the Timed Shot Table

Script every shot as a row: time range, what's in frame, what's heard, what's on screen. Keep all on-screen text inside the text-safe zone defined in the reference.

### Step 6: Voice Pass

Verify spoken lines and on-screen text against `voice-dna.md` and `icp.md`. The save test: would the ICP save this to reference later?

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/video-[platform]-[topic]-draft.md`

For standalone requests (Simple Mode): Return output inline. Do not create a file unless the user asks.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/video-[platform]-[topic]-draft.md",
  "assessment": "[1-line: voice X/10, hook X/10, pacing X/10]",
  "ready_for": "quality-gate"
})
```

**File format:**
```markdown
# Video Script: [Platform] — [Topic]

**Campaign:** [campaign name or "standalone"]
**Duration:** [target, within platform cap per references/platform-formats.md]
**Goal:** [awareness|leads|follows|traffic]
**Audio track:** [diegetic|voiceover|trending — one, chosen deliberately]
**Spoken word count:** [N words / budget from duration]

---

## Shot Table

| Time | Visual | Audio | On-Screen Text |
|------|--------|-------|----------------|
| 0:00-0:02 | [Hook shot — mid-action] | [Sound] | [Text or —] |
| ... | ... | ... | ... |

---

## Caption + Hashtags

[Post caption, per the platform row in references/platform-formats.md Quick Constraints Table]

---

## Self-Assessment

- Hook lands in window: [yes/no]
- Voice match: [1-10]
- Word count vs budget: [N/budget]
- Notes: [anything to flag for review]
```

---

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Platform:** TikTok
**Duration:** 20 seconds
**Goal:** Awareness (technical audience)
**Audio:** Diegetic (keyboard, terminal bell) — process sound is the payoff
**Word budget:** ~55 spoken words

| Time | Visual | Audio | On-Screen Text |
|------|--------|-------|----------------|
| 0:00-0:02 | Screen recording, mid-deploy: red FAILED banner slams in | Error chime, typing continues | "deploy #4 failed. watch this." |
| 0:02-0:06 | Cursor types one command: `acme rollback --last-good` | Keys, terminal bell | — |
| 0:06-0:11 | Split screen: prod dashboard errors draining to zero, timer running | Soft keys | "42 seconds to green" |
| 0:11-0:16 | Terminal: `acme drill schedule --monthly` autocompletes | Keys | "the fix isn't the rollback. it's drilling it monthly" |
| 0:16-0:20 | Dashboard fully green; cursor hovers the drill calendar | Terminal bell, silence | "teams that drill: 40 min incidents -> 8" |

**Spoken:** none — fully diegetic; the on-screen text carries the narrative.
**Caption:** Your rollback is a runbook checkbox until the Friday it isn't. Monthly drills made ours boring. #devops #cicd

---

## Quality Checklist

Before marking complete:

- [ ] Hook is visual, mid-action, and lands inside the reference's hook window
- [ ] Duration within the platform's cap per `references/platform-formats.md` (no numbers restated from memory)
- [ ] Spoken word count within the budget derived in Step 2 (read aloud to verify)
- [ ] Audio track chosen deliberately and named in the draft
- [ ] Technical detail in on-screen text, not voiceover
- [ ] All on-screen text inside the text-safe zone per the reference
- [ ] Voice matches `voice-dna.md` (spoken lines AND on-screen text)
- [ ] No anti-patterns from voice-dna.md present
- [ ] Self-assessment scores recorded
- [ ] File saved to correct output path
- [ ] **Persona match:** Name one hot button from the primary persona dossier that appears in the script (cite the section). Name one red flag the script avoids. (If no personas are defined, leave unchecked.)
