---
status: complete
priority: p1
issue_id: "007"
tags: [code-review, blocking, market-research, web-tools, review-sites]
---

# Market Research Phase 2b Sources G2 and TrustRadius Return Login Walls

## Problem Statement

`market-research/SKILL.md` Phase 2b instructs agents to mine G2, TrustRadius, and Capterra for JTBD customer language and exact quotes. G2 and TrustRadius both require user authentication to read full reviews — WebFetch of their review pages returns login walls or minimal preview content. An agent following this instruction will either fabricate quotes attributed to G2/TrustRadius or silently produce empty findings while marking the step complete.

This is the highest-value data source in Phase 2b (actual customer language in their words) and it's not accessible with available tools.

## Findings

**market-research/SKILL.md Phase 2b:**
> "G2 and TrustRadius: Mine for JTBD language, exact quotes about pain points and switching triggers"

Both sites:
- G2 (g2.com): Reviews require login after initial preview; full review text gated
- TrustRadius (trustradius.com): All reviews require login

Capterra (capterra.com) does expose some review content without login and is partially accessible.

Product Hunt, Reddit, and Hacker News (also listed in Phase 2b) are accessible via WebSearch/WebFetch without authentication.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Replace G2/TrustRadius with accessible equivalents and note the gap (Recommended)

Update Phase 2b to:
1. Remove G2 and TrustRadius as primary sources (they are inaccessible)
2. Promote Reddit, Product Hunt, and Hacker News as primary accessible sources
3. Keep Capterra as a partially-accessible source
4. Add: "If Firecrawl MCP is configured with authenticated sessions, G2 and TrustRadius reviews are accessible via scraping"
5. Add Google-indexed review snippet mining: `WebSearch(query="site:g2.com [competitor] reviews [pain point]")` — Google indexes preview snippets that don't require login

**Pros:** Honest about tool capabilities; provides working fallback
**Cons:** Google snippet mining is lower fidelity than full review text
**Effort:** Small — update Phase 2b source list with notes

### Option B: Add authenticated MCP path with accessible fallback

Structure Phase 2b as:

```
**Primary (if Firecrawl MCP with auth configured):**
- G2 reviews: firecrawl.scrape(url="g2.com/products/[product]/reviews", auth=true)
- TrustRadius: firecrawl.scrape(url="trustradius.com/products/[product]/reviews", auth=true)

**Fallback (always executable):**
- Reddit: WebSearch(query="[competitor] reviews reddit honest")
- Product Hunt: WebFetch(url="producthunt.com/products/[product]/reviews")
- Google review snippets: WebSearch(query="site:g2.com [competitor] [pain point]")
```

**Pros:** Complete coverage for users with Firecrawl; working path for all
**Cons:** More complex instruction set
**Effort:** Small

## Acceptance Criteria

- [ ] Phase 2b does not list inaccessible sources as primary without noting the authentication barrier
- [ ] All primary customer language sources in Phase 2b are accessible via WebSearch or WebFetch without login
- [ ] MCP-authenticated paths are clearly marked as optional with fallbacks

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
