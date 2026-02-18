---
status: pending
priority: p1
issue_id: "018"
tags: [code-review, research-specialist, mcp, websearch, webfetch]
---

# MCP Tool Invocations in research-specialist.md Are Prose Placeholders With No Executable Fallback

## Problem Statement

`research-specialist.md` lines 271, 286, 306 contain:
```
[Use MCP tool to query Perplexity]
[Use Firecrawl MCP]
[Use Playwright MCP]
```

These bracket-surrounded prose statements will not invoke any tool. An agent reading this section has no executable path for:
- Competitor website scraping (Firecrawl placeholder)
- Visual research / screenshot analysis (Playwright placeholder)
- Deep research queries (Perplexity placeholder)

`WebSearch` and `WebFetch` are available native tools that could substitute for all three in the current v1.1 configuration. The `IMPLEMENTATION-SUMMARY.md` correctly notes MCPs are not yet configured, but `research-specialist.md` presents them as active methods in the research workflow with no caveat adjacent to the placeholders.

The v2.0 skill annotations in the same file (line 484-492) show the correct pattern: explicitly say "not yet implemented, use X instead." The MCP placeholders need the same treatment.

A Research Specialist hitting these placeholders will either: (a) skip the steps silently, (b) attempt to write prose as if it were a tool call, or (c) improvise — all producing worse research quality with no error signal.

## Proposed Solution

Replace each placeholder with a conditional instruction:

```markdown
**Competitor website research:**
*Perplexity/Firecrawl MCPs not yet configured. Use instead:*
- `WebSearch(query="[competitor] marketing positioning")` for current web results
- `WebFetch(url="[competitor-url]")` to read specific competitor pages

**Visual research (landing page patterns):**
*Playwright MCP not yet configured. Use instead:*
- `WebFetch(url="[competitor-landing-page]")` to read page content
- Note visual structure and copy patterns from the fetched content
```

**Effort:** Small — 3 targeted replacements in research-specialist.md

## Acceptance Criteria

- [ ] No `[Use MCP tool to ...]` prose placeholders remain in research-specialist.md
- [ ] Each placeholder is replaced with an executable WebSearch or WebFetch instruction
- [ ] Each replacement includes a note that MCPs will enable richer research when configured

## Work Log

- 2026-02-18: Identified by agent-native-reviewer in second review pass
