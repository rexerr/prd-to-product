# Retro — 2026-06-21 08:52 CDT — CF-29 per-artifact FORMAT file, piloted on prd-creator (furnace-trial calibration pass)   (2nd session of the day)

First Wave-3 crib adoption, run as the furnace-trial calibration pass the [furnace-trial ticket](../../tickets/furnace-trial.md) Next #1 called for. Decision: [D-052](../DECISIONS.md). Plan: `~/.claude/plans/ethereal-orbiting-hollerith.md` (kept through 4 revisions).

## What was completed

- **CF-29 piloted on prd-creator/PRD.md** — new [`PRD-FORMAT.md`](../../skills/prd-creator/PRD-FORMAT.md) consolidates the scattered PRD shape-contract (12-core + 2-optional skeleton, per-section + style + content rules, hand-off contract); the reference-side bodies moved out of `principles.md` (×4 sections → pointers); FORMAT authoritative-on-conflict. Runtime-firing preserved (Camp-A operative rules stay in the loaded template). Closed a latent 11/12/14 section-count drift. Scope, design, and the four sign-off riders are in [D-052](../DECISIONS.md) and the plan — not restated here (CF-06).
- **Furnace-trial calibration pass executed** — raw plan → Cowork un-pre-filtered; the blind cc-subagent ran for measurement only, withheld from Cowork. 4 Cowork rounds, each a real catch, converging.
- **Bookkeeping:** D-052 logged (not mirrored); CF-29 → `Piloted (→ D-052)` in the pocock tracker; roadmap marker bumped; Cowork's 11-row ledger append present in the working tree (D-018 carve-out — swept to its own commit).

## The calibration finding (the point of the pass)

The cc-subagent (round 0, blind, on the raw plan) surfaced **none** of the must-fixes Cowork caught across 4 rounds — it returned should-considers + could-not-verifies, no must-fix. Cowork found 5 must-fixes total (false-RED verification, the section-count drift, the runtime-loading gap, the r2 premise error, the Camp-B grep-scope error). **Reading:** the in-session pre-filter is not a Cowork substitute on this plan — consistent with [D-043](../DECISIONS.md). The divergence argues *for* keeping Cowork the oracle, not against it.

**Mechanics wrinkle worth recording:** the calibration design (withhold the subagent log from Cowork so both grade raw) also prevents Cowork — the **sole** ledger writer (D-043) — from transcribing `cc-subagent` rows. So this plan's ledger has `cowork` rows but no `cc-subagent` rows; the subagent's round-0 findings live only in the session transcript. A clean same-plan divergence number needs both reviewers' rows; the sole-writer + withhold combination can't produce them in one pass without a separate transcription step Rex feeds back to Cowork. Flag for the furnace-trial ticket.

## Failure this session

- **Tag: bad substitution (near-miss — caught in plan mode, never reached product).**
- **Name the artifact.** Twice I asserted *where a rule lives* from an **under-scoped grep**, and Cowork caught both: (round 3) "style rules are not in the loaded template" from `grep templates/PRD.md.template` — true for the template but I'd implied they were unloaded *everywhere*; (round 4) "sentence-case lives only in unloaded principles" — a repo-wide grep showed `SKILL.md:55` (boot/loaded) carries it. Same class both times: I ran the read (furnace Check 1) but **scoped it to the file I expected the answer in**, not repo-wide.
- **Tool or agent?** Agent judgment — the furnace preflight Check 1 ("cite every codebase claim to a read") passed because a read *existed*; it doesn't force the read to be *broad enough* to ground a "lives only in X" claim.
- **Does it generalize?** Yes — any "X is the only place Y appears" claim is false-able by a wider grep; n=2 in one session is a real pattern.
- **→ The change it demands:** a furnace-preflight sharpening candidate — **"a *negative/exhaustive* claim ('only in X', 'appears nowhere else', 'not loaded anywhere') must be backed by a repo-wide grep, not a single-file one."** Rule-of-Two is met *within this session* (n=2), but both instances were the same plan under iterative review, so I'm logging it as a **candidate**, not auto-adopting — promote to a furnace Check-1 sub-case if it recurs in a *separate* furnace plan. (Avoids the ceremony-accretion the tag-log instrument guards against.)

## Files changed

- [`skills/prd-creator/PRD-FORMAT.md`](../../skills/prd-creator/PRD-FORMAT.md) — new; the consolidated shape contract.
- [`skills/prd-creator/principles.md`](../../skills/prd-creator/principles.md) — 4 sections thinned to rationale + pointers (move-not-duplicate).
- [`skills/prd-creator/templates/PRD.md.template`](../../skills/prd-creator/templates/PRD.md.template) — header pointer; line-48 inbound pointer redirected to FORMAT; operative cues kept.
- [`skills/prd-creator/SKILL.md`](../../skills/prd-creator/SKILL.md) — FORMAT entry added; sentence-case thin-mention kept + pointer.
- [`skills/prd-creator/NOTES.md`](../../skills/prd-creator/NOTES.md) — tests 1–3 point at FORMAT; test 1 corrected to 12-core; line-21 note frozen as historical.
- [`skills/prd-creator/generator/decisions.md`](../../skills/prd-creator/generator/decisions.md) — one-line section-name authority pointer.
- [`docs/DECISIONS.md`](../DECISIONS.md), [`docs/cribs-from-pocock-craft.md`](../cribs-from-pocock-craft.md), [`docs/cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md) — bookkeeping.
- [`skills/furnace-plan/trial-ledger.md`](../../skills/furnace-plan/trial-ledger.md) — Cowork's measurement append (D-018; not authored by this session, swept separately).

## Key decisions made

- [D-052](../DECISIONS.md) — CF-29 piloted on prd-creator; reference-only FORMAT; Camp-B rules left reference-only; propagation deferred Rule-of-Two. (Not mirrored — craft-structure, self-evident on read.)

## Open items

- **Furnace-trial:** record this calibration's divergence (cc-subagent 0 must-fix vs Cowork 5) in the ticket; resolve the sole-writer-vs-withhold mechanics wrinkle (how `cc-subagent` rows get into the ledger for a withheld-log calibration). The furnace-preflight repo-wide-grep candidate above rides the same ticket.
- **CF-29 propagation:** DSB `DESIGN_SYSTEM.md` FORMAT file, then a *scoped* context-engineering subset (which artifact types, not all ~25) — each its own pass, gated on this pilot proving out.
- **`context-engineering/NOTES.md:70`** carries the same stale "eleven-section" phrasing — fold into the deferred context-engineering FORMAT slice.

## Next session

- Pick up the furnace-trial ledger reconciliation (the mechanics wrinkle above), or open the DSB CF-29 propagation with `/furnace-plan`. PRD-FORMAT pilot is the live evidence for whether the consolidation earns propagation.
