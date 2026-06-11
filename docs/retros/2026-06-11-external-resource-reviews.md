# Retro — 2026-06-11 18:19 CDT — External resource reviews: animations.dev + obra/superpowers   (1st session of the day)

## What was completed

- **Reviewed Emil Kowalski's "Agents with Taste" article + his `web-animation-design` skill** (installed on this machine via the animations.dev activate script). Verdict: independently validates our "every rule cites its failure mode" architecture rule (his positive-polarity twin: "every taste decision has a logical reason"); strengthens the pending DSB HTML-supplement case (motion can only be *felt* in a live preview).
- **Extract-then-kill on the skill, per Rex:** durable content preserved in [`docs/animation-taste-reference.md`](../animation-taste-reference.md) (Part 1 skill-craft patterns, Part 2 candidate DSB motion-defaults material), then the skill uninstalled from all three harnesses it had landed in (`~/.claude/skills/`, `~/.codex/skills/`, `~/.cursor/skills/`). Reason: ~40-keyword proactive trigger description loading into every session on every project. Reinstall is one curl (recorded in the doc header).
- **Stashed verbatim copies on the Desktop** at `~/Desktop/claude md + skills/web-animation-design/` (recovered byte-identical from the installer's embedded base64 — 10918 + 6490 bytes, matching the originals).
- **Full review of github.com/obra/superpowers** (cloned, read all 14 skills + bootstrap hook + writing-skills meta-methodology + contributor guidelines). Logged four BACKLOG entries: pressure-testing gap for behavior-shaping prose, CSO description audit, fix candidate D (terminal-state handoffs) on the chain-orchestration item, and a fold-into-incidental-edits liftables line.

## Failure this session

- **none.** Scopes were small and Rex-directed throughout; no substitution work, no template changes. One process deviation noted honestly below.

## Files changed

- `docs/animation-taste-reference.md` — new; curated extract of the animations.dev skill with provenance + reinstall command.
- `BACKLOG.md` — DSB motion-defaults candidate added (commit `cdc0f97`); chain-orchestration item amended with fix candidate D + three new superpowers-sourced entries (commit `dde448c`).
- `docs/retros/2026-06-11-external-resource-reviews.md` — this retro.
- Off-repo (machine config, Rex-directed): deleted `web-animation-design` from three harness skill dirs; created the Desktop stash folder.

## Key decisions made

- **Kill the globally-installed animation skill rather than tame it** (Rex's call): trigger saturation made it fire on every frontend session; content preserved in-repo and on Desktop, reinstall trivially reversible. Not a `D-NNN` — machine config, not a repo constraint.
- **All superpowers findings parked with promotion triggers, nothing adopted now** — explicitly avoiding the ceremony-accretion failure the retro failure-tag instrument watches for. The tone caution (their Iron-Law persuasion style vs. our evidence-first calm prose) is written into the BACKLOG entry itself.

## Verification

- Doc-change contract applied: cross-references in the new doc and all BACKLOG edits re-checked — internal links (`docs/animation-taste-reference.md`, retros, council reports) resolve; external links are GitHub/article URLs.
- Desktop stash verified byte-identical by size match against the originals installed at 17:36 (10918 / 6490 bytes); skill removal verified by directory-absence check across six candidate harness dirs.
- **Not covered:** no behavioral verification of anything — nothing behavior-shaping was changed (which is fitting, given the session's own headline finding about pressure-testing prose).

## Deviation noted

- **Retro is a trailing commit, not bundled.** The session ran as three Rex-directed turns, each committed run-to-done at turn end (`cdc0f97`, `dde448c`); the before-commit-bundle convention assumes one work-unit per session. Real tension between per-turn run-to-done and session-end bundling — fine this time (no push happened, so no double-push waste), but worth knowing the convention's assumption.

## Open items

- All parked in BACKLOG with triggers (DSB motion layer, pressure-testing prose, CSO audit, fix candidate D, liftables). Nothing left mid-flight.

## Next session

- **Rex's stated plan: a batch of additional external resources to review for the system.** Pattern from this session that worked: review → verdict mapped against existing BACKLOG/decisions → park with promotion triggers, adopt nothing in-session. The two reviews so far (Emil, superpowers) both fed the same items (DSB HTML supplement, chain orchestration, verification contract) — watch whether the next batch keeps converging on those; convergence is promotion evidence.
- Standing gated items unchanged: HTML memo (3 questions + D-NNN), plan-review mining run (Workflow opt-in), the two `.claude/` self-edits, `block-deploy-cli.sh`/`block-worktree.sh` stdin fixes.
