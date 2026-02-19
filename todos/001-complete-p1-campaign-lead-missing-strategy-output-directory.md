---
status: complete
priority: p1
issue_id: "001"
tags: [code-review, blocking, file-paths, campaign-lead]
---

# Campaign Lead mkdir Missing `strategy/` Subdirectory

## Problem Statement

The Campaign Lead's directory creation command does not include `strategy/`, but two new skills write their output there:
- `positioning-angles/SKILL.md` saves to `output/campaigns/[slug]/strategy/positioning-angles-[date].md`
- `lead-magnet-strategy/SKILL.md` saves to `output/campaigns/[slug]/strategy/lead-magnet-concept-[date].md`

If Campaign Lead scaffolds a campaign directory without `strategy/`, agents executing these skills will fail with a "directory does not exist" error when trying to save output.

## Findings

The `campaign-lead.md` directory creation section includes `drafts/`, `edited/`, `ready/`, `research/`, `reviews/`, and `analytics/` — but not `strategy/`. The two new strategy skills write to `strategy/` subdirectory but no agent creates it first.

**Location:** `.claude/agents/campaign-lead.md` — campaign directory scaffolding section

**Affected skills:**
- `.claude/skills/positioning-angles/SKILL.md` — Step 6 output path
- `.claude/skills/lead-magnet-strategy/SKILL.md` — Step 9 output path

**Identified by:** architecture-strategist, agent-native-reviewer

## Proposed Solutions

### Option A: Add `strategy/` to Campaign Lead mkdir (Recommended)

Update the `mkdir -p` command in campaign-lead.md to include the strategy subdirectory:

```
mkdir -p output/campaigns/[slug]/{research,strategy,drafts,reviews,edited,ready,analytics}
```

**Pros:** Single fix, correct place (Campaign Lead owns scaffolding), consistent with existing pattern
**Cons:** None
**Effort:** Small — one-line change

### Option B: Have each strategy skill create its own directory

Add `mkdir -p` at the start of each strategy skill before writing output.

**Pros:** Skills are self-contained
**Cons:** Inconsistent with existing pattern where Campaign Lead owns scaffolding; redundant across skills
**Effort:** Small per skill, but adds complexity

## Acceptance Criteria

- [ ] `strategy/` appears in Campaign Lead directory scaffolding command
- [ ] `positioning-angles/SKILL.md` output path resolves to an existing directory during campaign execution
- [ ] `lead-magnet-strategy/SKILL.md` output path resolves to an existing directory during campaign execution

## Work Log

- 2026-02-18: Identified during v1.2 PR review by architecture-strategist and agent-native-reviewer
