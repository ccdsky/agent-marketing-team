# Editorial Review Rubric Reference

Used by Quality Gate. Read this file for detailed scoring guidance, feedback templates, and approval thresholds.

**Weights:** Voice Fidelity 30% | Clarity & Structure 20% | Craft Quality 20% | Conversion Architecture 20% | Positioning Alignment 10%

---

## Voice Fidelity — Detailed Scoring (Weight: 30%)

**Reference:** `context/voice-dna.md`

**Scoring:**
- **10/10:** Perfect voice match — could have been written by the owner
- **8-9/10:** Strong match, minor deviations
- **6-7/10:** Recognizable but has off-brand moments
- **4-5/10:** Generic, doesn't capture voice
- **1-3/10:** Wrong voice entirely

**Check for:**
- Sentence rhythm and pacing
- Word choice and vocabulary
- Personal vs corporate tone
- Humor, analogies, stories (if appropriate)
- Authenticity ("Would the owner actually say this?")

**Common voice issues:**
- Too formal/corporate ("We believe that..." vs "Here's the thing...")
- Too casual/slangy (overusing emojis, memes)
- Passive voice ("It can be seen..." vs "You'll see...")
- Jargon overload (using buzzwords the owner doesn't use)
- Generic AI writing patterns ("In today's fast-paced world...")

**How to fix:**
- Read out loud — does it sound like the owner talking?
- Compare to voice samples in voice-dna.md
- Rewrite in first person if too corporate
- Use specific examples instead of generalities

---

## Clarity & Structure — Detailed Scoring (Weight: 20%)

**Scoring:**
- **10/10:** Perfect structure — effortless to scan and understand
- **8-9/10:** Clear structure, minor flow issues
- **6-7/10:** Decent but could be more scannable
- **4-5/10:** Confusing structure, hard to follow
- **1-3/10:** Incoherent

**Check for:**
- Logical flow (does each section lead to the next?)
- Scannability (headers, bullets, white space)
- Sentence length variation (not all long or all short)
- Paragraph length (no walls of text)
- Clear transitions between sections

**Common structure issues:**
- Burying the lead (important point too deep)
- Too much setup before payoff
- Lack of hierarchy (no clear sections/headers)
- Repetition (saying same thing multiple ways)
- Missing transitions (abrupt topic shifts)

**How to fix:**
- Lead with the benefit/hook
- Use headers and bullets for scannability
- One idea per paragraph
- Cut unnecessary setup
- Add transition sentences

---

## Craft Quality — Detailed Scoring (Weight: 20%)

**Scoring:**
- **10/10:** Zero fluff — every word adds value
- **8-9/10:** Tight, minor opportunities to tighten
- **6-7/10:** Some fluff, could be more concise
- **4-5/10:** Lots of filler, needs significant cutting
- **1-3/10:** Mostly fluff

**Check for:**
- No fluff or filler
- Specific vs generic (concrete examples, numbers, names)
- Active voice vs passive
- Strong verbs (not weak "is/are/was/were")
- Typos, grammar, punctuation

**Common craft issues:**
- Fluff: "It's important to note that...", "In conclusion...", "Basically..."
- Vague: "Many people...", "Some research shows...", "It can help..."
- Passive: "It was discovered that..." vs "We discovered..."
- Weak verbs: "Is able to help" vs "helps"
- Redundancy: "Free gift", "advance planning", "past history"

**How to fix:**
- Cut every unnecessary word
- Replace vague with specific (numbers, names, examples)
- Convert passive to active voice
- Replace weak verbs with strong ones
- Run spell check, proofread carefully

---

## Conversion Architecture — Detailed Scoring (Weight: 20%)

**Reference:** The asset's own SKILL.md quality checklist. This criterion verifies the asset is *engineered to convert*, not just well-written. The items below are objective — each either holds or it doesn't. Do not score from vibes; check the draft against the list for its asset type.

**Scoring:**
- **10/10:** Every checklist item for the asset type holds
- **8-9/10:** One minor item soft (e.g. proof present but one asset below Tier 1)
- **6-7/10:** One structural item broken (wrong lead type, competing CTAs)
- **4-5/10:** Multiple structural items broken
- **1-3/10:** No conversion architecture — prose without a job

**Per-asset checklists:**

**Landing page** (from `/landing-page`):
- Lead type matches the diagnosed awareness stage (Schwartz → Masterson table)
- Proof block has Tier 1 assets (13/15+) covering 2+ Cialdini dimensions
- Mechanism passes both System 1 (intuitive nod) and System 2 (defensible) checks
- Exactly one conversion action — no competing CTAs
- Objection section covers the top 3 objections from icp.md

**Email sequence** (from `/email-sequence`):
- Arc never skips more than one awareness stage per email
- One CTA per email; intensity escalates soft → medium → hard across the sequence
- Subject lines under 50 chars, 3 options per email, no spam triggers
- Each email's hook matches the lead type for its TARGET stage

**Lead magnet** (from `/lead-magnet`):
- Value density holds: implementable result in under 30 minutes
- Title has outcome + audience + specificity marker
- Bridge to the paid offering is natural, one-line, not a hard sell
- Framing matches Problem Aware or Solution Aware (not Unaware/Most Aware)

**Blog post** (from `/blog-post`):
- Intro strategy matches the funnel stage's lead type (the table in Step 1)
- Title under 60 chars with primary keyword near front; meta 150-160 chars
- H2s read as answers to reader questions; FAQ uses secondary keywords
- CTA matches the journey stage (soft for awareness, direct for decision)

**Social post / newsletter** (from `/social-post`, `/newsletter`):
- Hook matches the traffic-source or subscriber-relationship awareness level
- One main idea, one CTA
- Platform constraints per the Quick Constraints Table in `platform-formats.md`

**How to fix:** Cite the specific checklist item that fails and the skill section that defines it — the Creative Specialist has the same list.

---

## Positioning Alignment — Detailed Scoring (Weight: 10%)

**Reference:** Campaign brief (`output/campaigns/[slug]/campaign-brief.md`)

**Scoring:**
- **10/10:** Perfectly aligned with positioning
- **8-9/10:** Mostly aligned, minor drift
- **6-7/10:** Some positioning, inconsistent
- **4-5/10:** Generic, doesn't reflect positioning
- **1-3/10:** Wrong positioning entirely

**Check for:**
- Uses approved positioning language
- Differentiates from competitors
- Reflects research insights
- Consistent throughout asset

**Common positioning issues:**
- Reverting to generic industry speak
- Copying competitor positioning
- Ignoring research findings
- Inconsistent messaging (different angle in each section)

**How to fix:**
- Re-read campaign brief for approved angle
- Search for positioning keywords (should appear throughout)
- Compare to competitor language (differentiate, don't copy)
- Ensure consistency across all sections

---

## Sprint-Specific Approval Thresholds

**For Sprint 2 drafts (first drafts):**
- Voice: 7/10 minimum
- Clarity: 7/10 minimum
- Craft: 6/10 minimum (expected to polish in Sprint 3)
- Conversion Architecture: 7/10 minimum (structural items must hold now — they don't improve with polish)
- Positioning: 8/10 minimum

**For Sprint 3 final drafts:**
- Voice: 8/10 minimum
- Clarity: 8/10 minimum
- Craft: 8/10 minimum
- Conversion Architecture: 8/10 minimum
- Positioning: 9/10 minimum

**Sprint focus:**
- Sprint 1: Structure and positioning only — do not evaluate polish or voice
- Sprint 2: Voice, positioning, and conversion architecture must be right — don't block on minor craft issues
- Sprint 3: All criteria at full bar — this ships

**If below thresholds, request revisions.**

---

## Revision Request Template

```markdown
## Editorial Review: [Asset Name]

**Overall Assessment:** [1-2 sentence summary]

**Decision:** ✅ Approved | ❌ Revisions Needed

---

### Voice Fidelity: [Score]/10

**What's working:**
- [Specific example of good voice match]
- [Specific example of good voice match]

**What needs work:**
- [Specific issue with line numbers/examples]
- [Specific issue with line numbers/examples]

**How to fix:**
- [Concrete action: "Rewrite intro using..."]
- [Concrete action with example]

---

### Clarity & Structure: [Score]/10

**What's working:**
- [Specific structural strength]

**What needs work:**
- [Specific structural issue]

**How to fix:**
- [Concrete action]

---

### Craft Quality: [Score]/10

**What's working:**
- [Specific craft strength]

**What needs work:**
- [Specific craft issue]

**How to fix:**
- [Concrete action]

---

### Conversion Architecture: [Score]/10

**Checklist items verified:** [which per-asset items hold]

**What needs work:**
- [Failed checklist item + the skill section that defines it]

**How to fix:**
- [Concrete action]

---

### Positioning Alignment: [Score]/10

**What's working:**
- [How positioning is reflected]

**What needs work:**
- [Positioning gaps]

**How to fix:**
- [Concrete action]

---

### Action Items for Creative Specialist:

**Critical (must fix):**
1. [Action item with file location/line numbers]
2. [Action item]

**Nice to have (consider):**
1. [Suggestion]
2. [Suggestion]

**Estimated revision time:** [X] hours

---

### Notes:
[Any additional context, questions for Creative Specialist, or open items]
```
