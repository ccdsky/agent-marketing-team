---
status: pending
priority: p3
issue_id: "050"
tags: [code-review, TEAM.md, verbosity, duplication, CLAUDE.md]
---

# TEAM.md and CLAUDE.md Contain Duplicated/Non-Operational Sections — Agent Roles Table, Quality Standards, Quick Start

## Problem Statement

`TEAM.md` and `CLAUDE.md` each contain sections that duplicate the other or serve only human orientation purposes: the "Agent Roles (Quick Reference)" table in TEAM.md duplicates CLAUDE.md's routing table, "Quality Standards" appears verbatim in both files, and CLAUDE.md's "Quick Start" section restates examples already in the routing section.

## Findings

**TEAM.md "Agent Roles (Quick Reference)" table** (~12 lines) — duplicates CLAUDE.md routing table word-for-word. Agents read their own file, not a table of peers.

**TEAM.md "Campaign Learning Culture" section** (~22 lines) — duplicates campaign-lead.md's Campaign Retrospective section (which is the correct home since only Campaign Lead runs retrospectives).

**CLAUDE.md "Quality Standards"** (~9 lines) — identical to TEAM.md Quality Standards. TEAM.md is the authoritative source agents read.

**CLAUDE.md "Quick Start"** (~15 lines) — two example flows ("Write a LinkedIn post" and "Create a lead gen campaign") that restate the routing rules section's same examples.

**Total estimated removable: ~58 lines across two files**

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Remove duplicates, keep canonical versions (Recommended)

- **TEAM.md:** Remove "Agent Roles (Quick Reference)" table; remove "Campaign Learning Culture" section
- **CLAUDE.md:** Remove "Quality Standards" (TEAM.md is canonical); remove "Quick Start" section (routing rules already cover both examples)

**Effort:** Low — delete four sections across two files

## Acceptance Criteria

- [ ] No section appears in both TEAM.md and CLAUDE.md with identical content
- [ ] Campaign Learning Culture exists only in campaign-lead.md (the operational home)
- [ ] Quick Start examples removed from CLAUDE.md — routing rules are self-sufficient

## Work Log

- 2026-02-19: Identified during v1.3 code review by code-simplicity-reviewer
