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

## The manual playbook (what to actually do with a bundle)

This is a **product-side** procedure — it runs in the real app's repo, **not** in this kit. Nothing here modifies `prd-to-product`.

1. **Recreate components from the bundle, per its README** — pixel-perfect in the target stack, not by copying the prototype's structure. The bundle stays the **source of record** for component recreation and visual ground truth (screenshots + the live prototype).
2. **`cp` the token values into the product repo.** The real app needs tokens **in its own repo** to build; a Claude Design bundle is a disposable export. Because the values are lossless, a literal copy of the `:root` custom properties into the product's own CSS is safe — keep the bundle's structure rather than forcing it into the scale-first template.
3. **Keep the bundle as the design source of record** for anything not yet transcribed (theming variants, motion, the screenshots). Do not treat the `cp`'d tokens as the canonical design — the bundle is.
4. **Tailwind:** the bundle is vanilla CSS-vars. Do **not** translate to Tailwind during adoption; carry the custom-property system across as-is.

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
- Councils: [handoff](council/council-report-2026-06-09-design-handoff.html) · [audit](council/council-report-2026-06-09-audit.html).
- Open work: [`BACKLOG.md`](../BACKLOG.md).
