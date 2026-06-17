# Retro — 2026-06-17 16:39 CDT — furnace-plan migration + audit-skill housekeeping   (2nd session of the day)

## What was completed

Two interrelated pieces of decision-log work, both Rex-approved before execution:

1. **`context-engineering-audit` housekeeping (D-019).** Asked to make the skill "working and globally accessible," I surfaced that promoting it conflicts with [D-013](../DECISIONS.md) (which declined a brownfield-audit tool and ruled drift is fixed by hand) *and* that the skill predates — and lacks — the 2026-06-13 pilots' non-optional "field-0 gate" (without it, an audit on a never-scaffolded project produces a harmful false-positive cascade). Rex chose **don't symlink**. Fixed stale `ROADMAP.md`→`BACKLOG.md` refs in the skill, recorded the not-promoted status in `NOTES.md`, and logged **D-019** (+ DECISIONS_ACTIVE mirror).

2. **furnace-plan migration (D-020).** Moved the skill + `trial-ledger.md` out of the bare, unbacked `~/.claude/skills/furnace-plan/` into `skills/furnace-plan/`, symlinked back like the chain siblings. Executed **copy-first** (copy → `diff -r` verify → commit backup → only then remove original + symlink) because the source was the sole copy of irreplaceable data. Reframed the ledger header to a durable cross-project learning ledger (rows + legend byte-identical). Logged **D-020** as a hosting/policy decision relying on D-018, not re-deciding it.

## Failure this session

- **none** (execution). The session ran clean: the incoming plan's staleness was *caught*, not propagated; two Cowork rounds returned no must-fixes after round-1 fixes; all verification checks passed.
- **Recurring meta-pattern worth naming (not a this-session failure):** the **next-free-decision-id went stale for the third time** (D-016→D-017 caught earlier; this session the supplied plan still targeted D-018, which D-018/D-019 had since claimed → corrected to D-020). The standing fix held — re-read the id immediately before writing — and is now baked into the furnace flow. If it recurs a 4th time, consider a mechanical id-allocator rather than relying on the discipline.

## Files changed

Commit `6405b9c` (backup, pre-reframe):
- `skills/furnace-plan/SKILL.md`, `skills/furnace-plan/trial-ledger.md` — copied verbatim into the repo before the original was touched.

Commit `b66a331` (migration + housekeeping):
- `skills/furnace-plan/trial-ledger.md` — header reframed (trial scorecard → durable learning ledger); rows/legend byte-identical.
- `CLAUDE.md` — workspace line names the two non-chain skills; file-scoped ledger-commit-sweep convention added to the D-018 carve-out paragraph.
- `README.md` — verify grep + note for `furnace-plan` (deliberately *not* `context-engineering-audit`).
- `BACKLOG.md` — two "lives outside this repo" claims relocated; done migration bullet removed (record → this retro); new low-pri item for the README-loop-vs-D-019 tension.
- `docs/DECISIONS.md` / `docs/DECISIONS_ACTIVE.md` — **D-020** + mirror.
- `docs/furnace-plan-migration-brief.md` — SUPERSEDED banner.
- `skills/context-engineering-audit/{NOTES.md,procedure.md}` — D-019 housekeeping (ROADMAP→BACKLOG, not-promoted status).

## Key decisions made

- **D-019** — `context-engineering-audit` stays a design record, not promoted to global.
- **D-020** — `furnace-plan` hosted + versioned in this repo; ledger reframed; plan-mode forcing recorded. Hosting/policy only, not a furnace-trial verdict.
- **Ledger stays in `skills/furnace-plan/`, not `docs/`** — the dir-level symlink keeps Cowork's `~/.claude/...` write path stable (verified write-through). Resolves the migration brief's open question in favor of stable-path over standing-doc-under-docs.

## The furnace→Cowork loop worked (trial evidence)

This plan was authored via `/furnace-plan` and reviewed by Cowork across two rounds. Cowork caught four real things — the stale D-018→D-020 id (bucket-2), a README/D-019 contradiction (bucket-3 must-fix), an asymmetric string-swap that would've left incoherent text (bucket-3 refinement), and the ledger-commit-path gap (bucket-3 refinement). **These are exactly the rows the trial ledger exists to capture** — but at author time neither writer could reach the file (Cowork couldn't see `~/.claude`; the furnace can't write the ledger). Now that the ledger is in-repo, a future Cowork review can append them.

## Open items

- **Pending ledger row for this plan.** Cowork's suggested classifications above are not yet written to `skills/furnace-plan/trial-ledger.md`. Append on the next Cowork review now that the file is reachable in-repo.
- **README-loop-vs-D-019 tension** — filed in BACKLOG (low priority): the generic `for skill in skills/*/` install loop would symlink `context-engineering-audit` for a fresh cloner, contradicting D-019. Doesn't affect Rex's machine.
- **Possible retro gap** — the D-018 + migration-brief commits (`89d88b1`, `a5f0b7d`) may not have their own retro; today's earlier retro covers cribs/C-27 (D-017). Not reconciled here; flagging only.

## Next session

- Nothing blocking. The furnace trial continues; the first real `/furnace-plan` → Cowork run after this will exercise the in-repo ledger's positive (row-producing) path for the first time.
