# Personas

One Markdown file per buyer persona. The team reads this index during Pre-Task Protocol; full dossiers load only when a task targets a specific persona.

`example-persona.template.md` is a reference template. **Copy it to your own `<slug>.md` before editing — never edit the template in place.**

Files matching `*.template.md` are reference templates only — never selected as a persona by the agent.

## Persona Library

| Slug | Name | Role | Audience Role | One-sentence Summary | Primary Use |
|------|------|------|---------------|----------------------|-------------|
| `example-persona.template` | Morgan Reyes (reference) | Mid-market B2B founder/CEO | prospect | Reference template for a panel-ready persona dossier | Structural example only — not selectable as a real persona |

## Adding a Persona

1. Copy `example-persona.template.md` to `<your-slug>.md` (kebab-case, no `.template.` suffix). The filename is the authoritative slug — frontmatter `slug:` must match the filename exactly.
2. Fill out the frontmatter: `name`, `slug`, `role`, `summary`, `primary_use`, `audience_role` (`prospect` | `intermediary` | `internal-stakeholder`), `description`.
3. Replace each section with content grounded in real research — sales calls, interviews, support tickets, win/loss data. Invented personas underperform.
4. Add a row to the table above.
5. Keep the AI Agent Simulation Block YAML well-formed — `/buyer-panel` consumes it.

A thin persona is better than no persona. Iterate over time.

## Panel-Composition Recipes

`/buyer-panel` can convene named recipes (full-prospect-panel, buying-committee, channel-gatekeeper-review, and more) that filter on `audience_role`. See `skills/buyer-panel/references/recipes.md` for the full list.
