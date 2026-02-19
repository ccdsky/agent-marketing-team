---
status: pending
priority: p3
issue_id: "032"
tags: [code-review, simplicity, examples, research-specialist, creative-specialist]
---

# Example Workflows Are Too Long — Unique Content Is ~10% of Total Length

## Problem Statement

`research-specialist.md` "Example Research Workflow" (lines 406-455, ~50 lines) and `creative-specialist.md` "Example Writing Workflow" (lines 477-547, ~70 lines) walk through 6-8 steps each. In both cases, steps 1, 2, 4, 5, 6 are the universal self-claiming protocol already described above them in the file. The unique content is 10-15 lines per example — just the actual research/writing methodology step.

An LLM re-reading these examples gets no new information from the protocol steps it just read.

## Proposed Solution

Reduce each example to show only the non-obvious steps:

```markdown
**Example: Research competitor positioning**

3. Run research (the unique part):
   - WebSearch: "[competitor] positioning 2026"
   - WebFetch each competitor's pricing page
   - Extract: language patterns, positioning angles, pricing signals
   - Identify 3 gaps not addressed by competitors

4. Write research package to `knowledge/research/dev-cli-competitive-2026-02.md`
```

The protocol steps (claim, read brief, complete) are removed — they're in the protocol section above.

**Effort:** Small — trim 2 example sections by ~80% each

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
