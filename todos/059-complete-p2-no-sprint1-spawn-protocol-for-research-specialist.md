---
status: pending
priority: p2
issue_id: "059"
tags: [code-review, delegation, research-specialist, sprint1, campaign-lead]
---

# No Sprint 1 Spawn Protocol for Research Specialist

## Problem Statement

Sprint 2 and Sprint 3 now have explicit ⚠️ Kickoff Protocols with mandatory Task() spawning steps. Sprint 1 has no equivalent. Research Specialist is the only specialist that operates exclusively in Sprint 1, and the v1.3 evaluation documented it was spawned as an `Explore` type subagent rather than `general-purpose` with its own definition read. The Sprint 1 section contains only TaskCreate calls and an advisory note ("Campaign Lead coordinates — does not execute research"), but no spawn directive.

The architectural gap is the same as the pre-PR Sprint 2 gap: the instruction describes what tasks to create but omits "then spawn Research Specialist to execute them." Additionally, Research Specialist's `Before You Start` section still delegates entirely to "Follow Pre-Task Protocol in TEAM.md" with no explicit Read() calls — unlike the three content specialists who received explicit context reads in this PR.

## Findings

**Sprint 1 section note (campaign-lead.md, line ~133):**
```
**Note:** Campaign Lead coordinates — does not execute research or positioning work. Tasks [S1-1], [S1-2], [S1-3] are executed by Research Specialist.
```

This is advisory text, not a spawn protocol. No Task() call specified.

**research-specialist.md Before You Start:**
```
Follow **Pre-Task Protocol** in `.claude/agents/TEAM.md`.
```

No explicit Read() calls for voice-dna.md, icp.md, or business-profile.md.

**v1.3 evaluation evidence (campaign-evaluation.md, lines 56-58):**
Research Specialist was spawned as `Explore` type, not `general-purpose`. It "functioned as a research tool rather than an autonomous specialist."

**Files:** `.claude/agents/campaign-lead.md` Sprint 1 section; `.claude/agents/research-specialist.md` Before You Start
**Identified by:** architecture-strategist, agent-native-reviewer

## Proposed Solution

**Part A:** Add Sprint 1 Spawn Protocol to campaign-lead.md Sprint 1 section:

```
### ⚠️ Sprint 1 Kickoff Protocol (Mandatory)

After creating all Sprint 1 tasks with TaskCreate and setting dependencies with TaskUpdate:

1. Spawn Research Specialist: Task(
     subagent_type="general-purpose",
     prompt="You are the Research Specialist for [campaign-name]. Read .claude/agents/research-specialist.md, then claim and execute all available [S1] research tasks from TaskList() in a loop until no unclaimed unblocked [S1] research tasks remain. Complete each task fully before claiming the next. When done, report which tasks you completed.",
     description="Research Specialist — [campaign-slug]"
   )
2. Wait for Research Specialist to complete (Task() returns with completion report)
3. Synthesize research findings into positioning angles and asset structure
4. Prepare Sprint 1 checkpoint for user approval
```

**Part B:** Add explicit context reads to research-specialist.md Before You Start:

```
Read(file_path="context/icp.md")
Read(file_path="context/business-profile.md")
Read(file_path="context/brand-guide.md")  # Skip if file doesn't exist
```

(voice-dna.md is less critical for research but should also be added for consistency.)

**Effort:** Small
**Risk:** Low

## Acceptance Criteria

- [ ] Sprint 1 section has ⚠️ Kickoff Protocol with Task() spawning of Research Specialist as general-purpose
- [ ] Research Specialist spawn prompt matches canonical TEAM.md template with description= and completion tail
- [ ] research-specialist.md Before You Start has explicit Read() calls for icp.md and business-profile.md

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist and agent-native-reviewer. Coordinates with todo 056 (context read pattern).
