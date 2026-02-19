---
status: complete
priority: p1
issue_id: "004"
tags: [code-review, blocking, expert-review, prompt-template]
---

# Expert Review Step 2 Subagent Prompt Template Has Empty Criteria Placeholder

## Problem Statement

`expert-review/SKILL.md` Step 2 provides a subagent prompt template with `[specific criteria for this expert]` as a placeholder. No actual criteria are filled in. Subagents spawned with this template will receive no evaluation rubric and will improvise, producing inconsistent expert reviews that defeat the purpose of a structured panel.

The scoring weights table (Step 5) defines how to weight each expert's output but doesn't feed back into Step 2's prompt template — the criteria gap means subagents will produce assessments that may not map to the scoring dimensions.

## Findings

**expert-review/SKILL.md Step 2 prompt template:**
```
You are [Expert Name], a [Expert Description].

Review this [asset type]:

[Asset content]

Evaluate against [specific criteria for this expert].

Score each criterion 1-10.
Provide specific, actionable feedback.
```

The `[specific criteria for this expert]` placeholder is never populated. For comparison, the scoring weights table in Step 5 defines concrete dimensions (e.g., "Conversion Copywriter: headline strength, benefit clarity, objection handling") — these should be the criteria in Step 2.

**Identified by:** agent-native-reviewer, architecture-strategist

## Proposed Solutions

### Option A: Pre-populate criteria in Step 2 per expert per asset type (Recommended)

Replace the generic template with asset-specific expert prompts. For example, for landing pages:

**Conversion Copywriter prompt:**
```
You are a Conversion Copywriter specializing in B2B SaaS landing pages.

Review this landing page:
[Asset content]

Evaluate these criteria (score each 1-10):
1. Headline strength — Does it speak to the primary pain point immediately?
2. Benefit clarity — Are benefits concrete and specific (not vague)?
3. Objection handling — Does the page preempt the top 3 buyer objections?
4. CTA strength — Is the call to action clear, specific, and low-friction?
5. Social proof — Is proof credible and specific?

Provide specific, actionable feedback for each criterion.
```

Include one pre-populated prompt block per expert per asset type in the skill file.

**Pros:** Subagents receive complete, unambiguous instructions; output maps directly to scoring weights
**Cons:** Increases skill file size significantly; criteria must be maintained per asset type
**Effort:** Medium — requires writing criteria for 5 experts x 4 asset types = 20 prompt blocks

### Option B: Define criteria in a lookup table, reference from template

Create a "Criteria Reference" section in expert-review/SKILL.md that lists evaluation dimensions per expert role. The template references: "Apply criteria from the [Expert Name] row in the Criteria Reference table."

**Pros:** More maintainable; single source of truth; template stays clean
**Cons:** Requires agent to correctly look up and apply table — indirect reference increases failure risk
**Effort:** Medium

## Acceptance Criteria

- [ ] No `[placeholder]` text remains in any subagent prompt template in expert-review/SKILL.md
- [ ] Each expert receives evaluation criteria that map to their row in the scoring weights table
- [ ] A subagent spawned from the template can produce a scored review without additional context

## Work Log

- 2026-02-18: Identified during v1.2 PR review by agent-native-reviewer
