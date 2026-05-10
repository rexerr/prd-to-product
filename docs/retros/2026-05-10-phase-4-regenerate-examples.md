# Retro — 2026-05-10 — Phase 4 regenerate examples

Phase 4 of [ROADMAP.md](../../ROADMAP.md). Three example regenerations plus an in-phase generator-convention fix. The convention work and the small-example refresh shipped as one commit; medium and large as a second commit; this retro completes the phase.

## What was completed

### Commit 1 — Phase 4 task 1 + env_pattern convention (commit `c43511e`)

The narrow parking-lot drift item (`output-small/` `"//"` comments and the three hook scripts' headers + echo bodies diverging from current templates) expanded mid-task when regen surfaced a real template defect: `env_pattern` default values in [`decisions.md`](../../skills/context-engineering/generator/decisions.md) were wrapped in markdown backticks (and contained literal backticks around `` `.env.local` ``), but the shell template substituted that value into a double-quoted `echo` where backticks would trigger command substitution. Phase 1 implicitly resolved this by substituting unbackticked values, but the convention was undocumented.

Resolution applied option (a) from the parking-lot triage:

- `env_pattern` values are **plain strings** in [`decisions.md`](../../skills/context-engineering/generator/decisions.md) (no internal backticks, no markdown wrappers).
- One-paragraph convention statement added directly under the defaults table.
- Four markdown template consumers wrap the substituted value in backticks at the substitution site: [`AGENTS.md.template:43`](../../skills/context-engineering/templates/AGENTS.md.template), [`claude-rules-flat-CLAUDE.md.template:54`](../../skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template) and `:136`, [`claude-rules-modular/git-and-deploy.md.template:23`](../../skills/context-engineering/templates/claude-rules-modular/git-and-deploy.md.template).
- One shell template consumer ([`block-env-commit.sh.template:7`](../../skills/context-engineering/templates/claude-hooks/block-env-commit.sh.template)) substitutes the plain value with no wrapping — no command-substitution risk.

The convention generalizes: "any future parameter that needs to appear in both markdown and shell contexts is a plain string at the source; markdown consumers wrap; shell consumers don't." Avoids context-dependent stripping logic in the generator and avoids parameter doubling.

The doubled-period item ([FUTURE.md](../FUTURE.md) continuous-mode watch from Phase 1) hit its second observation in this regen (`Never commit .env.local..` in the regenerated `block-env-commit.sh`). Per the continuous-mode discipline, second instance triggers fix. Dropped the period after the `<env_pattern>` marker in [`block-env-commit.sh.template:7`](../../skills/context-engineering/templates/claude-hooks/block-env-commit.sh.template); `env_pattern` already ends in a period. Removed the watch item from [FUTURE.md](../FUTURE.md); resolution recorded in [PARKING_LOT.md](../PARKING_LOT.md) "Resolved items".

`output-small/`: settings.json `"//"` comments refreshed, three hook scripts' comment headers + echo bodies refreshed, [CLAUDE.md](../../skills/context-engineering/examples/output-small/CLAUDE.md) env-vars + credentials lines updated to reflect the new markdown-wrap shape. JSON parses; all three hooks exit 2 with clean single-period BLOCKED messages.

### Commit 2 — Phase 4 tasks 2+3 (medium + large abbreviated regen + transcript companions)

Both medium and large regenerated as full replacements. Transcript companions regenerated alongside their abbreviated sketches because keeping the abbreviated current while the transcript references a different project shape was the exact failure mode Phase 4 exists to prevent (users see stale patterns, scaffold projects that don't match what the skill produces).

**Medium** — `craft-letters` (Vite+Cloudflare Pages, modular shape via the `voice_and_tone == true` trigger, one AI surface, basic styling). Demonstrates:

- Modular shape reached via voice-and-tone, not the ≥2-surfaces or tokens-with-linter thresholds. This is the case the modular criterion exists to catch.
- Non-Vercel deploy parameterization: `deploy_target_has_cli_conflict == false` for Cloudflare → `block-deploy-cli.sh` not emitted, no "Never use the X CLI" line in code rules.
- `env_pattern` convention round-trip: Cloudflare default substitutes as plain string into shell echo, wrapped at markdown consumption sites.
- Voice-and-tone as a path-scoped rule with substituted `paths:` frontmatter.

**Large** — `triage-classifier` (Python service on Fly.io, modular via `ai_surface_count == 3`, no UI, no voice-and-tone). Demonstrates the **structural parameterization cascade**: four orthogonal flag values (`uses_visual_confirmation_gate=false`, `stack_has_client_server_split=false`, `deploy_target_has_cli_conflict=false`, `voice_and_tone=false`) each drop distinct content from the emitted output. End result is the minimum modular shape — one hook, one-item recency block, no `ai-shared.md`, no `voice-and-tone.md`, no `block-deploy-cli`, no `block-worktree`. The previous Next.js+Vercel `intelligence-feed` example could not exercise these suppressions because every flag resolved true.

## Required retro notes (per session direction)

### Coverage map

```
small  = flat-baseline                              (Next.js+Vercel, flat, no AI, no voice)
medium = modular + voice + UI + non-Vercel         (Vite+Cloudflare, 1 surface)
large  = modular + 3-surfaces + no-UI + structural (Python on Fly, no voice)
```

Each example demonstrates a distinct behavior cluster. The library covers voice-and-tone (medium), structural suppressions (large), and the minimal flat-shape baseline (small).

### Deliberate uncovered shapes

- **Modular + UI + Vercel + multi-surface** (the previous `intelligence-feed` shape — the most common Next.js modular project). Not exercised by any current example.
- **Flat + non-Vercel** (a small project on Cloudflare/Netlify/Fly without voice-and-tone or multi-surface AI). Not exercised.

This is a deliberate trade — the examples demonstrate behaviors, not a test matrix — but it is worth recording so a future "we're missing X" question does not reopen the design without evidence. If a real failure surfaces from users not seeing the common Next.js modular shape, promote it from [FUTURE.md](../FUTURE.md). For now, the parameterization argument is more load-bearing than the common-shape demo.

### Replacement, not addition

The previous `prompt-coach` (medium, Next.js, flat, 1 surface) and `intelligence-feed` (large, Next.js, modular, 3 surfaces, voice-and-tone, tokens-with-linter) examples are **replaced**, not augmented. Intelligence-feed's combined coverage of modular+UI+Vercel+3-surfaces+voice-and-tone+vocabulary-lock+tokens-with-linter is going away. The trade is "demonstrate parameterization aggressiveness" over "demonstrate the most-common-shape." Both transcripts were rewritten; the previous projects are not preserved anywhere in `examples/`.

If retros or commits reference the old project names: the previous transcripts existed at `transcript-medium.md` (prompt-coach) and `transcript-large.md` (intelligence-feed). Their content is in git history. The Phase 1 retro's `phase-1-prd.md validation` reference and the Phase 3 retro do not call them by name, so the rot is contained.

### Voice-and-tone moved from large to medium

The previous large case carried voice-and-tone as one of seven exercised features. The new large case drops voice-and-tone to make room for the structural-suppression demo. Voice-and-tone coverage moves to the new medium case (`craft-letters`), where the rule is the modular trigger itself rather than one feature among many. Without this note, a future reader hitting the new large and seeing no voice-and-tone might conclude the feature was dropped or file it as a regression — it was neither; the trade was made deliberately.

## Files changed

Commit 1:

- [skills/context-engineering/examples/output-small/.claude/settings.json](../../skills/context-engineering/examples/output-small/.claude/settings.json) — `"//"` comments refreshed.
- Three hook scripts in [`output-small/.claude/hooks/`](../../skills/context-engineering/examples/output-small/.claude/hooks/) — headers + echo bodies refreshed.
- [skills/context-engineering/examples/output-small/CLAUDE.md](../../skills/context-engineering/examples/output-small/CLAUDE.md) — env-vars + credentials lines.
- [skills/context-engineering/generator/decisions.md](../../skills/context-engineering/generator/decisions.md) — `env_pattern` defaults table cleaned + convention statement added.
- Four markdown template consumers updated to wrap `env_pattern` with backticks.
- [block-env-commit.sh.template](../../skills/context-engineering/templates/claude-hooks/block-env-commit.sh.template) — period dropped after `<env_pattern>` marker.
- [docs/PARKING_LOT.md](../PARKING_LOT.md) — convention item + doubled-period item moved to Resolved.
- [docs/FUTURE.md](../FUTURE.md) — doubled-period watch item removed.

Commit 2:

- [skills/context-engineering/examples/transcript-medium.md](../../skills/context-engineering/examples/transcript-medium.md) — replaced; `craft-letters` (Vite+Cloudflare).
- [skills/context-engineering/examples/output-medium-abbreviated.md](../../skills/context-engineering/examples/output-medium-abbreviated.md) — replaced; modular shape via voice-and-tone trigger.
- [skills/context-engineering/examples/transcript-large.md](../../skills/context-engineering/examples/transcript-large.md) — replaced; `triage-classifier` (Python+Fly).
- [skills/context-engineering/examples/output-large-abbreviated.md](../../skills/context-engineering/examples/output-large-abbreviated.md) — replaced; structural suppression cascade demo.

Commit 3:

- This retro.

## Key decisions made

- **Convention fix shipped in-phase, not deferred.** Phase 4's failure mode is "users see stale patterns and scaffold projects that don't match what the skill produces." Shipping the medium/large regen on top of an unresolved markdown-vs-shell ambiguity would have baked the inconsistency twice and left the convention undocumented. Per Phase 4 abort criterion, the surfaced template gap was in scope to resolve. ~25 lines of generator/template work made the two larger regens deterministic.
- **Doubled-period fixed on second observation, not deferred a third time.** The [FUTURE.md](../FUTURE.md) continuous-mode discipline says "Fix when the second instance lands." Phase 4 task 1 regen was the second instance. Discipline applied without an in-the-moment exception.
- **Transcripts regenerated alongside abbreviated sketches.** Strict Phase 4 ROADMAP scope named only the `output-*-abbreviated.md` files. Internal coherence beat strict scope: shipping current abbreviated files that reference stale transcripts would have re-created the exact failure Phase 4 exists to prevent. Caveat from session direction was honored: intake.md was re-read for structural correctness before writing the new transcripts, and no substantial intake-flow drift was found, so the lift stayed bounded.
- **Replacement over augmentation for medium/large.** The old `prompt-coach` and `intelligence-feed` examples were replaced rather than retained as a fourth/fifth example. Three examples covering distinct behaviors is more maintainable than five covering overlapping behaviors.
- **Large case drops voice-and-tone in trade for structural-suppression demo.** Picking a richer Python project to retain voice-and-tone would have diluted both signals. Coverage moves to medium; the new large stays focused on parameterization-as-real-feature.

## Open items / next session

- **Continuous-mode is now live for the skill.** ROADMAP's "Continuous mode" section governs further edits. Triggers: a real failure mode in dog-fooded session work (capture in [PARKING_LOT.md](../PARKING_LOT.md), fix on second instance), a Claude Code feature shipping that obsoletes a current pattern, or a new piece of evidence cited inline. Do not edit on speculation.
- **One [FUTURE.md](../FUTURE.md) continuous-mode watch item remains:** `stack_summary_one_line` row missing for `stack=other + deploy_target=none`. Wait for second instance.
- **[FUTURE.md](../FUTURE.md) Section A (Thariq nine-category gaps) is unchanged.** No real failures from this phase to promote.
- **HTML-over-Markdown investigation** ([`docs/html-over-markdown-brief.md`](../html-over-markdown-brief.md)) remains the only parallel-eligible scope. D-001 (markdown-only) still binds.

## Process note: session size

This session exceeded the per-session feature limit ([CLAUDE.md](../../CLAUDE.md) "Hard scope limits: Feature ≤ 300 lines per session") at user direction. Total lines changed: ~450 across the two commits plus this retro. The limit is for protecting against scope creep when the agent might not realize the scope; the user named Phase 4's full scope (three regens, in-phase convention fix, transcript companions) before any commit. Recording the deviation explicitly so it does not become precedent. Future phases that legitimately need this much surface should propose splitting across sessions before starting, not after.
