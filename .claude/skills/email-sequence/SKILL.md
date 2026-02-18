# Email Sequence Skill

## Purpose

Write automated email campaigns — drip sequences, nurture sequences, onboarding sequences, or lead magnet delivery sequences. Produces complete, ready-to-load emails with subject lines, preview text, and body copy.

Invoke when: Campaign needs an email sequence. Works for cold, warm, and hot audiences.

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Voice and tone
- `context/icp.md` — Subscriber mindset, pain points, language
- `context/business-profile.md` — Offering details and positioning
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md`
- Research package (if available): `knowledge/research/[relevant]-[date].md`

---

## Framework

### Step 1: Define Sequence Type and Arc

**Sequence types:**

| Type | Trigger | Goal | Length |
|------|---------|------|--------|
| **Lead magnet delivery** | Opt-in for lead magnet | Deliver value + warm to next step | 3-5 emails |
| **Nurture** | General opt-in | Build trust, establish authority | 5-10 emails |
| **Onboarding** | Trial/customer signup | Drive activation and success | 5-7 emails |
| **Launch** | Product launch window | Convert to buyers | 5-7 emails |
| **Re-engagement** | Inactive subscribers | Win back or clean list | 3-5 emails |

**Sequence arc:** Plan the emotional journey before writing individual emails:
```
Email 1: [Emotional state at start] → deliver promise
Email 2: Build on promise, add depth
Email 3: Introduce conflict or challenge
Email 4: Resolve with insight or solution
Email 5: CTA + urgency or next step
```

### Step 2: Write Each Email

For each email, complete in this order:

#### 1. Subject Line (write 3 options, choose the strongest)
**Formulas:**
- Curiosity gap: "The one thing most [ICP] get wrong about [topic]"
- Direct benefit: "Your [lead magnet name] is inside"
- Story: "What happened when I tried [approach]"
- Question: "Are you making this mistake?"
- Specific: "[Number] [timeframe] from now, you could [outcome]"

**Rules:**
- Under 50 characters for mobile (9 words max)
- No spam triggers: "free", "guarantee", "!!!",  ALL CAPS
- First word is always visible on mobile

#### 2. Preview Text (50-100 chars)
Extends the subject line. Never repeat the subject line. Tease what's inside.

#### 3. Opening Hook (first 2 sentences)
The subscriber scans this before deciding to read. Options:
- Reference shared experience ("Last week, a [ICP role] told me...")
- Lead with the most valuable insight ("The fastest way to [goal] isn't what you think.")
- Story start ("Three years ago, I made a decision that...")

#### 4. Body (voice-matched, one idea per email)
**Email body structure:**
```
[Opening hook — 2 sentences]

[Bridge — connects hook to main idea — 1-2 sentences]

[Main idea — 3-6 short paragraphs, one idea each]
  - Concrete example or story to illustrate
  - Specific, actionable insight
  - Connection to reader's situation

[Transition — leads to the CTA]

[CTA — one action, one link]

[Signature — personal, matches voice]
```

**Length guidance:**
- Lead magnet delivery emails: 150-300 words (they want the thing, not a novel)
- Nurture emails: 300-600 words (value-dense)
- Launch emails: 400-800 words (need to sell)

#### 5. CTA
One link, one action. Never two CTAs in the same email.

**CTA types by sequence stage:**
- Early emails: soft CTA (reply to this email, read this article)
- Middle emails: medium CTA (download this, watch this)
- Later emails: hard CTA (buy, book a call, join)

### Step 3: Review the Full Sequence

Read all emails in sequence. Check:
- Does the arc make sense? Is there a beginning, middle, end?
- Does each email earn the right to the next?
- Is the CTA escalation gradual (not hard-selling in email 1)?
- Does the voice remain consistent across all emails?

### Step 4: Voice and ICP Check

For each email:
- Read aloud against voice-dna.md patterns
- Verify language matches ICP's vocabulary
- Remove any "AI writing" tells (hedging, passive voice, generic advice)

---

## Output Format

Save each email as a separate file:

`output/campaigns/[campaign-slug]/drafts/email-sequence/email-01-[slug].md`
`output/campaigns/[campaign-slug]/drafts/email-sequence/email-02-[slug].md`

Plus a sequence overview file:
`output/campaigns/[campaign-slug]/drafts/email-sequence/sequence-overview.md`

**Individual email file format:**
```markdown
# Email [N]: [Short title]

**Send timing:** Day [X] after trigger / [specific date]
**Sequence goal:** [what this email does in the arc]

---

## Subject Line Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

**Recommended:** Option [N] — [brief reason]

## Preview Text
[Preview text]

---

## Body

[Full email body, ready to paste into email platform]

---

## Self-Assessment
- Voice match: [1-10]
- Subject line strength: [1-10]
- CTA clarity: [1-10]
```

**Sequence overview file format:**
```markdown
# Email Sequence: [Campaign Name]

**Type:** [lead magnet delivery | nurture | onboarding | launch | re-engagement]
**Length:** [N] emails
**Trigger:** [What starts the sequence]

## Sequence Arc
[Describe the emotional journey and arc of the sequence]

## Email Index
| # | Title | Send Timing | Goal | CTA |
|---|-------|------------|------|-----|
| 1 | [title] | Day 0 | [goal] | [CTA] |
...

## Performance Benchmarks (to track after launch)
- Open rate target: [X]%
- Click rate target: [X]%
- Conversion target: [X]%
```

---

## Quality Checklist

Before marking complete:

- [ ] Sequence arc defined (beginning → middle → end)
- [ ] Each email has 3 subject line options
- [ ] Subject lines under 50 characters, no spam triggers
- [ ] Opening hooks strong enough to earn the read
- [ ] One CTA per email (never two)
- [ ] CTA escalates naturally across the sequence
- [ ] Voice consistent across all emails (read-aloud test)
- [ ] ICP language used throughout (check icp.md Language Patterns)
- [ ] Sequence overview file created
- [ ] All files saved to correct path structure
