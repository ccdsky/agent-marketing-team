---
status: pending
priority: p2
issue_id: "043"
tags: [code-review, distribution-specialist, analytics, escalation, data-request]
---

# Distribution Specialist Analytics Task Has No Mechanism to Request User Data

## Problem Statement

`distribution-specialist.md` Analytics Workflow correctly notes that the agent cannot autonomously query GA4, ConvertKit, or ad platforms and needs the user to supply metrics. However, the Self-Claiming Analytics Tasks section tells the agent to claim analytics tasks (which become unblocked after publishing) without any instruction for immediately escalating to request the data. The agent will claim the task, have nothing to work with, and either generate placeholder data or stall.

## Findings

**distribution-specialist.md Analytics Workflow:**
> "You cannot autonomously query GA4, ConvertKit, or ad platforms. To generate a performance report, ask the user to paste in their metrics."

**distribution-specialist.md Self-Claiming Analytics Tasks:**
> "Look for: Tasks involving performance monitoring, analytics, reporting. Status: pending. blockedBy: empty (campaign published)."

No instruction to immediately escalate with a specific data request after claiming. The agent has no template for what to ask.

**Identified by:** agent-native-reviewer

## Proposed Solutions

### Option A: Add immediate escalation instruction to analytics claiming section (Recommended)

After claiming an analytics task, immediately escalate:

```
After claiming an analytics task, do not attempt to generate data. Escalate immediately using the escalation format:

"📊 Analytics Task Claimed: [task name]

To generate this report, I need you to paste in these metrics:
- **Email metrics** (from ConvertKit/Mailchimp): Open rate, click rate, unsubscribe rate per email in the sequence
- **Opt-in rate** (from your landing page tool): Visitors → form submissions
- **Traffic by source** (from GA4): Direct, organic, social, referral breakdown
- **Time period:** [dates of campaign]

Paste the data above and I'll generate the full performance report."
```

**Effort:** Small — add escalation template to analytics claiming section

## Acceptance Criteria

- [ ] After claiming an analytics task, Distribution Specialist immediately escalates with a specific data request
- [ ] The escalation message lists exactly what data is needed and where to find it
- [ ] The agent does not attempt to generate a report before data is supplied

## Work Log

- 2026-02-19: Identified during v1.3 code review by agent-native-reviewer
