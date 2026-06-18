# Furnace-plan learning ledger

A **durable, cross-project record** of what Cowork's `/plan-review` (and, in future, other distinct reviewers) catches in `/furnace-plan`-authored plans — each row one finding, classified into a bucket — kept versioned so the furnace+reviewer loop accumulates learning across *every* project rather than scattering it across per-session retros. It serves two purposes: (1) **ongoing improvement** of the furnace's verification preflight, by surfacing which bucket-1 / bucket-2 catches recur; and (2) one specific **open sub-question** — whether the preflight has earned promotion from an invoke-skill to an `ExitPlanMode` hook, graded on the *distribution* of buckets over time, not a raw catch count. The bucket legend and promote/kill/tighten triggers below answer (2); the growing row history serves (1).

**Writer:** Cowork's `/plan-review` skill appends rows here as it reviews — one or more per round, regardless of which project the plan was for. Claude Code (the furnace) never writes here. The header below is static; only the table grows.

**Subject vs. writer:** this file lives under the `furnace-plan` skill because the furnace is what it measures, even though `/plan-review` is what writes it.

---

## Buckets (the classification)

- **Bucket 1 — no-read-behind-it.** A count or "X is missing / X is named" asserted from memory or a filename that the furnace's preflight Check 1 ("every codebase claim traces to a read *this session*") *should* have forced a read to catch. → **Forcing function underperforming. Tighten the preflight; do not kill.**
- **Bucket 2 — read-but-wrong / unfalsifiable inference.** A claim the furnace believed verified — it read the source and still misread it, or made an inference no codebase read could establish. Self-review structurally cannot reach this. → **The distinct-verifier (Cowork) is load-bearing; not a kill.**
- **Bucket 3 — genuine judgment / scope / design call.** Neither the preflight nor self-review's job — correctly Cowork + Rex's. **Note: bucket 3 spans severity** — it can be a low-stakes refinement *or* a must-fix design flaw (see 06-15 R1, the over-broad trigger). That is why severity is its own column.

## How to read it for the promotion / kill decision

- **Promote (earn the hook):** catches collapse to **mostly bucket-3 *refinements*** — few/no must-fixes of any bucket. A hook that automates the preflight only helps bucket 1, so the furnace earns it once bucket 1 is gone and what's left is the judgment tier the hook was never going to touch.
- **Tighten the preflight:** **bucket 1 recurs.** The forcing function isn't being executed; a hook would just automate a half-working layer.
- **Distinct verifier stays load-bearing:** **bucket 2 persists.** The blind spot is real and a planning prompt can't reach it — the fix is a fresh-context verifier fed the ledger, not a kill, and not a hook.
- **Watch severity, not just bucket.** Mostly bucket-3 *must-fixes* means the furnace is still shipping flawed plans of a kind no mechanical layer could catch — that argues *against* the hook, not for it.

When the furnace preflight is ever changed (e.g. read-enforcement tightened), add a dated `### --- preflight tightened YYYY-MM-DD ---` divider row so before/after trend is visible without a version column.

Full rationale and triggers: `~/Sites/prd-to-product/BACKLOG.md` (furnace-plan trial, In progress) and `docs/DECISIONS.md`.

---

## Ledger

| Date | Project | Plan | Round | Bucket | Severity | What Cowork caught |
|---|---|---|---|---|---|---|
| 2026-06-14 ~10:45 CDT | prd-to-product | chain-handoffs D-014/D-015 | 1 | 1 | must-fix | claimed new decision = D-013; already taken (skipped the read-the-log step) |
| 2026-06-14 ~10:45 CDT | prd-to-product | chain-handoffs D-014/D-015 | 1 | 2 | must-fix | "DSB never named in either file" — false; context-engineering/SKILL.md:59 names it (read but misread) |
| 2026-06-14 ~10:45 CDT | prd-to-product | chain-handoffs D-014/D-015 | 2 | 3 | refinement | `notes.md` — invented filename BACKLOG never specified |
| 2026-06-14 ~10:45 CDT | prd-to-product | chain-handoffs D-014/D-015 | 2 | 3 | refinement | chain-composition path-match should be named explicitly in D-015 |
| 2026-06-14 ~10:45 CDT | prd-to-product | chain-handoffs D-014/D-015 | 2 | 3 | refinement | temporal-claim check missing from verification |
| 2026-06-15 ~11:30 CDT | prd-to-product | red-team Rung 1 handoff | 1 | 2 | must-fix | conditional critique copy in always-printed Format block while claiming examples stay valid *because* it's conditional — internal contradiction |
| 2026-06-15 ~11:30 CDT | prd-to-product | red-team Rung 1 handoff | 1 | 3 | must-fix | over-broad trigger ("any V1/V2 cut") fired on every PRD — collapsed conditional into mandatory |
| 2026-06-15 ~11:30 CDT | prd-to-product | red-team Rung 1 handoff | 2 | 3 | refinement | fill-slot instantiation / sharper identity-defining cue / verification-scope clarification |
| 2026-06-17 (1st session) | prd-to-product | skill-frontmatter validation hook (C-27/D-017) | 1 | 2 | must-fix | [backfilled] fail-open lockout: a missing/mis-pathed `skills/` SKILL.md would block every commit — hook must fail open |
| 2026-06-17 (1st session) | prd-to-product | skill-frontmatter validation hook (C-27/D-017) | 1 | 2 | must-fix | [backfilled] forgeable whole-file field grep: `name`/`description` matched anywhere in the file, not only inside the frontmatter block |
| 2026-06-17 (1st session) | prd-to-product | skill-frontmatter validation hook (C-27/D-017) | 1 | 2 | must-fix | [backfilled] unterminated-frontmatter pass-through: a block missing its closing `---` fence passed validation |
| 2026-06-17 (1st session) | prd-to-product | skill-frontmatter validation hook (C-27/D-017) | 2 | 3 | refinement | [backfilled] missing-closing-fence case — judgment-tier improvement (the converge-toward-bucket-3 pattern held) |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 1 | 3 | must-fix | [backfilled] `mv` on the only unbacked copy is irreversible if `~/.claude` and `~/Sites` are cross-volume (mv→copy+unlink); use cp → verify (`diff -r`) → commit → rm → symlink instead |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 1 | 3 | refinement | [backfilled] README note that the install loop "covers" `context-engineering-audit` contradicts same-day D-019; mention only furnace-plan, file the loop-vs-D-019 tension separately |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 1 | 3 | refinement | [backfilled] 2nd "lives outside this repo" in BACKLOG sits in a "recorded here per where-facts-live" parenthetical that goes obsolete post-move; sentence-level rewrite, not a blanket string swap |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 1 | 3 | refinement | [backfilled] Cowork appends rows but can't commit; without a sweep-into-next-commit convention the "durable/versioned" goal is only met at commit time |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 2 | 3 | refinement | [backfilled] keep the commit-sweep convention worded narrowly to `trial-ledger.md`, not a general "commit changes you didn't make" rule (footgun) |
| 2026-06-17 (2nd session, ~16:39 CDT) | prd-to-product | furnace-plan migration | 2 | 3 | refinement | [backfilled] at D-020 write time, confirm the DECISIONS_ACTIVE mirror doesn't duplicate D-018's existing ACTIVE entry on the Cowork-write rule |
| 2026-06-17 ~20:40 CDT | prd-to-product | CF-03 red-capable-repro gate | 1 | 2 | refinement | verify-step-3 ledger claim that new path token "matches line 72" is imprecise — line 72 uses qualified `skills/context-engineering/examples/output-small/`, new wording uses bare `examples/output-small/`; only a substring match, not the verbatim match the step asserts |
| 2026-06-17 ~20:40 CDT | prd-to-product | CF-03 red-capable-repro gate | 1 | 3 | refinement | rule grows 1 line → ~6 sentences in always-loaded CLAUDE.md (the file the repo's own CF-01 note diagnoses as sprawl-prone); tighten wording, esp. the thin half-(b) debug-log clause |
| 2026-06-18 ~12:00 UTC | prd-to-product | C-09+CF-06 retro cluster (D-024) | 1 | 3 | refinement | sync-marker edit under-specified: plan says "refresh date" but CF-03 precedent records the adoption event in the line-1 marker — append "C-09 + CF-06 adopted (→D-024)" and use 2026-06-18, not a bare date bump |
| 2026-06-18 ~12:00 UTC | prd-to-product | C-09+CF-06 retro cluster (D-024) | 1 | 3 | refinement | tracker-cell flips quoted only the "N adopted" fragment; instruct edit-in-place of that fragment, preserving "Mining complete; …rest standing" (row 15) / "Mined + 6-lens re-mined…rest Proposed" (row 16) instead of overwriting the whole cell |
