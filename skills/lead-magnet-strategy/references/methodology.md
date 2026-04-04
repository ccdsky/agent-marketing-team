# Lead Magnet Strategy — Extended Reference

## Methodology Sources

Hormozi ($100M Leads) — Bridge Framework, Value Equation, three lead magnet types, "give away the secrets." Exposure Ninja — CLOSURE framework, Train Journey Principle, Three Pillars test, Homer Simpson Principle.

---

## Lead Magnet Type Selection Guide

| Type | Best For | B2B Examples |
|------|----------|-------------|
| **Problem Revealer** | ICPs who don't know how bad the problem is | Free audit, assessment, gap analysis, benchmark report |
| **Sample / Trial** | ICPs who need to experience before buying | Free pilot project, one-month access, first campaign free |
| **One Step** | ICPs who need process clarity | Free strategy session, architecture review, campaign brief |

**Selection logic:**
- If the ICP needs to *discover* the problem → Problem Revealer
- If the ICP is *aware* but hesitant to commit → Sample/Trial
- If the ICP is *ready* but wants to verify competence → One Step

## Delivery Mechanism Options

| Mechanism | Perceived Value | Scalability | Best For |
|-----------|----------------|-------------|----------|
| Software/Tool (calculator, assessment, template) | High | High | B2B SaaS, data-driven ICPs |
| Information (guide, checklist, framework) | Medium | High | Education-first markets |
| Service (free session, free audit) | Highest | Low | High-ticket, enterprise sales |
| Physical (report, workbook) | High | Medium | Enterprise/high-touch sales |

**B2B bias:** Prioritize Software/Tool and Service types. Information-only rarely justifies contact info in a crowded market.

---

## Value Equation — Denominator Guidance

**Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)**

Time Delay and Effort are in the denominator — lower scores mean faster/easier, which increases Value. A score of 1 for each means "instant and effortless." Score them honestly: slow or effortful lead magnets should get high denominator scores, which correctly reduces the Value calculation.

**Minimum threshold:** Value score ≥ 6.25 (i.e., 5×5 / 2×2) before proceeding.

**Denominator is the competitive advantage.** Anyone can claim a big dream outcome. The question is: can you deliver it faster and with less effort than alternatives?

---

## Name Specificity Formula and Examples

**Formula:** [Specific outcome] + [Target audience marker] + [Timeframe or mechanism]

**Strong name examples:**
- "The B2B SaaS CAC Benchmark Calculator: See How Your Customer Acquisition Costs Compare to 500+ Similar Companies" ✅
- "The 90-Day Content Audit for Marketing Teams Who Need Results Before Q4" ✅

**Weak name examples:**
- "5 Lead Generation Tactics" ❌ (no outcome, no audience, no specificity)
- "The Ultimate Guide to B2B Marketing" ❌ (too broad, no outcome)

**Evaluation criteria for each name:**
- Does it name a specific outcome?
- Does it identify the target ICP?
- Does it include a timeframe or specificity marker?
- Would the ICP pause their scroll for this?

---

## Homer Simpson Delivery Principle — Full Checklist

Design for the distracted, time-poor, mobile user:
- **Form:** Name + email only. No phone, company, job title (unless sales-led)
- **Delivery:** Instant — email delivers within 60 seconds of signup
- **Format:** PDF, video link, or tool URL — not a file download requiring special software
- **Mobile:** Must work perfectly on mobile (large majority of B2B buyers check on phones)
- **No account creation** — ever

---

## Distribution Channel Framework

| Channel | Format Requirements | Audience Fit | Cost | Expected Conv. Range |
|---------|--------------------|--------------|----- |---------------------|
| Blog CTAs | Content relevance | Medium-High | Low | 1-3% of readers |
| LinkedIn posts/DMs | Short-form value preview | High | Low-Medium | 2-5% of engaged |
| LinkedIn ads | Visual + copy | High | Medium-High | 0.5-2% of clicks |
| Google ads | Search-intent match | Medium | Medium-High | 2-5% of clicks |
| Newsletter co-marketing | Format fit | High | Medium | 3-8% of opens |
| Podcast mention | Memorable URL | High | Low-Medium | 1-4% of listeners |
| Direct outreach | Personalization | Very High | High-time | 5-15% of prospects |

---

## Campaign Mode Handoff Template

Include in output so Campaign Lead can create the email sequence task:

```
TaskCreate(
  subject="[S2] Draft — Email sequence nurturing [lead magnet topic] opt-ins",
  description="Design email nurture sequence for [lead magnet name] opt-ins. Read nurture goals from lead magnet concept brief: output/campaigns/[slug]/strategy/lead-magnet-concept-[date].md → section 'Nurture Sequence Goals'. Use /email-sequence skill to determine arc, count, and structure from those goals."
)
```

---

## Full Output Template

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

**Type selection rationale:** [1-2 sentences on why this type fits the ICP's stage and business model]

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

## Nurture Sequence Goals

**Delivery:** [How lead magnet arrives — instant email link / PDF / tool URL — within 60 seconds]
**First-touch moment:** [What value does the subscriber get in the first 5 minutes?]
**Next problem revealed:** [Which problem does the lead magnet expose that the core offer solves?]
**Nurture goal:** [What should the subscriber believe or be able to do before a conversion offer is appropriate?]

*Brief these goals to `/email-sequence` skill — let it determine the arc, email count, and structure.*

---

## Distribution Channels

| Channel | Format | Audience Fit | Benchmark Range (est.) |
|---------|--------|--------------|------------------------|
| [Channel] | [Format req.] | [High/Med/Low] | [X%] |

*Industry benchmark ranges. Replace with your actual conversion rates after first campaign.*

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
