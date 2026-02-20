# Campaign Retrospective Workflow

Used by Campaign Lead after every campaign ships. Extracts learnings into the knowledge base so every future campaign benefits.

---

## When to Run

Run a retrospective after:
- Campaign completes Sprint 3 (primary trigger)
- Campaign is cancelled or paused mid-sprint (partial retro)
- A single-asset run that produced notable insights

Even quick campaigns deserve a quick retro. 10 minutes of documentation compounds into hours saved later.

---

## Retrospective Process

### Step 1: Gather Evidence

Before answering the 5 questions, collect:
- Task completion times vs estimates
- Quality Gate scores from each asset
- Distribution Specialist's Week 1 analytics report: `knowledge/feedback/analytics/[campaign-slug]-retrospective-[date].md`
- Any escalations or blockers that occurred
- Sprint 1 checkpoint: what did user approve vs revise?
- Sprint 2 checkpoint: what feedback was given?

**Two-phase completion note:** When the retrospective runs immediately after Sprint 3 (before launch), the analytics report won't exist yet. Collect all available evidence and answer Questions 1–4 from process observations. For Question 5 (performance patterns), note that analytics are pending and revisit after Week 1 data arrives. Do not wait for analytics to answer process questions — they are answerable now.

### Step 2: Answer the 5 Retrospective Questions

```markdown
## Campaign Retrospective: [Campaign Name]
**Date:** [YYYY-MM-DD]
**Campaign slug:** [campaign-slug-YYYY-MM]

### 1. What worked better than expected?
[Specific things — with evidence. Not "everything went well."]

Examples of good answers:
- "Research phase took 4 hours vs 8 estimated because customer language was well-documented in the research package"
- "Email sequence open rates 47% vs 30% target — hook formula from social-post skill worked for email too"

### 2. What didn't work?
[Be honest. Evidence-based.]

Examples:
- "Landing page needed 3 revision cycles because voice-dna.md lacked examples of how owner writes CTA copy"
- "Sprint 1 checkpoint was too vague — user approved direction but feedback showed misalignment on tone"

### 3. Where did we waste time or tokens?
[Inefficiencies to eliminate]

Examples:
- "Researched competitor SEO rankings — not useful for this campaign type"
- "Quality Gate reviewed same asset twice because Creative Specialist hadn't read the first review"

### 4. What would we do differently?
[Process improvements for next campaign]

Examples:
- "Add a 'voice sample review' step before drafting where we confirm voice-dna applies to this asset type"
- "Create an email-sequence-specific positioning brief before drafting (not just the campaign brief)"

### 5. What patterns should we codify?
[Specific learnings worth saving to the knowledge base]

Examples:
- "Hook formula for LinkedIn posts: [specific pattern] — 3x better engagement"
- "Lead magnets under 5 pages convert better than comprehensive guides for this ICP"
```

### Step 3: Extract and Save Learnings

For each pattern identified in Question 5, save to the appropriate category:

**Category map:**
```
Timing patterns → knowledge/learnings/campaigns/timing/
Asset combinations → knowledge/learnings/campaigns/asset-mix/
Agent coordination insights → knowledge/learnings/campaigns/coordination/
Task breakdown that worked → knowledge/learnings/campaigns/task-patterns/
Quality gate catches → knowledge/learnings/campaigns/quality-gates/
Full retrospectives → knowledge/learnings/campaigns/retrospectives/
```

**Learning file format:**
```markdown
---
date: YYYY-MM-DD
campaign: [campaign-slug]
category: [timing|asset-mix|coordination|task-patterns|quality-gates]
tags: [relevant-tags]
---

# [Pattern Name]

## What We Learned
[Specific, evidence-based insight]

## When to Apply
[Conditions under which this pattern applies]

## How to Apply
[Specific implementation guidance]

## Evidence
[Data or observation that supports this]

## Counter-evidence
[When this pattern might not apply]
```

### Step 4: Flag Agent Improvements for Human Review

If the retrospective reveals a consistent issue with how an agent operates, **do not edit agent files directly**. Document the suggested improvement in the retrospective file and flag it for human review:

```markdown
## Recommended Agent Updates

**human_review_required: true**

| Agent File | Section | Suggested Change | Evidence |
|------------|---------|-----------------|----------|
| [agent-name].md | [Section name] | [What to add/change] | [Data or observation from this campaign] |
```

The human reviews these suggestions and applies approved changes. This prevents incorrect edits from compounding into systemic issues.

### Step 5: Create Archive Entry

Write a summary archive entry so future campaigns can discover this one via Grep:

```
Write(
  file_path="knowledge/archive/[campaign-slug]-[YYYY-MM-DD].md",
  content="# Campaign Archive: [name]\n\n**Completed:** [date]\n**Goal:** [original goal]\n**Result:** [actual result]\n**Campaign files:** output/campaigns/[slug]/\n\n[2-3 sentence summary of key outcomes and assets]"
)
```

Note: Campaign files in `output/campaigns/[slug]/` remain in place. The archive entry provides a searchable record in the knowledge base.

---

## Retrospective File Location

Save the full retrospective to:
`knowledge/learnings/campaigns/retrospectives/[campaign-slug]-[YYYY-MM-DD]-retro.md`

---

## Lightweight Retro (Single Assets)

For single-asset requests (one LinkedIn post, one newsletter issue), a full retro is overkill. Instead, Campaign Lead or Creative Specialist adds a brief note to the output file:

```markdown
## Post-Task Note
- What worked: [one sentence]
- What to do differently: [one sentence]
- Pattern worth saving: [Yes/No — if yes, file it]
```

Only file a learning if it would change how the next similar task is done.
