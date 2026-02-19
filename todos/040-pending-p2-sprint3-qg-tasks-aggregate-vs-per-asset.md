---
status: pending
priority: p2
issue_id: "040"
tags: [code-review, campaign-lead, sprint-planning, quality-gate, sprint3, metadata]
---

# Sprint 3 Quality Gate Task Structure Inconsistent — Aggregate vs Per-Asset Creates Metadata Gap

## Problem Statement

`campaign-lead.md` Sprint 3 creates three separate Quality Gate tasks (one per asset), while `sprint-planning.md` creates one aggregated "Final editorial review" task. When Quality Gate uses a single aggregated task, it cannot write per-asset deliverable paths to separate metadata records — Distribution Specialist then cannot find individual edited file paths for each asset.

## Findings

**campaign-lead.md Sprint 3 example:**
```
[19] Edit lead magnet (Quality Gate, 1h) - BLOCKED_BY: [16]
[20] Edit landing page (Quality Gate, 1h) - BLOCKED_BY: [17]
[21] Edit email sequence (Quality Gate, 2h) - BLOCKED_BY: [18]
```

**sprint-planning.md Sprint 3 tasks:**
```
TaskCreate: "[S3] Quality Gate — Final editorial review"
```

When one aggregated task is used, `metadata["deliverable"]` can only hold one path. Distribution Specialist needs individual edited file paths for each asset. Per-asset tasks cleanly separate metadata and are already the correct model shown in campaign-lead.md.

**Identified by:** architecture-strategist

## Proposed Solutions

### Option A: Update sprint-planning.md Sprint 3 to create per-asset QG tasks (Recommended)

Replace the single aggregated QG task with:
```
TaskCreate: "[S3] Quality Gate — Edit lead magnet"
TaskCreate: "[S3] Quality Gate — Edit landing page"
TaskCreate: "[S3] Quality Gate — Edit email sequence"
```

Each task carries its own `metadata["deliverable"]` pointing to the respective edited file.

**Effort:** Small — edit sprint-planning.md Sprint 3 task list

## Acceptance Criteria

- [ ] sprint-planning.md Sprint 3 creates per-asset Quality Gate tasks (not one aggregated task)
- [ ] Each QG task can carry independent metadata with its edited file path
- [ ] Distribution Specialist can find individual edited file paths per asset

## Work Log

- 2026-02-19: Identified during v1.3 code review by architecture-strategist
