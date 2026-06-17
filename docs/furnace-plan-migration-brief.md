# Furnace-plan migration brief

<!-- Written 2026-06-17 as a cold-start handoff. Self-contained: assumes no memory of the authoring conversation. Purpose: context for reviewing Rex's plan to move the furnace-plan skill (and its trial ledger) into version control. -->

**Read this to review Rex's migration plan against decided constraints and open questions.** Rex has his own plan for the move; this brief is the context to evaluate it, not a plan itself.

## Situation (facts, with paths)

- The **`furnace-plan` skill lives at `~/.claude/skills/furnace-plan/`** as a **bare real directory** — `SKILL.md` + `trial-ledger.md`, **not a symlink, not in any repo, not backed up.** This violates Rex's global rule (*"skills under development live in a versioned `~/Sites/` repo and are symlinked into `~/.claude/skills/` — never a bare real directory there"*). It was edited as recently as 2026-06-17.
- The repo's **other four skills** (`context-engineering`, `prd-creator`, `design-system-bootstrap`, `context-engineering-audit`) are correctly **symlinked from `prd-to-product/skills/`**.
- **`trial-ledger.md` is the furnace trial scorecard** — the bucket-classification of what Cowork's `/plan-review` catches in furnace-authored plans. It is **written by Cowork** (not Claude Code), is **global** (captures every project Cowork reviews, on purpose), and holds **8 backfilled rows + legend**. Created 2026-06-16 to fix bucket data being scattered across retros. Background: the "Furnace-plan trial" item in [`BACKLOG.md`](../BACKLOG.md) and [`docs/retros/2026-06-16-furnace-trial-ledger.md`](retros/2026-06-16-furnace-trial-ledger.md).
- furnace-plan's **development history** (councils, drafts, trial retros) **already lives in prd-to-product** (`docs/council/...furnace...`, `research/feedback-extracts/furnace-draft.md`, `docs/retros/...furnace...`).

## What changed this session (the unblock)

- **[D-018](DECISIONS.md) (committed `89d88b1`) sharpened the no-agent-writes rule.** It was a blanket "outside agents write nothing here"; it's now **"outside agents may not write *product* (skills, code, docs, decisions), but a designated append-only *measurement* artifact they own — the trial ledger — may be written by that agent."** Category test: *product, or the agent's own measurement output?*
- **Consequence:** the Cowork-write conflict that previously forced the ledger out to the unbacked `~/.claude/` path is **gone.** The ledger can now live in a version-controlled repo and Cowork can still append to it.

## Direction this session leaned (not executed — for the plan to honor or revisit)

- **Ledger → into prd-to-product**, where it's backed up *and* reviewable next to the skills it exists to improve (Rex's stated need). D-018 now permits this.
- **Skill → home to `prd-to-product/skills/furnace-plan/` + symlink**, like the other four. After D-018 removed the only objection (the Cowork-write conflict), prd-to-product beat a dedicated repo because the skill's whole dev history is already here.

These are leanings, not locked. Rex's plan may differ — evaluate it.

## Open questions the plan should resolve

1. **Skill home** — `prd-to-product/skills/furnace-plan/` + symlink (matches the four siblings), or a dedicated repo? (Session leaned prd-to-product.)
2. **Ledger home + form** — where in prd-to-product, and **promote it from a dated retro to a *standing* scorecard doc** (e.g. `docs/furnace-trial/ledger.md`) so it accumulates rather than fragments across retros. **Preserve the 8 existing rows.**
3. **Cowork write path** — Cowork writes the ledger via its canonical path; confirm the new location is the single path Cowork targets, and that D-018's carve-out is discoverable where Cowork looks.
4. **Global-capture preservation** — the ledger captures *all* projects, not just this repo. Hosting one file here (reachable via symlink) is fine; confirm Cowork still finds/writes the one canonical path from any project.
5. **Migration mechanics** — move bare-dir contents into the repo, replace `~/.claude/skills/furnace-plan` with a symlink, lose neither the ledger rows nor SKILL.md edits.

## Constraints the plan must respect

- **Gated:** "where a skill lives" is a product/architecture decision → Rex's explicit go (he's driving; it's his plan).
- **Live data:** the ledger has 8 rows — don't clobber.
- **D-018 governs the write carve-out** — don't re-open it; build on it.
- **Global rule:** versioned `~/Sites/` repo + symlink is the whole point (fixes the backup violation).
- **Don't move the dev history** — councils/drafts/retros are a record; they stay where they are.

## Adjacent, separate (don't fold into the move)

- **Q3 — Codex vs Cowork as the reviewer.** Open question from this session: Codex (GPT-family) is more model-independent from a Claude author than Cowork (Claude-family), so it may catch blind spots Cowork can't. Recommended as an *experiment* — run Codex alongside Cowork on the next few trial plans and compare — not a swap. Not part of the move; flagged so it isn't lost. A furnace-plan repo that permits the reviewer to write the ledger works the same whether the reviewer is Cowork, Codex, or both.

## Pointers

- [D-018](DECISIONS.md) — the rule sharpening that unblocks this.
- [`BACKLOG.md`](../BACKLOG.md) "Furnace-plan trial" — the trial mechanics + grading.
- `~/.claude/skills/furnace-plan/trial-ledger.md` — the ledger to migrate (bare, unbacked).
- [`docs/retros/2026-06-16-furnace-trial-ledger.md`](retros/2026-06-16-furnace-trial-ledger.md) — how the ledger was built and why it's global + Cowork-written.
