---
status: pending
priority: p2
issue_id: "016"
tags: [code-review, keyword-research, fallback, data-sources]
---

# Keyword Research Step 2 Has No Fallback When Sales Call Transcripts Unavailable

## Problem Statement

`keyword-research/SKILL.md` Step 2 lists "sales call transcripts" as the #1 priority source for extracting ICP language. Most users of this system won't have sales call transcripts, CRM notes, or customer interview recordings available as files. The skill provides no fallback path — no instruction on what to do when Source #1 (and #2 and #3) are unavailable before escalating.

An agent following this step will either fabricate ICP language from training priors or stall waiting for input, with no defined behavior.

## Findings

**keyword-research/SKILL.md Step 2 sources:**
1. Sales call transcripts (priority 1) — typically unavailable
2. Support ticket themes (priority 2) — typically unavailable  
3. Customer interview recordings (priority 3) — typically unavailable
4. Voice of customer surveys (priority 4) — sometimes available
5. ICP profile from context/ (fallback)

The skill notes "ICP profile from context/" as a fallback but doesn't provide explicit fallback language — the agent may not recognize it as "use this when all else fails."

**Identified by:** code-simplicity-reviewer

## Proposed Solutions

### Option A: Make fallback explicit and add web-based alternatives (Recommended)

Restructure Step 2 as:

```
## Step 2: ICP Language Mining

**If any of these are available, use them (highest quality):**
- Sales call transcripts (file path provided by user)
- Support ticket themes (CRM export or file)
- Customer interview notes

**If not available (most common case):**
1. Read `context/icp.md` for documented pain points and language
2. Mine Reddit, forums, Slack communities for ICP language:
   WebSearch(query="[ICP job title] [pain point] reddit")
3. Mine review sites for competitor products:
   WebFetch(url="producthunt.com/products/[competitor]/reviews")
4. Use context/business-profile.md to understand customer outcomes

**Escalate only if:** context/icp.md is missing AND no web sources have relevant discussions.
```

**Pros:** Executable in all contexts; ICP profile is always available after setup; web mining provides real language
**Cons:** Web mining ICP language is lower quality than direct customer input — but available
**Effort:** Small

### Option B: Add single fallback note at end of source list

Add: "If none of the above are available, proceed using context/icp.md as your ICP language source. Web mining from forums and review sites (Step 3 approach) can supplement."

**Pros:** Minimal change; preserves existing structure
**Cons:** Less explicit; agent must infer when to use fallback
**Effort:** Trivial

## Acceptance Criteria

- [ ] An agent with no sales transcripts has a complete, executable path through Step 2
- [ ] context/icp.md is explicitly named as a fallback source
- [ ] The skill does not require unavailable internal data to proceed

## Work Log

- 2026-02-18: Identified during v1.2 PR review by code-simplicity-reviewer
