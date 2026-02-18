# Sprint Planning Workflow

Used by Campaign Lead to structure any campaign into three sprints with checkpoints.

---

## When to Use

Invoke this workflow whenever Campaign Lead receives a multi-asset campaign request (lead generation, product launch, content sprint). Single-asset requests don't need full sprint planning — use Simple Mode instead.

---

## Sprint Structure

| Sprint | Goal | Human Checkpoint |
|--------|------|-----------------|
| **Sprint 1: Plan & Sketch** | Validate strategy before building anything | Yes — user approves direction |
| **Sprint 2: Refine & Deepen** | First drafts + expert review | Yes — user approves creative |
| **Sprint 3: Execute & Ship** | Polish and publish | No — executing approved direction |

---

## Sprint 1: Plan & Sketch

**Goal:** Get the strategy right before burning tokens on assets.

**Tasks to create:**

```
TaskCreate: "Research — [Topic]: [target audience pain points]"
TaskCreate: "Research — [Topic]: competitor positioning"
TaskCreate: "Research — [Topic]: customer language mining"
TaskCreate: "Positioning — Generate 3-5 angles"
TaskCreate: "Campaign structure — Sketch asset plan and timeline"
TaskCreate: "Metrics — Define success criteria"
TaskCreate: "Sprint 1 Checkpoint — Compile and present to user"
```

**Dependency chain:**
```
Research tasks → (all must complete) → Positioning → Campaign Structure → Checkpoint
```

**Sprint 1 checkpoint deliverables:**
- Market research synthesis (1 page)
- 3-5 positioning angle options (with brief rationale for each)
- Campaign structure sketch (assets, sequence, timeline)
- Success metrics definition
- Token budget estimate for Sprint 2

**Checkpoint format:**
```markdown
## Sprint 1 Checkpoint: [Campaign Name]

### Market Context
[2-3 key findings from research]

### Positioning Options
**Option A:** [angle] — [brief why it works]
**Option B:** [angle] — [brief why it works]
**Option C:** [angle] — [brief why it works]

### Recommended Direction
[Which option and why]

### Campaign Structure
[What assets, in what order, for what goal]

### Success Metrics
- Primary: [metric + target]
- Secondary: [metric + target]

### Decision Needed
Which positioning angle? Any adjustments to asset plan?
```

---

## Sprint 2: Refine & Deepen

**Goal:** Create first drafts. Expect feedback. Don't expect to ship from Sprint 2.

**Only create Sprint 2 tasks after user approves Sprint 1 direction.**

**Tasks to create (based on approved asset plan):**

```
TaskCreate: "Draft — Lead magnet: [title]"
TaskCreate: "Draft — Landing page: [campaign name]"
TaskCreate: "Draft — Email sequence: [N] emails"
TaskCreate: "Expert review — Lead magnet (Creative Specialist runs Task tool subagents)"
TaskCreate: "Expert review — Landing page (Creative Specialist runs Task tool subagents)"
TaskCreate: "Quality Gate — Review all Sprint 2 drafts"
TaskCreate: "Sprint 2 Checkpoint — Compile drafts + expert reviews + present"
```

**Dependency chain:**
```
All drafts → Expert reviews → Quality Gate review → Checkpoint
(Drafts can run in parallel)
(Expert review for each asset can run after that asset is drafted)
```

**Sprint 2 checkpoint deliverables:**
- All draft assets
- Expert review synthesis for each asset
- Quality Gate assessment
- Specific feedback requested from user

**Checkpoint format:**
```markdown
## Sprint 2 Checkpoint: [Campaign Name]

### Drafts Ready for Review
- Lead magnet: [link/path]
- Landing page: [link/path]
- Email sequence: [link/path]

### Expert Review Highlights
[Key findings from expert agents — what's strong, what needs work]

### Quality Gate Assessment
[Voice match scores, clarity issues, recommended revisions]

### Feedback Needed
[Specific questions for user — max 3]

### Sprint 3 Preview
[What will change based on anticipated feedback]
```

---

## Sprint 3: Execute & Ship

**Goal:** Polish, publish, track. No checkpoint needed — this executes approved direction.

**Only create Sprint 3 tasks after user provides feedback on Sprint 2.**

**Tasks to create:**

```
TaskCreate: "Revise — Lead magnet (based on Sprint 2 feedback)"
TaskCreate: "Revise — Landing page"
TaskCreate: "Revise — Email sequence"
TaskCreate: "Quality Gate — Final editorial review"
TaskCreate: "Distribution — Format for web"
TaskCreate: "Distribution — Set up email sequence in platform"
TaskCreate: "Distribution — Publish campaign"
TaskCreate: "Distribution — Set up analytics tracking"
TaskCreate: "Distribution — Week 1 performance report"
```

**Dependency chain:**
```
Revisions (parallel) → Quality Gate → Distribution tasks (parallel) → Analytics
```

---

## Task Granularity Guidelines

**Right size:** 30 minutes to 3 hours per task.

| Too small (combine) | Right size | Too large (split) |
|--------------------|-----------|------------------|
| "Create output directory" | "Research competitor positioning" | "Build entire campaign" |
| "Read voice-dna" | "Draft landing page hero section + body" | "Write all emails" |
| "Update task status" | "Quality Gate review — lead magnet" | "Research everything" |

**Rule:** A task should produce one concrete, handoff-ready deliverable.

---

## Self-Claiming Protocol

Specialists self-claim tasks in order:
1. Check TaskList for tasks with no `blockedBy` dependencies
2. Claim with: `TaskUpdate(taskId="[ID]", status="in_progress", owner="[agent-name]")`
3. Execute the task
4. Complete with: `TaskUpdate(taskId="[ID]", status="completed")`
5. Add brief comment on what was produced and where it's saved

**Campaign Lead:** Monitor task list. Unblock dependencies. Present checkpoints. Escalate blockers.
