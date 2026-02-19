---
status: pending
priority: p1
issue_id: "033"
tags: [code-review, TEAM.md, setup, pre-flight, context-files, escalation]
---

# System Pre-Flight References Non-Existent /writer:setup — Context Files Have No Population Path

## Problem Statement

`TEAM.md` System Pre-Flight instructs agents to escalate to the user with "Run `/writer:setup` or manually fill in the template" if context files contain placeholder text. But `/writer:setup` does not exist anywhere in the codebase. The escalation path dead-ends. Since all three context files (`context/voice-dna.md`, `context/icp.md`, `context/business-profile.md`) are currently in placeholder/template state, every agent correctly following the pre-flight will halt immediately with a broken escalation message.

## Findings

**TEAM.md System Pre-Flight:**
> "If any file contains placeholder text: Stop. Escalate to the user: 'Context file [name] needs to be populated before I can work. Run `/writer:setup` or manually fill in the template.'"

No `.claude/skills/setup/` directory exists. No `setup.md`. Not listed in `CLAUDE.md` Available Skills. The command does not exist.

The three context files (`context/voice-dna.md`, `context/icp.md`, `context/business-profile.md`) appear to be template files with placeholder text awaiting user population.

This means the entire system is blocked until a human manually populates all three files, and no structured guidance exists for doing so correctly.

**Identified by:** architecture-strategist, agent-native-reviewer

## Proposed Solutions

### Option A: Create a `/setup` skill (Recommended)

Create `.claude/skills/setup/SKILL.md` with a guided interview format:

```
# Setup Skill

Walk the user through populating the three context files:
1. Ask questions about their business, voice, and ICP
2. Write answers to context/voice-dna.md, context/icp.md, context/business-profile.md
3. Confirm completion
```

Update TEAM.md pre-flight to reference `/setup`.

**Effort:** Medium — write a new skill + update TEAM.md

### Option B: Fix the escalation message to give concrete manual instructions (Fast fix)

Replace the dead reference in TEAM.md with actionable guidance:

> "Stop. Escalate to user: 'Before I can work, you must fill in three context files:
> - `context/voice-dna.md` — Your writing voice and tone
> - `context/icp.md` — Your target customer profile
> - `context/business-profile.md` — Your business and offerings
>
> Each file contains a template with inline instructions. Fill in all sections and return.'"

**Effort:** Trivial — replace one line in TEAM.md

## Acceptance Criteria

- [ ] TEAM.md pre-flight escalation message does not reference a non-existent command
- [ ] An agent escalating due to unpopulated context files gives the user actionable next steps
- [ ] The user can follow the guidance and complete context file setup without further help

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist and agent-native-reviewer
