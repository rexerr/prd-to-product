# Retro — 2026-06-18 23:10 CDT — Wave-2 Sprint 3, CF-13 fire-wired-behavior bullet (10th session of the day)

## What was completed

Adopted **CF-13** ("dynamic final-step self-exercise") into the `context-engineering` scaffolded verification rule. Authored via `/furnace-plan`; Cowork-reviewed across **2 rounds** (rev-1 → 3 must-fixes; rev-2 → 0 must-fixes, 2 refinements applied as rev-3); Rex approved Option A. See [D-041](../DECISIONS.md); not restated here (CF-06).

- One **unconditional** bullet — "Wired-up behavior must be fired, not inferred" — added to "Verification before claiming done" in **both** rule shapes (`claude-rules-modular/session-discipline.md.template`, `claude-rules-flat-CLAUDE.md.template`), placed **before all OPTIONAL markers** so it survives every gate combination, plus a compressed fold into the one flat fixture `output-small/CLAUDE.md:50`.
- Scope finding that shaped it: CF-13 was **mostly already practiced** — the hook-firing (H) reading is already in `generator/output-summary.md` §2 and this repo's `CLAUDE.md:72`; furnace-plan Check 2 already condemns inspection-that-can't-reach-the-test. The only net-new gap was the scaffolded rule. So **Option A** (scaffolded rule only); furnace-plan landing deferred as near-covered (Rule of Two).
- Bookkeeping: CF-13 → `Adopted (→D-041)`; roadmap marker bumped; BACKLOG S3 line updated; out-of-scope finding logged to BACKLOG + D-041.

## Failure this session

- **Tag: bad substitution (dominant) — really an assert-without-read miss at the preflight layer.** My rev-1 furnace preflight shipped a **verification methodology that rested on a false premise**: it asserted a dry-run substitution of the flat template would diff "clean (no new bullet)" against `output-small/CLAUDE.md`. But `output-small` is **hand-written and compressed** (`CLAUDE.md:23`), not a template render — the flat template's Session-discipline is 11 `###` subsections, the example collapses it to a 14-bullet list. The stated RED/GREEN was unreachable, and a literal attempt risked expanding the example to template-verbatim (whole-section rewrite). Caught by Cowork R1 MF1.
  - **Name the artifact.** The rev-1 plan's Verification §1 ("diff vs current output-small → clean") — an assertion about the template↔example *relationship* I never read `CLAUDE.md:23` to verify.
  - **Tool or agent?** Agent — I took the Explore agent's summary of `output-small`'s contents as if it established the example was a *render* of the template; it didn't, and I didn't check.
  - **Second miss, same class:** rev-1 said "append the bullet" to the modular Verification section without tracing the OPTIONAL-marker structure — which would have landed it inside the `tooling_check` gate (dropped when `has_check_script == false`). Caught by Cowork R1 MF2/MF3.
  - **→ The change it demands:** Check 1 must bite on the **verification plan's own premises**, not just the plan's body claims — "a dry-run diffs clean" is a codebase-relationship claim that needs a read (here: is the example a render or hand-written?). Logged as a furnace Check-1 candidate at *propose* (below).

- **Furnace-trial signal.** Cowork CF-13 catches classified: **R1 = two bucket-1** (forcing-function underperformed — the verification-premise miss and the marker-placement miss were both assert-without-read that Check 1 *should* have forced); **R2 = two bucket-3 refinements** (soften "empirically settles" given no executable generator; flag the latent OPTIONAL-gating candidate as parse-conditional + cover both templates — correctly Cowork's judgment layer). No bucket-2. The bucket-1 pair is the third data point pushing the same direction as the DG-01 session's completeness-claim miss: **the preflight under-forces verification of claims about repo structure/relationships.** Held at *propose* — mid-trial instrument, Rule of Two. Cowork owns the ledger; the 6 CF-13 rows it wrote are swept in a dedicated commit before the product commit (D-018).

## What verification did and did not cover

- **Covered:** gates-off render (self-consistency, not independent — no executable generator per `CLAUDE.md:23/77`) confirmed the new bullet survives in both shapes with `uses_visual_confirmation_gate == false` AND `has_check_script == false`; eyeball-delta confirmed `output-small:50` changed only by the wired-behavior clause; no `PARAMETERIZE` introduced.
- **Did not cover:** the actual single-line-vs-contiguous-block parse of OPTIONAL markers (no executable generator to settle it) — routed to BACKLOG as a parse-conditional candidate, and CF-13's own bullet is unaffected because it sits before all markers.

## Files changed

3 product files (2 rule templates + `output-small/CLAUDE.md`) + 4 bookkeeping (DECISIONS, pocock crib tracker, roadmap, BACKLOG) + this retro. Cowork's `trial-ledger.md` append swept separately (D-018). Exact paths in `git status`; not enumerated (CF-06).

## Key decisions made

- [D-041](../DECISIONS.md) — CF-13 adopted as an unconditional fire-wired-behavior bullet in the scaffolded verification rule (Option A); furnace-plan landing deferred as near-covered. Not mirrored to `DECISIONS_ACTIVE.md` (template content; D-039/D-040 precedent).

## Open items

- **Furnace Check-1 sharpening** — now **three** candidates at *propose*: string/equality precision (CF-03), completeness/enumeration (DG-01), and **verification-plan-premise** (this session — Check 1 should force a read behind "a dry-run diffs clean" / "X is a render of Y"). For the next trial review to weigh against the scorecard; not adopted (gated SKILL.md edit, mid-trial).
- **OPTIONAL-marker gating candidate** — parse-conditional latent issue in both rule templates (universal "Never claim success…" sentence in modular, logic bullet in flat may drop for no-visual projects). Logged to BACKLOG; settle gating semantics before fixing; cover both surfaces.
- **Wave 2 continues.** S3 remaining: G-14\* + AB-03; then S4 DSB (G-19), solo CF-07.
- **Commit hygiene** — Cowork's `trial-ledger.md` append gets its own "Sweep Cowork ledger append" commit before the product commit (D-018).
- **No push this session** — commits staged locally; push when asked.

## Next session

- Continue S3 — next is **G-14\*** (the ~40-file provenance-banner sweep with the JSON-can't-comment fork; needs its own scoping) or **AB-03**. Open with `/furnace-plan`.
