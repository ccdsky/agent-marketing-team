---
status: pending
priority: p1
issue_id: "001"
tags: [code-review, architecture, agent-coordination, blocking]
---

# Task Comments Have No Execution Mechanism

## Problem Statement

Every agent definition instructs agents to "add a comment" to a task after completing it. This is the primary inter-agent communication channel — it's how agents signal deliverable locations, pass self-assessments, and notify downstream agents. However, no `TaskComment` tool exists, and no `comment` parameter is shown in any `TaskUpdate` call. The instruction appears as prose followed by what the comment should say, but no executable tool call is provided.

Without this, agents cannot:
- Tell downstream agents where deliverables are saved
- Pass self-assessments to Quality Gate
- Communicate the "✅ APPROVED FOR PUBLISHING" signal Distribution Specialist checks before claiming tasks
- Flag blockers without creating out-of-band files

## Findings

The pattern appears in:
- `.claude/agents/research-specialist.md` — lines 78-88
- `.claude/agents/creative-specialist.md` — lines 157-173 and 710-729
- `.claude/agents/quality-gate.md` — lines 122-142 and 758/768
- `.claude/agents/campaign-lead.md` — multiple locations
- `.claude/workflows/sprint-planning.md` — line 182

**Evidence from creative-specialist.md:**
```
### 9. Complete Task
When done, update task:
TaskUpdate(taskId="[ID]", status="completed")
[Add task comment with deliverable location and self-assessment]
```
The bracketed instruction `[Add task comment...]` has no tool call syntax.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Use TaskUpdate metadata field (Recommended)
The `TaskUpdate` tool supports a `metadata` parameter. Add deliverable path and assessment score to metadata:
```
TaskUpdate(
  taskId="[ID]",
  status="completed",
  metadata={
    "deliverable": "output/campaigns/[slug]/drafts/landing-page-draft.md",
    "self_assessment": "8/10 voice match — strong hook, ICP-relevant"
  }
)
```
Update all five agent files to use this pattern consistently.

**Pros:** Uses existing tool, no new infrastructure
**Cons:** Metadata fields aren't visible in TaskList summary — next agent must call TaskGet to read them
**Effort:** Medium — 5 files to update

### Option B: Handoff note files
Agents write a structured handoff note to `.claude/agents/handoffs/[task-id].md` after completing tasks:
```
Write(
  file_path=".claude/agents/handoffs/[task-id].md",
  content="Deliverable: [path]\nAssessment: [score/notes]"
)
```
Next agent reads this before claiming downstream task.

**Pros:** Simple, auditable, uses existing Write tool
**Cons:** Requires cleanup protocol; handoffs/ directory exists but has no management instructions
**Effort:** Medium — 5 files + handoff note template

### Option C: Include deliverable path in task description at claim time
When claiming a task, the agent updates its description to include the output path:
```
TaskUpdate(
  taskId="[ID]",
  status="in_progress",
  description="[Original description] → Output: output/campaigns/[slug]/drafts/landing-page-draft.md"
)
```

**Pros:** Zero new infrastructure
**Cons:** Overwrites original task description; can't append
**Effort:** Small — update agent claim patterns

## Acceptance Criteria

- [ ] One canonical mechanism is defined for task-to-task communication
- [ ] The mechanism uses an actual tool call (not prose) in every agent file
- [ ] Quality Gate can determine draft file location without guessing
- [ ] Distribution Specialist can confirm editorial approval before publishing

## Work Log

- 2026-02-18: Identified by agent-native-reviewer during PR review
