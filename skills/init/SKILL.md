---
name: init
description: Initialize a new project for the marketing team — scaffolds context, knowledge, and output directories with template files. Run once per project before any campaign work.
---

# Initialize Marketing Project

## Purpose

Scaffold the working directory with the context, knowledge, and output directories the marketing team needs. Creates template files the user populates before running their first campaign.

Run once per project. Safe to re-run — skips files that already exist.

---

## Framework

### Step 1: Create Directory Structure

Create these directories in the current working directory:

```
mkdir -p context
mkdir -p knowledge/research
mkdir -p knowledge/learnings/campaigns/timing
mkdir -p knowledge/learnings/campaigns/asset-mix
mkdir -p knowledge/learnings/campaigns/coordination
mkdir -p knowledge/learnings/campaigns/task-patterns
mkdir -p knowledge/learnings/campaigns/quality-gates
mkdir -p knowledge/learnings/campaigns/retrospectives
mkdir -p knowledge/archive
mkdir -p knowledge/feedback/analytics
mkdir -p output/campaigns
```

### Step 2: Create Context Templates

**Only create files that don't already exist.** If a file exists, skip it — the user may have already populated it.

#### `context/voice-dna.md`

```markdown
# Voice DNA

Analyze 3-5 of your writing samples and document your voice profile here.

## Sentence Patterns
- [How do your sentences flow? Short and punchy? Long and winding? Mixed?]

## Word Choice
- [What words do you gravitate toward? What vocabulary level?]

## Tone
- [Formal or casual? Personal or corporate? Authoritative or conversational?]

## Personality Traits
- [What personality comes through? Humor? Directness? Warmth?]

## Anti-Patterns (What You'd Never Say)
- [Phrases, words, or styles that would sound wrong in your voice]

## Writing Samples
[Paste 3-5 examples of your actual writing below — blog posts, emails, LinkedIn posts, newsletters. The more varied, the better the voice match.]
```

#### `context/icp.md`

```markdown
# Ideal Customer Profile

## Demographics
- **Role:** [Job titles and seniority]
- **Company size:** [Revenue range or employee count]
- **Industry:** [Sectors you serve]

## Pain Points
- [What frustrates them daily?]
- [What are they trying to fix?]
- [What have they tried that didn't work?]

## Goals
- [What does success look like for them?]
- [What metrics do they care about?]

## Language
- [Exact phrases they use to describe their problems]
- [Industry jargon they use naturally]
- [Words they'd never use]

## Where They Hang Out
- [LinkedIn groups, Slack communities, subreddits, conferences]
- [What publications do they read?]
- [Who do they follow?]

## Common Objections
- [What stops them from buying?]
- [What concerns come up in sales conversations?]
```

#### `context/business-profile.md`

```markdown
# Business Profile

## Company
- **Name:** [Your company name]
- **What you do:** [One sentence]
- **Founded:** [Year]

## Products/Services
- [Product 1]: [What it does, who it's for, price point]
- [Product 2]: [What it does, who it's for, price point]

## Value Proposition
- [Why should someone choose you over alternatives?]

## Differentiation
- [What do you do that competitors don't?]
- [What's your unique mechanism or approach?]

## Customer Results
- [Specific outcomes customers have achieved]
- [Testimonials, case studies, data points]

## Your Story
- [Why does this company exist?]
- [What motivated you to build this?]
```

#### `context/brand-guide.md` (optional — create as template)

```markdown
# Brand Guide (Optional)

## Visual Identity
- **Colors:** [Primary and secondary brand colors]
- **Fonts:** [Heading and body fonts]
- **Logo usage:** [Guidelines]

## Tone by Platform
- **LinkedIn:** [Professional but approachable? Thought leadership?]
- **Twitter/X:** [Casual? Punchy? Provocative?]
- **Email:** [Personal? Direct? Educational?]
- **Website:** [Authoritative? Warm? Technical?]

## Banned Phrases
- [Words or phrases that should never appear in your content]

## Required Elements
- [Anything that must appear in all content — disclaimers, CTAs, etc.]
```

### Step 3: Create .gitignore for User Data

If no `.gitignore` exists in the working directory, create one:

```
# Context files (may contain sensitive business information)
context/voice-dna.md
context/icp.md
context/business-profile.md
context/brand-guide.md

# Campaign outputs (generated content, often large)
output/

# Knowledge base (may contain proprietary research)
knowledge/research/
knowledge/feedback/

# OS
.DS_Store
```

If `.gitignore` already exists, append only the lines that aren't already present.

### Step 4: Report Setup Status

After creating all directories and templates, report:

```markdown
## Marketing Project Initialized

**Created:**
- `context/` — 4 template files (voice-dna, icp, business-profile, brand-guide)
- `knowledge/` — research, learnings, archive, and analytics directories
- `output/campaigns/` — campaign output directory

**Next step:** Populate the 3 required context files before running any campaign:
1. `context/voice-dna.md` — Paste 3-5 writing samples and document your voice patterns
2. `context/icp.md` — Define your ideal customer profile with their exact language
3. `context/business-profile.md` — Document your products, positioning, and customer results

`context/brand-guide.md` is optional — fill it in if you have established brand standards.

**Then try:** "Write a LinkedIn post about [topic you know well]" to test voice matching.
```

---

## Quality Gate

- [ ] All directories created
- [ ] Template files created only where they didn't already exist
- [ ] User informed which files need population
- [ ] No existing files were overwritten
