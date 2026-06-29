# Retro — 2026-06-29 10:08 CDT — Kanban → scaffold Pass 3 (generator wiring + render tool + close-out)   (1st session of the day)

Picking up [`tickets/archive/kanban-into-scaffold.md`](../../tickets/archive/kanban-into-scaffold.md) (board Seq 1) after Pass 2 ported the board *shape* into the scaffold. This session shipped **Pass 3** — the final pass — via `/furnace-plan`, then implemented it in three scope-checked sub-passes (3a/3b/3c). Plan: [`~/.claude/plans/snuggly-tinkering-graham.md`](../../../.claude/plans/snuggly-tinkering-graham.md) (furnace preflight + blind Opus review + 2 Cowork rounds). This **completes** the 3-pass kanban-into-scaffold work; ticket archived.

## What was completed

- **3a — render tool emission.** New [`templates/claude-scripts/render-backlog-kanban.py.template`](../../skills/context-engineering/templates/claude-scripts/render-backlog-kanban.py.template) emitted to `.claude/scripts/` (always, inside the allowlist) — the ported Pass-1 script with two fixes: walk-up root resolution (works at the deeper path; exits non-zero without writing if no `BACKLOG.md` ancestor) and a robust `<!-- TAGS -->` parse. Inclusion-table row + `.py` provenance-banner row in [`generator/decisions.md`](../../skills/context-engineering/generator/decisions.md); `/end-session` render-regen wiring + stale-phrasing fix; `output-summary.md` gitignore line. [D-070](../DECISIONS.md) logged + mirrored. Commit `1c481b0`.
- **3b — wire the two markers.** Replaced the orphaned Phase-1 derivation section with an **agent-composed** "Board seeding" spec filling `board_seed_rows` + `backlog_tags_block`; reframed intake Q31; re-routed `open_decisions_list_or_none`. Commit `169b517`.
- **3c — retire + reconcile sweep.** Full `backlog_include_v2`/`Later-V2` retirement (~9 files; PRD V2-extraction re-routed to icebox/backlog seed rows); Build-plan/open-decisions cross-refs reframed to the board model across 6 template sites; `phase_*` transcript fills renamed; [D-004](../DECISIONS.md) given a "superseded in part by D-070" pointer; ticket archived (`git mv` + status→done + link-depth fix) and this repo's board row retired. Commit `e4986cd` (17 files, 80 lines).
- **Verification** per pass: render tool live-fired (clean fixture render, RED-capable, not-found exits non-zero, no write to `/`); 3b deterministic skeleton (gate+area axes, every row's Type/Lane/Seq/Tags) reproduces the fixture exactly; 3c grep shows only intended survivors; `check-live-links` 0 broken.
- **Independent check drove a real fix (not a rubber-stamp).** A cold Opus subagent re-derived the board from the "Board seeding" spec + `transcript-small` intake, blind to the fixture. It matched the deterministic core (both axes, deploy-shell row) but **diverged twice**: it tagged the Resend-wiring row with two areas (`area:api, area:email`) where the fixture uses one, and it emitted **no** icebox row (read "no spam captcha" as a hard exclusion, while the fixture parks "spam-filter upgrade" in icebox). Both were genuine spec gaps → tightened `generator/decisions.md` "Board seeding": one `area:` per row (the max-2 budget is area+gate, not two areas), and an explicit upgrade-path-vs-hard-exclusion cut for the icebox decision. Type assignment stays judgment by design.

## Failure this session

- **Tag:** none (no goal-drift / bad-substitution / scope-creep / lost-context failure landed) — but **two process near-misses** worth the lesson→change jump.
- **Near-miss 1 — silent partial commit.** The 3c `git add <17 explicit paths> && git commit` included the **old** ticket path (`tickets/kanban-into-scaffold.md`, already renamed by `git mv`). `git add` hit `fatal: pathspec ... did not match` and aborted staging the *other 16 files*, yet the `&&` chain still ran `git commit` (git add's fatal didn't propagate as expected), producing commit `93ee9e0` that captured **only the bare rename** (`0 insertions(+), 0 deletions(-)`). Caught only because I ran `git show --stat` + `git status` afterward and saw all 16 edits still in the working tree; amended to `e4986cd`.
  - **Tool or agent?** Agent — I listed a stale path (the pre-`mv` name) in an explicit-add list.
  - **Generalizes?** Yes, a class: any `git mv` followed by an explicit-path `git add` that re-lists the old path will abort the add; pairing it with `&& git commit` can ship a near-empty commit silently.
  - **→ Change it demands:** none minted (the existing "verify the commit captured what you intended" instinct caught it — `git show --stat` after committing is the working backstop). If this recurs, the fix is a habit of `git status` *before* committing a multi-file stage, not a new rule. Logged here as n=1.
- **Near-miss 2 — plan's "byte-for-byte" verify was unachievable as written** once Rex chose agent-composed derivation (the glosses are free prose). Resolved in-flight by splitting the verify into a *deterministic skeleton* (byte-matchable: axes, lane/seq/type/tag) + *semantic gloss* match — the same standard the rest of the scaffold's generative fixtures use. Not a failure (caught at verify-design time), but a reminder that "byte-for-byte" only applies to deterministic substitution, not composed content.

## Files changed

See commits `1c481b0` (3a), `169b517` (3b), `e4986cd` (3c) and the earlier ledger sweep `a8c43cd`. Net: 1 new template, ~22 generator/template/doc/example files reconciled, 1 ticket archived, [D-070](../DECISIONS.md) added.

## Key decisions made

- **Board derivation is agent-composed from intake, not a stack-keyed table** (Rex's call). The fixture's `area:` tags (`form·api·email`) and seed rows are project-content-derived; a fixed stack table can't reproduce them. Surfaced as an architecture checkpoint mid-3b before wiring. Recorded in [D-070](../DECISIONS.md) / `generator/decisions.md` "Board seeding".
- **`backlog_include_v2` / `Later-V2` retired fully** (Rex's call) — the board's `icebox`/`backlog` lanes own deferral; no second mechanism. PRD V2-extraction re-routes into icebox/backlog seed rows.
- **Found + fixed a latent parser bug** in the render tool (first-`<!-- TAGS -->`-match grabbed the board-intro prose mention). This repo's own [`scripts/render-backlog-kanban.py`](../../scripts/render-backlog-kanban.py) shares it (escapes only by block ordering) — **port-back flagged as a background task**, not done here.

## Open items

- **Port-back:** the robust TAGS parse to this repo's `scripts/render-backlog-kanban.py` (spawned task; latent, not breaking).
- The 3-pass kanban-into-scaffold work is **complete**; ticket archived. No remaining sub-passes.

## Next session

- Nothing queued from this work. Board Seq 1 is now "Agent-process & context-harness upgrades." If picking up the port-back task, it is a ≤10-line one-file change.
