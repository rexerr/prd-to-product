<!-- Synced through: C-41 (steinberger) · CF-29/16-keepers (pocock-craft) · DG-02 (designer) · AB-03/AB-i3 (claude-skill-bundles) — 2026-06-18; CF-03 adopted (→D-023) 2026-06-17; C-09 + CF-06 adopted (→D-024) 2026-06-18; C-14 adopted (→D-025) 2026-06-18; C-10 adopted (→D-026) 2026-06-18; CF-04 adopted (→D-027) 2026-06-18; C-15 adopted (→D-028) 2026-06-18; CF-02 adopted (→D-029) 2026-06-18; DG-02 declined-and-parked (→D-030) 2026-06-18 — Wave 1 cribs all resolved. gstack mined + adversarially verified 2026-06-18 (G-01–G-21; 7 survivors → Wave 2). Wave-2 Sprint 1 underway: C-16 adopted (→D-031) 2026-06-18; G-16 adopted (→D-032) + G-01 adopted-as-revised (→D-032) 2026-06-18; CF-15 deferred from Sprint 1 (near-no-op on furnace-plan; stays Proposed); CF-20 adopted (→D-033) 2026-06-18; CF-23 adopted (→D-034, mirrored to DECISIONS_ACTIVE) 2026-06-18; G-11 adopted (→D-035) 2026-06-18 — Sprint 1 complete (C-16/G-16/G-01/CF-20/CF-23/G-11 adopted, CF-15 deferred). Wave-2 Sprint 2 complete (prd-creator surface): CF-18 adopted (→D-036, rule 1 scoped) + G-06 adopted (→D-037) + G-08 adopted (→D-038) 2026-06-18. Wave-2 Sprint 3 (context-engineering surface) underway: C-09/CF-06/C-14 retro-template backport into the scaffolded template + `output-small` fixture (→D-039) 2026-06-18; DG-01 even-coverage synthesis rule adopted as a conditional modular `.claude/rules` scaffold, Q35a-gated (→D-040) 2026-06-18; remaining S3 = CF-13 + G-14* + AB-03. Update this marker whenever a source tracker gains cribs or a crib changes status. -->

# Cribs adoption roadmap — one strategy across all four trackers

**Read this when:** deciding what crib-work to do next, or at session start to see the current wave.

The four crib trackers are **inventories** (what exists, organized by source). This file is the **strategy** (what to adopt, in what order, how to verify, and how it stays out of the cracks). It deliberately does **not** copy the cribs — it points to them, so there is one source of truth per crib and one prioritized plan over all of them.

> **Why a roadmap and not one merged file.** Merging the inventories would destroy the per-source provenance (who mined what, against which failure) and the Steinberger sheet is already "effectively complete." Keeping four source-organized trackers + one thin pointer-roadmap is the C-19 move (pointer, never copy). This roadmap is the only place that *sequences across* sources.

## The trackers it sequences

| Tracker | IDs | Source | Status |
|---|---|---|---|
| [`cribs-from-steinberger-ecosystem.md`](cribs-from-steinberger-ecosystem.md) | `C-01`–`C-41` | Van Horn / Steinberger ecosystem | Mining complete; 5 adopted (C-27→D-017, C-09→D-024, C-14→D-025, C-10→D-026, C-15→D-028), rest standing |
| [`cribs-from-pocock-craft.md`](cribs-from-pocock-craft.md) | `CF-01`–`CF-29` (22 live) | Pocock + Ciemborowicz | Mined + 6-lens re-mined 2026-06-17; 4 adopted (CF-03→D-023, CF-06→D-024, CF-04→D-027, CF-02→D-029), rest Proposed |
| [`cribs-from-designer-skills.md`](cribs-from-designer-skills.md) | `DG-01`–`DG-02` (+ investigates) | Owl-Listener (MC Dean) | Mined 2026-06-17; thin yield; DG-02 declined (→D-030), DG-01 Proposed |
| [`cribs-from-claude-skill-bundles.md`](cribs-from-claude-skill-bundles.md) | `AB-01`–`AB-03` (+ investigates) | Claude first-party engineering/design/data bundles | Mined 2026-06-18 (before connector disconnect); thin yield; all Proposed. Source not re-fetchable — frozen in `harness-domain-notes.md` |
| [`cribs/cribs-from-gstack.md`](cribs/cribs-from-gstack.md) | `G-01`–`G-21` (G-17 retired) | `garrytan/gstack` (MIT) | Mined + adversarially verified 2026-06-18; 7 survive / 8 revise / 3 park / 2 refuted (G-02 no-op, G-10 misread). Survivors sequenced into Wave 2 below |

---

## The adoption lifecycle — what to do, when

A crib moves `Proposed → Adopted` by one repeatable loop. Do **not** batch-adopt; one crib (or one tight cluster) per pass.

1. **Pick** the top un-started item from the **current wave** (named in `BACKLOG.md`). Don't skip ahead a wave — waves are ordered by leverage-per-effort and by dependency.
2. **Scope-gate it.** A cheap-edit crib (Wave 1) runs inside the normal scope gate. A structural crib (Wave 3) or a Big Rock gets `/furnace-plan` first. Recommend a **council** only for a genuine fork (the AGENTS.md flip, touching D-001) — never for a prose edit.
3. **Edit** the named landing surface only.
4. **Verify** per the crib's verification class (below). No "looks correct."
5. **Ship:** flip the crib's Status to `Adopted (→ D-NNN)` in its *source tracker*, log `D-NNN` in `DECISIONS.md` (mirror to `DECISIONS_ACTIVE.md` if it's a binding constraint), and bump this file's sync marker if the wave advanced.
6. **Record** it in the session retro (per the retro convention).

## Verification playbook — how to test each class

Every crib falls into one class; this maps the CLAUDE.md "Verification before claiming done" contract onto crib-work so "how do I test it" is answered once.

| Class | Crib kind | How to verify |
|---|---|---|
| **(T) Template/rule/skill** | a change to what a skill scaffolds or emits | dry-run the substitution; **diff against `skills/context-engineering/examples/output-small/`**; the golden tree must change only where intended (C-08 spirit) |
| **(H) Hook/gate** | a `.claude/` hook or `settings.json` gate | copy the emitted script to `/tmp/<test>/`, **live-fire each blocked op in a fresh session**, confirm it fires *and* doesn't block legitimate ops ([D-017 contract](retros/2026-05-10-phase-1-validation.md)) |
| **(D) Doc/convention** | a CLAUDE.md / retro-template / DECISIONS convention | re-read after editing; **confirm every cross-reference resolves**; check no duplicated content drifts from its source (CF-06) |

---

## The waves — what order

Ordered by leverage-per-effort, then dependency. Each row: crib(s) · landing surface · verification class. **Pull from the lowest open wave first.**

### Wave 1 — cheap wins (each a sub-50-line edit that closes a live latent failure)

| Crib | Lands on | Class |
|---|---|---|
| `C-14` dated/named/quoted-artifact failure tags | the failure-tag doctrine (`docs/retros/README.md`, principles, SKILL.md) | (D) |
| `C-15` hoist binding contracts to the top | each multi-section SKILL.md | (T) |
| `C-09` retro "→ durable work unit" columns | `docs/retros/README.md` template | (D) |
| `C-10` freshness/sync marker on curated mirrors | `DECISIONS_ACTIVE.md` | (D) |
| `CF-03` red-capable-repro gate + tagged debug logs | CLAUDE.md "Reproduce before fixing" | (D) |
| `CF-02` durable-PRD rules (no stale paths; Testing Decisions) | prd-creator output discipline | (T) |
| `CF-06` de-dup-by-reference retro/handoff rule | `docs/retros/README.md` + `end-session` | (D) |
| `CF-04` concept-keyed declined-ledger | DECISIONS "Declined" + the parked sections of these trackers | (D) |
| `DG-02` semantic-not-directional token naming | design-system-bootstrap | (T) · *first resolve: is RTL in DSB scope?* |

### Wave 2 — high-value medium (bigger, high leverage)

| Crib | Lands on | Class |
|---|---|---|
| `C-16` decision-ready handoff brief | furnace-plan → Cowork/Rex handoff | (D) |
| `CF-18` interview discipline (recommended-answer / explainer / explore-first) | prd-creator interview | (T) |
| `CF-13` dynamic final-step self-exercise | context-engineering, furnace-plan verification | (T)/(H) |
| `CF-15` two-axis review, no-cross-rerank | furnace-plan ledger, retros | (D) |
| `CF-20` skill self-skip gate | furnace-plan, prd-creator | (T) |
| `CF-23` two-load model for the invocation cut | skill-authoring (chain vs non-chain) | (D) |
| `CF-07` source-immutability & merge-on-re-run | co-edited-doc rules; generator re-run path | (T) |
| `DG-01` even-coverage synthesis rule | context-engineering `.claude/rules` (also hardens our own fan-out) | (T) |
| `AB-03` per-project-type red-capable-repro definitions *(rides CF-03 — fold in at/after CF-03)* | CLAUDE.md "Reproduce before fixing" + generated harness repro rule | (D) |

**gstack survivors — added 2026-06-18, adversarially verified (default-refuted skeptic, real-file evidence; verdicts in [`cribs/cribs-from-gstack.md`](cribs/cribs-from-gstack.md) § Adversarial verification). Pull as a cohort into the next furnace-plan. 6 actionable + 1 blocked.**

| Crib | Lands on | Class |
|---|---|---|
| `G-16` mandatory unresolved-decisions terminal sentinel (last ledger line = `NO UNRESOLVED DECISIONS` or an enumerated block; unbolded) | furnace-plan ledger spec | (T) |
| `G-08` semantic-leak checklist before finalizing (5 categories) | prd-creator output gate — *drop gstack's regex/audit-sink infra; checklist only* | (T) |
| `G-06` anti-sycophancy posture (banned-hedge list + take-a-position-and-name-what-would-change-it) | prd-creator interview conduct — *keep the brainstorm-divergence carve-out explicit* | (T) |
| `G-11` engineered-blindness verifier (withhold your reasoning; pass artifact + criteria only; named self-verify fallback) | CLAUDE.md delegate-to-subagent line | (D) |
| `G-19` memorable-thing positioning anchor + falsifiable design rationale (cite an observable, not a vibe) | design-system-bootstrap DESIGN_SYSTEM.md companion (the C-39 doc) | (T) |
| `G-14` generated-file provenance banner | context-engineering emitted files + `output-small` — *INVERT gstack's wording → "safe to hand-edit; re-run to regenerate shape"; cite hand-edit-in-ignorance, not clobber (D-005 owns clobber)* | (T) |
| `G-18` fence external reviewer off instruction-bearing files (`skills/**/SKILL.md`) | the `C-24` oracle/council prompt — **BLOCKED: that prompt template isn't built yet; adopt when it is** | (D) |

> **Sequencing note (gstack cohort).** All are sub-50-line edits. Cleanest single-file first: `G-16` (furnace-plan) and `G-11` (CLAUDE.md). `G-18` rides on `C-24` (Wave 3 / unbuilt) — don't plan it standalone. The 8 REVISE-tier gstack cribs are *not* here: they survived only as one-to-three-line sharpenings or folds into existing cribs (C-18/CF-13, C-22) and are recorded in the tracker, not given wave slots.

### Wave 3 — real build (net-new structure; `/furnace-plan` each)

| Crib | Lands on | Class |
|---|---|---|
| `CF-29` per-artifact FORMAT file *(the one `implement`)* | context-engineering, prd-creator, DSB | (T) |
| `CF-22` family router `/which-skill` | over the chain + non-chain family | (T) |
| `CF-21` wrapper + engine variant composition | furnace-plan family | (T) |
| `C-01` R/KTD citation graph | furnace-plan + the Cowork loop | (D) |
| `C-02` anti-bulk-accept primitives | furnace-plan ledger | (D) |
| `C-07` destructive-regen guard | context-engineering (after confirming D-005/D-006 cover) | (H) |

### Big Rocks — each its own decision + plan (gated on Rex)

- **AGENTS.md-canonical flip** — decided 2026-06-17, not executed; a real migration (`/furnace-plan` it). Council-grade was the bar to *decide*; it's decided, so execution is a planning task.
- **Build the `solutions/` scar-tissue library** (decision #3) — the biggest unbuilt thing; **unblocks `CF-05`** (rule-compression method) and is the home for `C-14`-tagged failure cards.
- **`CF-05` rule-compression method** — gated on the `solutions/` library existing.
- **`AB-01` mobile (React Native/Expo) project type** and **`AB-02` data/analytics project type** — each *expands what project types the generator scaffolds*, which is the shape-vs-content fork (how much domain content a "scaffolds shape, not content" generator bakes in — architecture rule #3). **Council before building** per D-009; then `/furnace-plan` each. Full harvested content frozen in [`harness-domain-notes.md`](harness-domain-notes.md).

**Parked (not scheduled):** the investigate-tier and useful-someday items in each tracker's "Parked / Investigate" sections. They re-enter a wave only when their open question is resolved — they are *not* lost (that's the CF-04 discipline), but they don't get a wave slot until promoted.

---

## How this stays out of the cracks

Three mechanisms, so crib-work doesn't lose to the rest of `BACKLOG.md`:

1. **One standing BACKLOG row** points here and names the **current wave** — surfaced every session start (CLAUDE.md reads BACKLOG first). The backlog never lists individual cribs (no context rent, C-12); it points.
2. **This file's sync marker** (top) tells you at a glance whether the roadmap is current with the trackers; a wave advancing or a new mine bumps it.
3. **Status lives in the source tracker**, not here — so there's no drift between "is it adopted" and the crib itself. This roadmap only sequences; it never tracks state.

> **Ratified as [D-022](DECISIONS.md)** (2026-06-17) — this roadmap's lifecycle + wave discipline is a recorded decision, not just a doc. The three trackers stay source-organized inventories; this file is the only cross-source sequencing layer.
