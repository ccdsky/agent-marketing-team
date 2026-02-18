---
status: pending
priority: p1
issue_id: "016"
tags: [code-review, agent-coordination, inter-agent-communication, quality-gate, distribution-specialist]
---

# Quality Gate and Distribution Specialist Still Read "Task Comments" Not Metadata

## Problem Statement

TEAM.md and creative-specialist.md were updated to use `TaskUpdate(metadata={...})` as the inter-agent communication channel (P1 fix #001). However, the Quality Gate and Distribution Specialist were not updated consistently — they still instruct agents to look for "task comments" that don't exist as a Claude Code tool.

`quality-gate.md` lines 50-57:
```
Check task comments:
TaskGet(taskId="[ID]")
Look for:
- Creative Specialist marked writing task as "completed"
- Draft file path provided
- Self-assessment included
- Expert review summary (if Sprint 2)
```

`TaskGet` returns task metadata fields, not freeform comments. The QG is told to look for a "draft file path" in comments, but that path lives in `metadata["deliverable"]` set by the Creative Specialist's `TaskUpdate`.

`distribution-specialist.md` line 57 checks for "✅ APPROVED FOR PUBLISHING" comment from Quality Gate — a string that exists in no tool output. The Quality Gate's completion sets `metadata["ready_for": "distribution"]`, not a comment.

`quality-gate.md` lines 127-141 (approval "comment") and 154-186 (revision "comment") also use prose comment format instead of metadata.

This means: the Creative Specialist correctly writes metadata, but QG cannot find it (looks for comment instead), so QG cannot locate the draft file. The entire Sprint 2 → Sprint 3 handoff is broken.

## Proposed Solution

**Option A (preferred):** Update Quality Gate and Distribution Specialist "Verify" steps to read metadata from `TaskGet`, not comments. Replace prose "check task comments" with:

```
TaskGet(taskId="[ID]")
# Read metadata fields:
# metadata["deliverable"] — path to the draft file
# metadata["assessment"] — Creative Specialist self-assessment
# metadata["expert_review"] — expert review summary
# metadata["ready_for"] — next agent role (e.g., "quality-gate")
```

Update Quality Gate completion step to write metadata instead of "comment":
```
TaskUpdate(
  taskId="[ID]",
  status="completed",
  metadata={
    "deliverable": "output/campaigns/[slug]/edited/[asset]-edited.md",
    "assessment": "9/10 voice — approved for publishing",
    "ready_for": "distribution-specialist"
  }
)
```

**Option B:** Create a HANDOFF.md file convention at a known path that agents write and read instead of task metadata.

**Effort:** Medium — 3 agent files need targeted edits (quality-gate.md, distribution-specialist.md, research-specialist.md completion steps)

## Acceptance Criteria

- [ ] quality-gate.md step 2 reads `metadata["deliverable"]` from TaskGet, not "task comments"
- [ ] quality-gate.md completion step writes metadata (deliverable path, assessment, ready_for)
- [ ] distribution-specialist.md approval verification reads QG metadata from TaskGet
- [ ] research-specialist.md completion step uses TaskUpdate metadata (not prose "add comment")
- [ ] No agent file refers to "task comments" as a communication mechanism

## Work Log

- 2026-02-18: Identified by agent-native-reviewer and architecture-strategist in second review pass
