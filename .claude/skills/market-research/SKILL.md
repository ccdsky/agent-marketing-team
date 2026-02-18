# Market Research Skill

## Purpose

Execute a structured B2B competitive intelligence workflow with clear AI-executable phases and explicit flags for what requires human validation. Produces a research brief that feeds positioning, content strategy, and campaign design.

Invoke when: Research Specialist receives a market research request, or Campaign Lead needs competitive intelligence before Sprint 1 positioning work.

---

## Thought Leader Foundations

This skill synthesizes five complementary research lenses:

**Sean Ellis (GrowthHackers) — The 40% Test:** PMF survey: "How would you feel if you could no longer use [product]?" 40%+ "very disappointed" = product-market fit. The follow-up questions are the gold: "What is the main benefit?" gives value prop language in the customer's own words. "What alternative would you use?" maps the real competitive landscape.

**Bob Moesta / Clayton Christensen — Jobs-to-be-Done:** Four Forces of Progress: Push (frustration with current state) + Pull (attraction to new solution) must overcome Anxiety (fear of switching) + Habit (comfort with status quo). "Only people have Jobs-to-be-Done, not organizations" — in enterprise B2B, find the specific person willing to spend political capital to champion the purchase. Career risk is real: "What if it goes wrong and I look bad?"

**Adele Revella (Buyer Persona Institute) — 5 Rings of Buying Insight:** Priority Initiative (what triggers the search), Success Factors (expected outcomes), Perceived Barriers (what eliminates you), Buyer's Journey (who influences), Decision Criteria (what makes them choose). 77% of marketers never reference their buyer personas — because most are fabricated from demographics, not researched from actual buying decisions. Interview non-customers and lost deals, not just happy customers.

**Rand Fishkin / SparkToro — Audience Intelligence:** Observe what your audience actually does online (follows, reads, watches, discusses) instead of asking what they think. Behavioral data at scale vs. self-reported survey data. Identifies channels, creators, and publications that actually reach your ICP.

**Peep Laja / Wynter — Message Testing:** 4-layer test: Clarity → Relevance → Value → Differentiation. Test with verified category buyers, not internal stakeholders. Brand tracking every 6-12 months: unaided awareness, aided awareness, perception, consideration.

**The critical cross-cutting insight:** The most dangerous market research mistake is asking people what they want instead of studying what they do. Ellis measures disappointment, not satisfaction. Moesta reconstructs purchase stories, not wishlists. Revella follows buyer narratives, not scripts. Fishkin observes behavior, not self-reports. Laja tests with real buyers, not committees.

**AI agent advantage:** Observational desk research (what people DO) is often more reliable than self-reported data (what people SAY). This makes the agent's desk research capability genuinely valuable, not a poor substitute for human interviews.

---

## Required Inputs

Before starting, always read:
- `context/business-profile.md` — What we're researching against (product, offer, category)
- `context/icp.md` — Target buyer profile (if available — we're trying to validate and enrich this)
- Research scope: What specific questions does the requester need answered?

**Define scope before starting:**
- Are we doing a full market analysis or a competitor deep-dive?
- Is this for a new market entry or existing category?
- What decisions does this research need to inform?

---

## Framework

### Phase 1: LANDSCAPE (AI-Executable)

**Goal:** Map the market before going deep on any one competitor.

#### 1a. Market Mapping
- Define the market category and adjacent categories
- Estimate market size and growth (from public sources: analyst reports, press releases, funding announcements)
- Identify the major segments within the market (by company size, industry, use case)
- Flag any recent disruptions: new entrants, regulatory changes, technology shifts, M&A

#### 1b. Competitor Identification
Identify competitors across three tiers:
- **Tier 1 — Direct:** Products that buyers would directly compare
- **Tier 2 — Adjacent:** Products that solve a related problem (buyers sometimes choose instead)
- **Tier 3 — Alternative:** The real competitive alternative — often "do nothing," spreadsheets, or manual processes

For each competitor, document:
- Name, URL, founding year, funding stage
- Target customer (from their website/marketing)
- Core value proposition (from their homepage headline)
- Pricing model (public pricing or pricing page structure)
- Company size (employees from LinkedIn)

#### 1c. Positioning Analysis
For each Tier 1 and Tier 2 competitor:
- Homepage headline: What outcome do they lead with?
- Sub-headline: Who do they target?
- Social proof used: Customers named? Numbers claimed?
- CTA: What action do they ask for?
- Category language: What do they call the space they're in?

Look for:
- Positioning clusters (where multiple competitors say similar things — opportunity for differentiation)
- Positioning gaps (problems the ICP has that no one is claiming to solve)
- Category framings (is anyone trying to create a new category?)

#### 1d. Technology and Trend Scanning
- Key technology trends affecting this market (AI, regulatory, economic)
- Recent funding activity and what it signals about market direction
- Job postings from competitors (what they're hiring for reveals strategic direction)
- Recent product launches or major feature announcements

---

### Phase 2: DEEP INTELLIGENCE (AI-Executable with Web/Tool Access)

**Goal:** Understand what buyers actually think and how they actually behave.

#### 2a. Competitor Messaging Analysis (Laja's 4-Layer Framework)
For each top competitor, evaluate their messaging:
- **Clarity:** Is the value proposition immediately understandable?
- **Relevance:** Does it speak to real buyer problems?
- **Value:** Is the promised outcome worth caring about?
- **Differentiation:** Could another company say this exact thing?

Score each competitor 1-5 on each layer. Low scores = your positioning opportunity.

#### 2b. Customer Language Extraction (JTBD Four Forces)
Mine reviews and community discussions for customer language organized by JTBD forces:

**Sources:** G2, Capterra, TrustRadius, Product Hunt, Reddit (relevant subreddits), LinkedIn comments, App Store reviews (if applicable)

**Organize findings by force:**
- **Push language** (frustration with old solution): "I was tired of...", "We kept running into...", "The problem with [old tool] was..."
- **Pull language** (attracted to new solution): "What sold me was...", "The thing that made me switch...", "I chose them because..."
- **Anxiety language** (fear of switching): "I was worried about...", "My concern was...", "I wasn't sure if..."
- **Habit language** (comfort with status quo): "We'd always just...", "It seemed easier to just keep..."

This language is direct input for messaging, not just research.

#### 2c. Audience Behavior Mapping
Where does the ICP actually consume content and make decisions?

- **Online communities:** Which subreddits, Slack groups, LinkedIn groups, Discord servers?
- **Newsletters:** What publications do they read? (Check who their influencers cite)
- **Podcasts:** Which shows come up repeatedly in ICP discussions?
- **Creators:** Who do they follow and engage with on LinkedIn/Twitter?
- **Events:** Which conferences, webinars, communities do they participate in?

#### 2d. Content Gap Analysis
Review the top 5-10 pieces of content from competitors:
- What topics do they own? (Where they have the most traffic, links, engagement)
- What topics are they ignoring? (Problems the ICP has that no one is writing about)
- What's the quality bar? (Is there room to create something 10x better?)
- What formats work? (Long-form guides, tools, calculators, data reports, case studies)

---

### Phase 3: RESEARCH BRIEF (AI Synthesis)

**Goal:** Turn Phase 1-2 data into actionable intelligence for the Campaign Lead.

Compile findings into a structured brief using all five research lenses:

1. **Market landscape summary** (Ellis lens: where is the market in its maturity curve?)
2. **Competitive positioning map** (Dunford lens: who's positioned where, and where are the gaps?)
3. **Buyer psychology synthesis** (Moesta/JTBD lens: what pushes people to act, what holds them back?)
4. **Audience behavior map** (Fishkin lens: where does the ICP actually spend attention?)
5. **Messaging opportunity analysis** (Laja lens: where is competitor messaging weak?)

For each section, include:
- Key finding (1-2 sentences)
- Supporting evidence (quotes, data, examples)
- Implication for positioning/content strategy
- Confidence level: **HIGH** (direct evidence) / **MEDIUM** (reasonable inference) / **LOW** (speculation)

---

### Phase 4: PRIMARY RESEARCH SUPPORT (Human Leads, AI Assists)

**Important:** This phase acknowledges what AI can't do alone. Flag these needs explicitly rather than skipping them.

AI prepares instruments for human-led primary research:

#### 4a. JTBD Interview Guide
Based on Phase 2 findings, generate a structured buyer interview guide:
- Opening: "Take me back to the day you decided to [search for/purchase]..."
- Explore each JTBD force with follow-up probes
- Revella's 5 Rings: Priority Initiative, Success Factors, Perceived Barriers, Buyer Journey, Decision Criteria
- Closing: "What would you tell someone who was considering [product]?"

#### 4b. PMF Survey (if applicable)
Ellis-style survey instrument:
- Core question: "How would you feel if you could no longer use [product]?"
- Value prop question: "What is the main benefit you receive from [product]?"
- Competitive question: "What would you use instead?"
- Improvement question: "What type of person do you think would most benefit from [product]?"

#### 4c. Message Test Variants
Based on positioning gaps identified in Phase 3, draft 3-5 headline variants for testing:
- Each variant tests a different positioning angle
- Include the competitive framing that each headline implies
- Format ready for Wynter-style or 5-second test

---

## Output Format

Save to: `knowledge/research/market-research-[company/topic]-[date].md`

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
- [...]

### Competitive Map

**Tier 1 — Direct Competitors**

| Company | Value Prop | Target | Pricing | Size |
|---------|-----------|--------|---------|------|
| [Name] | [Headline positioning] | [ICP] | [Model] | [~X employees] |
[...]

**Tier 2 — Adjacent Competitors**
[Same table]

**Tier 3 — Real Competitive Alternative**
[Description of what buyers do instead — the status quo]

### Positioning Clusters and Gaps

**Where everyone is saying the same thing:** [The positioning cluster — the safe, undifferentiated zone]
**Where no one is competing:** [The gap — unaddressed buyer problems or underserved segments]
**Category framing attempts:** [Anyone trying to name a new category?]

---

## Phase 2: Deep Intelligence

### JTBD Customer Language Map

**Push (frustrations driving switching):**
> "[Direct quote from review/community]" — Source: [G2/Reddit/etc.]
> "[Direct quote]"
[...]

**Pull (what attracts buyers to new solutions):**
> "[Direct quote]"
[...]

**Anxiety (fears about switching):**
> "[Direct quote]"
[...]

**Habit (status quo comfort):**
> "[Direct quote]"
[...]

### Audience Behavior Map

| Channel | Activity Level | Why They're There | Distribution Opportunity |
|---------|---------------|-------------------|--------------------------|
| [Reddit r/X] | High | [Topic focus] | [How to participate] |
[...]

### Content Gap Analysis

**Topics competitors own:** [Well-covered territory to approach differently or avoid]
**Underserved topics:** [Real ICP problems that nobody is addressing well]
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
[...]

---

### Positioning Hypotheses

Based on this research, 3-5 positioning angles worth testing:

1. **[Angle name]:** [One sentence framing] — Confidence: [H/M/L]
2. [...]

*These feed directly into /positioning-angles for scoring and development.*

---

## Phase 4: Primary Research Instruments

### JTBD Interview Guide

[Full interview guide with opening, probe questions, closing]

### PMF Survey (if applicable)

[Survey questions in order]

### Message Test Variants

| Variant | Headline | Positioning angle being tested |
|---------|----------|-------------------------------|
| A | [Headline] | [Angle] |
[...]

---

## Research Gaps and Confidence Flags

**What we couldn't find:**
- [Gap 1 — what primary research could fill it]
- [...]

**Where to be cautious:**
- [Area with LOW confidence findings — and why]

**Recommended next steps:**
- [ ] [Specific human-led research to validate key hypotheses]
- [ ] [Data source to access if not available in desk research]
```

---

## Quality Checklist

Before marking complete:

- [ ] Market scope defined before starting (not just "the market")
- [ ] Three-tier competitive landscape mapped (direct + adjacent + real alternative)
- [ ] Positioning analysis covers at least 5 competitors (4-layer Laja framework)
- [ ] Customer language organized by JTBD four forces (not just a list of quotes)
- [ ] Audience behavior mapped (channels, not just demographics)
- [ ] Content gap analysis completed (topics competitors ignore)
- [ ] Confidence levels assigned to all key findings (HIGH/MEDIUM/LOW)
- [ ] Positioning hypotheses generated (feeds /positioning-angles)
- [ ] Primary research instruments included where applicable (interview guide, survey, message test variants)
- [ ] Research gaps honestly flagged (no speculation presented as fact)
- [ ] File saved to correct path
