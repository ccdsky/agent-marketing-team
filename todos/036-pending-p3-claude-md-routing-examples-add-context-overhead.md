---
status: pending
priority: p3
issue_id: "036"
tags: [code-review, simplicity, CLAUDE.md, routing, verbosity]
---

# CLAUDE.md Routing Blocks Contain Worked Examples That Restate Agent File Content

## Problem Statement

CLAUDE.md's 5 routing sections (Research Specialist, Creative Specialist, Quality Gate, Distribution Specialist, Campaign Lead) each include a "Primary flow" multi-step sequence and an "Example" block showing a 7-10 step campaign execution. Total: ~150-200 lines.

These examples duplicate what the agent files define as their primary workflows. For routing, trigger keywords and "Route when user says" patterns are sufficient. The worked examples show the LLM what to do *after* routing — but the agent file it routes to already contains that information in detail.

CLAUDE.md is loaded into every conversation, including simple single-asset requests. A user asking for a LinkedIn post causes the system to load full multi-step campaign flow examples before routing to creative-specialist.md.

## Proposed Solution

Keep: trigger keywords, "Route when user says" patterns, agent name, and pointer to agent file.

Remove: "Primary flow" sequences and "Example" blocks from each routing section.

Result: Each routing section is 5-8 lines instead of 20-35 lines. CLAUDE.md loses ~120 lines and becomes a true routing document rather than a partial agent manual.

**Effort:** Medium — edit 5 routing sections in CLAUDE.md (remove ~120 lines)

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer and architecture-strategist in second review pass
