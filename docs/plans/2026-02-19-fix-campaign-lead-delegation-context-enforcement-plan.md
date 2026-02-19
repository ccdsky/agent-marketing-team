---
title: "fix: Campaign Lead Delegation and Context Compliance Enforcement"
type: fix
status: completed
date: 2026-02-19
source: docs/plans/campaign-evaluation.md
version: v1.4
---

# fix: Campaign Lead Delegation and Context Compliance Enforcement

## Overview

The v1.3 campaign evaluation ("Why ERP Projects Fail") revealed three systemic failures in the agent coordination model despite producing publication-quality content: Sprint 2 delegation was 0% correct (Campaign Lead wrote all 9 output files itself), context consumption was incomplete (only `icp.md` read directly; `voice-dna.md` and `brand-guide.md` never read), and no retrospective or knowledge compounding occurred. Sprint 3 corrected only after a one-sentence user prompt — proving agents are capable of the behavior but that the architecture documents are insufficient to trigger it without human intervention.

This plan fixes the root causes through targeted prompt-level changes to agent definition files. No infrastructure changes are required.

---

## Problem Statement

### Root Cause 1: No Delegation Trigger at the Decision Point

`campaign-lead.md` Sprint 2 section says "create Sprint 2 tasks with TaskCreate" but never says "then spawn specialists to execute them." The instruction to delegate lives in `TEAM.md` Execution Model, not at the moment the agent decides how to execute Sprint 2. **The agent followed its Sprint 2 instructions precisely — the instructions were wrong.**

Session line 172 (the smoking gun):
> *"Good - tasks are set up with dependencies. Now let me read the skill files I'll need for drafting, and then claim and execute Task 5 (blog post draft)."*

### Root Cause 2: Context Window Efficiency Perverse Incentive

The Campaign Lead already has all context loaded. Spawning subagents means each specialist starts fresh, reads agent definitions and context files, then executes. The path of least resistance was self-execution. Nothing in the agent definition countered this incentive.

### Root Cause 3: File Ownership is Advisory, Not Legible

The ownership table in `TEAM.md` is a reference table, not an enforcement mechanism. No agent definition tells the Campaign Lead "you cannot write to `drafts/`" — only that specialists own those directories. Without a negative constraint legible at the decision point, the constraint is invisible under pressure.

### Root Cause 4: Context Protocol Not Validated

The Pre-Task Protocol in `TEAM.md` lists what to read but contains no validation step. No agent definition explicitly checks "have I read these files before proceeding?" The protocol was followed partially (icp.md) and skipped otherwise.

### Root Cause 5: Retrospective Placed After Launch (Too Late)

`campaign-lead.md` places retrospective "After campaign launches and week 1 data is in." Sprint 3 completed and was summarized — but since the trigger is post-launch analytics, not post-Sprint-3 completion, the Campaign Lead never ran it.

---

## Proposed Solution

Eight targeted changes to agent definition files. All are text additions or replacements to existing sections. No new infrastructure, no hooks, no structural changes.

---

## Files to Modify

| File | Changes | Priority |
|------|---------|----------|
| `.claude/agents/campaign-lead.md` | Header negative list, Sprint 1 context gate, Sprint 2 kickoff protocol, Sprint 3 retrospective enforcement, self-check protocol | P0 |
| `.claude/agents/TEAM.md` | Pre-Task Protocol validation step | P1 |
| `.claude/agents/creative-specialist.md` | Explicit context reads in Before You Start | P1 |
| `.claude/agents/quality-gate.md` | Explicit context reads in Before You Start | P1 |
| `.claude/agents/distribution-specialist.md` | Explicit context reads in Before You Start | P2 |
| `docs/test-plan-v1.4.md` | New delegation test 2.12 as must-pass criterion | P2 |

---

## Technical Considerations

### Why prompt-level enforcement over infrastructure enforcement

The evaluation's Fix 8 considered three options for structural enforcement:
1. **Prompt-level** (each agent knows exactly which directories it can/cannot write to)
2. **Post-sprint audit** (scan git log after each sprint, flag violations at checkpoint)
3. **Pre-task validation** (hook around Write() calls, block unauthorized paths)

Option 3 (Write() hooks) was assessed as potentially infeasible in Claude Code's architecture. Option 2 adds overhead but doesn't prevent the violation. **Option 1 is recommended as first implementation** — it's the highest-leverage, lowest-effort, and most reversible change.

### Parallel vs sequential spawning (Fix 4 note)

The evaluation prescribes sequential spawning (spawn Creative Specialist → wait → spawn Quality Gate → wait). This is conservative but correct: QG depends on Creative Specialist output. However, within Sprint 2, multiple Creative Specialist tasks (blog, email, LinkedIn, newsletter) could be parallelized. The Sprint 2 kickoff protocol below separates the Creative-to-QG handoff but allows parallel drafting within the Creative Specialist's own loop.

### Retrospective timing

Moving the retrospective trigger from "after week 1 analytics" to "after all Sprint 3 tasks complete" means running the retro without performance data. This is acceptable — the retro's value is process learning, not outcome measurement. Add a note that the retro can be revisited/updated when Week 1 analytics arrive.

---

## Implementation Plan

### Change 1: campaign-lead.md — Header Negative List

**Section:** `## Your Core Responsibilities` (current lines 7–17)

**Replace** the current single line `**You coordinate. Specialists execute.**` with:

```markdown
**You coordinate. Specialists execute.**

**YOU DO NOT:**
- Write drafts (that's Creative Specialist)
- Run expert reviews (that's Creative Specialist)
- Score or edit assets (that's Quality Gate)
- Format for platforms (that's Distribution Specialist)
- Write to `drafts/`, `edited/`, or `ready/` directories (those belong to specialists)

If no specialist is available, spawn one using the Campaign Mode pattern in TEAM.md. Never do the work yourself.
```

---

### Change 2: campaign-lead.md — Sprint 1 Context Validation Gate

**Section:** `## Sprint 1: Plan & Sketch` (current lines 108–178)

**Add** after the section header and before `*Sprint philosophy:...* ` line:

```markdown
### Context Validation Gate (Required Before Any Sprint 1 Task)

Before creating any Sprint 1 tasks, verify you have read:
- [ ] `context/voice-dna.md` — voice patterns and writing samples
- [ ] `context/icp.md` — ICP definitions and language
- [ ] `context/business-profile.md` — offerings and positioning
- [ ] `context/brand-guide.md` — banned phrases and platform guidelines (if file exists — skip if not)

Read any you haven't loaded yet. Do not create Sprint 1 tasks without all required files.
```

---

### Change 3: campaign-lead.md — Sprint 2 Delegation Enforcement

**Section:** `## Sprint 2: Refine & Deepen` (current lines 182–236)

**Add** at the top of the Sprint 2 section, before `### Your Sprint 2 Task Breakdown`:

```markdown
### ⚠️ Sprint 2 Kickoff Protocol (Mandatory)

**CRITICAL:** You create Sprint 2 tasks and then spawn specialists. You do NOT draft, review, or edit content yourself.

When the user approves Sprint 2:

1. Create all Sprint 2 drafting tasks with TaskCreate (`[S2]` prefix)
2. Create all Sprint 2 expert review tasks with TaskCreate (embed drafting task IDs)
3. Create all Sprint 2 editing tasks with TaskCreate (blocked by expert review tasks)
4. Set all dependencies with TaskUpdate
5. Spawn Creative Specialist: `Task(subagent_type="general-purpose", prompt="You are the Creative Specialist for [campaign-name]. Read .claude/agents/creative-specialist.md, then claim and execute all available tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain.")`
6. Wait for Creative Specialist to complete all drafting and expert review tasks
7. Spawn Quality Gate: `Task(subagent_type="general-purpose", prompt="You are the Quality Gate for [campaign-name]. Read .claude/agents/quality-gate.md, then claim and execute all available editing tasks from TaskList() serially.")`
8. Wait for Quality Gate to complete all editing tasks
9. Compile Sprint 2 checkpoint from completed task metadata

**STOP CHECK:** If you find yourself reading a skill file, writing a draft, or creating a file in `drafts/` or `edited/` — STOP. You are violating the delegation model. Spawn the appropriate specialist instead.
```

---

### Change 4: campaign-lead.md — Sprint 3 Delegation Enforcement

**Section:** `## Sprint 3: Execute & Ship` (current lines 240–261)

**Add** at the top of the Sprint 3 section, before `### Your Sprint 3 Task Breakdown`:

```markdown
### ⚠️ Sprint 3 Kickoff Protocol (Mandatory)

When the user approves Sprint 3:

1. Create all Sprint 3 revision tasks with TaskCreate (`[S3]` prefix)
2. Create all Sprint 3 distribution tasks (blocked by revision + editing tasks)
3. Set all dependencies with TaskUpdate
4. Spawn Creative Specialist for revisions: `Task(subagent_type="general-purpose", prompt="...")`
5. Wait for revisions complete
6. Spawn Quality Gate for final editorial: `Task(subagent_type="general-purpose", prompt="...")`
7. Wait for editorial complete
8. Spawn Distribution Specialist(s): `Task(subagent_type="general-purpose", prompt="...")`
9. Wait for all Distribution Specialist tasks to complete
10. **Run campaign retrospective** (see Retrospective Protocol below)
11. Present pre-launch summary

**STOP CHECK:** Same as Sprint 2 — if you find yourself writing content, STOP and spawn a specialist.
```

---

### Change 5: campaign-lead.md — Self-Check Protocol (New Section)

**Add** as a new section after `## Sprint 3: Execute & Ship` and before `## Progress Monitoring`:

```markdown
## File Ownership Self-Check

**Before creating any file, run this check:**

1. What directory am I writing to?
2. Is that directory in my ownership zone? (Campaign Lead owns only `campaign-brief.md` and the campaign root directory — NOT `drafts/`, `edited/`, or `ready/`)
3. If writing to a specialists' directory: STOP. Which specialist owns this? Have I spawned them?

**Ownership quick reference:**

| Directory | Owner |
|-----------|-------|
| `output/campaigns/[slug]/campaign-brief.md` | Campaign Lead ✅ |
| `output/campaigns/[slug]/drafts/` | Creative Specialist only |
| `output/campaigns/[slug]/edited/` | Quality Gate only |
| `output/campaigns/[slug]/ready/` | Distribution Specialist only |
| `knowledge/research/` | Research Specialist only |
| `knowledge/learnings/` | Campaign Lead (after retrospective) |
| `analytics/` | Distribution Specialist only |
```

---

### Change 6: campaign-lead.md — Retrospective Timing Fix

**Section:** `## Campaign Retrospective (After Launch)` (current lines 364–370)

**Replace** the entire section with:

```markdown
## Campaign Retrospective (After Sprint 3 Completes)

After all Sprint 3 tasks are complete and Distribution Specialist has created platform briefs, **run the campaign retrospective before presenting the pre-launch summary.**

```
Read(file_path=".claude/workflows/retrospective.md")
```

**MANDATORY steps:**
1. Read `.claude/workflows/retrospective.md`
2. Answer all 5 retrospective questions with specific, evidence-based observations
3. Identify at least one learning worth codifying
4. Save learnings to `knowledge/learnings/campaigns/[category]/` with proper frontmatter
5. Create archive entry in `knowledge/archive/`

The Sprint 3 checkpoint is NOT complete until the retrospective is done and at least one learning is saved.

**Note:** The retrospective can be revisited and updated when Week 1 analytics arrive. But the process questions (what worked, what didn't, coordination patterns) are answerable immediately and should not wait for performance data.
```

---

### Change 7: TEAM.md — Pre-Task Protocol Validation Step

**Section:** `## Pre-Task Protocol` (current lines 101–111)

**Add** after the bulleted read list:

```markdown
**Validation step (Campaign Lead and specialists):** Before claiming your first task in a session, confirm you have loaded each required file. If a file hasn't been read in this session, read it now. Do not proceed on cached assumptions — context may have changed since the last campaign.

**Brand guide note:** If `context/brand-guide.md` exists, it is required reading regardless of OPTIONAL designation in older protocols. It contains banned phrases that can disqualify otherwise excellent content.
```

---

### Change 8: Specialist Agent Files — Explicit Context Reads

**Target files:**
- `.claude/agents/creative-specialist.md` — `## Before You Start` section (line 21–23)
- `.claude/agents/quality-gate.md` — `## Before You Start` section (line 21–24)
- `.claude/agents/distribution-specialist.md` — `## Before You Start` section

**Add** to each `## Before You Start` section:

```markdown
**Explicitly read these files before claiming your first task:**
```
Read(file_path="context/voice-dna.md")
Read(file_path="context/brand-guide.md")  # Skip if file doesn't exist
```

Do not rely on context inherited from Campaign Lead. Each specialist runs as a subagent with a fresh context window.
```

---

### Change 9: Test Plan — Add Delegation Test 2.12

**Create or update** the test plan for v1.4 to include:

```markdown
| # | Test | Pass | Fail |
|---|------|------|------|
| 2.12 | **Delegation model.** Did Campaign Lead spawn specialist subagents for Sprint 2 execution? | Creative Specialist and Quality Gate each spawned as separate `Task()` subagents with `general-purpose` type. Campaign Lead created zero files in `drafts/` or `edited/`. All 9 Sprint 2 output files created by correct agents. | Campaign Lead wrote drafts, ran QG, or created files in `drafts/`/`edited/` directly. Specialists were not spawned as separate agents. |
```

**Classification:** Must-pass criterion (same weight as voice fidelity tests 2.1–2.4). A campaign that produces excellent content with 0% delegation compliance is an architecture failure, not a content success.

---

## Acceptance Criteria

### Functional Requirements
- [x] Campaign Lead does NOT write any files to `drafts/`, `edited/`, or `ready/` directories
- [x] Campaign Lead spawns Creative Specialist as `general-purpose` subagent for Sprint 2 drafting
- [x] Campaign Lead spawns Quality Gate as `general-purpose` subagent for Sprint 2 editing
- [x] Campaign Lead reads all four context files before Sprint 1 tasks are created (including `brand-guide.md` if present)
- [x] Campaign Lead runs retrospective immediately after Sprint 3 tasks complete, before pre-launch summary
- [x] Retrospective produces at least one learning file saved to `knowledge/learnings/`

### Architecture Requirements
- [x] Each specialist agent reads `voice-dna.md` and `brand-guide.md` at session start (not inherited from Campaign Lead)
- [x] TEAM.md Pre-Task Protocol includes validation step, not just list

### Test Plan Requirements
- [x] Test 2.12 (delegation model) added as must-pass criterion
- [x] Future test runs can verify delegation by checking file creation agent vs expected owner

---

## System-Wide Impact

**Interaction graph:** Changes to `campaign-lead.md` Sprint 2 section affect every future multi-asset campaign. The Sprint 2 kickoff protocol replaces implicit behavior (agent decides how to execute) with explicit behavior (numbered sequence with STOP CHECK). This is the highest-leverage change.

**Error propagation:** If Campaign Lead misreads the kickoff protocol and still executes directly, the STOP CHECK language provides a secondary catch. If that fails too, the self-check protocol (Change 5) provides a third catch at the file-write decision point.

**State lifecycle risks:** Moving retrospective from post-launch to post-Sprint-3 means the retro runs without Week 1 analytics. This is explicitly noted — retro is designed to be revisited. No state corruption risk.

**API surface parity:** All specialists (Creative, QG, Distribution, Research) now have parallel context-read requirements. This ensures consistent voice compliance regardless of which agent writes which asset.

**Integration test scenarios:**
1. Sprint 2 kickoff: Verify Campaign Lead's first tool call after Sprint 2 approval is TaskCreate (not Read of a skill file)
2. File ownership: After Sprint 2 completes, grep git log to confirm all `drafts/` files were authored by Creative Specialist task
3. Context reads: Verify `voice-dna.md` appears in each specialist subagent's tool calls before first Write
4. Retrospective trigger: Verify retrospective runs before pre-launch summary, not after

---

## Dependencies & Risks

**Dependencies:**
- No external dependencies. All changes are to local markdown files.
- Changes to `campaign-lead.md` are the prerequisite for changes to test plan (need to know what behavior we're testing).

**Risks:**
- **Over-specification risk:** Adding too many STOP CHECKs could make the Campaign Lead excessively self-doubting and slow. Mitigate: Keep stop checks short and actionable, not preachy.
- **Spawning overhead:** Each correct delegation adds 1-2 subagent spawns per sprint, increasing token usage by ~15-20%. This is the correct architectural tradeoff — coordination cost for role fidelity.
- **Sequential spawning bottleneck:** The kickoff protocol prescribes Creative → wait → QG sequential spawning. This is correct for dependency reasons but adds latency. Future optimization: allow parallel creative drafts within a single Creative Specialist invocation.

---

## Success Metrics

**Primary:** Next campaign run achieves 100% delegation compliance (0 files written by Campaign Lead to specialist-owned directories).

**Secondary:**
- All 4 context files read by Campaign Lead before Sprint 1 (including brand-guide)
- All specialist subagents read `voice-dna.md` independently
- Retrospective completed and at least 1 learning saved before pre-launch summary
- Test 2.12 (delegation model) passes as must-pass criterion

**Baseline:** v1.3 test — 0% delegation compliance Sprint 2, 100% Sprint 3 (after user correction).

---

## References & Research

### Evidence Base
- Campaign evaluation: `docs/plans/campaign-evaluation.md`
- Session transcript: `~/.claude/projects/-Users-chris-Development-test1.3-agent-marketing-team/909e34f5-0295-4202-ac0f-d4e3e7e4551f.jsonl` (2.2MB, 492 lines)
- Smoking gun: Session line 172 — Campaign Lead internal reasoning before self-executing Sprint 2

### Files to Modify
- `.claude/agents/campaign-lead.md` (9 changes across 6 sections)
- `.claude/agents/TEAM.md` (1 change, Pre-Task Protocol)
- `.claude/agents/creative-specialist.md` (1 change, Before You Start)
- `.claude/agents/quality-gate.md` (1 change, Before You Start)
- `.claude/agents/distribution-specialist.md` (1 change, Before You Start)
- `docs/test-plan-v1.4.md` (new file or updated test plan)

### Evaluation Fixes Mapping
| Evaluation Fix | Plan Change | Status |
|---------------|-------------|--------|
| Fix 1: Explicit delegation directives in Sprint sections | Changes 3, 4 | Included |
| Fix 2: Reinforce anti-pattern in header | Change 1 | Included |
| Fix 3: Self-check protocol before file creation | Change 5 | Included |
| Fix 4: Make spawning mandatory in sprint transitions | Changes 3, 4 | Included |
| Fix 5A: Context validation gate in Campaign Lead | Change 2 | Included |
| Fix 5B: Context reads in specialist definitions | Change 8 | Included |
| Fix 6: Retrospective enforcement post-Sprint-3 | Changes 4, 6 | Included |
| Fix 7: Add delegation test to test plan | Change 9 | Included |
| Fix 8: Structural enforcement (Option 1: prompt-level) | Changes 1, 5 | Included |

### Open Questions for Planning Review
1. **Research synthesis boundary:** Should Campaign Lead compile research into positioning angles, or is that Research Specialist's job? The evaluation called this a "gray area." Determine the answer and update agent definitions if needed.
2. **Spawning agent type for Research Specialist:** The evaluation found it was spawned as `Explore` type, not `general-purpose`. Should TEAM.md's spawning pattern explicitly specify `general-purpose` for all specialists (including Research)?
3. **Brand-guide optionality:** TEAM.md currently marks brand-guide as "optional." Given that it contains banned phrases critical to quality compliance, should it be promoted to required? Or kept optional with stronger enforcement language?
