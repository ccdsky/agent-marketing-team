# Newsletter Skill

## Purpose

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
Newsletter subjects are different from marketing emails:
- More personal, less clickbait
- Can be conversational ("Something I've been thinking about")
- Can be specific ("The mistake I made with [topic]")
- Can be intriguing ("Why [conventional wisdom] is backwards")

**Test:** Would you open this email from a friend?

#### Opening Paragraph

The most important paragraph. Either:
1. Start with a specific, vivid detail (not a vague setup)
2. Make a surprising claim and commit to it
3. Drop the reader into the middle of a story

Avoid: "In today's issue, we'll cover..." / "This week, I want to talk about..." — these are weak openers that signal low-value content.

#### Body

Match the format chosen in Step 2. Key rules:
- Short paragraphs (1-3 sentences)
- White space is a design element
- One idea per paragraph
- Concrete examples > abstract claims
- Personal > polished

**Voice check during writing:** Does this sound like a human talking, not a marketing department writing?

#### Closing

Options:
- Question for the reader (invites replies, builds community)
- Forward-looking: "Next week I'm going to..."
- Simple sign-off that matches the newsletter's established tone

#### P.S. (optional but high-read)
The P.S. gets read almost as much as the subject line. Use it for:
- One soft CTA
- A bonus thought that didn't fit in the body
- A personal note

### Step 4: Voice Pass

Read aloud. Ask:
- Would someone forward this to a colleague? (if not, why not?)
- Does this feel like a conversation or a broadcast?
- Are there any sentences that sound like they were written by a marketing team?
- Does it sound like the owner's actual voice?

Rewrite any paragraphs that fail these tests.

---

## Output Format

Save to: `output/campaigns/[campaign-slug]/drafts/newsletter-[YYYY-MM-DD]-draft.md`

For standalone issues (Simple Mode): Return output inline. Do not create a file unless the user asks.

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
