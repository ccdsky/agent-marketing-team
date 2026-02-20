---
status: pending
priority: p3
issue_id: "063"
tags: [code-review, test-plan, documentation-clarity]
---

# Delegation Audit Protocol Bash Block Implies Non-Existent Automation

## Problem Statement

`docs/test-plan-v1.4.md` Delegation Audit Protocol (lines 86-99) wraps a manual verification process in a bash code block. The code block has comments describing what to check but no executable commands. This implies tooling that doesn't exist and creates cognitive overhead — a test runner reading the section asks "what command do I run?" before realizing it's a manual checklist. The audit is inherently manual (inspect session log files) and should be presented as prose.

## Findings

**Current (test-plan-v1.4.md, lines 86-99):**
```bash
# After Sprint 2 completes, check file ownership via session log
# Pass: drafts/ files created by Creative Specialist subagent Task() calls, not Campaign Lead
# Pass: All files in `edited/` were created by Quality Gate subagent Task() calls
# Fail: either file type created by Campaign Lead

# Evidence to look for in session log:
# - Task() call spawning creative-specialist before any Write() to drafts/
# ...
```

This is a bash comment block with no executable content. The content describes a manual inspection of session log files (JSONL format in ~/.claude/projects/).

**File:** `docs/test-plan-v1.4.md`, lines 86-99
**Identified by:** code-simplicity-reviewer

## Proposed Solution

Replace bash code block with prose:

```markdown
## Delegation Audit Protocol

After Sprint 2 completes, manually verify:

1. Locate the session log in `~/.claude/projects/[project-slug]/[session-id].jsonl`
2. Search for Write() tool calls to `drafts/` and `edited/` directories
3. Verify each Write() call is within a Task() subagent's context (not in the main session from Campaign Lead)
4. Verify Task() spawning calls for Creative Specialist appear before any Write() to `drafts/`
5. Verify Task() spawning calls for Quality Gate appear before any Write() to `edited/`

**Pass:** All specialist-directory writes occur within spawned subagent contexts
**Fail:** Campaign Lead (main session) makes Write() calls to `drafts/` or `edited/`
```

**Effort:** Trivial
**Risk:** None

## Acceptance Criteria

- [ ] Delegation Audit Protocol presented as numbered prose, not bash code block
- [ ] Audit steps describe the actual manual process accurately (JSONL session log inspection)
- [ ] No implied automation

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by code-simplicity-reviewer.
