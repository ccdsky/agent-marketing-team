---
status: pending
priority: p1
issue_id: "017"
tags: [code-review, campaign-lead, bash, file-paths, directory-creation]
---

# Campaign Directory Creation Uses Relative Paths — Will Fail If cwd Is Not Project Root

## Problem Statement

`campaign-lead.md` step 4 (campaign kickoff workflow) uses relative paths for `mkdir`:

```bash
mkdir -p output/campaigns/[campaign-slug]-[YYYY-MM]/
mkdir -p output/campaigns/[campaign-slug]-[YYYY-MM]/{research,drafts,edited,ready,analytics}
```

Claude Code's working directory is not guaranteed to be the project root. If an agent's cwd is different (e.g., a subdirectory, or the user's home), `mkdir -p output/...` creates the directory in the wrong location — or fails silently if `output/` doesn't exist there. Since `output/` is gitignored, there is no scaffolded directory on a fresh clone. The directory genuinely must be created at runtime.

Every campaign starts by creating this directory structure. If it's created in the wrong place, all subsequent `Write` calls to `output/campaigns/[slug]/drafts/` will also fail.

## Proposed Solution

**Option A (preferred):** Use absolute path with the known project root:
```bash
Bash("mkdir -p /Users/chris/Development/agent-marketing-team/output/campaigns/[slug]/{research,drafts,edited,ready,analytics}")
```

**Option B:** Resolve project root first, then use it:
```bash
Bash("cd /Users/chris/Development/agent-marketing-team && mkdir -p output/campaigns/[slug]/{research,drafts,edited,ready,analytics}")
```

**Option C:** Use `Bash("pwd")` to confirm cwd before mkdir, and warn if not the expected root.

**Effort:** Small — 2 line edits in campaign-lead.md

## Acceptance Criteria

- [ ] campaign-lead.md mkdir commands use absolute path or explicitly cd to project root first
- [ ] The path used matches the actual project location (`/Users/chris/Development/agent-marketing-team`)
- [ ] campaign-brief.md write path also uses absolute path or confirmed relative path

## Work Log

- 2026-02-18: Identified by agent-native-reviewer in second review pass
