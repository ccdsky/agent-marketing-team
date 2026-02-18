---
status: pending
priority: p3
issue_id: "030"
tags: [code-review, repurpose, newsletter, skills, sprint-planning, integration]
---

# Repurpose and Newsletter Skills Are Orphaned From Campaign Templates and Sprint Model

## Problem Statement

`repurpose/SKILL.md` and `newsletter/SKILL.md` are well-written skills but are never referenced in:
- Any campaign template (lead-gen-campaign.md, product-launch.md, content-sprint.md)
- Any sprint-planning.md task example
- Any campaign-lead.md flow description

An agent executing a campaign would never know to invoke these skills unless explicitly asked. They cannot self-discover them from the campaign structure.

Repurposing is a natural Sprint 3 distribution activity. Newsletter is a natural content-sprint deliverable. Their absence from the sprint machinery means they're only accessible via explicit user requests.

## Proposed Solution

Add brief integration notes to sprint-planning.md:

```markdown
**Sprint 3 optional tasks** (include if campaign brief calls for them):
- `TaskCreate: "[S3] Repurpose — [asset] for [platform]"` — if social promotion is planned
- `TaskCreate: "[S3] Newsletter — [topic]"` — if campaign includes a newsletter touchpoint
```

Similarly, reference newsletter in content-sprint.md's campaign asset plan.

**Effort:** Small — 4-6 lines added to sprint-planning.md, 1 line in content-sprint.md

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
