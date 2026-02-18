---
status: pending
priority: p2
issue_id: "009"
tags: [code-review, skills, social-post, simplicity]
---

# social-post/SKILL.md Has Phantom Duplicate Steps

## Problem Statement

`social-post/SKILL.md` has 6 steps while every other skill has 4. Two of those steps are structural duplicates:

- **Step 3** ("Write Platform-Specific Format") — contains full structural templates for LinkedIn, Twitter, Substack
- **Step 4** ("Write the Draft") — says only "Write the full post following the chosen structure"

Step 4 adds zero information. The agent already knows what to do from Step 3. Similarly, Steps 5 and 6 split "Voice Check" and "ICP Relevance Check" into separate steps, while every other skill combines these into a single "Voice and ICP Pass."

The inconsistency makes social-post feel like it was written separately from the rest of the skills and will cause agents to waste a step doing the same work twice.

## Proposed Solution

Merge Steps 3 and 4 into one step: "Write Platform-Specific Draft."
Merge Steps 5 and 6 into one step: "Voice and ICP Pass."

Result: 4 steps, consistent with all other SKILL.md files.

**Effort:** Small — restructure step headers, no content change needed

## Acceptance Criteria

- [ ] social-post/SKILL.md has 4 steps matching the pattern of all other SKILL.md files
- [ ] No content is removed — only step boundaries merged

## Work Log

- 2026-02-18: Identified by simplicity-reviewer during PR review
