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

## Task Naming Convention

**Prefix all tasks with their sprint:** `[S1]`, `[S2]`, or `[S3]`

This lets agents determine which sprint they're in by reading the task title from `TaskGet`, which governs sprint-specific behavior (draft depth, review thresholds, etc.).

```
[S1] Research — [topic]
[S2] Draft — [asset]
[S3] Revise — [asset]
```

---

## Sprint 1: Plan & Sketch

**Goal:** Get the strategy right before burning tokens on assets.

**Tasks to create:**

```
TaskCreate: "[S1] Research — [Topic]: [target audience pain points]"
TaskCreate: "[S1] Research — [Topic]: competitor positioning"
TaskCreate: "[S1] Research — [Topic]: customer language mining"
TaskCreate: "[S1] Positioning — Generate 3-5 angles"
TaskCreate: "[S1] Campaign structure — Sketch asset plan and timeline"
TaskCreate: "[S1] Metrics — Define success criteria"
TaskCreate: "[S1] Checkpoint — Compile and present to user"
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
TaskCreate: "[S2] Draft — Lead magnet: [title]"
TaskCreate: "[S2] Draft — Landing page: [campaign name]"
TaskCreate: "[S2] Draft — Email sequence: [N] emails"
TaskCreate: "[S2] Expert review — Lead magnet (Creative Specialist runs Task tool subagents)"
TaskCreate: "[S2] Expert review — Landing page (Creative Specialist runs Task tool subagents)"
TaskCreate: "[S2] Quality Gate — Review all drafts"
TaskCreate: "[S2] Checkpoint — Compile drafts + expert reviews + present"
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
TaskCreate: "[S3] Revise — Lead magnet (based on Sprint 2 feedback)"
TaskCreate: "[S3] Revise — Landing page"
TaskCreate: "[S3] Revise — Email sequence"
TaskCreate: "[S3] Quality Gate — Edit lead magnet"
TaskCreate: "[S3] Quality Gate — Edit landing page"
TaskCreate: "[S3] Quality Gate — Edit email sequence"
TaskCreate: "[S3] Distribution — Format for web"
TaskCreate: "[S3] Distribution — Set up email sequence in platform"
TaskCreate: "[S3] Distribution — Publish campaign"
TaskCreate: "[S3] Distribution — Set up analytics tracking"
TaskCreate: "[S3] Distribution — Week 1 performance report"
```

**Optional Sprint 3 tasks** (add if campaign brief calls for them):
```
TaskCreate: "[S3] Repurpose — [asset] for [platform]"   ← if social promotion is planned
TaskCreate: "[S3] Newsletter — [topic]"                  ← if campaign includes a newsletter
```

**Dependency chain:**
```
Revisions (parallel) → Quality Gate per asset (parallel) → Distribution tasks (parallel) → Analytics
```
Note: each Quality Gate task is blocked by its corresponding revision task, not all revisions.

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
