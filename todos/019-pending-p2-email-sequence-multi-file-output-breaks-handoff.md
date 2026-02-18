---
status: pending
priority: p2
issue_id: "019"
tags: [code-review, email-sequence, quality-gate, distribution-specialist, file-conventions]
---

# Email Sequence Skill Produces Multi-File Output But Handoff Assumes Single File

## Problem Statement

`email-sequence/SKILL.md` saves output to a subdirectory with one file per email:
```
output/campaigns/[slug]/drafts/email-sequence/email-01-[slug].md
output/campaigns/[slug]/drafts/email-sequence/email-02-[slug].md
output/campaigns/[slug]/drafts/email-sequence/sequence-overview.md
```

But `quality-gate.md` reads:
```
Read(file_path="output/campaigns/[slug]/drafts/[asset]-draft.md")
```

And `creative-specialist.md` task completion metadata holds a single `"deliverable"` path. The TaskUpdate metadata spec only supports one deliverable path string — not a list or directory.

The Quality Gate has no instruction to enumerate a directory of files. The Distribution Specialist has the same single-file assumption. On every email sequence task, the Quality Gate will receive one file path in metadata, but the actual deliverable is a directory with N+1 files.

## Proposed Solution

**Option A (preferred):** Email sequence skill saves to a single consolidated file (`email-sequence-[slug]-draft.md`) that contains all emails as sections. Each email is a `## Email N: [Subject]` section within one document. Simple to read, simple to hand off.

**Option B:** Update Quality Gate to handle directory deliverables — detect if deliverable path ends in `/`, and if so, `Glob` the directory and read all files in order.

**Option C:** Email sequence skill saves one `sequence-overview.md` that embeds the full content of each email inline.

**Effort:** Small-Medium — either update email-sequence SKILL.md to use single file, or update QG to handle directories.

## Acceptance Criteria

- [ ] Email sequence deliverable is either a single file or QG/DS explicitly handle multi-file sequences
- [ ] `creative-specialist.md` TaskUpdate metadata can correctly point to the email sequence deliverable
- [ ] Quality Gate can read and review the complete email sequence without additional instructions

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
