---
status: pending
priority: p2
issue_id: "025"
tags: [code-review, simplicity, duplication, context-files]
---

# "Before You Start: Read Context" Section Duplicated Six Times (~60 Lines)

## Problem Statement

The list of context files to read before any work appears in:
1. `CLAUDE.md` — "Context Files (Always Read Before Work)" table
2. `campaign-lead.md` lines 22-33
3. `research-specialist.md` lines 21-28
4. `creative-specialist.md` lines 21-31
5. `quality-gate.md` lines 22-28
6. `distribution-specialist.md` lines 25-30

All six say the same thing: read voice-dna.md, icp.md, business-profile.md, and the campaign brief before working. This is ~60 lines of duplication that could be one section in TEAM.md.

Each agent also loads this section into context before executing. The combined overhead is larger than the section itself.

## Proposed Solution

Move to TEAM.md under "Pre-Task Protocol":

```markdown
## Pre-Task Protocol

Before claiming any task, read:
- `context/voice-dna.md`
- `context/icp.md`
- `context/business-profile.md`
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if in a campaign)
- Relevant research: `knowledge/research/[topic]-[date].md` (if available)
```

Each agent file drops its "Before You Start" section entirely and refers to TEAM.md.

**Effort:** Small — edit 5 agent files + CLAUDE.md, expand TEAM.md

## Acceptance Criteria

- [ ] Pre-task context reading protocol exists once in TEAM.md
- [ ] Agent files do not individually restate the context file list
- [ ] CLAUDE.md context files table removed or condensed to a single reference

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
