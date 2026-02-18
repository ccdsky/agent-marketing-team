---
status: pending
priority: p1
issue_id: "002"
tags: [code-review, agent-coordination, skills, blocking]
---

# Skill Invocation Has No Executable Form

## Problem Statement

The Creative Specialist's workflow (step 5) says to "invoke appropriate content skill" and shows:
```
[Use /landing-page skill or create manually following framework]
```

There is no defined mechanism for how an LLM agent actually "loads" a skill. The SKILL.md files contain the frameworks agents must follow — that is valid — but `creative-specialist.md` never tells agents to `Read(.claude/skills/landing-page/SKILL.md)`. Instead it provides brief inline summaries of each skill that conflict with the full SKILL.md specs (e.g., LinkedIn character count: inline summary says "800-1300 chars," `social-post/SKILL.md` says "150-300 words optimal").

An agent following `creative-specialist.md` literally will improvise from the brief inline summaries rather than reading the 200-line detailed frameworks in the SKILL.md files.

## Findings

- `.claude/agents/creative-specialist.md` lines 83-91: "invoke" language with no tool call
- `.claude/agents/creative-specialist.md` lines 236-402: inline skill summaries that conflict with canonical SKILL.md content
- `social-post/SKILL.md` line 69: "150-300 words optimal" vs creative-specialist.md line 297: "800-1300 chars"

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Replace invoke language with explicit Read() call (Recommended)
Update Step 5 in `creative-specialist.md` from:
```
- Landing page → `/landing-page` skill
```
To:
```
- Landing page → Read(file_path=".claude/skills/landing-page/SKILL.md") and follow its framework
```

Also remove the inline skill summaries (lines 236-402) to eliminate the contradiction. The SKILL.md files are the authoritative source — the summaries are a maintenance liability.

**Pros:** Eliminates conflict, makes SKILL.md files authoritative, reduces creative-specialist.md by ~100 lines
**Cons:** creative-specialist.md becomes thinner (acceptable — quality improves)
**Effort:** Medium — rewrite step 5 + remove inline summaries

### Option B: Keep inline summaries, fix conflicts, add Read() call
Keep the summaries as quick reference but add an explicit Read() instruction before each, and audit all specs against their SKILL.md for conflicts.

**Pros:** Preserves quick-reference context
**Cons:** Creates maintenance burden — two sources of truth to keep in sync
**Effort:** Large — audit all 7 summaries for conflicts

## Acceptance Criteria

- [ ] `creative-specialist.md` contains explicit `Read(file_path=".claude/skills/[name]/SKILL.md")` for each skill
- [ ] No conflicting specs between creative-specialist.md and any SKILL.md file
- [ ] Agent can execute skill without improvising the framework

## Work Log

- 2026-02-18: Identified by agent-native-reviewer during PR review
