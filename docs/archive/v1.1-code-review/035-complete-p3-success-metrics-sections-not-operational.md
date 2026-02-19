---
status: pending
priority: p3
issue_id: "035"
tags: [code-review, simplicity, success-metrics, agent-files, motivational-content]
---

# "Your Success Metrics" Closing Sections in Agent Files Are Motivational, Not Operational

## Problem Statement

Every agent file ends with a "Your Success Metrics" section listing 5-6 bullet points defining what success looks like for that role. Examples:
- research-specialist.md: "Research is actionable. Research is timely. Research informs strategy."
- quality-gate.md: "Quality maintained. Feedback is actionable. Consistency ensured."

These sections (~10 lines × 5 files = ~50 lines total) are useful for humans reading the documentation to understand intent. An LLM agent executing tasks does not consult a success metrics list during work — it follows the workflow steps defined above.

Loading this content into every conversation adds ~10 lines per agent with no behavioral impact.

## Proposed Solution

Remove the "Your Success Metrics" section from all five agent files. The closing line (`*You are the X. Do Y.*`) is sufficient as a role reminder.

If the success metrics serve a useful purpose for human readers, they belong in the README, not in agent instruction files.

**Effort:** Trivial — delete 5 sections (~50 lines total)

## Work Log

- 2026-02-18: Identified by code-simplicity-reviewer in second review pass
