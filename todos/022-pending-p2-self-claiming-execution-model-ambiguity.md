---
status: pending
priority: p2
issue_id: "022"
tags: [code-review, agent-coordination, execution-model, task-tool, parallel-execution]
---

# Self-Claiming Model Does Not Clarify Persona-Switch vs. Task() Subagent Execution

## Problem Statement

The system describes agents "self-claiming tasks" and working "in parallel" — but never clarifies whether specialists are:

(a) **Persona switches** — One LLM conversation where Campaign Lead switches to Research Specialist persona, executes sequentially, then switches back. No true parallelism.

(b) **Task() subagents** — Campaign Lead spawns specialists via the `Task` tool, which genuinely run in parallel but in separate contexts without shared file access by default.

(c) **Hybrid** — Simple Mode uses persona-switching; Campaign Mode uses Task() subagents.

This matters because:
- If (a): "parallel" work is impossible; the coordination model is misleading
- If (b): specialists cannot access output/ files created in the parent conversation without explicit Read() calls; the file-ownership model needs adjustment
- If (c): this needs to be documented so agents know which mode to use

`creative-specialist.md` lines 239-249 explicitly describes "Writer 1 claims lead magnet, Writer 2 claims landing page, Writer 3 claims email sequence, all simultaneously" — but this only works if each "writer" is a Task() subagent, not a persona switch.

## Proposed Solution

Add an "Execution Model" section to TEAM.md:

```markdown
## Execution Model

**Simple Mode (single asset):** Campaign Lead or the activated specialist operates directly within the conversation. No subagents. Sequential persona-switch if needed. "Parallel" is inapplicable.

**Campaign Mode (multi-asset sprint):** Campaign Lead uses the Task tool to spawn specialist agents as subagents. Each subagent has access to the shared file system (the project directory). Subagents can run in parallel, each claiming and executing a different task. Campaign Lead monitors via TaskList.

When spawning a specialist:
```
Task(
  subagent_type="general-purpose",
  prompt="You are the Creative Specialist for the [campaign-name] campaign. Read .claude/agents/creative-specialist.md and claim your next available task from TaskList.",
  description="Creative Specialist — [campaign-slug]"
)
```
```

**Effort:** Small — 1 section added to TEAM.md, reference added to campaign-lead.md

## Acceptance Criteria

- [ ] TEAM.md explicitly defines Simple Mode and Campaign Mode execution models
- [ ] campaign-lead.md shows the Task() call for spawning specialists in Campaign Mode
- [ ] "Parallel" language is qualified with the execution model it requires

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
