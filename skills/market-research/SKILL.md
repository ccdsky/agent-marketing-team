---
name: market-research
description: Execute structured B2B competitive intelligence — competitor mapping, customer language mining, messaging analysis, and positioning gap identification.
---

# Market Research Skill

## When to Use

Execute a structured B2B competitive intelligence workflow. Produces a research brief that feeds positioning, content strategy, and campaign design. Invoke when Research Specialist receives a market research request, or Campaign Lead needs competitive intelligence before Sprint 1 positioning work.

---

## Required Inputs

Before starting, always read:
- `context/business-profile.md` — What we're researching against (product, offer, category)
- `context/icp.md` — Target buyer profile (if available — we're trying to validate and enrich this)
- Research scope: What specific questions does the requester need answered?

Define scope before starting: full market analysis or competitor deep-dive? New market entry or existing category? What decisions does this research need to inform?

---

## Procedure

**Phase 1: LANDSCAPE** (AI-Executable)

1. Map the market: category definition, size/growth estimate, key segments, recent disruptions.
2. Identify competitors in three tiers: Tier 1 Direct, Tier 2 Adjacent, Tier 3 Alternative (status quo). For details on fields to capture per tier, see `references/methodology.md`.
3. Analyze Tier 1 + Tier 2 positioning: homepage headline, sub-headline, social proof, CTA, category language. Identify positioning clusters, gaps, and category framing attempts.
4. Scan technology trends, recent funding, competitor job postings, product launches.

**Phase 2: DEEP INTELLIGENCE** (AI-Executable with Web/Tool Access)

5. Score each top competitor's messaging on Laja's 4 layers (Clarity / Relevance / Value / Differentiation, 1-5 each). Low scores = positioning opportunity. For full scoring guide, see `references/methodology.md`.
6. Mine customer language from review sites and communities. Organize by JTBD four forces: Push / Pull / Anxiety / Habit. For source access details and confidence levels by source type, see `references/methodology.md`.
7. Map audience behavior: communities, newsletters, podcasts, creators, events where ICP consumes content.
8. Identify content gaps: topics competitors own, underserved topics, format opportunities.

**Phase 3: RESEARCH BRIEF** (AI Synthesis)

9. Compile 4-6 key findings using five research lenses: market landscape (Ellis), competitive positioning (Dunford), buyer psychology (Moesta/JTBD), audience behavior (Fishkin), messaging opportunity (Laja). Each finding: summary, evidence, implication, confidence level (HIGH/MEDIUM/LOW).

**Phase 4: PRIMARY RESEARCH INSTRUMENTS** (Human Leads, AI Assists)

10. Write instruments: JTBD interview guide, PMF survey (if applicable), message test variants (3-5 headline variants testing different positioning angles). Mark phase complete when instruments are written. For full instrument templates, see `references/methodology.md`.

---

## Output

Save to: `knowledge/research/market-research-[company/topic]-[date].md`

Required sections:
- Phase 1: Market Landscape (Market Overview, Competitive Map, Positioning Clusters and Gaps)
- Phase 2: Deep Intelligence (JTBD Customer Language Map, Audience Behavior Map, Content Gap Analysis)
- Phase 3: Research Brief (4-6 findings with confidence levels, Competitor Messaging Scorecard, Positioning Hypotheses)
- Phase 4: Primary Research Instruments (status noted, instruments written)
- Research Gaps and Confidence Flags

For full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "knowledge/research/market-research-[company/topic]-[YYYY-MM-DD].md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "research-specialist or campaign-lead"
})
```

---

## Example

**Scenario:** Market research for Acme CI/CD — a CI/CD platform for mid-market engineering teams.

**Phase 1 excerpt:**

Category: CI/CD Automation. Size: ~$3.2B, growing 18% YoY (analyst estimate).

Tier 1 — Direct Competitors:

| Company | Value Prop | Target | Pricing |
|---------|-----------|--------|---------|
| CircleCI | Fast pipelines for engineering teams | Mid-market devs | Usage-based |
| BuildKite | Self-hosted, enterprise-grade CI | Enterprise/compliance | Per-agent |

Tier 3 — Real Competitive Alternative: In-house Jenkins maintained by a DevOps engineer. Most teams Acme loses to "do nothing" are managing Jenkins and not ready to pay for managed CI.

**Phase 2 excerpt — Push language:**
> "I spent more time maintaining Jenkins than writing code. That was the last straw." — Reddit r/devops
> "Every update broke something. Our pipelines were fragile for 6 months." — Capterra review (MEDIUM confidence — Google snippet)

**Phase 3 excerpt — Finding 1:**
Summary: Mid-market teams switch from Jenkins specifically because of maintenance burden, not pipeline speed.
Evidence: 8/11 reviews mentioning "switch" reference ops time, not performance.
Implication: Lead with "maintenance-free" positioning, not speed.
Confidence: HIGH

---

## Quality Gate

Before marking complete:

- [ ] Three-tier competitive landscape mapped — includes "do nothing" / status quo as Tier 3
- [ ] Customer language organized by JTBD four forces (not just a quote list)
- [ ] Confidence levels assigned to all key Phase 3 findings (HIGH/MEDIUM/LOW)
- [ ] Phase 4 status labeled: "Primary research conducted: Yes / No / Pending"
- [ ] Research gaps flagged honestly — no [LOW] confidence findings presented as conclusions
