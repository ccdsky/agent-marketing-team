---
status: pending
priority: p1
issue_id: "032"
tags: [code-review, TEAM.md, execution-model, subagent, campaign-mode, loop]
---

# Subagent Loop Exit Condition Missing — Agents Claim One Task Then Exit

## Problem Statement

`TEAM.md` Execution Model describes Campaign Lead spawning specialists as subagents that "self-claim their next available task." But the spawning prompt does not include a loop exit condition. A subagent claims one task, executes it, completes it, and then exits — because it has no instruction to check for more tasks. This means Campaign Lead must re-spawn the agent for each task rather than each agent running its task queue to completion.

## Findings

**TEAM.md Execution Model spawning prompt:**
```
Task(
  subagent_type="general-purpose",
  prompt="You are the [role] for the [campaign-name] campaign. Read .claude/agents/[role].md and claim your next available task from TaskList().",
  ...
)
```

"Your next available task" implies claiming one task. After completing it, the subagent has no instruction to loop. The "Self-Claiming Workflow" in TEAM.md (lines 299-334) describes the protocol for one task cycle but says nothing about repeating until the queue is empty.

In practice, the Campaign Lead spawning one subagent per sprint invocation would need to re-invoke the subagent for each task — or each subagent should loop until no tasks remain.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Add loop instruction to spawning prompt (Recommended)

Update the spawning prompt to include loop behavior:
```
Task(
  subagent_type="general-purpose",
  prompt="You are the [role] for the [campaign-name] campaign. Read .claude/agents/[role].md. Claim and complete tasks matching your role keywords from TaskList() in a loop until no unclaimed unblocked tasks for your role remain. Report back when complete.",
  ...
)
```

Add to TEAM.md after the spawning prompt: "Each spawned agent runs a task loop: TaskList → find unclaimed matching task → claim → execute → complete → repeat. On exit (no tasks): report to Campaign Lead."

**Effort:** Small — update spawning prompt and add loop documentation in TEAM.md

### Option B: Campaign Lead spawns one agent per task (explicit)

Document that Campaign Lead spawns one subagent per task, not one per sprint. Simpler to reason about but higher overhead.

**Effort:** Small — clarify Execution Model documentation

## Acceptance Criteria

- [ ] TEAM.md spawning prompt includes a loop pattern with explicit exit condition
- [ ] Subagents know when to stop claiming and report back
- [ ] The loop exit condition ("no more tasks for my role") is explicit

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
