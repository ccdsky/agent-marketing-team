# Keyword Research — Extended Reference

## Methodology Sources

Ahrefs/Soulo — Business Potential Score (0-3), Traffic Potential over volume. Fishkin/SparkToro — zero-click reality, B2B dark social discovery. Crestodina/Orbit — two-track system (money phrases vs. content keywords). Simmonds/Foundation — distribution-first. Sonders — inverse research (goals → hypotheses → validate). Schwartz — product-led SEO.

---

## Customer Language Mining — Sources by Quality

1. Sales call transcripts or notes (icp.md should have these — if not, flag for the owner)
2. Customer support tickets — exact phrases customers use when frustrated
3. Review sites: G2, Capterra, Product Hunt reviews for similar products
4. Reddit and LinkedIn comments in ICP communities
5. Job postings — the language companies use when hiring reveals their real problems

**Principle:** "How do I get my team to actually use the CRM" beats "CRM adoption strategies."

---

## Business Potential Score — Full Scoring Table

| Score | Meaning | Example |
|-------|---------|---------|
| **3** | Product is the irreplaceable solution | "[Product category] software for [specific use case]" |
| **2** | Product is very helpful in solving this | "How to [problem the product directly solves]" |
| **1** | Product is tangentially relevant | "Best practices for [adjacent topic]" |
| **0** | No natural product connection | "[Broad industry concept]" |

**Rule:** Only include keywords scoring 2-3 in the final keyword map. Score-1 keywords go on a "watch list." Score-0 keywords are excluded.

---

## SERP Reality Check — What to Flag

This is the step that decides whether a keyword is worth the cost of a full article (draft + review + owner checkpoint). Do not skip it for Priority 1 candidates.

For top candidates (highest Business Potential × Traffic Potential):
- **Who ranks?** DA90+ enterprise sites? Niche specialists? User forums?
- **Content format:** Long-form guides? Short answers? Tool pages? Product pages?
- **AI Overviews / Featured Snippets:** Is this fully answered in the SERP? (Zero-click risk — in 2026 an AI Overview is the single biggest click thief. Flag its presence explicitly.)
- **Freshness signals:** Are old pages ranking, or is Google rewarding recent content?

**Flag keywords where:**
- Top results are from Gartner, Forbes, or Wikipedia (very hard to compete)
- An AI Overview or featured snippet answers the query completely in the SERP (zero-click, low value)
- Top results require video or interactive content (format mismatch)

**How to run it — data source ladder** (see *Keyword Data Sources* below for the same ladder):
- **DataForSEO available (preferred):** Query the live SERP for each P1 candidate. Use the **Live** queue here — this is an interactive, on-demand check where accuracy matters and volume is small. Capture: presence of AI Overview, featured snippet + its source domain, top-10 organic domains (for enterprise-dominance flag), and SERP features present. One request per candidate; batch the P1 list, do not query the whole map.
- **Fallback (always executable):** Run the query in WebSearch and read the results page — note whether an AI answer box / featured snippet appears and which domains hold the top spots.

### People Also Ask (PAA) extraction

While checking the SERP, harvest the **People Also Ask** questions for each P1 candidate — these are real buyer questions in Google's own words and are high-value inputs for both customer-language mining and blog outlines.
- **DataForSEO available:** The SERP response returns structured PAA elements (question text, answer snippet, source domain, source URL). Extract them alongside the reality check — no extra request.
- **Fallback:** `WebSearch(query="[keyword]")` and read the "People also ask" box, or `WebSearch(query="[topic] site:reddit.com OR site:quora.com")` for forum-sourced questions.

Feed harvested PAA questions into the FAQ sections of the editorial calendar and pass them to `/blog-post` as outline input.

---

## Keyword Data Sources

Use the highest available rung; fall through silently when a tool is absent (mirrors the data-access ladder the Distribution Specialist uses).

1. **DataForSEO (preferred, if the `dataforseo` MCP server is connected):**
   - **Volume, CPC, competition:** Keywords Data / Google Ads endpoints.
   - **Related & suggested keywords, difficulty, search-intent, monthly trend:** DataForSEO Labs (Related Keywords for semantic expansion).
   - **Cost discipline (required):** default to the **Standard** queue ($0.0006/req) for all keyword and batch lookups — reserve the Live queue (~3.3× cost) for the interactive SERP reality check only. Keep `depth=10` (deeper SERPs bill as a multiple). Batch keyword lookups rather than querying one term at a time. See `TEAM.md` → *Optional Data Integrations*.
2. **Fallback (always executable):** WebSearch — type the keyword, observe autocomplete and related searches.
   - Question-format keywords: `WebSearch(query="how to [topic] site:reddit.com OR site:quora.com")` — forums surface actual buyer questions.
   - Google Keyword Planner (free with a Google Ads account) for volume estimates.

**Labeling rule:** When numbers come from DataForSEO, present them as measured (cite the source). When they come from the WebSearch fallback, keep the "(est.)" label per the Pipeline Impact rules below — do not present fallback estimates as measured data.

---

## Buyer Journey Tags — Detailed Definitions

| Tag | Description | Content type |
|-----|-------------|-------------|
| **Awareness** | ICP doesn't know a solution exists — problem-aware | Problem-framing guides, industry data |
| **Consideration** | ICP is evaluating options | Comparison content, "how to choose" guides |
| **Decision** | ICP is ready to choose | Product pages, case studies, demos |
| **Retention** | Existing customers deepening usage | How-to content, advanced guides |

Also tag which ICP role the keyword targets — individual contributor, manager, executive, procurement each searches differently.

---

## Pipeline Impact Estimation Guidance

For Money Phrase keywords (Track A):
- **Rough monthly traffic potential** (if ranked in top 3)
- **Likely conversion rate range** (industry benchmark)
- **Estimated leads per month** (directional benchmark, not measured)
- **Deal value alignment** (does this traffic attract the right ICP for deal size?)

**Important labeling rule:** Label every number as "(est.)" and note: "Replace conversion rates with your actual historical rates for accurate projections."

**Do not sum the Est. Leads/Mo column** — keyword audiences overlap significantly.

---

## Distribution Channel Planning — Per Topic

For each final keyword/topic, identify 2-3 distribution channels beyond SEO:
- Can this be repurposed as a LinkedIn post (educational take)?
- Is there a subreddit or Slack community where this would be valuable?
- Does this fit a newsletter deep-dive or social snippet?
- Can this be pitched to a trade publication the ICP reads?

Strong content strategy creates one piece that distributes in 5+ ways (Simmonds).

---

## Priority Matrix

| Priority | Criteria | Action |
|----------|----------|--------|
| P1 | Business Potential 3 + High Traffic Potential + Achievable KD | Create immediately |
| P2 | Business Potential 3 + Lower Traffic Potential or Higher KD | Schedule next quarter |
| P3 | Business Potential 2 + High Traffic Potential | Create if capacity allows |

---

## Full Output Template

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

**Vocabulary patterns:** [Note any consistent language patterns — what ICP says vs. what marketing says]

---

## Track A: Money Phrases

| Keyword | Monthly Volume | Trend | Traffic Potential | KD | Business Potential | Priority |
|---------|---------------|-------|-------------------|----|--------------------|----------|
| [keyword] | [~X/mo] | [↑/→/↓ or %YoY] | [X/mo] | [X] | [3] | P1 |

*Trend: 12-month direction from DataForSEO Labs where available (a keyword growing YoY is a different bet than a flat one). Leave blank if using the WebSearch fallback.*

**SERP notes:** [Per-keyword flags from the SERP reality check — AI Overview present? featured-snippet source? enterprise-dominated top 10?]

---

## Track B: Content Keywords

| Keyword | Monthly Volume | Trend | Traffic Potential | KD | Business Potential | Journey Stage | ICP Role | Priority |
|---------|---------------|-------|-------------------|----|--------------------|---------------|----------|----------|
| [keyword] | [~X/mo] | [↑/→/↓] | [X/mo] | [X] | [2-3] | [Awareness/Consideration] | [role] | P1 |

---

## Buyer Questions (People Also Ask)

Real questions harvested from the SERP for P1 keywords — feed these into blog FAQ sections and pass to `/blog-post`.

| Question | Source keyword | Source domain (if from DataForSEO) |
|----------|---------------|-------------------------------------|
| [PAA question] | [keyword it appeared under] | [domain / "WebSearch fallback"] |

---

## Watch List (Business Potential: 1)

| Keyword | Rationale for watching |
|---------|------------------------|
| [keyword] | [why it's interesting but not ready] |

---

## Editorial Calendar Suggestions

**Month 1 — Foundation pieces (highest Priority 1 content keywords):**
- [Keyword → suggested headline → format → distribution channels]

**Month 2 — Depth pieces:**
- [...]

**Ongoing — Money phrases (product pages to create/optimize):**
- [keyword → page type → target ICP role]

---

## Pipeline Impact Estimate (Track A)

*All figures below are benchmark estimates based on industry data — not projections from your actual campaign performance. Replace conversion rates with your historical rates before using in planning.*

| Keyword | Est. Monthly Traffic (top 3) | Conv. Rate (benchmark est.) | Est. Leads/Mo (est.) | ICP Fit |
|---------|------------------------------|----------------------|----------------|---------|
| [keyword] | [X] | [X% est.] | [X est.] | [Strong/Medium] |

**Directional pipeline estimate:** [X leads/mo if top 3 rankings achieved on Priority 1 keywords — replace with actual data for accurate forecasting]

---

## Audience Attention Map

| Channel | ICP Activity Level | Content Formats That Work | Distribution Opportunity |
|---------|-------------------|--------------------------|--------------------------|
| [Reddit r/X] | [High/Medium] | [Long answers, resources] | [Which topics fit here] |
| [LinkedIn] | [...] | [...] | [...] |

---

## Research Gaps

- [Flag any areas where data was unavailable or uncertain]
- [Primary research needed: e.g., "sales call transcripts for ICP vocabulary — request from owner"]
```
