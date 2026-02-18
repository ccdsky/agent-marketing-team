---
status: pending
priority: p2
issue_id: "028"
tags: [code-review, simplicity, duplication, quick-reference]
---

# "Quick Reference: Your Tool Use" Sections Duplicate Body Content (~100 Lines)

## Problem Statement

Every agent file ends with a "Quick Reference: Your Tool Use" section showing TaskUpdate claim, TaskUpdate complete, Read, Write tool calls — all of which already appear with more context in the body of the same file. The sections exist in:

1. `campaign-lead.md` lines 592-636
2. `research-specialist.md` lines 510-546
3. `creative-specialist.md` lines 566-606
4. `quality-gate.md` lines 734-775
5. `distribution-specialist.md` lines 896-929

Total: ~100 lines across five files. An LLM reading top-to-bottom doesn't benefit from a summary of what it just read. These sections exist for human quick-reference (like a printed cheat sheet) but are wasteful in an LLM context window.

## Proposed Solution

Remove all five "Quick Reference" sections. The tool calls in the body of each agent file already provide this information with context — which is more useful than a decontextualized list.

If a cheat-sheet is desired for human readers, move one example to the README.

**Effort:** Small — delete sections from 5 files

## Acceptance Criteria

- [ ] No "Quick Reference: Your Tool Use" section in any agent file
- [ ] All removed content was already present with context in the file body (verify before deleting)

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
