---
status: pending
priority: p2
issue_id: "023"
tags: [code-review, distribution-specialist, analytics, external-data, capability-boundary]
---

# Distribution Specialist Analytics Section Claims Automation That Requires Unspecified External Access

## Problem Statement

`distribution-specialist.md` describes a detailed analytics workflow (lines 429-778) that requires:
- Google Analytics event data and goal completions
- ConvertKit or Mailchimp open/click rates
- Heatmap data from Hotjar
- A/B test results

None of these systems expose data to a Claude agent without MCP integrations or API access. The file names these platforms but never specifies how the agent accesses them. There are no tool calls for fetching analytics data — just report format templates.

The practical result: the Distribution Specialist can generate a performance report *template* and fill in numbers that the user pastes in, but cannot autonomously pull or monitor metrics. The weekly report described as automated is actually a formatting exercise.

This creates false expectations: Campaign Lead is told "Distribution Specialist tracks performance and reports weekly" — implying automation. A user relying on this will wait for a report that cannot be generated without their manual data input.

## Proposed Solution

Add a "Data Access" note to distribution-specialist.md analytics section:

```markdown
**Analytics Data Access**
Platform data (GA4, ConvertKit, Mailchimp, Hotjar) requires the user to paste raw metrics into the conversation, or configure MCP integrations (see README for MCP setup).

**If data is provided:** Use the report formats below to structure and analyze it.
**If data is not provided:** Ask the user to paste in the key metrics before generating the report.

Autonomous analytics pull is a v2.0 capability pending MCP configuration.
```

Also update CLAUDE.md's Distribution Specialist description to reflect this accurately.

**Effort:** Small — 1 clarifying note in distribution-specialist.md

## Acceptance Criteria

- [ ] distribution-specialist.md is explicit that analytics require user-provided data or MCP configuration
- [ ] No claim of autonomous metric retrieval without specifying the tool that enables it
- [ ] User knows what to provide when requesting a performance report

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
