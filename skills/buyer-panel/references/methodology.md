# Buyer Panel — Extended Reference

## Per-Persona Prompt Template

When dispatching each persona sub-agent (parallel or sequential), use this template. The orchestrator substitutes the bracketed values; the sub-agent reads its own dossier from the path passed in.

```
You are now embodying [persona name]. Read your dossier at [path to persona dossier].
Then evaluate [asset path] strictly from this persona's perspective — would you buy?
Answer the questions below in this persona's voice, citing specific hot buttons and
red flags from your dossier.

Stay in character throughout. Use the vocabulary, sentence rhythm, and concerns from
the "What They Say Out Loud" and "AI Agent Simulation Block" sections of your dossier.
Do not break character to offer craft critique — that's a different skill's job. Your
job is to react as the buyer.

Output format:

## [Persona Name] — Buy Signal: [YES / NO]

### 1. Does this relate to you?
[In-character answer. Specifics from the asset only — do not generalize.]

### 2. What about it appeals to you?
[In-character. Cite the asset sections that landed and which hot buttons they hit.]

### 3. What about it turns you off?
[In-character. Cite the asset sections that broke trust and which red flags they tripped.]

### 4. What do you wish it said that would make you buy now?
[In-character. Be concrete — the change you'd want, not abstract principles.]

### 5. Would you buy this product/service? (yes / no — be decisive)
[YES or NO. No "it depends." Pick the side your dossier points to and commit.]

### 6. What's your reasoning?
[2-4 sentences in character. Reference your specific situation and the asset's
specific framing.]
```

**Critical rules for the orchestrator:**
- Pass the dossier **path**, never the dossier content. The sub-agent reads its own file.
- Pass the asset **path**, not asset content. The sub-agent reads it for itself.
- Use "embody" not "pretend" — the wording materially affects in-character output quality.
- Run all personas with the same six-question set so synthesis is comparable.

---

## The Six Questions (Justin Brooke's framework, adapted)

1. **Does this relate to you?** — relatability check. If the persona doesn't recognize themselves in the first scan, the rest is irrelevant.
2. **What about it appeals to you?** — resonance points. Identifies what to keep.
3. **What about it turns you off?** — friction and red-flag triggers. Identifies what to fix.
4. **What do you wish it said that would make you buy now?** — the buy-trigger gap. Generates the most actionable revisions.
5. **Would you buy this product/service? (yes / no — be decisive)** — forced binary commits the persona to a position. "It depends" is not allowed.
6. **What's your reasoning?** — the why behind the yes/no. Aggregates into consensus or surfaces split reactions.

---

## Synthesis Weighting Rules

Confirm response count before synthesizing. Apply these thresholds:

| Personas Responded | Action |
|--------------------|--------|
| 100% (full panel) | Full confidence. Synthesize directly. |
| 60% to <100% | Normalize across responding personas. Label header: "REDUCED CONFIDENCE — [N]/[total] personas responded." Note which personas did not respond and why if known. |
| <60% | Do not synthesize. Note: "Buyer panel incomplete — [N]/[total] personas responded. Re-run before relying on this signal." Set task metadata `{"buyer_panel_status": "incomplete", "personas_responded": N}`. |

**Identifying consensus vs. split:**

- **Consensus yes** — a resonance point cited by ≥60% of responding personas. List as Consensus Resonance; do not flag for change.
- **Consensus no** — an objection cited by ≥60% of responding personas, OR any hot-button violation flagged by any persona whose dossier names it as a category-defining red flag. List as Consensus Objection; promote to Must Fix.
- **Split reactions** — a point where personas explicitly disagree (one persona's appeal is another's turn-off). Surface in the Conflicting Persona Reactions section; do not average. Note: this is signal, not noise — splits often reveal segmentation work the asset needs to do better.
- **Single-persona signal** — an objection or appeal from one persona only. Promote to Should Fix if the persona's dossier names it as high-impact (e.g., a category-defining red flag for that segment); otherwise Nice to Have.

---

## Output Template

Save to `output/campaigns/[slug]/reviews/buyer-panel-[asset-type]-[YYYY-MM-DD].md` (campaign mode) or `output/buyer-panel-[asset-name]-[YYYY-MM-DD].md` (standalone).

```markdown
# Buyer Panel: [Asset Type] — [Campaign Name or Asset Name]

**Date:** [YYYY-MM-DD]
**Asset reviewed:** [path to draft]
**Panel composition:** [recipe name OR explicit persona list]
**Personas convened:** [persona-1, persona-2, persona-3, ...]
**Personas responded:** [N]/[total]

---

## Aggregate Buy Signal

| Persona | Signal | 1-line reason |
|---------|--------|---------------|
| [Persona 1] | YES / NO | [Reason in their voice] |
| [Persona 2] | YES / NO | [Reason in their voice] |

**Yes count:** [N]/[total]

---

## Consensus Resonance (Don't change these)

- [Resonance point — cited by [X] personas] — [why it lands]

---

## Consensus Objections

- [Objection — cited by [X] personas] — [why it blocks the buy]

---

## Must Fix

### Issue 1: [Short title]
**Flagged by:** [Persona names]
**Location:** [Asset section / line]
**Problem:** [What's wrong in the persona's voice]
**Suggested fix:** [Specific change]
**Expected impact:** [What changes for these personas]

---

## Should Fix (Single-Persona High-Impact)

### Issue [N]: [Short title]
[Same structure]

---

## Nice to Have

- [Brief note — section — persona]

---

## Conflicting Persona Reactions

| Topic | Persona A says | Persona B says | Recommendation |
|-------|----------------|----------------|----------------|
| [Topic] | [View in voice] | [View in voice] | [How to reconcile — separate sections, segmented hero, etc.] |

---

## Revision Checklist

- [ ] [Must fix 1]
- [ ] [Must fix 2]
- [ ] [Should fix 1]

**Route back to Creative Specialist when:** All must-fix items are checked off. Optional follow-up: re-run buyer panel to confirm the signal shifted.
```

---

## Panel-Composition Guidance

**When to use the full persona library:** broad ad review where you want maximum coverage and don't yet know which segment will respond; brand-message testing across the whole audience; periodic full-audit of evergreen pages. Cost: high token usage and harder-to-act-on synthesis when the panel is large (>8 personas).

**When to use a recipe (most common):** Sprint 2 drafts in an active campaign where the brief already targets specific personas; ad-variant scoring against a known segment; sales-page review where you want a defined panel composition (e.g., the full buying committee, not just the economic buyer). Recipes are role-based filters on the `audience_role` frontmatter field — they adapt to the user's specific persona library without naming slugs.

**When to use a single-persona check:** optimizing a page for one ICP without committee noise; quick relatability check during drafting; A/B variant scoring for one segment. Use the same output template — the Aggregate Buy Signal table simply has one row.

**Default behavior when no input given:** if the campaign brief names primary personas, use those; otherwise fall back to all `audience_role: prospect` personas. Never default to "every file in `context/personas/`" without filtering — that includes intermediaries and internal stakeholders whose signal answers a different question than "would the prospect buy?"
