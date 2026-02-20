---
status: pending
priority: p1
issue_id: "055"
tags: [code-review, blocking, delegation, sprint-scoping, campaign-lead]
---

# Sprint 2 Creative Specialist Spawn Missing [S2] Task Scoping

## Problem Statement

The Sprint 2 Kickoff Protocol's Creative Specialist spawn prompt tells the subagent to "claim and execute all available tasks matching your role" without scoping to Sprint 2 tasks. The Sprint 3 Kickoff Protocol correctly scopes to `[S3]` tasks. Without `[S2]` scoping, if any Sprint 3 tasks were prematurely created or any other unblocked tasks exist, the Creative Specialist spawned in Sprint 2 could claim them, causing cross-sprint task pollution.

## Findings

**Sprint 2 spawn (current):**
```
prompt="...then claim and execute all available tasks matching your role from TaskList()..."
```

**Sprint 3 spawn (correct, has scoping):**
```
prompt="...then claim and execute all available [S3] revision tasks..."
```

The asymmetry is unintentional. Sprint 2 should match Sprint 3's pattern by filtering to `[S2]` tasks.

**File:** `.claude/agents/campaign-lead.md`, Sprint 2 Kickoff Protocol step 5
**Identified by:** architecture-strategist

## Proposed Solution

Update Sprint 2 Creative Specialist spawn prompt to add [S2] scoping:

```
prompt="You are the Creative Specialist for [campaign-name]. Read .claude/agents/creative-specialist.md, then claim and execute all available [S2] tasks matching your role from TaskList() in a loop until no unclaimed unblocked [S2] tasks for your role remain. Complete each task fully before claiming the next. When done, report which tasks you completed."
```

**Effort:** Small (one-line change, coordinate with todo 054)
**Risk:** Low

## Acceptance Criteria

- [ ] Sprint 2 Creative Specialist spawn prompt includes [S2] task scoping
- [ ] Sprint 2 Quality Gate spawn prompt includes [S2] editing task scoping
- [ ] Both [S2] scoping changes applied alongside todo 054's canonical template fixes

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist. Should be fixed together with todo 054.
