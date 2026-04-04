# Market Research — Extended Reference

## Methodology Sources

Ellis (GrowthHackers) — 40% PMF test, value prop language mining. Moesta/Christensen — JTBD four forces (Push/Pull/Anxiety/Habit). Revella (Buyer Persona Institute) — 5 Rings of Buying Insight. Fishkin/SparkToro — audience behavior observation. Laja/Wynter — 4-layer messaging test (Clarity/Relevance/Value/Differentiation).

---

## Phase 1: LANDSCAPE — Detailed Sub-Steps

### 1a. Market Mapping
- Define the market category and adjacent categories
- Estimate market size and growth (from public sources: analyst reports, press releases, funding announcements)
- Identify the major segments within the market (by company size, industry, use case)
- Flag any recent disruptions: new entrants, regulatory changes, technology shifts, M&A

### 1b. Competitor Identification by Tier

| Tier | Label | Description | Fields to Capture |
|------|-------|-------------|-------------------|
| 1 | Direct | Products buyers directly compare | Name, URL, founding year, funding, ICP, value prop, pricing, size |
| 2 | Adjacent | Solve related problem; sometimes chosen instead | Same fields |
| 3 | Alternative | Real competitive alternative — "do nothing," spreadsheets, manual processes | Description of what buyers do instead |

### 1c. Positioning Analysis — Per Competitor Checklist
- Homepage headline: What outcome do they lead with?
- Sub-headline: Who do they target?
- Social proof used: Customers named? Numbers claimed?
- CTA: What action do they ask for?
- Category language: What do they call the space they're in?

Look for:
- **Positioning clusters** — multiple competitors saying similar things (opportunity for differentiation)
- **Positioning gaps** — problems the ICP has that no one is claiming to solve
- **Category framings** — anyone trying to create a new category?

### 1d. Technology and Trend Scanning
- Key technology trends affecting this market (AI, regulatory, economic)
- Recent funding activity and what it signals about market direction
- Job postings from competitors (what they're hiring for reveals strategic direction)
- Recent product launches or major feature announcements

---

## Phase 2: DEEP INTELLIGENCE — Detailed Sub-Steps

### 2a. Competitor Messaging Analysis — Laja's 4-Layer Framework

For each top competitor, score 1-5 on:
- **Clarity** — Is the value proposition immediately understandable?
- **Relevance** — Does it speak to real buyer problems?
- **Value** — Is the promised outcome worth caring about?
- **Differentiation** — Could another company say this exact thing?

Low scores = positioning opportunity.

### 2b. Customer Language Sources and Confidence Levels

**Sources accessible without login:** Product Hunt, Reddit (relevant subreddits), LinkedIn comments, Capterra (partial), App Store reviews

**Sources requiring login (use fallback):** G2 and TrustRadius require authentication — WebFetch returns login walls. Fallback: `WebSearch(query="site:g2.com [competitor] reviews [pain point]")` returns Google-indexed snippets.

**Confidence by source type:**

| Source Type | Default Confidence | Override condition |
|-------------|-------------------|--------------------|
| Direct customer quote (review, interview) | HIGH | Single outlier only → MEDIUM |
| Competitor website copy | HIGH | Content dated >1 year → MEDIUM |
| Analyst report / research study | MEDIUM | Study <6 months old → HIGH |
| Forum/Reddit discussion | MEDIUM | Single thread only → LOW |
| Google snippet (G2/TrustRadius via search) | MEDIUM | Single result only → LOW |
| AI Overview / SERP summary | LOW | Never upgrade — paraphrase only |
| Agent inference from patterns | LOW | Corroborated by 2+ sources → MEDIUM |

**If Firecrawl MCP is configured with authenticated sessions:** G2 and TrustRadius are accessible via `firecrawl.scrape()` — use for highest-quality review mining.

**JTBD Four Forces — organizing customer language:**
- **Push** (frustration with old solution): "I was tired of...", "We kept running into...", "The problem with [old tool] was..."
- **Pull** (attracted to new solution): "What sold me was...", "The thing that made me switch...", "I chose them because..."
- **Anxiety** (fear of switching): "I was worried about...", "My concern was...", "I wasn't sure if..."
- **Habit** (comfort with status quo): "We'd always just...", "It seemed easier to just keep..."

### 2c. Audience Behavior Mapping — Channels to Check
- **Online communities:** Subreddits, Slack groups, LinkedIn groups, Discord servers
- **Newsletters:** What publications do they read? (Check who their influencers cite)
- **Podcasts:** Which shows come up repeatedly in ICP discussions?
- **Creators:** Who do they follow and engage with on LinkedIn/Twitter?
- **Events:** Which conferences, webinars, communities do they participate in?

### 2d. Content Gap Analysis
- What topics do competitors own? (Where they have most traffic, links, engagement)
- What topics are they ignoring? (Problems the ICP has that no one is writing about)
- What's the quality bar? (Room to create something 10x better?)
- What formats work? (Long-form guides, tools, calculators, data reports, case studies)

---

## Phase 4: PRIMARY RESEARCH INSTRUMENTS

### 4a. JTBD Interview Guide Template

Opening: "Take me back to the day you decided to [search for/purchase]..."
- Explore each JTBD force with follow-up probes
- Revella's 5 Rings: Priority Initiative, Success Factors, Perceived Barriers, Buyer Journey, Decision Criteria
- Closing: "What would you tell someone who was considering [product]?"

### 4b. PMF Survey (Ellis-Style)
- Core question: "How would you feel if you could no longer use [product]?"
- Value prop question: "What is the main benefit you receive from [product]?"
- Competitive question: "What would you use instead?"
- Improvement question: "What type of person do you think would most benefit from [product]?"

### 4c. Message Test Variants
- Each variant tests a different positioning angle
- Include the competitive framing each headline implies
- Format ready for Wynter-style or 5-second test

---

## Full Output Template

```markdown
# Market Research Brief: [Market/Company]

**Date:** [YYYY-MM-DD]
**Scope:** [What was researched and why]
**Commissioned by:** [Campaign Lead / direct request]
**Feeds into:** [Positioning work / campaign brief / Sprint 1]

---

## Phase 1: Market Landscape

### Market Overview

**Category:** [Name and definition]
**Size and growth:** [Estimate + source]
**Maturity:** [Emerging / Growing / Mature / Declining]
**Key segments:** [By company size, use case, or vertical]

**Recent disruptions:**
- [Disruption 1 — implication]

### Competitive Map

**Tier 1 — Direct Competitors**

| Company | Value Prop | Target | Pricing | Size |
|---------|-----------|--------|---------|------|
| [Name] | [Headline positioning] | [ICP] | [Model] | [~X employees] |

**Tier 2 — Adjacent Competitors**
[Same table]

**Tier 3 — Real Competitive Alternative**
[Description of what buyers do instead — the status quo]

### Positioning Clusters and Gaps

**Where everyone is saying the same thing:** [The positioning cluster]
**Where no one is competing:** [The gap]
**Category framing attempts:** [Anyone trying to name a new category?]

---

## Phase 2: Deep Intelligence

### JTBD Customer Language Map

**Push (frustrations driving switching):**
> "[Direct quote]" — Source: [G2/Reddit/etc.]

**Pull (what attracts buyers to new solutions):**
> "[Direct quote]"

**Anxiety (fears about switching):**
> "[Direct quote]"

**Habit (status quo comfort):**
> "[Direct quote]"

### Audience Behavior Map

| Channel | Activity Level | Why They're There | Distribution Opportunity |
|---------|---------------|-------------------|--------------------------|
| [Reddit r/X] | High | [Topic focus] | [How to participate] |

### Content Gap Analysis

**Topics competitors own:** [Well-covered territory]
**Underserved topics:** [Real ICP problems nobody addresses well]
**Format opportunities:** [Formats missing from the space]

---

## Phase 3: Research Brief

### Finding 1: [Descriptive title]

**Summary:** [1-2 sentences]
**Evidence:** [Specific quotes, data, examples]
**Implication:** [What this means for positioning or content]
**Confidence:** HIGH / MEDIUM / LOW

[Repeat for 4-6 key findings]

---

### Competitor Messaging Scorecard (Laja Framework)

| Competitor | Clarity | Relevance | Value | Differentiation | Overall | Opportunity |
|-----------|---------|-----------|-------|-----------------|---------|-------------|
| [Name] | [1-5] | [1-5] | [1-5] | [1-5] | [avg] | [where they're weak] |

---

### Positioning Hypotheses

Based on this research, 3-5 positioning angles worth testing:

1. **[Angle name]:** [One sentence framing] — Confidence: [H/M/L]

*These feed directly into /positioning-angles for scoring and development.*

---

## Phase 4: Primary Research Instruments

**Status:** Instruments written — [Primary research conducted: Yes / No / Pending]
*If "No" or "Pending": note which hypotheses remain unvalidated by primary data.*

### JTBD Interview Guide

[Full interview guide with opening, probe questions, closing]

### PMF Survey (if applicable)

[Survey questions in order]

### Message Test Variants

| Variant | Headline | Positioning angle being tested |
|---------|----------|-------------------------------|
| A | [Headline] | [Angle] |

---

## Research Gaps and Confidence Flags

**What we couldn't find:**
- [Gap 1 — what primary research could fill it]

**Where to be cautious:**
- [Area with LOW confidence findings — and why]

**Recommended next steps:**
- [ ] [Specific human-led research to validate key hypotheses]
- [ ] [Data source to access if not available in desk research]
```
