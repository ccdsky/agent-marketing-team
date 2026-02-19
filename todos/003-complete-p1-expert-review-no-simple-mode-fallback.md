---
status: complete
priority: p1
issue_id: "003"
tags: [code-review, blocking, expert-review, simple-mode, task-tool]
---

# Expert Review Has No Simple Mode Fallback When Task Tool Unavailable

## Problem Statement

`expert-review/SKILL.md` Step 2 instructs: "Use the Task tool to spawn each expert simultaneously." There is no fallback for simple mode (single-agent context) where the Task tool is unavailable. In simple mode, the quality checklist at the bottom of creative-specialist.md requires expert review — making it permanently unsatisfiable for any single-agent invocation.

The result: an agent in simple mode following creative-specialist.md instructions will reach Step 8 (run expert review), attempt to spawn subagents, fail silently or error, and have no defined path forward.

## Findings

**expert-review/SKILL.md Step 2:**
> "Use the Task tool to spawn each expert simultaneously"

No alternative path exists for:
- Simple content requests (single agent, no Task tool)
- Environments where Task tool is disabled
- Low-stakes Sprint 1 sketches where full expert panels are overkill

**creative-specialist.md Step 8:**
> "(Optional) Run Expert Review — For Sprint 2 drafts, run expert review before marking complete"

The "(Optional)" qualifier exists in creative-specialist.md but expert-review/SKILL.md itself has no tiered invocation path — it's all-or-nothing multi-agent.

**Identified by:** agent-native-reviewer, code-simplicity-reviewer

## Proposed Solutions

### Option A: Add "Simple Mode" section to expert-review/SKILL.md (Recommended)

Before Step 1, add a mode check:

```
## Mode Check

**Multi-agent mode (Task tool available):** Follow Steps 1-6 below — spawn expert panel in parallel.

**Simple mode (no Task tool):** Perform sequential expert review inline. For each expert in the panel:
1. State the expert perspective ("As a Conversion Copywriter reviewing this landing page...")
2. Apply their criteria
3. Score against rubric
4. Compile synthesis

Output format is identical. Performance is slower but quality is preserved.
```

**Pros:** Preserves skill usability in all contexts; same output format regardless of mode
**Cons:** Sequential mode is slower and less cognitively separated than true parallel subagents
**Effort:** Small

### Option B: Make expert review explicitly optional at skill level

Add to expert-review/SKILL.md: "If Task tool is unavailable, document the gap in task metadata and skip. Quality Gate will compensate."

**Pros:** Simple; avoids complex inline simulation
**Cons:** Quality Gate doesn't have expert panel criteria — gap is real, not compensated
**Effort:** Small but creates quality gap

## Acceptance Criteria

- [ ] An agent in simple mode (no Task tool) has a defined path through expert-review/SKILL.md
- [ ] The simple mode path produces output in the same format as multi-agent mode
- [ ] creative-specialist.md Step 8 references which mode to use when

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
