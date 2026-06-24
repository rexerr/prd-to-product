# Retro — 2026-06-24 ~13:30 UTC — no-jargon-leak scan ported to CE + DSB (D-064); blind-review taint caught

`/furnace-plan`'d and shipped the no-jargon-leak slice of the council's invariant/semantic-checks backlog item (Seq 2). Ported prd-creator's existing "Scaffolding-leak scan before finalizing" (a mechanical category-grep run before writing) to `context-engineering` and `design-system-bootstrap`, which had the prose rule but no mechanical backstop. The scan surfaced a real shipped leak — `(Q7c)`, an internal intake label hardcoded into a user-facing CSS comment — now fixed. Logged [D-064](../DECISIONS.md#d-064).

## What was completed

- **Scan ported to both skills** — new `## Scaffolding-leak scan before finalizing` in `context-engineering/generator/decisions.md` and `design-system-bootstrap/generator/decisions.md`, plus a cross-ref at DSB intake.md's `8c. Confirm before writing`. Category patterns: `[Cc]luster [0-9]`, `Q[0-9][a-z]`, `state.?map`, the comment-marker form of `PARAMETERIZE`/`OPTIONAL`, and `D-0[0-9]` scoped by content region. All three skills now carry the scan (parity grep confirms).
- **Real leak fixed** — `(Q7c)` removed from `globals.css.template:68,81` and the rendered fixture. RED→GREEN verified (`grep -niE 'Q[0-9][a-z]'` hit the fixture live, clean after fix).
- **No false positives** — both `output-small` fixtures grepped clean under all five patterns; confirmed the marker pattern does NOT flag the English word "optional" ("optional layout slots" in DESIGN_SYSTEM.md).
- **Paperwork** — [D-064](../DECISIONS.md#d-064) logged (not mirrored — visible by reading the skills); DECISIONS_ACTIVE marker bumped to D-064; [BACKLOG](../../BACKLOG.md) row updated (no-jargon-leak done; provenance-grounded (2c) remains the open slice). 8 product/doc files; Cowork's 6-row ledger append swept separately (D-018).

## Failure this session — tag: lost context (process discipline)

**The blind review was run wrong, and it took Rex to catch it.** The furnace skill is explicit: the reviewer prompt contains ONLY (1) plan path, (2) acceptance criteria in plain language, (3) the rubric-pointer instruction — *"Pass nothing else. Do not paste your reasoning."* I added a verification bullet that **handed the reviewer my own findings** ("confirm prd-creator's scan at decisions.md:101–114, the (Q7c) occurrences…") and never pinned the model, so it likely ran on Haiku. A weak reviewer given an answer key can only rubber-stamp — exactly the anchoring (G-11 / [D-035](../DECISIONS.md)) the step exists to prevent.

- **Tool or agent?** Agent. The skill instruction was unambiguous; I didn't follow it.
- **The proof it mattered:** after Rex flagged it, I re-ran clean (neutral goal-level prompt, pinned to Opus). The clean pass **caught a real issue the tainted one missed** — the `D-0[0-9]` exception described the generator's internal files, not the emitted output the scan targets. Same plan, same reviewer type; the only variables were prompt hygiene and model. That comparison is the cleanest possible evidence for the discipline.
- **Does it generalize?** Two fixes: (1) execution — keep the reviewer prompt strictly to the three permitted elements (no findings, no reasoning); (2) a genuine **skill gap** — furnace-plan says "Explore type" but doesn't pin a capable model, and Explore defaulted to a weak one. Pinning the reviewer model is a real `furnace-plan` improvement (logged as next-step, not done this session — it's a shipped-product self-edit needing its own scope gate).

## Verification — what it did and didn't cover

- **Red-capable, observed:** the `(Q7c)` grep went red on live shipped output before the fix, green after. Both fixtures clean under all five patterns; planted-leak test confirms the patterns catch real hits.
- **Independent review:** blind Opus reviewer (clean prompt) + Cowork `/plan-review`. The first (tainted) blind pass was discarded as procedurally invalid.
- **Did NOT cover:** the scan is a manual pre-write grep with no executable harness (no test runner in this repo) — no code enforces that a future agent actually runs it at the pre-write gate. Same trust model prd-creator's scan already runs on; Cowork flagged this as inherent. Also surfaced but NOT chased (out of scope): a possible divergence between `docs/DECISIONS.md.template:40` ("Numbered D-001, D-002") and the `output-small` DECISIONS.md (no numbering).

## Key decisions

- **[D-064](../DECISIONS.md#d-064)** — no-jargon-leak (council 2b) shipped by porting prd-creator's category-grep scan to the other two generators; form fixed as category/anchored patterns, never a literal word-list; provenance-grounded (2c) deferred. Not council-gated (additive enforcement of D-010), not mirrored.

## Next session

- **Pin the furnace-plan blind reviewer to a capable model** (and reinforce "pass only the three elements") — a `furnace-plan` SKILL.md self-edit, scope-gated. Today's taint miss is the evidence. Possible BACKLOG row if not done immediately.
- Open slice on the board: **provenance-grounded check (2c)** — the remaining half of the invariant/semantic-checks item, likely sharing this scan's pre-write gate.
