---
status: pending
priority: p3
issue_id: "052"
tags: [code-review, campaign-lead, keyword-research, monitoring, estimates, precision]
---

# Wall-Clock Monitoring Thresholds and Pipeline Estimate Precision Are Inapplicable to LLM Execution

## Problem Statement

Two separate files contain precision-implying constructs that don't work in an LLM agent context:

1. `campaign-lead.md` Progress Monitoring uses clock-time thresholds ("in_progress > 24 hours") that agents cannot autonomously monitor — they only check tasks when invoked.
2. `keyword-research/SKILL.md` pipeline impact table format implies per-row estimates are additive, which compounds uncertainty in ways not flagged.

## Findings

**campaign-lead.md Progress Monitoring:**
> "Tasks in_progress > 24 hours → Check in with agent
> Tasks in_progress > 48 hours → Consider reassignment
> Tasks blocked > 72 hours → Escalate"

LLM agents don't have continuous monitoring. They check when invoked. The 24/48/72-hour threshold implies autonomous polling that doesn't exist.

**keyword-research/SKILL.md pipeline table:**
```
| [keyword] | [X] | [X% est.] | [X est.] | [Strong/Medium] |
```
The table structure invites summing rows — but the same searcher may appear across keyword entries, making the figures non-additive. No note warns against this.

**Identified by:** architecture-strategist, code-simplicity-reviewer

## Proposed Solutions

### Fix 1: Replace clock-time thresholds with invocation-relative triggers

> "Each time Campaign Lead is invoked, run TaskList(). Flag any task in_progress with no recent activity (no status change since last invocation). If stuck: reassign. If still stuck next invocation: escalate."

### Fix 2: Add anti-sum note to pipeline table

Below the Pipeline Impact table in keyword-research/SKILL.md output template:
> "Note: Do not sum rows — traffic estimates are not additive (the same searcher may appear across multiple keyword entries). Use the total directional estimate only."

**Effort:** Small — two targeted edits

## Acceptance Criteria

- [ ] campaign-lead.md Progress Monitoring uses invocation-relative (not wall-clock) thresholds
- [ ] keyword-research/SKILL.md pipeline table includes a note warning against row summation

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist and code-simplicity-reviewer
