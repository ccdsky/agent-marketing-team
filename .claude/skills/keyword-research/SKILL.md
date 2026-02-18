# Keyword Research Skill

## Purpose

Discover high-value keyword opportunities for B2B content strategy, scored by business potential rather than search volume. Produces a prioritized keyword map organized by buyer journey stage, content type, and distribution channel.

Invoke when: Research Specialist receives a keyword research request, or Campaign Lead needs a content strategy foundation for Sprint 1.

---

## Methodology Sources

Ahrefs/Soulo — Business Potential Score (0-3), Traffic Potential over volume. Fishkin/SparkToro — zero-click reality, B2B dark social discovery. Crestodina/Orbit — two-track system (money phrases vs. content keywords). Simmonds/Foundation — distribution-first. Sonders — inverse research (goals → hypotheses → validate). Schwartz — product-led SEO.

---

## Required Inputs

Before starting, always read:
- `context/icp.md` — ICP roles, pain points, vocabulary, where they spend time
- `context/business-profile.md` — Products/services, use cases, competitive differentiators
- `context/voice-dna.md` — Topic areas the owner has authority to speak about
- Research package: `knowledge/research/[relevant]-[date].md` (prior market research if available)

If `context/icp.md` is sparse on ICP vocabulary and hangouts, run `/market-research` first.

---

## Framework

### Step 1: Define Business Goals and ICP Problems

**Before touching keyword tools:**

- What business outcomes does this content need to drive? (Pipeline, signups, brand awareness, retention?)
- Which ICP segment is this for? (From icp.md — job title, company size, pain stage)
- What are the top 3-5 problems this ICP is actively trying to solve?
- What would they type into Google when experiencing those problems?

Write these as problem statements in the ICP's own language, not in product-marketing language.

### Step 2: Mine Customer Language

The best keyword ideas come from customers, not keyword tools:

**Sources to check (in order of quality):**
1. Sales call transcripts or notes (icp.md should have these — if not, flag for the owner)
2. Customer support tickets — exact phrases customers use when frustrated
3. Review sites: G2, Capterra, Product Hunt reviews for similar products
4. Reddit and LinkedIn comments in ICP communities
5. Job postings — the language companies use when hiring reveals their real problems

**Output:** A list of phrases in customer language, not marketing language. "How do I get my team to actually use the CRM" beats "CRM adoption strategies."

### Step 3: Discover Audience Attention Channels

**Pre-check:** If market-research has already been completed for this campaign, read the Audience Behavior Map from `knowledge/research/market-research-[topic]-[date].md` Phase 2c. Extract channels, content formats, and communities from there — skip the research below and proceed to Step 4 with the existing data.

**If no prior market-research (standalone keyword research):** Map where this ICP consumes content beyond Google:

- **Communities:** Slack groups, Discord servers, subreddits, LinkedIn groups
- **Newsletters:** What newsletters do they subscribe to? (Check icp.md content preferences)
- **Podcasts:** Which shows do they listen to?
- **Creators/Influencers:** Who do they follow on LinkedIn/Twitter?
- **Publications:** Trade press, industry blogs, analyst reports they read

This shapes the distribution plan for each content piece (Step 10).

### Step 4: Generate Topic Hypotheses

From the problems identified in Steps 1-2, generate 15-25 topic hypotheses:

- Each topic should map to a specific ICP problem or goal
- Topics should represent what the ICP would actually search for, not what the business wants to say
- Consider: beginner, intermediate, and expert-level queries for the same topic

Format: `[ICP problem/goal] → [topic hypothesis] → [likely search intent]`

### Step 5: Validate with Keyword Data

For each topic hypothesis, identify 2-5 keyword variants and look up:
- **Search Volume** (monthly, rough estimate — use as directional signal, not gospel)
- **Traffic Potential** (Ahrefs metric: total traffic the top-ranking page gets — more reliable than volume)
- **Keyword Difficulty** (KD score: 0-100, higher = harder to rank)
- **SERP Features** present (Featured Snippet, People Also Ask, AI Overview, zero-click signals)

**Data sources available:**
- If MCP/browser tools available: Use Ahrefs, Semrush, or Moz APIs
- Fallback (always executable): Use WebSearch — type the keyword, observe autocomplete suggestions and related searches returned in results; these reveal real search behavior without JS rendering
- Question-format keywords: Use `WebSearch(query="how to [topic] site:reddit.com OR site:quora.com")` — forums surface the actual questions buyers type, more reliably than Google's PAA boxes (which require browser rendering)
- Google Keyword Planner (free with Google Ads account) for volume estimates

### Step 6: Score Business Potential (Ahrefs 0-3 Scale)

For each keyword, assign a Business Potential score:

| Score | Meaning | Example |
|-------|---------|---------|
| **3** | Product is the irreplaceable solution | "[Product category] software for [specific use case]" |
| **2** | Product is very helpful in solving this | "How to [problem the product directly solves]" |
| **1** | Product is tangentially relevant | "Best practices for [adjacent topic]" |
| **0** | No natural product connection | "[Broad industry concept]" |

**Rule:** Only include keywords scoring 2-3 in the final keyword map. Score-1 keywords go on a "watch list." Score-0 keywords are excluded.

### Step 7: Check SERP Reality

For top candidates (highest Business Potential × Traffic Potential), check:

- **Who ranks?** DA90+ enterprise sites? Niche specialists? User forums?
- **Content format:** Long-form guides? Short answers? Tool pages? Product pages?
- **AI Overviews / Featured Snippets:** Is this fully answered in the SERP? (Zero-click risk)
- **Freshness signals:** Are old pages ranking, or is Google rewarding recent content?

**Flag keywords where:**
- Top results are from Gartner, Forbes, or Wikipedia (very hard to compete)
- Google answers the query completely in the SERP (zero-click, low value)
- Top results require video or interactive content (format mismatch)

### Step 8: Split into Two Tracks

Separate final keywords into:

**Track A — Money Phrases (Commercial Intent)**
- For product/service/landing pages
- Searcher is evaluating solutions or ready to buy
- Signals: "best [product type]," "[product type] for [use case]," "alternatives to [competitor]," "[product type] pricing"
- Conversion-focused; lower volume but higher intent

**Track B — Content Keywords (Informational Intent)**
- For blog posts, guides, educational content
- Searcher is learning or solving a problem
- Signals: "how to [do thing]," "what is [concept]," "guide to [process]"
- Trust-building; higher volume, builds audience over time

### Step 9: Map to Buyer Journey Stage and ICP Role

For each keyword, tag:

| Tag | Description |
|-----|-------------|
| **Awareness** | ICP doesn't know a solution exists yet — problem-aware content |
| **Consideration** | ICP is evaluating options — comparison/guide content |
| **Decision** | ICP is ready to choose — product page / case study content |
| **Retention** | Existing customers deepening usage — how-to/advanced content |

Also tag which ICP role the keyword targets (if multiple roles in icp.md):
- Individual contributor, manager, executive, procurement — each searches differently

### Step 10: Plan Distribution Channels Per Topic

For each final keyword/topic, identify 2-3 distribution channels beyond SEO:

- Can this be repurposed as a LinkedIn post (educational take on the topic)?
- Is there a subreddit or Slack community where this would be valuable?
- Does this fit a newsletter deep-dive or as a social snippet?
- Can this be pitched to a trade publication that the ICP reads?

Strong content strategy creates one piece that distributes in 5+ ways (Simmonds).

### Step 11: Estimate Pipeline Impact

For Money Phrase keywords (Track A), estimate:

- **Rough monthly traffic potential** (if ranked in top 3)
- **Likely conversion rate range** (industry benchmark — replace with your actual rate)
- **Estimated leads per month** (directional benchmark estimate, not a measured number)
- **Deal value alignment** (does this traffic attract the right ICP for deal size?)

**Important:** These estimates are industry benchmarks from training data — not projections from your actual campaign data. Label every number in your output as "(est.)" and note: "Replace conversion rates with your actual historical rates for accurate projections." Use these as a directional prioritization tool, not as a forecast.

This turns keyword research into a revenue conversation, not a traffic conversation.

### Step 12: Build Prioritized Output

Organize final keywords into a prioritized map:

- **Priority 1:** High Business Potential (3) + High Traffic Potential + Achievable KD
- **Priority 2:** High Business Potential (3) + Lower Traffic Potential or Higher KD
- **Priority 3:** Business Potential (2) + High Traffic Potential

---

## Output Format

Save to: `knowledge/research/keyword-research-[company/topic]-[date].md`

```markdown
# Keyword Research: [Company/Product/Topic]

**Date:** [YYYY-MM-DD]
**ICP segment:** [primary target]
**Business goal:** [what this content strategy needs to achieve]

---

## Customer Language Mining

**Key phrases from customer sources:**
- [Phrase 1 — source]
- [Phrase 2 — source]
[...]

**Vocabulary patterns:** [Note any consistent language patterns — what ICP says vs. what marketing says]

---

## Track A: Money Phrases

| Keyword | Monthly Volume | Traffic Potential | KD | Business Potential | Priority |
|---------|---------------|-------------------|----|--------------------|----------|
| [keyword] | [~X/mo] | [X/mo] | [X] | [3] | P1 |
[...]

**SERP notes:** [Any flags from Step 7 for specific keywords]

---

## Track B: Content Keywords

| Keyword | Monthly Volume | Traffic Potential | KD | Business Potential | Journey Stage | ICP Role | Priority |
|---------|---------------|-------------------|----|--------------------|---------| ---------|----------|
| [keyword] | [~X/mo] | [X/mo] | [X] | [2-3] | [Awareness/Consideration] | [role] | P1 |
[...]

---

## Watch List (Business Potential: 1)

| Keyword | Rationale for watching |
|---------|------------------------|
| [keyword] | [why it's interesting but not ready] |

---

## Editorial Calendar Suggestions

**Month 1 — Foundation pieces (highest Priority 1 content keywords):**
- [Keyword → suggested headline → format → distribution channels]
- [...]

**Month 2 — Depth pieces:**
- [...]

**Ongoing — Money phrases (product pages to create/optimize):**
- [keyword → page type → target ICP role]

---

## Pipeline Impact Estimate (Track A)

*All figures below are benchmark estimates based on industry data — not projections from your actual campaign performance. Replace conversion rates with your historical rates before using these in planning.*

| Keyword | Est. Monthly Traffic (top 3) | Conv. Rate (benchmark est.) | Est. Leads/Mo (est.) | ICP Fit |
|---------|------------------------------|----------------------|----------------|---------|
| [keyword] | [X] | [X% est.] | [X est.] | [Strong/Medium] |

**Directional pipeline estimate:** [X leads/mo if top 3 rankings achieved on Priority 1 keywords — replace with actual conversion data for accurate forecasting]

---

## Audience Attention Map

| Channel | ICP Activity Level | Content Formats That Work | Distribution Opportunity |
|---------|-------------------|--------------------------|--------------------------|
| [Reddit r/X] | [High/Medium] | [Long answers, resources] | [Which topics fit here] |
| [LinkedIn] | [...] | [...] | [...] |
[...]

---

## Research Gaps

- [Flag any areas where data was unavailable or uncertain]
- [Primary research needed: e.g., "sales call transcripts for ICP vocabulary — request from owner"]
```

---

## Quality Gate

Before marking complete:

- [ ] Started from ICP problems and business goals — not from keyword tool suggestions
- [ ] Customer language mined from at least 2 sources (context/icp.md + at least one external source)
- [ ] All keywords scored Business Potential 0-3 — only BP 2-3 in final map (1 in watch list, 0 excluded)
- [ ] SERP reality checked for Priority 1 keywords (zero-click flags, enterprise dominance, format match)
- [ ] Pipeline estimates labeled "(benchmark est.)" — not presented as measured data
- [ ] Research gaps flagged (including if sales transcripts were unavailable)
