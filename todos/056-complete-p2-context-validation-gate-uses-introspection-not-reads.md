---
status: pending
priority: p2
issue_id: "056"
tags: [code-review, context-reads, campaign-lead, agent-behavior]
---

# Context Validation Gate Uses Introspection Instead of Unconditional Read() Calls

## Problem Statement

The Sprint 1 Context Validation Gate in `campaign-lead.md` instructs Campaign Lead to "verify you have read" the four context files. The TEAM.md validation step added in this PR says "confirm you have loaded each required file." Both formulations use a cognitive metaphor — the agent introspects its own context window to see what it has loaded. LLMs do not have a reliable self-inventory mechanism. An agent may declare files loaded without actually calling Read(), especially in long sessions where files may have been read earlier.

The specialist files (creative-specialist.md, quality-gate.md, distribution-specialist.md) correctly use unconditional Read() calls, not introspective verification. The Context Validation Gate should match that pattern.

## Findings

**Current (campaign-lead.md, Sprint 1 Context Validation Gate):**
```
Before creating any Sprint 1 tasks, verify you have read:
- [ ] `context/voice-dna.md`
- [ ] `context/icp.md`
- [ ] `context/business-profile.md`
- [ ] `context/brand-guide.md` (if file exists)
Read any you haven't loaded yet.
```

**Correct pattern (creative-specialist.md, Before You Start):**
```
Read(file_path="context/voice-dna.md")
Read(file_path="context/brand-guide.md")  # Skip if file doesn't exist
```

The checkbox introspection pattern invites the agent to skip the tool call if it believes the files are already in context. The unconditional Read() pattern forces the tool call every time.

**Files:** `.claude/agents/campaign-lead.md` Sprint 1 Context Validation Gate; `.claude/agents/TEAM.md` validation step (same issue)
**Identified by:** agent-native-reviewer

## Proposed Solution

Replace the checkbox introspection with unconditional Read() calls:

```
### Context Reads (Execute Before Any Sprint 1 Task)

Read(file_path="context/voice-dna.md")
Read(file_path="context/icp.md")
Read(file_path="context/business-profile.md")
Read(file_path="context/brand-guide.md")  # Skip if file doesn't exist

Do not create Sprint 1 tasks until all four reads are complete.
```

Apply same fix to TEAM.md validation step: convert "confirm you have loaded" to explicit Read() calls.

**Effort:** Small
**Risk:** Low

## Acceptance Criteria

- [ ] Context Validation Gate replaced with unconditional Read() calls (no checkbox introspection)
- [ ] TEAM.md Pre-Task Protocol validation step updated to explicit Read() calls or references the unconditional-read pattern
- [ ] All four context files listed (not just voice-dna and brand-guide)

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by agent-native-reviewer.
