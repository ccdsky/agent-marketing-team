---
status: complete
priority: p1
issue_id: "005"
tags: [code-review, blocking, keyword-research, web-tools, google]
---

# Keyword Research Step 5 PAA Fallback Not Executable via WebSearch/WebFetch

## Problem Statement

`keyword-research/SKILL.md` Step 5 instructs agents to use "People Also Ask (PAA) boxes" from Google as a keyword discovery signal. PAA boxes are JavaScript-rendered elements in Google SERPs — they are not returned by WebSearch (which returns result snippets, not rendered SERP elements) or WebFetch (which fetches raw HTML, not JS-rendered content). An agent following this instruction will either hallucinate PAA results or silently skip this step.

## Findings

**keyword-research/SKILL.md Step 5:**
> "Mine People Also Ask (PAA) boxes for question-format keywords"

Google's PAA boxes are dynamically rendered by JavaScript after initial page load. WebSearch returns result metadata (titles, snippets, URLs) but not SERP UI elements like PAA boxes. WebFetch of google.com returns a redirect or partial HTML without rendered JS elements.

This is a category error: the instruction assumes browser-level access to Google's rendered SERP, but the available tools (WebSearch, WebFetch) access Google's search index, not its rendered page DOM.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Replace PAA instruction with AlsoAsked or AnswerThePublic web fetch (Recommended)

Replace PAA mining with fetching question-format keywords from tools that expose their data via accessible URLs:

```
# For question-format keywords:
WebFetch(url="https://alsoasked.com/search?q=[seed+keyword]")
# Extract "People Also Asked" question clusters from AlsoAsked's accessible web UI

# Or use search query patterns that surface questions:
WebSearch(query="site:reddit.com OR site:quora.com [topic] [pain point]")
```

**Pros:** Uses actually executable tools; produces question-format keywords; accessible without JS rendering
**Cons:** AlsoAsked may change their URL structure; rate limits may apply
**Effort:** Small — replace one instruction with executable alternatives

### Option B: Reframe as "question format" mining from accessible sources

Replace PAA instruction with:
> "Mine question-format keywords from forums and Q&A sites (Reddit r/[topic], Quora, Stack Overflow) using WebSearch patterns like 'how to [topic]', 'why does [problem]', 'what is [concept]'"

**Pros:** Always executable; richer signal than PAA (actual community questions vs. Google's curated list)
**Cons:** Less systematic than PAA's topic clustering
**Effort:** Small

### Option C: Note as Playwright-only step

Mark this step as: "Requires Playwright MCP or browser automation. If unavailable, skip and proceed to Step 6."

**Pros:** Honest about capability gap
**Cons:** Reduces skill completeness in most environments
**Effort:** Trivial

## Acceptance Criteria

- [ ] Step 5 in keyword-research/SKILL.md uses only tools available without browser automation
- [ ] Question-format keyword mining produces real output an agent can execute
- [ ] If Playwright is used, it is clearly marked as optional with a fallback

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
