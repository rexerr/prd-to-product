# Retro — 2026-07-01 — Client-work OS: evidence-backed filing (Theragen harvest)   (5th session of the day)

**Dominant failure tag: none.** A file-and-decide session (explicitly not a build). No product/skill/generator code touched; everything landed as evidence docs, a ticket, and board rows. One process note below on the mid-session scope expansion.

## What happened

Advanced the backlog row "Client-work OS project type (Every mine)" with first-party evidence from the live **Theragen ActaStim Sync 3.0** engagement — the first harvest of the build-bespoke-then-harvest strategy.

1. **Scope-gated open.** Read the two initial Desktop docs (harvest + PRD brief), the target row, `DECISIONS_ACTIVE`, latest retro; presented a scope check; Rex approved + agreed the two calls (no `D-NNN`; import the Desktop docs for durability).
2. **First filing.** Copied harvest + PRD brief into `docs/product-briefs/`; wrote `tickets/client-work-os.md`; upgraded the anchor row (secondhand → evidence-backed, `gate:council`); folded `/mine` cross-source reconciliation into the `/mine` hardening row; added a thin iced `friday-postcard` row (confirmed none existed).
3. **Three more docs arrived** (system brief, build-sequence brief, skill-gaps brief) with "commit." They materially sharpened the structure, so I folded before committing rather than commit a coarser version: enriched the ticket into a **two-track** model, copied the three briefs in, and added a **skill-gaps self-instrumenting** board row.

## The real insight the extra docs surfaced

The council fork is **downstream**, not upstream of everything. My first ticket collapsed the whole direction into one `gate:council` block. The briefs show two tracks:
- **Track B (incremental, reversible, no-council, already live):** scaffold Theragen, engagement + personal routines, and the skill-gaps instrumentation — these *generate* the evidence.
- **Track A (costly, hard-to-reverse, council-gated):** does context-engineering get a dedicated research-design *mode* — decided *from* that evidence at harvest time (Phase 3).

And the **skill-gaps mechanism is now unblocked** — its hard dependency (the context-lifecycle ticket) landed 2026-06-20 ([D-048](../DECISIONS.md#d-048)). That's the near-term actionable, so it earned its own board row rather than staying buried in a council-gated ticket.

## Gates (the session's explicit ask)

- **Context-lifecycle: CLEARED** in-repo (D-048, 2026-06-20). The harvest's "queued behind the context-lifecycle ticket" is Theragen-workspace sequencing — external; noted so it's not read as a live in-repo dependency.
- **Council: OPEN and flagged** on Track A (mode-vs-standalone), not auto-run.

## Verification

- `render-backlog-kanban.py`: **0 tag warnings** after every board edit. `check-live-links.py`: **clean** (122 → 125 live docs, no broken links).
- **No dry-run against `output-small/`** — correct: zero skill/template *product* edited. **No `D-NNN`** — gated direction, not a committed build (project-setup precedent); the visibility/sensitivity + skill-gaps DECISIONS entries are build-time.
- Self-verified — no independent sub-task verifier on the synthesis.

## Process note / deviation

- **Mid-session scope expansion.** The three new docs + "commit" arrived after the approved scope. I chose to fold them in (accuracy: committing a version I knew mischaracterized the gate structure would be worse) and add one board row, rather than re-gate. Judgment call inside the file-and-decide remit; flagged transparently in-thread. If Rex wanted a bare commit of the first filing, this over-delivered — but the two-track correction is load-bearing enough to justify it.
- **Personal routines (`/capture`, `/next`, …) are noted in the ticket but are not prd-to-product product** — they're Rex's user-level skills. Recorded for the whole-system picture only; nothing authored here.

## Port-back check

No scaffold-template change this session. The skill-gaps mechanism, once built, *is* a generator/port target (its own row now tracks it). No generic-lesson port — this was filing, not a discipline change.
