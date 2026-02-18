---
status: pending
priority: p2
issue_id: "008"
tags: [code-review, agent-coordination, file-paths, grep]
---

# /path/to/ Placeholder Paths in Grep Examples Will Fail

## Problem Statement

`campaign-lead.md` (lines 31 and 632) and `research-specialist.md` (line 545) include Grep examples using placeholder paths:
```
Grep pattern="[topic]" path="/path/to/agent-marketing-team/knowledge/learnings/campaigns/"
```

An agent executing these literally will either fail (if the path doesn't exist) or produce no results (if it resolves to nothing). The actual path is `/Users/chris/Development/agent-marketing-team/knowledge/learnings/campaigns/`.

## Proposed Solution

Replace `/path/to/agent-marketing-team/` with the actual absolute path in all Grep examples. Since this is a personal development machine, the real path is stable enough to hardcode.

Or: Instruct agents to resolve the project root first:
```bash
Bash("pwd")  # → /Users/chris/Development/agent-marketing-team
```
Then construct the path dynamically.

**Effort:** Small — 3 line edits

## Acceptance Criteria

- [ ] No Grep examples use `/path/to/` placeholder
- [ ] Grep examples use actual absolute path or include project root resolution

## Work Log

- 2026-02-18: Identified by agent-native-reviewer during PR review
