---
status: pending
priority: p3
issue_id: "029"
tags: [code-review, retrospective, archive, bash, file-operations]
---

# Retrospective Archive Step Has No Clear Executable Tool Call

## Problem Statement

`retrospective.md` Step 5 says:
```
Move campaign outputs to the archive:
output/campaigns/[slug]/ → knowledge/archive/[slug]/
Or create an archive entry linking to the campaign outputs.
```

"Move" implies a filesystem operation (`mv` or `cp -r`), which requires Bash. The Read/Write/Edit tools cannot move or copy directories. The "or create an archive entry" fallback is executable with Write, but is presented as a secondary option.

An agent attempting Step 5 literally will try to "move" a directory without a clear tool path and may improvise or fail silently.

## Proposed Solution

Clarify Step 5 to use the executable fallback as the primary action:

```markdown
### Step 5: Create Archive Entry

Write a summary archive entry:
```
Write(
  file_path="knowledge/archive/[campaign-slug]-[date].md",
  content="# Campaign Archive: [name]\n\n**Completed:** [date]\n**Campaign files:** output/campaigns/[slug]/\n\n[Brief summary of outcomes and key assets]"
)
```

Note: Campaign files in `output/campaigns/[slug]/` remain in place (gitignored). The archive entry provides a searchable record in the knowledge base.
```

**Effort:** Trivial — rewrite Step 5 in retrospective.md

## Work Log

- 2026-02-18: Identified by agent-native-reviewer in second review pass
