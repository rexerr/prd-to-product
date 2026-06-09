# Council transcript — 2026-06-09 — FINAL AUDIT (post-fidelity-test)

Mapping (audit): `{"A": "The Architect", "B": "The Veteran", "C": "The Long View", "D": "The Skeptic", "E": "The Stranger"}`. Fidelity evidence: [`design-handoff-fidelity-test.md`](../design-handoff-fidelity-test.md). Report: [`council-report-2026-06-09-audit.html`](council-report-2026-06-09-audit.html).

## Framed question

Audit the refined plan with fidelity evidence in hand: the test returned **value-lossless but structurally non-isomorphic** (DSB's scale-first template fabricates shades; 3 vs 6 fonts; no tier for categorical accents / `--crt` / a toggle; one dark block vs base+twilight+3 surfaces+N colorways). Theming is mechanical. Plan: no 4th skill, no DSB mode; IF anything, a small token-adopt slash command (flat-primitives + thin alias layer + N theme blocks); recreation delegated to the bundle's README. Build now, defer until a 2nd bundle, or don't transcribe at all (reference the bundle)?

## Advisor verdicts (all five → defer / build nothing now)

- **The Skeptic** — right on no-skill/no-mode; wrong instinct on the command. N=1, format undefined at theme-vs-scratch; the bundle self-transcribes (README + `var()` alias), so a command only saves a copy-paste. Build nothing.
- **The Architect** — DEFER; authoritative artifact already exists; schema lock-in on n=1. Hand-do bundle #2, capture a docs checklist, Rule of Two before a command.
- **The Stranger** — lossless-values is the *opposite* of a win (transcription is `cp`); the structure is what doesn't fit, and the plan tools the mechanical part — backwards. Documented manual recipe; build nothing until proven twice.
- **The Long View** — the bundle's shape is the upstream's (a moving target); the *convention* (bundle-authoritative, kit references it) compounds, a transcriber depreciates. "Defer until bundle #2" ≈ "defer indefinitely," and that's the right outcome. Ship a one-page reference convention.
- **The Veteran** — "ingest external format" tools die by drift or by fabrication; the test caught the fabrication pre-ship. Defer to bundle #2; pressure-test "reference, don't transcribe" first.

## Peer review — votes

Strongest: **The Long View ×4**, The Skeptic ×1. Biggest blind spot: The Architect ×3, The Skeptic ×1, The Long View ×1.

## What the council collectively missed (the high-value gaps)

1. **Kit vs. product.** Every advisor said "reference the bundle." But the bundle is a **throwaway prototype export** — the real app needs tokens **in its own repo** to build. "Reference in place" is right for the kit and a fiction for the product; when the prototype is discarded, the reference points at a file that no longer exists.
2. **Command vs. saved prompt.** All five inherited the "importer rots" failure wholesale. A ~30-line command you re-run against a bundle you *hold* is a **saved prompt**, not a maintained generator — near-zero standing cost, cheap to write, cheap to delete. "Defer until proven twice" over-weights a lock-in risk that barely exists for a disposable re-runnable artifact.
3. **The fallback isn't free, and the mechanism is unspecified.** The endorsed manual recipe carries the **same n=1 schema-fitting risk** they condemn in the command, and "reference, don't transcribe" never names a mechanism (symlink? `@import`? pointer in CLAUDE.md?) — so the deliverable stays unbuilt.

## Chairman verdict

**Headline:** Don't build the command — but don't pretend "reference the bundle" is free either; ship the written fidelity baseline now and **copy the tokens into the product repo as a one-time `cp`**, because the prototype is disposable and the app has to build without it.

**Recommendation (reconciled):**
- **Keep killed:** the 4th skill and the DSB mode.
- **Don't build the command yet — right reason:** not because it's a dangerous importer (it's a saved prompt against a static bundle you own), but because at n=1 you can't separate theme from tweak-tool scratch, so you'd hardcode an N and a schema you can't validate. It's cheap to write later, which is *why* deferring costs nothing.
- **Ship now (not deferrable):** a one-time `cp` of the bundle's tokens into the product repo as its canonical `tokens.css` — not a symlink, not `@import`, not "reference in place." Lossless values make a literal copy safe. The bundle stays the source of record for component recreation (its README does that).
- **Write the recipe now as a recorded baseline, not a reusable tool:** the fidelity finding + manual steps as an *observation log* ("what this bundle required, where DSB's schema fabricated"), neutralizing the n=1-in-prose risk and giving bundle #2 a diff target.

Net: **kill two, defer one (cheaply), ship two now.**

**One thing to do first:** `cp` the bundle's tokens into the product repo as its own `tokens.css` (one-time, no symlink/import), and in the same commit drop the one-page fidelity baseline in the kit's docs.

## Alignment

| Advisor | Position | Argument |
|---|---|---|
| The Skeptic | Build nothing | N undefined + bundle self-transcribes; a command saves only a copy-paste — reference it. |
| The Architect | Defer, Rule of Two | Hand-do bundle #2, capture a checklist; command only after two real inputs. |
| The Stranger | Document, don't build | Transcription is `cp`; the structure is what doesn't fit — write the recipe, build nothing till proven twice. |
| The Long View | Defer indefinitely | Bundle-authority convention compounds; a transcriber depreciates on the next export schema. |
| The Veteran | Defer, pressure-test | Importers die by drift/fabrication; build on bundle #2, ask what a file buys over referencing. |

*Council session — 2026-06-09 (final audit).*
