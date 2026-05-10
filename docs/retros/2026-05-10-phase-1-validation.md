# Retro — 2026-05-10 — Phase 1 validation (regression + hook contract)

Phase 1 of [ROADMAP.md](../../ROADMAP.md). Throwaway validation pass before Phase 2 dog-foods the skill into this repo. Goal: catch problems cheaply. Outcome: skill is structurally sound; two cosmetic issues surfaced (one example-staleness, one substitution-glitch), neither triggers the abort criterion.

## What was completed

- **Task 1 — Modular dry-run** (React Vite SPA on Cloudflare Pages, 2 AI surfaces, visual-confirmation gate, hooks-on). Walked the generator logic from intake to file emission.
- **Task 2 — Vercel/Next.js dry-run** synthesized against the canonical [examples/output-small/](../../skills/context-engineering/examples/output-small/) and diffed.
- **Task 3 — Hook live-test (script level).** Copied [.claude/settings.json](../../skills/context-engineering/examples/output-small/.claude/settings.json) and the three hook scripts to `/tmp/phase-1-hook-test/`, chmod +x, ran each script directly. Verified JSON parses, exit codes, stderr messages.
- **Task 4 — This retro and commit.**

Tmp artifacts created (kept for inspection): `/tmp/phase-1-dryrun-modular/`, `/tmp/phase-1-dryrun-vercel/`, `/tmp/phase-1-hook-test/`. Outside the repo, throwaway, will not be committed.

## Pass / fail per check

### Task 1 — modular shape (React Vite + Cloudflare + 2 AI surfaces)

Inputs: `stack=react-vite`, `deploy_target=cloudflare`, `ai_surface_count=2`, `visual_confirmer_name=Sam`, `enforce_rules_as_hooks=true`.

Derived (from [generator/decisions.md:44-90](../../skills/context-engineering/generator/decisions.md)):
- `deploy_target_has_cli_conflict=false` — Wrangler is the standard deploy path; no CLI gate.
- `uses_visual_confirmation_gate=true` — UI stack + named confirmer.
- `env_pattern = .dev.vars locally; Cloudflare Pages env vars in production. Never commit .dev.vars.`
- `stack_summary_one_line = React + Vite on Cloudflare Pages`.
- `stack_has_client_server_split=true` (per [decisions.md:23](../../skills/context-engineering/generator/decisions.md)).

| # | Check | Result |
|---|---|---|
| 1 | Paired-write rule (modular): canonical AGENTS.md from [templates/AGENTS.md.template](../../skills/context-engineering/templates/AGENTS.md.template); CLAUDE.md is `@AGENTS.md`; flat templates suppressed. Inclusion table at [decisions.md:139-164](../../skills/context-engineering/generator/decisions.md) drives correct file list. | PASS |
| 2 | Recency renumbering: items 1–2 always; item 3 (`ai_constraint`) included (`ai_surface_count>=1 && stack_has_client_server_split`); item 4 (`vocabulary_constraint`) dropped (no canonical vocabulary). Renumbering rule at [decisions.md:230-246](../../skills/context-engineering/generator/decisions.md) produces contiguous 1, 2, 3. | PASS |
| 3 | `paths:` frontmatter substitution in [ai-surface-stub.md.template](../../skills/context-engineering/templates/claude-rules-modular/ai-surface-stub.md.template). Synthesized example written to `/tmp/phase-1-dryrun-modular/.claude/rules/ai-feed-enrichment.md`. Parsed: 3 plain string entries, no `<!--` markers leaked, all values non-empty. | PASS |
| 4 | OPTIONAL block gating in [git-and-deploy.md.template](../../skills/context-engineering/templates/claude-rules-modular/git-and-deploy.md.template): `deploy_cli_section`, `deploy_cli_why` drop cleanly because `deploy_target_has_cli_conflict=false`; `worktree_restriction`, `worktree_why`, `worktree_gotcha` retained because `uses_visual_confirmation_gate=true`. Markers correctly span both inline anchors and block sections. | PASS |
| 5 | `settings.json` JSON-aware substitution. Synthesized output at `/tmp/phase-1-dryrun-modular/.claude/settings.json` — block-env-commit kept, block-deploy-cli object dropped, both block-worktree entries (Bash + EnterWorktree) kept. Trailing comma cleaned. `python3 -m json.tool` returns OK. | PASS |
| 6 | Hook script substitution: `block-env-commit.sh` (env_pattern marker); `block-worktree.sh` (repo_local_path marker); `block-deploy-cli.sh` not emitted. All scripts retain `exit 2` and stderr `>&2` redirect. | PASS |

### Task 2 — Vercel/Next.js dry-run vs. canonical

Synthesized [/tmp/phase-1-dryrun-vercel/.claude/settings.json](file:///tmp/phase-1-dryrun-vercel/.claude/settings.json) from the current template against the canonical [examples/output-small/.claude/settings.json](../../skills/context-engineering/examples/output-small/.claude/settings.json).

`diff` output (only two lines differ):

```
"//" comment, line 2:
canonical: "...rules from CLAUDE.md as actual guarantees..."
template : "...rules from CLAUDE.md/AGENTS.md as actual guarantees..."

block-env-commit doc-comment, line 7:
canonical: "Hook: block-env-commit. Blocks 'git add .env*'."
template : "Hook: block-env-commit. Blocks 'git add .env*'. Always emitted."
```

Both diffs are in `"//"` comment fields (which Claude Code ignores). Functional content identical. Cause: the canonical example was generated against an earlier template; the template was later refined to mention AGENTS.md and to annotate the always-emit condition. **Result: PASS** — diff is trivially explainable as example-staleness, not a generator regression. Phase 4 (regenerate examples) will close this. JSON parses.

Hook script comparison (current template + Vercel substitutions vs. canonical hook scripts in output-small/.claude/hooks/):

- `block-env-commit.sh`: comment header diverges (template adds "This is a guarantee, not a guideline."), echo body diverges (template uses generic "follows this project's env pattern: <env_pattern>" + "deploy provider's UI"; canonical uses bespoke "live in .env.local locally and Vercel project env vars in production" + "Vercel's UI"). Same root cause: canonical is hand-crafted Vercel-specific copy; template is now parameterized.
- `block-deploy-cli.sh`: identical echo body after `<deploy_cli_name>` substitution → "Vercel CLI"; comment header has same parameterization-driven divergence.
- `block-worktree.sh`: identical echo after `<repo_local_path>` substitution; comment headers match closely.

All differences are explainable by parameterization. No structural regression. **Result: PASS.**

### Task 3 — Live-test (script-level)

Copied canonical settings + hooks to `/tmp/phase-1-hook-test/`, chmod +x.

| Script | Exit | Stderr present | Verdict |
|---|---|---|---|
| `block-env-commit.sh` | 2 | yes — full BLOCKED message | PASS |
| `block-deploy-cli.sh` | 2 | yes — full BLOCKED message | PASS |
| `block-worktree.sh` | 2 | yes — full BLOCKED message | PASS |

`python3 -m json.tool < settings.json` → OK. `chmod +x` confirmed via `ls -l`. **Result: PASS** at the script level.

Harness-level (does Claude Code actually fire each hook on the matched event?) deferred to follow-up — requires a fresh Claude Code session inside `/tmp/phase-1-hook-test/` rather than firing from this session. The script-level tests rule out three of the four likely culprits named in [ROADMAP.md:34](../../ROADMAP.md): chmod missing, JSON malformed, exit/stderr wrong. Remaining open: confirm `if: "Bash(<pattern>)"` permission syntax and `EnterWorktree` matcher actually fire under the harness. Independent evidence for the latter: this session's deferred-tool list contains `EnterWorktree` as a real tool name, so the matcher is well-formed.

## Findings worth carrying forward

- **`env_pattern` substitution produces a doubled period.** The default `env_pattern` strings in [decisions.md:60-66](../../skills/context-engineering/generator/decisions.md) end with periods (e.g., ``...Never commit `.env.local`.``). The hook template appends another period after the marker (`...env pattern: <env_pattern>. If you need...`). Substitution yields ``...Never commit `.env.local`.. If you need...``. Cosmetic, not blocking. Fix in Phase 2 or Phase 4 alongside any other template tweaks: drop the trailing period in the env_pattern defaults, or rephrase the hook template so the marker isn't followed by another period.
- **The canonical [examples/output-small/](../../skills/context-engineering/examples/output-small/) is stale relative to the current templates.** Specifically: the `"//"` comment fields in `settings.json` and the comment headers + echo bodies in the three hook scripts. Functional behavior is unchanged. The right fix is to regenerate the example as part of Phase 4 (which already covers the medium/large abbreviated examples — extend it to also re-run small).
- **`EnterWorktree` is a real Claude Code tool.** Confirmed live this session: it appears in the deferred-tool list at session start. One Explore agent flagged it as "not in upstream docs," but the live tool list is the authoritative source. The skill's matcher syntax in [templates/claude-settings.json.template:41](../../skills/context-engineering/templates/claude-settings.json.template) is correct as-written.
- **JSON-aware substitution works.** Removing the `block-deploy-cli` object (when its OPTIONAL key is false) and cleaning the trailing comma produced parseable JSON in the modular dry-run. Validated via `python3 -m json.tool`.

## Files changed

- `docs/retros/2026-05-10-phase-1-validation.md` — this retro (new).

No skill files modified. No abort triggered.

## Open items / next session

- **Phase 2 starts next.** Quick wins (3 session-discipline bullets, principles.md additions) + dog-food the skill on this repo.
- **Phase 4 should also regenerate the small example**, not just medium/large. The drift surfaced in Task 2 makes it concrete: comment fields in settings.json/hooks are out of sync with current templates.
- **Cosmetic glitch (env_pattern doubled period)** captured as a candidate Phase 2 or Phase 4 micro-fix. Adding to docs/PARKING_LOT.md when that file is created in Phase 2.
- **Harness-level hook live-fire** still TODO. Worth running once after Phase 2 so the dog-fooded scaffold is exercised end-to-end. Not a blocker — script-level + JSON parse + tool-name evidence cover the contract.
