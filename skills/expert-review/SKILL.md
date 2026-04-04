---
name: expert-review
description: Spawn 3-5 specialist reviewers to analyze a draft marketing asset from different expert perspectives, then synthesize into a prioritized revision list.
---

# Expert Review Skill

## When to Use

Spawn 3-5 specialized review agents to analyze a draft marketing asset from different expert perspectives simultaneously. Synthesizes parallel feedback into a prioritized revision list with specific changes and estimated impact. Invoke when a Sprint 2 draft is complete and ready for multi-perspective review before the Quality Gate, or when the user requests "expert review" on a specific asset.

**Do NOT invoke when:** Sprint 1 sketches or copy outlines (too early), simple social posts or short-form content (overhead not worth it), brief is still unclear (fix the brief first).

**Exception — Lead Magnet Strategy concept briefs:** These are Sprint 1 outputs but are ready for expert review. Use the "Lead Magnet Strategy" panel. Run at end of Sprint 1 before checkpoint presentation.

---

## Required Inputs

**Standalone invocation:** Ask for the asset file path and asset type before proceeding. Then read the asset.

**Called by Creative Specialist (campaign mode):** Call `TaskGet(taskId="[drafting-task-ID from task description]")` to read `metadata["deliverable"]` (draft file path). Then read the draft.

Before starting, always read:
- Draft asset file path (e.g., `output/campaigns/[slug]/drafts/landing-page-draft.md`)
- Asset type (landing page, lead magnet, email sequence, blog post, lead magnet strategy concept brief)
- Campaign brief if available: `output/campaigns/[slug]/campaign-brief.md`
- `context/icp.md` — Who the asset targets
- `context/voice-dna.md` — Voice standard to evaluate against

---

## Procedure

**Mode Check first:** If Task tool is available, spawn experts as parallel subagents (Steps 1-4). If Task tool is unavailable, run each expert sequentially inline — open with "As a [Expert Name], I'm evaluating this [asset type]..." and apply their criteria. Output format is identical either way.

1. **Select expert panel** based on asset type. Each asset type has a predefined panel of 3-5 specialists. For full panel definitions and scored dimensions per expert, see `references/methodology.md`.

2. **Spawn expert agents in parallel** (or run sequentially in simple mode). Each expert receives the draft, their specific evaluation framework, the ICP profile, and a standardized output format. Expand each expert's criteria into 4-6 specific scored dimensions before writing the prompt. For the agent prompt template, see `references/methodology.md`.

3. **Collect and synthesize.** Confirm response count: 5/5 = full weights; 3-4/5 = normalize weights (label "REDUCED CONFIDENCE"); <3/5 = do not synthesize, flag incomplete. Identify: consensus strengths (safe — don't change), consensus issues (highest priority), conflicting opinions. Conflict resolution: favor the expert whose lens aligns with the asset's primary job. Apply score weighting table by asset type. For partial response rules and full weighting tables, see `references/methodology.md`.

4. **Build prioritized revision list.** Three tiers: Must fix before Quality Gate (consensus issues + any HIGH priority), Should fix if possible (single-expert with clear impact), Nice to have (LOW priority, subjective). Each item: specific change + section/line reference + expected impact.

---

## Output

Save to: `output/campaigns/[campaign-slug]/reviews/expert-review-[asset-type]-[date].md`

Required sections: Aggregate Score table, Consensus Strengths, Must Fix Before Quality Gate, Should Fix, Nice to Have, Conflicting Opinions table, Creative Specialist Revision Checklist.

For full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/reviews/expert-review-[asset-type]-[YYYY-MM-DD].md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "creative-specialist"
})
```

---

## Example

**Scenario:** Expert review of a landing page draft for Acme CI/CD — a CI/CD platform for mid-market engineering teams.

**Panel selected:** Landing Page panel — Conversion Copywriter, CLOSURE Framework Auditor, ICP Relevance Reviewer, Voice Matcher, B2B Buyer Psychology Reviewer.

**Aggregate Score: 6.8/10** (weighted)

| Expert | Score | Primary finding |
|--------|-------|-----------------|
| Conversion Copywriter | 6/10 | Headline names the product category, not the buyer's pain |
| ICP Relevance Reviewer | 7/10 | Pain points are right but vocabulary is vendor-speak |
| Voice Matcher | 8/10 | Consistent with voice-dna.md — direct and jargon-light |
| CLOSURE Auditor | 7/10 | Social proof section present but logos only, no outcomes |
| B2B Psychology Reviewer | 6/10 | No career-risk framing; switching anxiety unaddressed |

**Must Fix Before Quality Gate:**

Issue 1: Headline doesn't speak to pain
- Flagged by: Conversion Copywriter, ICP Relevance Reviewer
- Location: Hero section, H1
- Problem: "Acme CI/CD — Enterprise-Grade Pipelines" names the product, not the buyer's trigger
- Suggested fix: Rewrite to lead with maintenance burden — e.g., "Stop Maintaining Jenkins. Ship Faster."
- Expected impact: Higher initial engagement; ICP recognizes their situation immediately

**Creative Specialist Revision Checklist:**
- [ ] Rewrite H1 to lead with buyer pain, not product category
- [ ] Replace logo-only social proof with outcome-based testimonials
- [ ] Add switching anxiety handler in the objections section

---

## Quality Gate

Before marking complete:

- [ ] Correct expert panel selected for asset type (not generic reviewers)
- [ ] Each expert prompt includes specific scored criteria (not vague "evaluate this")
- [ ] Consensus strengths identified — these are safe, do not flag for change
- [ ] Consensus issues clearly distinguished from single-expert opinions
- [ ] Conflicts resolved with explicit recommendation citing which expert's lens takes precedence
- [ ] Revision list prioritized: must-fix / should-fix / nice-to-have (not one flat list)
