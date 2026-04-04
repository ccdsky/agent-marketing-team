# Campaign Templates Reference

Used by Campaign Lead. Read this file when creating campaign briefs, sprint tasks, or checkpoint presentations.

---

## Campaign Brief Template

**File:** `output/campaigns/[campaign-slug]-[YYYY-MM]/campaign-brief.md`

```markdown
# Campaign: [Name]

## Goal & Success Metrics
[What we're trying to achieve, how we measure it]

## Target Audience
[ICP segment, specific pain points]

## Timeline
- Sprint 1: [dates] - Plan & Sketch
- Sprint 2: [dates] - Refine & Deepen
- Sprint 3: [dates] - Execute & Ship
- Launch: [date]

## Asset Plan
- [Asset 1]: [Purpose, format, key message]
- [Asset 2]: [Purpose, format, key message]
...

## Key Research Questions
[What we need to learn before we can execute]

## Strategic Decisions Made
[Decisions made and why - prevents re-litigating]

## Open Questions
[Unresolved items that need the user's input]

## Token Budget Estimate
- Sprint 1: [X]K tokens
- Sprint 2: [Y]K tokens
- Sprint 3: [Z]K tokens
- Total: ~[Total]K tokens
```

---

## Sprint Task-Creation Examples

### Sprint 1 Task Example

```
TaskCreate(
  subject="[S1] Research: Target audience pain points",
  description="Interview research + forum mining for developer pain points with CLI tools. Focus on: discoverability, onboarding, learning curve. Deliverable: knowledge/research/dev-cli-pain-points-[date].md",
  activeForm="Researching developer pain points"
)
```

### Sprint 1 Dependency Wiring

```
TaskUpdate(taskId="[S1-3]", addBlockedBy=["[S1-1]", "[S1-2]"])  # positioning needs both research tasks
TaskUpdate(taskId="[S1-4]", addBlockedBy=["[S1-3]"])              # structure needs positioning
TaskUpdate(taskId="[S1-5]", addBlockedBy=["[S1-4]"])              # metrics need structure
TaskUpdate(taskId="[S1-6]", addBlockedBy=["[S1-5]"])              # checkpoint needs metrics
```

### Sprint 2 Draft + Expert Review Wiring

```
# 1. Create the drafting task — note the real ID returned
TaskCreate(subject="[S2] Draft lead magnet: [title]", description="...")
# → returns taskId: 42

# 2. Embed the real ID in the expert review task description
TaskCreate(
  subject="[S2] Expert review: Lead magnet",
  description="Review the lead magnet draft. Drafting task ID: 42. Read skills/expert-review/SKILL.md for the framework.",
  activeForm="Running expert review"
)
```

Do not use planning labels (like `[S2-2]`) as task IDs — they are not resolvable by `TaskGet`.

---

## Sprint Checkpoint Presentation Formats

### Sprint 1 Checkpoint

```markdown
## Sprint 1 Checkpoint: [Campaign Name]

### Research Synthesis
[3-5 key insights from research tasks]

### Positioning Angle Options
[Present 3-5 positioning angles with rationale]

**Recommended:** [Which angle and why]

### Campaign Structure (if recommended angle selected)
- [Asset 1]: [Purpose]
- [Asset 2]: [Purpose]
...

### Success Metrics
[How we'll measure campaign effectiveness]

### Token Budget Estimate
- Sprint 1: [X]K tokens (spent)
- Sprint 2: [Y]K tokens (estimated)
- Sprint 3: [Z]K tokens (estimated)
- **Total: ~[Total]K tokens**

### Timeline
- Sprint 1: Complete ([X] days)
- Sprint 2: [Y] days (if approved)
- Sprint 3: [Z] days
- **Total: [Total] days to launch**

### Decision Needed
1. Which positioning angle?
2. Are proposed assets the right mix?
3. Any research gaps to address in Sprint 2?
4. Approve Sprint 2 kickoff?
```

### Sprint 2 Checkpoint

```markdown
## Sprint 2 Checkpoint: [Campaign Name]

### Drafts Completed
- ✅ Lead magnet: [Brief description, file path]
- ✅ Landing page: [Brief description, file path]
- ✅ Email sequence: [Brief description, file path]

### Expert Review Synthesis
**What's working:**
- [Consensus strengths from expert reviews]

**What needs work:**
- [Consensus issues from expert reviews]

**Specific recommendations:**
- [Concrete changes suggested]

### Self-Assessment
[Your honest evaluation of draft quality]

### Suggested Revisions
[Priority changes for Sprint 3]

### Decision Needed
1. Are drafts on the right track?
2. What specific revisions for Sprint 3?
3. Approve Sprint 3 kickoff?
```

### Sprint 3 Pre-Launch Summary

```markdown
## Ready to Launch: [Campaign Name]

✅ All assets revised and approved by Quality Gate
✅ Platform formatting ready

**Assets queued for publish:**
- Lead magnet: [path]
- Landing page: [path]
- Email sequence: [path]

**Reply "go" to publish**, or flag any last-minute changes.
```
