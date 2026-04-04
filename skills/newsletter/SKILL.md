---
name: newsletter
description: Write email newsletters with Schwartz subscriber-awareness matching in 4 formats (Personal Letter, Insight Post, Story+Lesson, Curated).
---

# Newsletter Skill

## When to Use

Write email newsletters that build deep reader relationships, establish authority, and drive action — without feeling like marketing. These are the emails people actually look forward to receiving.

Invoke when: Regular newsletter issue needed, or campaign includes a newsletter touch.

---

## Required Inputs

Before writing, always read:
- `context/voice-dna.md` — Voice, tone, and the personal writing style that makes newsletters feel human
- `context/icp.md` — Reader profile — their context, questions, and what makes them feel understood
- `context/business-profile.md` — Content pillars and offerings to connect to (lightly)
- Past issues (if any): search `output/campaigns/` for previous newsletter drafts

---

## Framework

### Step 1: Define This Issue

Clarify before writing:
- **Core idea:** One sentence — the single insight, story, or lesson this issue delivers
- **Reader transformation:** How should they feel or think differently after reading?
- **CTA (if any):** One soft action — reply, read an article, click a link (never hard sell in newsletters)
- **Issue length:** Short (300-500 words) | Medium (600-900 words) | Long (1000-1500 words)
- **Audience awareness level:** Newsletter subscribers are typically Product Aware or Most Aware — they already know you. Match your opening accordingly:

  | Subscriber Relationship | Schwartz Awareness Level | Opening Strategy |
  |------------------------|-------------------------|------------------|
  | New subscriber (first 3 issues) | Solution/Product Aware | Deliver on the promise that got them to subscribe — immediate value, light introduction of your perspective |
  | Established subscriber | Product Aware | Lead with insight, not introduction — they know who you are. Go deeper. |
  | Re-engagement (lapsed) | Problem Aware | Remind them why they subscribed — surface the pain point your content addresses |

  Newsletters rarely serve Unaware audiences (they opted in). Don't over-explain who you are or what you do — your subscribers already know.

**Rule:** One issue, one main idea. If you have two ideas, write two issues.

### Step 2: Choose a Format

#### Format A: The Personal Letter

Most natural for founders, creators, and thought leaders.

```
[Personal opening — recent experience or observation]
[The insight this sparked]
[How it connects to the reader's work/life]
[A specific, actionable takeaway]
[Soft CTA or closing question]
```

#### Format B: The Insight Post

Deep dive on one topic or trend.

```
[Hook — the surprising claim or question]
[Background — why this matters right now]
[Main insight — the thing most people miss]
[Evidence or example — specific, concrete]
[Implication — what this means for the reader]
[Next step or CTA]
```

#### Format C: The Story + Lesson

Narrative-driven, high engagement.

```
[Scene-setting opening — drop into a specific moment]
[What happened — the story]
[The turn — the thing that changed]
[The lesson extracted]
[The application — how reader can use this]
[Closing + soft CTA]
```

#### Format D: The Curated List

Lighter issue, great for busy weeks or building habits.

```
[Brief intro — why these picks matter]
[Item 1: [Title] — [1-2 sentence annotation]]
[Item 2: [Title] — [1-2 sentence annotation]]
[Item 3: [Title] — [1-2 sentence annotation]]
[Closing thought or question]
```

### Step 3: Write the Issue

#### Subject Line (write 3 options)

Test: Would you open this email from a friend?

#### Body + Closing

Match the format chosen in Step 2. Close with a question (invites replies) or forward-looking note. Optional P.S. for a soft CTA.

### Step 4: Voice Pass

Verify against `voice-dna.md` and `icp.md`. The forward test: would someone send this to a colleague?

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/newsletter-[YYYY-MM-DD]-draft.md`

For standalone issues (Simple Mode): Return output inline. Do not create a file unless the user asks.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/drafts/newsletter-[YYYY-MM-DD]-draft.md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "quality-gate"
})
```

**File format:**
```markdown
# Newsletter Draft: [Date] — [Working Title]

**Format:** [personal letter | insight post | story+lesson | curated list]
**Core idea:** [One sentence]
**Target length:** [X] words

---

## Subject Line Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

**Recommended:** [N] — [brief reason]

## Preview Text
[50-80 chars]

---

## Issue

[Full newsletter, ready to send]

---

## Self-Assessment

- Voice match: [1-10]
- Would I forward this? [Yes/No/Maybe — why]
- Subject line: [1-10]
- Opening strength: [1-10]
- Clarity of core idea: [1-10]
```

---

## Example

**Product:** Acme CI/CD — CI/CD platform for mid-market engineering teams
**Format:** Personal Letter
**Core idea:** The real reason mid-market CI/CD fails isn't tooling — it's
the missing rollback habit

---

**File:** `output/campaigns/acme-cicd-launch/drafts/newsletter-2026-04-04-draft.md`

```
## Subject Line Options
1. The deploy that changed how I think about rollbacks
2. Why your rollback plan probably won't work
3. Something most CI/CD guides skip

**Recommended:** Option 1 — personal hook, curiosity without clickbait

## Preview Text
It wasn't a tooling problem. It was a habits problem.

---

## Issue

Last month I watched a 20-person engineering team deploy a routine feature
update that took down their checkout flow for 47 minutes.

They had CI/CD. They had tests. They had a deployment checklist.

What they didn't have was a rollback they'd actually tested in production
conditions.

Here's what I've seen in team after team: rollback plans exist in theory.
Engineers add them to runbooks. Nobody runs them until it's an emergency.
Then they discover the rollback takes 12 minutes, not 2 — and that's 10
minutes your customers aren't buying anything.

The fix isn't a better rollback script. It's making rollback drills a
monthly habit — same as fire drills. Run it on a Tuesday. Learn what breaks.
Fix it before Friday matters.

Three things that change when teams build this habit:
1. Deploy anxiety drops (you've already seen the worst case)
2. Incident resolution time falls by 60-70%
3. Engineers stop avoiding deploys late in the sprint

If you're setting up or migrating your CI/CD pipeline, this is the one
checklist item most guides bury in section 4. Put it in section 1.

— [Sender Name]

P.S. We put together a migration checklist that puts rollback validation
front and center. [Download it here — link]
```

---

## Quality Checklist

Before marking complete:

- [ ] Subject line options written — passes the "forward from a friend" test
- [ ] Opening paragraph hooks without setup preamble
- [ ] One main idea (not two or three)
- [ ] Short paragraphs throughout (3 sentences max)
- [ ] At least one specific, concrete example
- [ ] Closing invites response or has clear soft CTA
- [ ] Voice passes read-aloud test (sounds human, not marketing)
- [ ] No "In today's issue..." or other weak opener patterns
- [ ] ICP would find this genuinely valuable (not just informational)
- [ ] Self-assessment complete
- [ ] File saved to correct output path
