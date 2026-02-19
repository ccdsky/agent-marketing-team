---
status: pending
priority: p3
issue_id: "053"
tags: [code-review, sprint1, positioning-angles, checkpoint, structural-enforcement, campaign-lead]
---

# Sprint 1 Checkpoint Guard Is Procedural Not Structural — Pre-Created Sprint 2 Tasks Would Bypass It

## Problem Statement

`positioning-angles/SKILL.md` and `lead-magnet-strategy/SKILL.md` include Sprint 1 Checkpoint sections that say "do not proceed to Sprint 2 asset creation without human approval." The enforcement mechanism is creation-time gating: Campaign Lead only creates Sprint 2 tasks after Sprint 1 approval. This works correctly as long as Campaign Lead follows sprint-planning.md. However, if Campaign Lead pre-creates all sprint tasks upfront (a reasonable behavior for task planning), Sprint 2 tasks become claimable before Sprint 1 approval is obtained.

Also: `expert-review/SKILL.md` Simple Mode fallback is not mentioned in `creative-specialist.md` Step 8, which could cause a Campaign Mode agent to attempt subagent spawning in a Simple Mode context.

## Findings

**positioning-angles/SKILL.md Sprint 1 Checkpoint:**
> "Do not proceed to Sprint 2 asset creation. This output presents options — the human selects the direction."

**sprint-planning.md Sprint 1:**
> "Only create Sprint 2 tasks after user approves Sprint 1 direction."

If followed, the guard works. But campaign-lead.md doesn't repeat this constraint where Campaign Lead creates tasks. An agent scanning only campaign-lead.md's Sprint 1 task breakdown could create all sprint tasks at once.

**expert-review/SKILL.md:** Has a clean Mode Check section. creative-specialist.md Step 8 says "Read the expert review skill and follow its framework" but doesn't mention the Mode Check.

**Identified by:** agent-native-reviewer (P3 — current design is sound, minor improvements only)

## Proposed Solutions

### Fix 1: Add constraint to campaign-lead.md Sprint 1 task creation section

Add one sentence: "Create Sprint 1 tasks only. Do NOT create Sprint 2 or Sprint 3 tasks until the Sprint 1 checkpoint is approved."

### Fix 2: Add Mode Check reminder to creative-specialist.md Step 8

Add one line: "The expert-review skill defines a Mode Check — run it first to determine if Task tool is available before spawning subagents."

**Effort:** Trivial — two one-line additions

## Acceptance Criteria

- [ ] campaign-lead.md Sprint 1 section explicitly prohibits pre-creating Sprint 2 tasks
- [ ] creative-specialist.md Step 8 mentions the expert review Mode Check
- [ ] Sprint 1 checkpoint enforcement is consistent across all documents that reference it

## Work Log

- 2026-02-19: Identified during v1.3 code review by agent-native-reviewer
