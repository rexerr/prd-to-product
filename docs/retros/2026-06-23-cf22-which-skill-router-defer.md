# Retro — 2026-06-23 — CF-22 family router: planned, deferred (D-059)   (3rd session of the day)

Ran `/furnace-plan` on Wave-3 crib CF-22 (a `/which-skill` family router). The furnace preflight caught a recorded-decision boundary that reframed the task from "build it" to "should we build it" — and the answer, on the evidence, was **defer**. No skill was built; the work is a watching row + decision + the preserved plan.

## What was completed

- **Authored the CF-22 plan via `/furnace-plan`** ([plan](../../.claude/plans/radiant-soaring-yao.md)) — full build design for a thin explicit-invoke advisory router over the five invocable family skills, plus the defer path. Twice-baked: furnace preflight + one blind `Explore` review (which found only precision/presentation refinements), then Cowork `/plan-review` (Rex-run) — **Cowork caught one real factual error the blind cc-subagent missed** (see Verification).
- **Surfaced the crux as a decision-ready sign-off**, not a bare question: DEFER (A) / BUILD (B) / BUILD+escalate (C), with the D-014 boundary, the homework, and a recommendation (A). Rex picked **A**, matching the recommendation.
- **Logged [D-059](../DECISIONS.md#d-059)** — defer CF-22 to a `watching` row gated on an *observable* trigger (a logged skill-selection misfire, or the family opening beyond the single author). Resolved the original-task sub-fork in-plan: if ever built, it's a new skill in this repo only, never scaffolded into generated projects (architecture rule #3).
- **Paperwork:** CF-22 flipped to Deferred in the [pocock tracker](../cribs-from-pocock-craft.md); [roadmap](../cribs-adoption-roadmap.md) marker bumped (Wave-3 remaining: CF-21, C-01/C-02, C-07); BACKLOG Wave-3 `Next` updated + a CF-22 `watching` row added with the trigger; `DECISIONS_ACTIVE.md` marker bumped to D-059 (evaluated, not mirrored).

## Failure this session

- **Tag: bad substitution** (a codebase-fact claim not reconciled against the read). In the Path-B build spec I wrote "match the sibling shape (`furnace-plan`/`mine`)" *and* "set `disable-model-invocation: true`" — but I had **already read** both siblings' frontmatter this session and neither carries that field. I asserted two things that can't both be true without re-checking the read I'd just done. The blind cc-subagent missed it; **Cowork's `/plan-review` caught it.** It reached the plan but **shipped nothing** — Rex chose defer, and it's now corrected in D-059 + the shelved plan. This is exactly furnace preflight check 1 (cite every codebase claim to a read you ran), failing on a *reconciliation* step rather than a missing read: I had the read, I didn't diff my instruction against it. Generalizes as a watch-item — when a spec says "match X" and "also set Y," confirm X actually has Y before asserting both.
- **The other half went right:** the furnace's **preflight check 4 (diff against recorded decisions)** caught that CF-22 ≡ D-014's deliberately-gated fix-candidate B — the boundary the build would have crossed. Without it, the likely outcome was a speculative skill shipped against an unobserved failure. Second same-session instance of "the discipline turned a build into a justified non-build" (CF-29 → D-058 this morning).

## Verification — what it did and didn't cover

- **D-014 gate:** quoted verbatim from `docs/DECISIONS.md` line 166 (my own read, not the Explore agent's paraphrase) — the rule names "fix-candidate B smart-routing" and gates it on "soft handoffs observed dropped in a real run." Load-bearing; drove the whole decision.
- **Family inventory:** five invocable skills (chain ×3 + `furnace-plan` + `mine`); CEA off-surface (D-019), plan-review off-surface (D-042). Confirmed against `skills/*/SKILL.md` frontmatter + DECISIONS_ACTIVE reads.
- **No logged failure:** searched retros/board for an instance of the CF-22 failure mode — none found this session. This is the evidence the defer rests on; it's a "did-not-find," not a proof-of-absence, but sufficient at n=0 with a single author.
- **Blind review independence:** the `Explore` reviewer got only the plan path + acceptance criteria + rubric pointer (engineered blindness per D-035/G-11) — no author reasoning. It re-verified the inventory, the D-014 line, D-034, and D-058-as-highest independently, and surfaced two must-fixes (both presentation) + four refinements — **but missed** the frontmatter inconsistency below.
- **Cowork caught what the cc-subagent missed (calibration point):** Cowork's `/plan-review` flagged that the Path-B frontmatter spec was internally inconsistent — it asked to "match the sibling shape (`furnace-plan`/`mine`)" *and* "set `disable-model-invocation: true`," but neither sibling carries that field (they're explicit-invoke via the description prefix alone; whether the harness even honors the field is open, cribs line 82). Confirmed correct against the frontmatter I'd read earlier this session. This is textbook furnace-trial evidence: the in-session blind pre-filter catches presentation/precision; Cowork catches the real factual error (consistent with [D-043](../DECISIONS.md#d-043)). Corrected in [D-059](../DECISIONS.md#d-059)'s build-shape note and the shelved plan so a future build won't inherit it. The error was in the *shelved* build design only — it shipped nothing, since Rex chose defer.
- **D-NNN number:** re-grepped at write time (rule 1a) — D-058 highest, so D-059. Confirmed.
- **Did NOT cover:** cross-reference resolution of the new D-059 + board edits (doing it next, below); the plan's display links use `../../Sites/...` forms that are plan-file-only (the would-be SKILL.md links are noted as repo-relative, but no SKILL.md was written).

## Key decisions made

- **[D-059](../DECISIONS.md#d-059)** — defer CF-22; gated on observed failure or multi-user opening. Not council-gated (low-reversal-cost build-vs-don't). Not mirrored (no new agent-facing rule).
- **Sub-fork resolved:** router would be a this-repo skill, not a generator-scaffolded pattern.

## Open items

- **Wave-3 remaining:** CF-21 (wrapper+engine variant composition), C-01/C-02 (furnace-plan citation graph / anti-bulk-accept), C-07 (destructive-regen guard, gated on confirming D-005/D-006 don't already cover it) — each its own `/furnace-plan`.
- **CF-22 watching trigger** is live on the board; if it fires, the build design is ready in the furnace plan (no re-planning needed).

## Next session

- Pick the next Wave-3 crib. C-07 (destructive-regen guard) is worth checking first — it may already be covered by the D-005/D-006 write guard, in which case it's another fast satisfied-by-construction close like CF-29.
