# Lead Magnet Strategy Skill

## Purpose

Design high-converting lead magnet concepts based on the business's core offer, ICP pain points, and competitive landscape. Produces a scored concept brief before any content creation begins — preventing the common failure of building the wrong thing well.

Invoke when: Campaign Lead needs a lead magnet concept before assigning `/lead-magnet` content creation, or user requests "design a lead magnet for [business/campaign]."

**Important:** This skill produces a *concept brief*, not a finished lead magnet. The `/lead-magnet` skill creates the actual content. Always run this first.

---

## Methodology Sources

Hormozi ($100M Leads) — Bridge Framework, Value Equation, three lead magnet types, "give away the secrets." Exposure Ninja — CLOSURE framework, Train Journey Principle, Three Pillars test, Homer Simpson Principle.

---

## Required Inputs

Before starting, always read:
- `context/business-profile.md` — Core offer, target deal, unique mechanism
- `context/icp.md` — Pain points, vocabulary, content preferences, current alternatives
- `context/voice-dna.md` — Owner's positioning and areas of expertise
- Research package: `knowledge/research/[relevant]-[date].md` (if available — especially market research and positioning angles)
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if this is for a specific campaign)

---

## Framework

### Step 1: Define the Bridge

The bridge is the conceptual foundation. Get this right before anything else.

**Map it out:**

```
NARROW PROBLEM: [What specific problem can we solve completely?]
         ↓
LEAD MAGNET: [The complete solution to that narrow problem]
         ↓
NEXT PROBLEM REVEALED: [What problem does solving this reveal?]
         ↓
CORE OFFER: [How our paid offer solves that next problem]
```

**Test the bridge:**
- Is the narrow problem specific enough that someone can fully solve it with this lead magnet?
- Is the next problem revealed a natural logical consequence (not manufactured)?
- Does the core offer obviously solve the next problem (not a stretch)?
- Would the ICP recognize this path as sensible, not salesy?

If the bridge doesn't feel natural and logical, redesign before continuing.

### Step 2: Select Lead Magnet Type

Match the type to the business model and ICP:

| Type | Best For | B2B Examples |
|------|----------|-------------|
| **Problem Revealer** | ICPs who don't know how bad the problem is | Free audit, assessment, gap analysis, benchmark report |
| **Sample / Trial** | ICPs who need to experience before buying | Free pilot project, one-month access, first campaign free |
| **One Step** | ICPs who need process clarity | Free strategy session, architecture review, campaign brief |

**Selection guide:**
- If the ICP needs to *discover* the problem → Problem Revealer
- If the ICP is *aware* but hesitant to commit → Sample/Trial
- If the ICP is *ready* but wants to verify competence → One Step

Also consider the **delivery mechanism:**
- **Software/Tool** (calculator, assessment, template) — high perceived value, scalable
- **Information** (guide, checklist, framework) — lower cost, easier to produce
- **Service** (free session, free audit) — highest conversion, not scalable
- **Physical** (report, workbook) — best for enterprise/high-touch sales

B2B bias: Prioritize Software/Tool and Service types. Information-only rarely justifies contact info in a crowded market.

### Step 3: Score with the Value Equation

Before building anything, score the concept:

**Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)**

Rate each dimension 1-10:
- **Dream Outcome** — How desirable is the promised result to the ICP? (10 = career-changing, 1 = marginal)
- **Perceived Likelihood** — How believable is it that this delivers? (10 = guaranteed by social proof, 1 = claim only)
- **Time Delay** — How long until the ICP gets value? (1 = instant, 10 = weeks/months of waiting) ← lower is better for denominator
- **Effort & Sacrifice** — How much work does the ICP invest? (1 = zero effort, 10 = significant time required) ← lower is better for denominator

**Denominator note:** Time Delay and Effort are in the denominator — lower scores mean faster/easier, which increases Value. A score of 1 for each means "instant and effortless." Score them honestly: slow or effortful lead magnets should get high denominator scores, which correctly reduces the Value calculation.

**Score formula:** (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)

**Minimum threshold:** Value score ≥ 6.25 (i.e., 5×5 / 2×2) before proceeding. Below this → redesign.

**Denominator is the competitive advantage.** Anyone can claim a big dream outcome. The question is: can you deliver it faster and with less effort than alternatives?

### Step 4: Apply Exposure Ninja's Three Pillars Test

- **Relevancy:** Is this aligned with the ICP's current urgent need? (Not interesting — urgent)
- **Perceived Value:** Would the ICP feel this is worth giving their contact info for?
- **True to Your Word:** Can you actually deliver everything you're promising? Fully?

Fail any pillar → redesign before continuing.

### Step 5: Test Three Names

"5x more people read your headline than your body copy." — Hormozi

Generate three naming options using the specificity formula:
**[Specific outcome] + [Target audience marker] + [Timeframe or mechanism]**

Examples of strong names:
- "The B2B SaaS CAC Benchmark Calculator: See How Your Customer Acquisition Costs Compare to 500+ Similar Companies" ✅
- "The 90-Day Content Audit for Marketing Teams Who Need Results Before Q4" ✅
- "5 Lead Generation Tactics" ❌ (no outcome, no audience, no specificity)
- "The Ultimate Guide to B2B Marketing" ❌ (too broad, no outcome)

**Evaluation criteria for each name:**
- Does it name a specific outcome?
- Does it identify the target ICP?
- Does it include a timeframe or specificity marker?
- Would the ICP pause their scroll for this?

Select the strongest name. Note the other two as A/B test options.

### Step 6: Design Frictionless Delivery

Homer Simpson Principle — design for the distracted, time-poor, mobile user:

- **Form:** Name + email only. No phone, company, job title (unless sales-led)
- **Delivery:** Instant — email delivers within 60 seconds of signup
- **Format:** PDF, video link, or tool URL — not a file download requiring special software
- **Mobile:** Must work perfectly on mobile (a large majority of B2B buyers check on phones)
- **No account creation** — ever

### Step 7: Map the Nurture Goals

After the opt-in, what happens? The lead magnet starts the relationship — the email sequence completes it.

Define delivery mechanics and nurture goals for the `/email-sequence` skill to design the actual arc:

- **Delivery:** How does the lead magnet arrive? (Instant email link / PDF attachment / tool URL) — within 60 seconds of signup
- **First-touch moment:** What value does the subscriber get in the first 5 minutes?
- **Next problem revealed:** Which specific problem does the lead magnet expose that the core offer solves? (This is the bridge the sequence must complete)
- **Nurture goal:** What should the subscriber believe or be able to do by the time a conversion offer is appropriate?

**Do not prescribe the email count or arc structure here.** The `/email-sequence` skill designs the arc based on audience temperature, sequence goal, and the bridge defined above. Brief it with the delivery mechanics and nurture goals — let it determine structure.

### Step 8: Map Distribution Channels

How does the lead magnet reach the ICP? Identify 3-5 distribution channels:

- **Organic:** Blog CTAs (most relevant posts), homepage, LinkedIn posts/DMs, community sharing
- **Paid:** LinkedIn ads, Google ads (if keywords support it)
- **Partnership:** Referral from complementary newsletter, podcast mention, co-marketing
- **Sales:** Direct outreach tool (send to prospects as value-first opener)
- **Referral:** Strong enough that recipients share it (benchmark: "Would someone screenshot this and send it to a colleague?")

For each channel, note: format requirements, audience fit, cost (time or money), and expected conversion rate.

### Step 9: Quality Gate Test

Before finalizing the concept: "Would someone pay for this?"

If yes → proceed to content creation with `/lead-magnet` skill.
If no → back to Step 1. A weak lead magnet damages your brand across ALL channels.

**Additional quality gates:**
- "Would the ICP share this with a colleague?" (Hormozi's viral threshold)
- "Does this demonstrate our actual competence at what we sell?"
- "Is the bridge to our core offer obvious without being pushy?"

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/strategy/lead-magnet-concept-[date].md`

For standalone use: `output/drafts/lead-magnet-concept-[topic]-[date].md`

```markdown
# Lead Magnet Concept Brief: [Concept Name]

**Date:** [YYYY-MM-DD]
**Campaign:** [slug if applicable]
**Feeds into:** `/lead-magnet` skill for content creation

---

## The Bridge

**Narrow problem:** [Specific problem the lead magnet completely solves]
**Lead magnet:** [What it is, in one sentence]
**Next problem revealed:** [What problem solving this exposes]
**Core offer connection:** [How the paid offer solves the next problem]

**Bridge quality:** [Natural / Forced — and brief note on why]

---

## Lead Magnet Type and Format

**Type:** [Problem Revealer / Sample-Trial / One Step]
**Format:** [Software/Tool / Information / Service / Physical]
**Delivery mechanism:** [PDF / Tool URL / Email course / Video / Live session]

**Type selection rationale:** [1-2 sentences on why this type fits the ICP's stage and the business model]

---

## Value Equation Score

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Dream Outcome | [1-10] | [Why] |
| Perceived Likelihood | [1-10] | [Why] |
| Time Delay | [1-10] | [Why: how fast does ICP get value?] |
| Effort & Sacrifice | [1-10] | [Why: how much work from the ICP?] |

**Value Score:** ([Dream Outcome] × [Perceived Likelihood]) / ([Time Delay] × [Effort]) = **[X.X]**
**Threshold:** ≥ 6.25 required. [PASS / FAIL]

---

## Three Pillars Test

- **Relevancy:** [Pass/Fail — note on urgency]
- **Perceived Value:** [Pass/Fail — note on contact-info worthiness]
- **True to Your Word:** [Pass/Fail — can we deliver everything promised?]

---

## Name Options

**Primary (recommended):** [Full name]
**A/B option 1:** [Alternative]
**A/B option 2:** [Alternative]

**Name evaluation:** [1-2 sentences on why the primary wins]

---

## Delivery Design

- **Form fields:** [Name + Email only / variations]
- **Delivery time:** [Instant / within X minutes]
- **Format:** [PDF, video link, tool URL, etc.]
- **Mobile-friendly:** [Yes / Needs modification]

---

## Nurture Sequence Concept

**Email 1 (instant):** [What to deliver — no selling]
**Email 2 (day 2-3):** [What insight extends the value — reveals next problem]
**Email 3 (day 4-5):** [Social proof story — who solved the next problem]
**Email 4 (day 6-7):** [The offer — connect to core offer with single CTA]

*Brief this to Creative Specialist for `/email-sequence` execution.*

---

## Distribution Channels

| Channel | Format | Audience Fit | Estimated Conversion |
|---------|--------|--------------|----------------------|
| [Channel] | [Format req.] | [High/Med/Low] | [X%] |
[...]

**Primary channel recommendation:** [Where to focus first and why]

---

## Quality Gate Results

- [ ] "Would someone pay for this?" — [Yes / No + note]
- [ ] "Would the ICP share this with a colleague?" — [Yes / No + note]
- [ ] "Does this demonstrate our competence at what we sell?" — [Yes / No + note]
- [ ] "Is the bridge obvious without being pushy?" — [Yes / No + note]

**Recommendation:** [PROCEED to /lead-magnet creation / REDESIGN — and why]

---

## Brief for Creative Specialist

If proceeding to content creation, include this handoff:

- **Asset to create:** [Lead magnet name and format]
- **Key constraint:** Must fully solve [narrow problem] — not a teaser
- **Voice note:** [Specific voice-dna.md guidance relevant to this asset]
- **Bridge to maintain:** Reference the connection to [core offer] at the end
- **Length/format guidance:** [Specific scope — e.g., "10-15 checklist items, max 2 pages"]
```

---

## Quality Gate

Before marking complete:

- [ ] Bridge is natural and logical — solving narrow problem genuinely reveals the next problem (not manufactured)
- [ ] Value Equation score ≥ 6.25 — if below threshold, redesign before proceeding
- [ ] All three Exposure Ninja Pillars pass (Relevancy / Perceived Value / True to Your Word)
- [ ] Quality gate tests pass: "Would someone pay for this?" and "Would the ICP share it with a colleague?"
- [ ] Nurture goals section defines delivery mechanics and bridge — NOT a prescribed email arc
