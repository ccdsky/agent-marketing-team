---
name: email-sequence
description: Write automated email campaigns (drip, nurture, onboarding, lead magnet delivery) with Schwartz awareness-stage arcs and Masterson lead types.
---

# Email Sequence Skill

## When to Use

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
- Proof library (if available): `knowledge/research/proof-library-[company]-[date].md`

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

**Awareness-Stage Arc:**

In addition to the emotional arc above, map each email to an awareness-stage transition. The subscriber enters at one stage and should exit at the next:

| Email | Schwartz Awareness Transition | Job | Masterson Lead Type |
|-------|---------------------|-----|---------------------|
| 1 | Problem Aware → Solution Aware | Deliver value, name the mechanism | Solution Lead |
| 2 | Solution Aware → Solution Aware (deeper) | Expand mechanism, share non-obvious insight | Secret Lead |
| 3 | Solution Aware → Product Aware | Introduce your specific approach, case study | Proof Lead |
| 4 | Product Aware → Most Aware | Handle top objection, build certainty | Promise Lead |
| 5 | Most Aware → Convert | Clear offer, genuine urgency, one CTA | Direct Offer Lead |

*The table above shows a lead-magnet-delivery example. Adjust entry stage based on subscriber temperature:*
- **Nurture sequences:** Subscribers may enter at Unaware — add 1-2 emails at the start for story/problem-agitation before introducing solutions.
- **Launch sequences:** Subscribers are typically Solution or Product Aware — compress early stages, emphasize proof and offer.
- **Re-engagement sequences:** Subscribers were Most Aware but lapsed — restart at Problem Aware to rebuild relevance.

**Rule:** Never skip more than one awareness stage per email. If subscribers enter at Unaware, you need more emails — don’t jump straight to a product pitch.

Each email’s subject line and opening hook should match the Masterson lead type for its TARGET awareness stage (the stage you’re moving the reader toward, not where they start).

### Step 2: Write Each Email

For each email, complete in this order:

#### 1. Subject Line (write 3 options, choose the strongest)
**Formulas (top 2):**
- Curiosity gap: "The one thing most [ICP] get wrong about [topic]"
- Direct benefit: "Your [lead magnet name] is inside"

*(See `skills/email-sequence/references/subject-line-formulas.md` for full list)*

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

Save the complete sequence as a **single file** so Quality Gate and Distribution Specialist can read and hand off a single `metadata["deliverable"]` path:

`output/campaigns/[campaign-slug]/drafts/email-sequence-[slug]-draft.md`

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/email-sequence-[slug]-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

**File format:**
```markdown
# Email Sequence: [Campaign Name]

**Type:** [lead magnet delivery | nurture | onboarding | launch | re-engagement]
**Length:** [N] emails
**Trigger:** [What starts the sequence]

## Sequence Arc
[Describe the emotional journey: Email 1 → N]

## Email Index
| # | Title | Send Timing | Goal | CTA |
|---|-------|------------|------|-----|
| 1 | [title] | Day 0 | [goal] | [CTA] |

---

## Email 1: [Short title]

**Send timing:** Day [X] after trigger
**Goal:** [what this email does in the arc]

### Subject Line Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

**Recommended:** Option [N] — [brief reason]

### Preview Text
[Preview text]

### Body

[Full email body, ready to paste into email platform]

---

## Email 2: [Short title]
[... repeat for each email ...]

---

## Self-Assessment
- Voice consistency across sequence: [1-10]
- Subject line strength (average): [1-10]
- Arc coherence: [1-10]
```

---

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Sequence type:** Lead magnet delivery (CI/CD Migration Checklist)
**Trigger:** Opt-in form submission

---

**File:** `output/campaigns/acme-cicd-launch/drafts/email-sequence-cicd-checklist-draft.md`

```
## Sequence Arc
Email 1: Deliver checklist + plant the "why migrations fail" hook
Email 2: Share the #1 reason migration plans stall (non-obvious insight)
Email 3: Case study — how Lattice cut deploy time 60% in 6 weeks (proof)
Email 4: Handle the "we're too customized" objection head-on
Email 5: Offer a free pipeline audit (direct CTA)

## Email Arc Table
| # | Title               | Timing | Goal                        | CTA              |
|---|---------------------|--------|-----------------------------|------------------|
| 1 | Your checklist      | Day 0  | Deliver, build curiosity    | Download link    |
| 2 | The hidden blocker  | Day 2  | Non-obvious insight         | Reply or read    |
| 3 | The Lattice story   | Day 4  | Proof + social proof        | Read case study  |
| 4 | "We're too custom"  | Day 6  | Objection removal           | Book a call      |
| 5 | Free audit offer    | Day 8  | Convert to booked call      | Schedule audit   |

---

## Email 1: Your checklist is here

**Send timing:** Day 0 (immediate)
**Goal:** Deliver value, earn the read on email 2

### Subject Line Options
1. Your CI/CD migration checklist
2. Here's the checklist (+ one thing most teams miss)
3. Your download is ready

**Recommended:** Option 2 — plants curiosity without withholding the goods

### Preview Text
Opens right in your browser. Takes 4 minutes to read.

### Body

Hey [First Name],

Your CI/CD Migration Checklist is attached — [DOWNLOAD LINK].

It covers the 4 phases most teams skip that turn a 2-week migration into
a 3-month headache. Phase 3 (rollback validation) is the one that bites
everyone.

One thing I'll share tomorrow: the reason most migration plans stall has
nothing to do with the tooling. I'll show you what it actually is.

For now — grab the checklist and check off what you've already done.
You might be further along than you think.

— [Sender Name]

P.S. If you're mid-migration and something in the checklist doesn't apply
to your stack, just reply. I read every response.
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
- [ ] File saved to correct output path (single file containing full sequence)
