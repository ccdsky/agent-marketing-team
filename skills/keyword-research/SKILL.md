---
name: keyword-research
description: Discover high-value B2B keyword opportunities scored by business potential (0-3), organized by buyer journey stage and content type.
---

# Keyword Research Skill

## When to Use

Discover high-value keyword opportunities for B2B content strategy, scored by business potential rather than search volume. Produces a prioritized keyword map organized by buyer journey stage, content type, and distribution channel. Invoke when Research Specialist receives a keyword research request, or Campaign Lead needs a content strategy foundation for Sprint 1.

---

## Required Inputs

Before starting, always read:
- `context/icp.md` — ICP roles, pain points, vocabulary, where they spend time
- `context/business-profile.md` — Products/services, use cases, competitive differentiators
- `context/voice-dna.md` — Topic areas the owner has authority to speak about
- Research package: `knowledge/research/[relevant]-[date].md` (prior market research if available)

If `context/icp.md` is sparse on ICP vocabulary and hangouts, run `/market-research` first.

---

## Procedure

1. **Define business goals and ICP problems.** What business outcomes does this content need to drive? Which ICP segment? Top 3-5 problems they're actively solving? Write these as problem statements in the ICP's own language, not product-marketing language.

2. **Mine customer language.** Pull phrases from sales transcripts, support tickets, G2/Capterra reviews, Reddit/LinkedIn communities, job postings. For source priority ranking and quality guidance, see `references/methodology.md`.

3. **Map audience attention channels.** If prior market research exists, extract the Audience Behavior Map from `knowledge/research/market-research-[topic]-[date].md` Phase 2c — skip independent research. If no prior research: map communities, newsletters, podcasts, creators, and trade publications the ICP uses.

4. **Generate 15-25 topic hypotheses.** Map each to a specific ICP problem. Format: `[ICP problem/goal] → [topic hypothesis] → [likely search intent]`.

5. **Validate with keyword data.** For each hypothesis: search volume, traffic potential, keyword difficulty, SERP features. Use Ahrefs/Semrush if available; fallback to WebSearch autocomplete and `site:reddit.com OR site:quora.com` queries. For data source options, see `references/methodology.md`.

6. **Score Business Potential (0-3 scale).** 3 = product is the irreplaceable solution; 2 = product is very helpful; 1 = tangentially relevant; 0 = no connection. Only BP 2-3 enter the final map. BP 1 goes to watch list. BP 0 excluded. For full scoring table, see `references/methodology.md`.

7. **Check SERP reality** for top candidates. Flag zero-click risk, enterprise dominance (Gartner/Forbes/Wikipedia), and format mismatch. For full checklist, see `references/methodology.md`.

8. **Split into two tracks.** Track A — Money Phrases (commercial intent, product/landing pages). Track B — Content Keywords (informational intent, blog/guides).

9. **Tag buyer journey stage and ICP role.** Awareness / Consideration / Decision / Retention. Tag which ICP role (IC, manager, executive, procurement) each keyword targets.

10. **Plan 2-3 distribution channels per topic** beyond SEO: LinkedIn, communities, newsletter, trade press. For distribution channel framework, see `references/methodology.md`.

11. **Estimate pipeline impact for Track A.** Rough monthly traffic, benchmark conversion rate, estimated leads. Label all estimates "(est.)" — these are benchmark figures, not projections. Do not sum leads column (audiences overlap).

12. **Build prioritized output.** P1: BP3 + high traffic + achievable KD. P2: BP3 + lower traffic or higher KD. P3: BP2 + high traffic.

---

## Output

Save to: `knowledge/research/keyword-research-[company/topic]-[date].md`

Required sections: Customer Language Mining, Track A: Money Phrases, Track B: Content Keywords, Watch List, Editorial Calendar Suggestions, Pipeline Impact Estimate (Track A), Audience Attention Map, Research Gaps.

For full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "knowledge/research/keyword-research-[company/topic]-[YYYY-MM-DD].md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "research-specialist or campaign-lead"
})
```

---

## Example

**Scenario:** Keyword research for Acme CI/CD — a CI/CD platform for mid-market engineering teams.

**Customer language mining (from ICP sources):**
- "Jenkins keeps breaking after upgrades" — Reddit r/devops
- "CI pipeline flaky tests slowing our releases" — G2 review snippet
- "How much does it cost to maintain Jenkins" — support ticket language

**Track A — Money Phrases (sample):**

| Keyword | Volume | Traffic Potential | KD | BP | Priority |
|---------|--------|-------------------|----|----|----------|
| CI/CD platform for startups | ~400/mo | 1,200 | 38 | 3 | P1 |
| Jenkins alternative managed | ~200/mo | 600 | 29 | 3 | P1 |

**Track B — Content Keywords (sample):**

| Keyword | Volume | Traffic Potential | KD | BP | Journey Stage | Role | Priority |
|---------|--------|-------------------|----|----|---------------|------|----------|
| how to reduce CI pipeline time | ~1,100/mo | 3,400 | 45 | 2 | Consideration | IC/Manager | P1 |
| Jenkins maintenance cost | ~300/mo | 900 | 22 | 3 | Awareness | Manager | P1 |

**Pipeline impact (est.):** "Jenkins alternative managed" at top 3 → ~180 visits/mo × 3% conv. (est.) = ~5 leads/mo (est.). Replace with actual conversion data before planning.

---

## Quality Gate

Before marking complete:

- [ ] Started from ICP problems and business goals — not from keyword tool suggestions
- [ ] Customer language mined from at least 2 sources (context/icp.md + at least one external source)
- [ ] All keywords scored Business Potential 0-3 — only BP 2-3 in final map (1 in watch list, 0 excluded)
- [ ] SERP reality checked for Priority 1 keywords (zero-click flags, enterprise dominance, format match)
- [ ] Pipeline estimates labeled "(benchmark est.)" — not presented as measured data
- [ ] Research gaps flagged (including if sales transcripts were unavailable)
