# Retro — 2026-05-10 — context-engineering skill refinement

First retro for this repo. The repo authors the context-engineering skill but does not yet eat its own dog food (no `AGENTS.md`, no `CLAUDE.md`, no path-scoped rules at the root). Tracked as an open item below; deferred this session because more skill changes are queued and one scaffold pass is cheaper than two.

## What was completed

- Read the AGENTS.md arXiv paper (2025) and the skill independently. Evaluated another Claude session's critique against both, kept the parts that held up, pushed back on the parts that under-weighted the paper's own caveats (Python-only, Claude Code did not benefit from human-written files).
- Lifted Vercel/Next.js from hardcoded to parameters. New intake cluster 1.5 captures `stack` + `deploy_target`; templates and modular rules now use `<!-- PARAMETERIZE: stack_summary_one_line -->`, `<!-- PARAMETERIZE: deploy_target_name -->`, and the `<!-- OPTIONAL: deploy_cli_section -->` blocks.
- Added explicit Commands block (`install_cmd` / `dev_cmd` / `check_cmd` / `test_cmd` / `build_cmd` / `env_pattern`) to AGENTS.md and flat CLAUDE templates. The AGENTS.md paper's only clean positive finding: tools mentioned in context get used; tools not mentioned almost never do.
- Tightened recency block from 5 always-on items to 2 always-on + 2 conditional (AI, vocabulary). Removed duplication of body rules. Updated `decisions.md` renumbering rule.
- Softened absolute worktree ban to a conditional rule explained by the visual-confirmation gate. Worktrees are not anti-pattern; they are incompatible with single-dev-server visual confirmation specifically. New derived parameter `uses_visual_confirmation_gate` drives emission.
- Added redundancy guards to `decisions.md`: when `docs/PRD.md` is generated, "What this project is" in CLAUDE.md/AGENTS.md becomes a one-line tagline + pointer.
- Added "honest bets" + "auto memory" sections to `principles.md`. The skill's bets against the paper's findings are now explicit; auto-memory is documented as complementary (don't put learned-correction content in CLAUDE.md, it belongs in auto memory).
- Scaffolded `.claude/settings.json` + `.claude/hooks/` for harness-level enforcement of load-bearing rules. Three hooks emitted: `block-env-commit.sh` (always), `block-deploy-cli.sh` (when `deploy_target_has_cli_conflict`), `block-worktree.sh` (when `uses_visual_confirmation_gate`). Documented JSON-aware substitution (gate by `"//OPTIONAL"` keys, drop entire enclosing object on false). New intake question `Q5f: enforce_rules_as_hooks` defaults to true.
- Evaluated the viral "12-rule CLAUDE.md" article. Most rules were already covered by the skill in more enforceable form. Three were genuinely additive and got added: `Read before you write` (session-discipline), `Checkpoint between phases of multi-step work` (session-discipline), `Use the model only for judgment calls` (ai-shared). Headline "41% → 3% mistake rate" rejected as hype.
- Compressed `examples/output-small/CLAUDE.md` from 103 lines to 74 (with the new rules added). PRD pointer replaces inline project description.
- Committed and pushed: [be36ea1](https://github.com/rexerr/prd-to-product/commit/be36ea1).

## Files changed

- `skills/context-engineering/principles.md` — added "What this skill bets on", "Relationship to Claude Code's auto memory", new always-on patterns (read before write, checkpoint), softened worktree pattern, parameterized stack/deploy.
- `skills/context-engineering/SKILL.md` — scope boundary text reflects parameterized stack.
- `skills/context-engineering/generator/intake.md` — new cluster 1.5 (stack + commands + hooks opt-in), Q5a tagline, Q5b–Q5f, marker-map updates.
- `skills/context-engineering/generator/decisions.md` — stack/deploy defaults table, env_pattern table, deploy_target_has_cli_conflict table, redundancy guards, hooks emission section, JSON-aware substitution, recency renumbering rule (1–2 always, 3–4 conditional).
- `skills/context-engineering/generator/output-summary.md` — Commands-block verification step, hooks verification step.
- `skills/context-engineering/templates/AGENTS.md.template` — Commands block, parameterized tech-stack line, tightened recency, redundancy-guard markers.
- `skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template` — same shape changes as AGENTS.md, plus session-discipline gets read-before-write and checkpoint additions.
- `skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template` — read-before-write, checkpoint-between-phases.
- `skills/context-engineering/templates/claude-rules-modular/ai-shared.md.template` — model-only-for-judgment-calls section.
- `skills/context-engineering/templates/claude-rules-modular/git-and-deploy.md.template` — parameterized for any deploy target, worktree restriction conditional.
- `skills/context-engineering/templates/docs/ARCHITECTURE.md.template` — stack assertion now `<!-- PARAMETERIZE: stack_summary_one_line -->`.
- `skills/context-engineering/templates/claude-settings.json.template` — new. Hooks block with `"//OPTIONAL"` gating.
- `skills/context-engineering/templates/claude-hooks/{block-env-commit,block-deploy-cli,block-worktree}.sh.template` + `README.md.template` — new.
- `skills/context-engineering/examples/output-small/.claude/settings.json`, `.claude/hooks/*.sh`, `.claude/hooks/README.md` — concrete worked example.
- `skills/context-engineering/examples/output-small/CLAUDE.md` — compressed to 74 lines, added read-before-write and checkpoint to session discipline.

## Key decisions made

- **Stack and deploy target are parameters, not hardcoded.** Lifted from the V1 "hardcoded for Vercel + Next.js" stance. Drives the Commands block, the deploy-CLI rule, the worktree rule. Defaults table covers `nextjs`, `react-vite`, `node-cli`, `python`, `other` × `vercel`, `netlify`, `cloudflare`, `fly`, `railway`, `manual`, `none`.
- **Recency block holds 2 items always.** "Hard scope limits" and "Visual confirmation gates the commit." Anything else duplicates body content. Items 3 (AI), 4 (vocabulary) are conditional.
- **Worktree restriction is conditional, not absolute.** Worktrees themselves are a legitimate Git feature; the constraint is workflow-specific. Suppressed for non-UI stacks.
- **Hooks coexist with prose; they do not replace it.** The prose explains *why*; the hook guarantees *that*. Removing one without the other breaks either orientation or enforcement. Default is `enforce_rules_as_hooks = true`.
- **Auto memory is complementary, not in scope.** The skill scaffolds the human-written side; Claude Code's auto-memory system handles agent-discovered notes. Don't mix.
- **Three rules added from the viral article (5, 8, 10), eight rejected.** Rule headline rates rejected as hype; the AGENTS.md paper's transparent methodology is the better evidence base.

## Open items

- **Eat the dog food.** Run the skill on this repo. Scaffold `AGENTS.md`, `CLAUDE.md`, `docs/retros/` proper, `.claude/rules/` for skill-development conventions. Deferred this session because more skill changes are queued — the user said "no point in updating it more than once."
- **Regression-test the modular shape against the new tightened recency block.** All edits were validated against the small-example flat shape. Modular paths-scoped rule emission with `paths:` frontmatter substitution should be re-verified.
- **Regenerate medium and large abbreviated examples.** `examples/output-medium-abbreviated.md` and `examples/output-large-abbreviated.md` still reflect pre-refinement output. Defer until the small example shape settles.
- **Generator dry-run on a non-Vercel project.** Plan called for a hypothetical "React Vite SPA on Cloudflare Pages" dry-run to confirm the parameterization works end-to-end. Not yet executed.
- **Verify hook contract assumptions live.** Templates assume `if: "Bash(vercel *)"` permission-rule syntax works inside the `if` field, that exit 2 + stderr blocks the tool call, and that `EnterWorktree` is the exact tool name. Source: live `WebFetch` of `code.claude.com/docs/en/hooks` mid-session. Worth running each blocked operation once in a throwaway session before declaring the hook scaffold validated.
- **Post-edit `npm run check` hook deliberately not added.** Discussed but rejected — running on every edit is too aggressive for the user's scope-check workflow. Reconsider if a checkpoint-style version (after multi-edit batches only) makes sense.
- **The user's "big question" is still queued.** The session ended at the commit. Pick up there at the start of the next session.

## Next session

1. Hear the user's "big question" — they teed it up explicitly before the commit.
2. Decide whether to run the skill on this repo (path 2 from the retro discussion) or hold for further refinement first.
3. If more skill edits land before the dog-food pass, append to this retro or write a follow-up — do not scaffold the repo until the skill is genuinely settled.
