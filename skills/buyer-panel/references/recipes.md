# Buyer Panel — Composition Recipes

Five named recipes that compose buyer panels from the user's persona library. Three recipes filter on `audience_role` (`full-prospect-panel`, `buying-committee`, `channel-gatekeeper-review`). `single-segment-deep` takes an explicit persona slug. `platform-specific` filters on a custom tag that users add outside the v1 frontmatter contract. The role-filtered recipes adapt to whatever personas the user has authored without naming specific files.

To invoke a recipe, pass `recipe:[recipe-name]` to `/buyer-panel`. The orchestrator resolves the recipe to actual persona files by reading `context/personas/README.md` and filtering on the relevant frontmatter field.

---

## 1. `full-prospect-panel`

**Purpose:** Maximum-coverage buy signal from every defined prospect persona.

**Filter:** All personas with frontmatter `audience_role: prospect`.

**Use case:** Broad ad review with mixed audience; direct-response variant scoring across segments; brand-message testing where you want every prospect voice in the room; periodic audit of evergreen high-traffic pages.

**Watch-out:** Synthesis is harder to act on with >6-8 personas — split reactions multiply. If the asset is segment-specific, prefer `single-segment-deep` or a custom shortlist.

**Example invocation:** *"Run buyer-panel using the full-prospect-panel recipe against drafts/homepage-hero-v2.md."*

---

## 2. `buying-committee`

**Purpose:** Multi-stakeholder B2B buy signal — the economic buyer plus the people they consult internally before saying yes.

**Filter:** All personas with frontmatter `audience_role: prospect` AND all personas with frontmatter `audience_role: internal-stakeholder`.

**Use case:** Multi-stakeholder B2B decisions (the kind where the founder won't sign without the CFO's nod and the head of ops saying they can absorb the workload); proposal review; complex sales pages where the prospect will forward the link before booking the call.

**Watch-out:** This recipe assumes the user has authored internal-stakeholder personas (CFO, head of ops, IT, legal, etc.). If only prospect personas exist, the result is identical to `full-prospect-panel` — surface that in the output rather than silently degrading.

**Example invocation:** *"Run buyer-panel using the buying-committee recipe against drafts/sales-page-v1.md."*

---

## 3. `channel-gatekeeper-review`

**Purpose:** Will this asset survive a referral, partner-channel handoff, or analyst conversation? Reviews the asset through the lens of the intermediaries who will see it before — or instead of — the end buyer.

**Filter:** Personas with frontmatter `audience_role: intermediary` only.

**Use case:** Critical for service businesses with referral channels (the asset has to read well to the trusted peer who forwards it); partner-co-marketing collateral; publisher or analyst pitches; agency-channel materials. The intermediary persona has a different question ("does this make me look good if I send it?") that the prospect persona never asks.

**Watch-out:** Skip if the user has no intermediary personas defined — the skill should report this cleanly rather than synthesizing zero responses. This recipe is most valuable for service businesses; product companies with direct-only sales may not need it.

**Example invocation:** *"Run buyer-panel using the channel-gatekeeper-review recipe against drafts/partner-one-pager.md."*

---

## 4. `single-segment-deep`

**Purpose:** Optimize an asset for one named persona across multiple angles of the same draft without committee noise.

**Filter:** One named persona slug, passed explicitly. The recipe is structural rather than filter-based — it constrains the panel to a single voice and asks that voice to react with maximum depth.

**Use case:** Optimizing a landing page for one ICP when the campaign brief is single-persona; A/B variant scoring within one segment; iterative refinement where committee dynamics would add noise; persona-specific email sequence review.

**Watch-out:** Output Aggregate Buy Signal table has only one row — that's expected. The depth comes from richer answers to the six questions, not from cross-persona consensus. Pair with `buying-committee` later if multi-stakeholder coverage becomes needed.

**Example invocation:** *"Run buyer-panel using the single-segment-deep recipe with persona morgan-founder against drafts/landing-page-v3.md."*

---

## 5. `platform-specific`

**Purpose:** Panel composition for plugins, multi-product portfolios, or vertical-specific assets where personas are tagged by a specific platform or vertical.

**Filter:** Personas with frontmatter matching a custom tag (e.g., `platform: shopify`, `vertical: healthcare`, `product: enterprise`). The user supplies the tag value when invoking.

**Use case:** Multi-product or multi-vertical plugins where the persona library spans more than one offering; platform-specific landing pages where the relevant prospects share a custom tag the standard `audience_role` field doesn't capture; vertical-specific go-to-market materials.

**Watch-out:** Requires the user to have added the custom tag to their persona frontmatter — this is outside the locked v1 frontmatter contract. If the tag isn't present on any persona, the recipe falls back to the explicit list provided by the user or returns "no matches; specify personas explicitly."

**Example invocation:** *"Run buyer-panel using the platform-specific recipe with tag vertical:healthcare against drafts/healthcare-landing.md."*
