# Adopting a Claude Design bundle

**What this is:** an observation log and manual playbook, **not a tool.** Per [D-008](DECISIONS.md) the kit builds no adopt-skill, no `design-system-bootstrap` adopt-mode, and no token-adopt command. This doc is the kept knowledge from dismantling the first bundle, so a second one is re-derived against a recorded baseline instead of from scratch. It is also the **Rule-of-Two tripwire**: when the bundle ledger at the bottom gets a second row, that is the signal to re-evaluate whether a token-adopt command finally earns its keep.

Source investigation: [`design-handoff-fidelity-test.md`](design-handoff-fidelity-test.md) (the transcription test) and the original proposal in [`design-handoff-adopt-brief.md`](design-handoff-adopt-brief.md) (superseded). Decision rationale: [D-008](DECISIONS.md); audit verdict: [`council/council-report-2026-06-09-audit.html`](council/council-report-2026-06-09-audit.html).

---

## What a Claude Design bundle is

Claude Design (`claude.ai/design`) produces HTML/CSS/JS prototypes and exports a **handoff bundle** for a coding agent to implement. From bundle #1 (`the-council/spikes/claude-design/`):

- **A `README.md` aimed at coding agents** — declares itself a handoff bundle, names the file the user had open, and instructs: *recreate pixel-perfect in whatever tech fits the target codebase; do not copy the prototype's internal structure.* This README is the bundle's own adoption contract — honor it.
- **In-browser React** via Babel-standalone (unpkg React + `type="text/babel"`), not a build. The prototype is disposable; it is ground truth for *look and behavior*, not a source tree to lift.
- **Zero Tailwind.** Styling is plain CSS driven by a rich `:root` custom-property system — ~40 tokens across a few CSS files: semantic palette, `oklch()` accents, font stacks, motion easings, a CRT-intensity scalar.
- **It already *is* a design system** — more opinionated than DSB's `tokens.css` template generates, with **class-based theming** (e.g. `body.twilight` re-binds the same token names) and a runtime colorway tweak.
- **A PRD** (`uploads/PRD.md`) and screenshots as ground truth, with the target stack named in the PRD.

## The fidelity finding (why no automated importer)

Transcribing bundle #1's `:root` into our two-tier `tokens.css` showed the tokens are **value-lossless but structurally non-isomorphic**:

- **Lossless:** 40/40 token values transcribe verbatim — `oklch()`, easings, `rgba`, scalars all survive a literal copy.
- **Non-isomorphic to the scale-first template:** DSB's template *fabricates* a numeric shade scale; it cannot hold 6 font families in 3 type slots; it has no tier for ~5 categorical accents, the `--crt` scalar, or a theme toggle.

So the values are safe to copy but the *shape* is not safe to assume. The "fidelity trap" is real but scoped precisely to the **scale-first template**, not to CSS-vars as such. At **N=1 you cannot separate a shipped theme from tweak-tool scratch** (the bundle ships both a real palette and a runtime tweak panel), so any schema you encode now is unvalidated guesswork. A token-adopt command is cheap to write later — deferring costs nothing.

## The composition-fidelity finding (2026-06-19)

Re-examining the **same** bundle from the component/composition angle (not tokens) surfaced a failure the token fidelity test above did not: **playbook step 1 as originally written — "recreate pixel-perfect per the README" — drifts ~100% in practice.**

In `the-council`, the bundle shipped a real **~1,200-line prop-driven React component library** (`TarotCard`, `Waveform`, `Channel`, `ChromeWindow`, + emblem/sub-components). When the app was built:

- **0% of the components were adopted** — no imports from the bundle; every surface re-implemented inline as fresh JSX + CSS modules.
- **Only token values survived** (the `cp` of the token step worked); composition did not.
- **Every page diverged structurally** from the bundle's layout — not colors, *composition*: the home page dropped the hero/charter; the verdict page went single-column → two-column.

Root cause: **the finished design was absent from the build context, and fidelity was enforced by nothing.** Token compliance held because a linter checked it; composition drifted because no artifact was present at compose time and no gate required looking. "Recreate per README" silently assumes the builder consults the design — but nothing makes them, so they rebuild from the tokens plus a vibe.

Two distinctions the [2026-06-19 council](council/council-report-2026-06-19-adopt.html) drew, load-bearing for the fix:

- **Intra-app consistency** (does surface 2 build a button like surface 1?) is **mechanically checkable** — a hook/grep can flag an inline re-implementation of a component that already exists in the imported set. No human needed.
- **Fidelity-to-source** (does any surface match the bundle?) is a **judgment call** — it needs a human gate, but the gate survives only if it is *cheap and present*, not diligent. The fix is presence (the design lives in-repo next to the surfaces), not willpower.

The council re-confirmed [D-008](DECISIONS.md) **5/5** — still no adopt skill — and located the real fix as product-side *presence + wiring*, upgraded into the playbook below.

## The manual playbook (what to actually do with a bundle)

This is a **product-side** procedure — it runs in the real app's repo, **not** in this kit. Nothing here modifies `prd-to-product`.

1. **Bring the rendered design INTO the app repo first — presence beats recreation.** Before building any surface, drop the bundle's rendered pages (screenshots + component source) into the product repo at `design/reference/`, and **copy the bundle's real components in** as the starting point rather than recreating them from memory. The ~100%-drift failure (the-council) was caused by the design being *absent* at build time. The README's "recreate pixel-perfect, don't copy the prototype's internal structure" still governs *visual* fidelity and stack-fit — but start from the copied component source, don't retype from a glance.
2. **`cp` the token values into the product repo.** The real app needs tokens **in its own repo** to build; a Claude Design bundle is a disposable export. Because the values are lossless, a literal copy of the `:root` custom properties into the product's own CSS is safe — keep the bundle's structure rather than forcing it into the scale-first template.
3. **Add the always-on import rule** (below) to the product's `.claude/rules/`. It is what makes step 1 stick: import the components, never rebuild a covered surface without a cited reason, diff each new surface against its reference page.
4. **Split the enforcement.** Make intra-app consistency mechanical — a session-start check or hook that greps for inline re-implementations of imported components; accept fidelity-to-source as a human gate kept cheap by *presence*. **Re-snapshot `design/reference/` on each Claude Design re-export** — it goes stale every redesign; a surface diffed against a stale reference is flagged, not trusted.
5. **Keep the bundle as the design source of record** for anything not yet transcribed (theming variants, motion, the screenshots). Do not treat the `cp`'d tokens as the canonical design — the bundle is.
6. **Tailwind:** the bundle is vanilla CSS-vars. Do **not** translate to Tailwind during adoption; carry the custom-property system across as-is.

> Run this approach across **3 real handoffs** before reconsidering any kit change (per the [D-008](DECISIONS.md) 2026-06-19 extension). Still **product-side only** — no `prd-to-product` skill is built for this.

## Ready-to-drop import rule (product-side)

Drop into the **product** repo's `.claude/rules/design-adoption.md` — not this kit. ~20 lines, each rule citing its failure mode per house style:

```markdown
---
description: Adopt the Claude Design bundle's components; never rebuild a covered surface
paths: ["app/**", "components/**", "src/**"]
---
# Design adoption — import, don't rebuild

The rendered design of record lives in `design/reference/` (the bundle's pages + component source, re-snapshotted on each Claude Design export).

- **Import the bundle's components; never rebuild a surface they already cover.** Rebuilding inline requires a cited reason in the commit.
  **Failure it prevents:** components got rebuilt inline instead of imported → every page diverged in composition (~100% drift, the-council 2026-06).
- **Diff every new surface against its `design/reference/` page before commit.** No reference for a surface → add one before building it.
  **Failure it prevents:** design fidelity enforced by nothing drifts every time; token compliance alone does not hold composition.
- **A surface diffed against a stale reference is flagged, not trusted.** Re-snapshot `design/reference/` whenever the Claude Design export changes.
  **Failure it prevents:** enforcing fidelity to a design that no longer exists.
```

## Bundle ledger (Rule of Two)

Filling a second row is the trigger to revisit [D-008](DECISIONS.md) and decide whether a token-adopt command is worth building.

| # | Date | Bundle | Tokens | Notable structure | Outcome |
|---|------|--------|--------|-------------------|---------|
| 1 | 2026-06-09 | `the-council/spikes/claude-design/` | ~40, lossless | 6 fonts, ~5 categorical `oklch` accents, `--crt` scalar, class-based theming (`body.twilight`), runtime tweak panel | Fidelity test only; no adoption performed in-kit. Baseline recorded here. |
| 2 | — | *(awaiting a 2nd real bundle)* | — | — | **On arrival: re-derive against row 1, then decide on a token-adopt command.** |

## Cross-references

- Decision: [D-008](DECISIONS.md) · mirror in [`DECISIONS_ACTIVE.md`](DECISIONS_ACTIVE.md).
- Fidelity test: [`design-handoff-fidelity-test.md`](design-handoff-fidelity-test.md).
- Superseded proposal: [`design-handoff-adopt-brief.md`](design-handoff-adopt-brief.md).
- Councils: [handoff](council/council-report-2026-06-09-design-handoff.html) · [audit](council/council-report-2026-06-09-audit.html) · [composition-fidelity (2026-06-19)](council/council-report-2026-06-19-adopt.html).
- Open work: [`BACKLOG.md`](../BACKLOG.md).
