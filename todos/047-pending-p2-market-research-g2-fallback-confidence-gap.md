---
status: pending
priority: p2
issue_id: "047"
tags: [code-review, market-research, G2, confidence-levels, SERP, evidence-quality]
---

# Market Research G2 Fallback Doesn't Account for AI Overview SERP Absorption

## Problem Statement

`market-research/SKILL.md` Phase 2b documents a G2 login wall fallback using `site:g2.com` Google search. The fallback is accurate but doesn't acknowledge that Google's AI Overviews increasingly absorb G2 review content into summaries, replacing direct review snippets. Language extracted from AI Overview summaries is paraphrased, not verbatim customer voice — but no confidence caveat distinguishes this from direct snippet extraction.

## Findings

**market-research/SKILL.md Phase 2b fallback:**
> "Fallback: `WebSearch(query="site:g2.com [competitor] reviews [pain point]")` returns Google-indexed review snippets without login. Lower fidelity than full reviews but still captures real customer language."

The skill acknowledges the zero-click SERP reality in keyword-research (Fishkin reference) but does not apply that insight consistently to market research. AI Overview absorbed content should be labeled MEDIUM confidence, not conflated with real review snippet extracts.

The source-type confidence table (added in v1.2) assigns "Direct customer quote (review, interview) → HIGH" but doesn't differentiate between direct G2 access vs. Google snippet fallback vs. AI Overview summarized content.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add SERP confidence caveat to Phase 2b fallback + update confidence table (Recommended)

**Phase 2b fallback addition:**
> "Apply MEDIUM confidence to language from Google snippet fallback. If the SERP shows an AI Overview summarizing review content (paraphrased, not quoted), label findings LOW confidence and note data limitation in Phase 4."

**Source-type confidence table addition:**
| Google-indexed review snippet (site:g2.com) | MEDIUM | AI Overview paraphrase → LOW |

**Effort:** Small — two additions to market-research/SKILL.md

## Acceptance Criteria

- [ ] market-research/SKILL.md Phase 2b fallback includes confidence caveat for AI Overview absorption
- [ ] The source-type confidence table distinguishes direct G2 access from Google snippet fallback
- [ ] Agents cannot assign HIGH confidence to G2 language obtained through Google SERP fallback

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
