---
status: pending
priority: p3
issue_id: "014"
tags: [code-review, retrospective, file-naming]
---

# Retrospective File Naming Inconsistency (-retro Suffix)

## Problem Statement

`retrospective.md` line 137 specifies:
```
knowledge/learnings/campaigns/retrospectives/[campaign-slug]-[YYYY-MM-DD]-retro.md
```

`campaign-lead.md` line 523 specifies the same path but without the `-retro` suffix:
```
knowledge/learnings/campaigns/retrospectives/[campaign-slug]-[date].md
```

An agent using campaign-lead.md will create files that don't match the naming convention in retrospective.md, making them harder to grep by pattern.

Additionally, `retrospective.md` Step 1 says to "collect the Distribution Specialist's Week 1 analytics report" but doesn't specify the path. `distribution-specialist.md` saves analytics to `knowledge/feedback/analytics/[campaign-slug]-retrospective-[date].md`. The Campaign Lead running retrospective.md Step 1 won't know where to find the analytics input.

## Fix

1. Update `campaign-lead.md` retrospective file path to include `-retro` suffix
2. Add the analytics file path to `retrospective.md` Step 1:
   ```
   Distribution Specialist's analytics report: knowledge/feedback/analytics/[campaign-slug]-retrospective-[date].md
   ```

**Effort:** Small — 2 line edits

## Work Log

- 2026-02-18: Identified by agent-native-reviewer during PR review
