---
status: pending
priority: p1
issue_id: "054"
tags: [code-review, blocking, delegation, spawn-prompts, campaign-lead]
---

# Sprint 2 and Sprint 3 Spawn Prompts Diverge from TEAM.md Canonical Template

## Problem Statement

The Sprint 2 and Sprint 3 Kickoff Protocols in `campaign-lead.md` spawn specialist subagents using Task() calls that diverge from the canonical Campaign Mode pattern defined in `TEAM.md` (lines 121-128) in three ways: (1) `description=` parameter is missing from all six spawn calls, (2) the completion signal tail is truncated ("Complete each task fully before claiming the next. When done, report which tasks you completed." is absent), and (3) the Quality Gate spawn prompt omits the loop-until-done pattern. Without the completion tail, the "Wait for X to complete" steps (Sprint 2 steps 6 and 8, Sprint 3 steps 5, 7, 9) have no described mechanism — the spawned subagent provides no completion signal via report.

This is a correctness issue that could reproduce the Sprint 2 delegation failure the PR was written to prevent: if Quality Gate claims one editing task, completes it, and exits without a loop, Campaign Lead receives a partial execution with no error signal.

## Findings

**TEAM.md canonical pattern (lines 121-128):**
```
Task(
  subagent_type="general-purpose",
  prompt="You are the [role] for the [campaign-name] campaign. Read .claude/agents/[role].md, then claim and execute all available tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain. Complete each task fully before claiming the next. When done, report which tasks you completed.",
  description="[Role] — [campaign-slug]"
)
```

**Sprint 2 Creative Specialist spawn (campaign-lead.md, line ~213) — current:**
```
Task(subagent_type="general-purpose", prompt="You are the Creative Specialist for [campaign-name]. Read .claude/agents/creative-specialist.md, then claim and execute all available tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain.")
```

Missing: `description=` parameter. Missing: "Complete each task fully before claiming the next. When done, report which tasks you completed."

**Sprint 2 Quality Gate spawn (campaign-lead.md, line ~215) — current:**
```
Task(subagent_type="general-purpose", prompt="You are the Quality Gate for [campaign-name]. Read .claude/agents/quality-gate.md, then claim and execute all available editing tasks from TaskList() serially.")
```

Missing: `description=` parameter. Missing: loop-until-done clause. Missing: completion report.

Same issues in Sprint 3 spawn calls for Creative Specialist (step 4), Quality Gate (step 6), and Distribution Specialist (step 8).

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Match Canonical Template Exactly (Recommended)

Update all six Task() calls in campaign-lead.md to match the TEAM.md pattern. For Quality Gate, keep "serially" but add the loop and report tail.

Sprint 2 Creative Specialist:
```
Task(
  subagent_type="general-purpose",
  prompt="You are the Creative Specialist for [campaign-name]. Read .claude/agents/creative-specialist.md, then claim and execute all available [S2] tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain. Complete each task fully before claiming the next. When done, report which tasks you completed.",
  description="Creative Specialist — [campaign-slug]"
)
```

Sprint 2 Quality Gate:
```
Task(
  subagent_type="general-purpose",
  prompt="You are the Quality Gate for [campaign-name]. Read .claude/agents/quality-gate.md, then claim and execute all available [S2] editing tasks from TaskList() serially, one at a time, until no unclaimed editing tasks remain. Complete each fully before claiming the next. When done, report which tasks you completed.",
  description="Quality Gate — [campaign-slug]"
)
```

Apply same pattern to Sprint 3 steps 4, 6, 8.

**Pros:** Exact match to canonical; description= provides observability; completion report enables Campaign Lead to know when to proceed
**Cons:** Slightly longer prompts

### Option B: Update canonical template to be inline (not recommended)

Consolidate the Template into each sprint section rather than referencing TEAM.md. More verbose, harder to maintain.

**Effort:** Small
**Risk:** Low — pure text changes to campaign-lead.md

## Acceptance Criteria

- [ ] All six Task() calls in Sprint 2 and Sprint 3 kickoff protocols include `description=` parameter
- [ ] All six Task() calls include "Complete each task fully before claiming the next. When done, report which tasks you completed." completion tail
- [ ] Quality Gate spawn includes loop-until-done clause alongside "serially" constraint
- [ ] Sprint 2 Creative Specialist spawn scopes to [S2] tasks (see todo 055)
- [ ] Sprint 3 spawn prompts scope to [S3] tasks (already correct, verify preserved)

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by agent-native-reviewer and architecture-strategist. All six spawn calls need updating.
