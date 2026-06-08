# Retro — 2026-06-08 11:45 CDT — qventus-prototyper scaffold post-mortem (read-only)   (2nd session of the day)

> H1 timestamped + session-numbered per the `docs/agent-process-brief.md` §1.5 convention (dog-fooded since the 1st session today).

The gating "In progress" backlog item. qventus-prototyper (`/Users/rexc/Sites/qventus-prototyper`) is the only real scaffolded build available to validate `context-engineering` (+ siblings): 58 commits, full `docs/`, modular `.claude/`, 33 retros (2026-06-02 → 06-06), a real external stakeholder ("Steve," head of orthopedics at the client), and a 15-hour contract cap. Read-only audit per the brief in `BACKLOG.md`. Two parallel passes: a subagent mined all 33 retros; I diffed the scaffold against the skill templates + `examples/output-small/`.

This was the strongest evidence base the skill has had. Squirreled produced none (froze at the PRD); qventus exercised the scaffold through **two full architecture pivots** and still held.

## What was completed

- **Mined all 33 qventus retros** (subagent) for evidence on four questions: deploy-shell, design-system integrate-then-kill, chain composition, scaffold pain/wins. Every finding carries a retro citation + quoted sentence.
- **Structural-diffed the qventus scaffold** against `skills/context-engineering/templates/` and `examples/output-small/`: `AGENTS.md`, `CLAUDE.md`, the 4 modular rules, `session-start.md`, `settings.local.json`, `launch.json`, `.gitattributes`.
- **Resolved the gated backlog items with real evidence** (below) and updated `BACKLOG.md`.

## Findings

### 1. Deploy-shell pilot (build-defaults item 1) — VERDICT: qventus cannot validate it; the item stays open.

qventus has **no `deploy_target`, no deploy-shell in any ROADMAP phase, no deploy path ever exercised.** It's worse than a non-example — its scaffold was *authored to exclude* deployment, on three independent surfaces:
- `.claude/rules/git-and-deploy.md`: "There is no deploy target — the product is a downloadable HTML file... 'done' means pushed, not deployed."
- `docs/PRD.md` non-goals: "Hosting or publishing the prototype at a live URL — the deliverable is a file, not a hosted page."
- Phase 1 of the scaffolded ROADMAP is a brand/export phase whose done-criterion is "export produces a single self-contained HTML file," not a deploy-shell.

The `BACKLOG.md` caveat predicted exactly this. **build-defaults item 1 stays In-progress** but with its validation hope retired: it needs a project whose PRD treats a live URL as the deliverable. qventus closes the question of *whether qventus can validate it* (no), not the pilot itself.

### 2. Design-system layer — VERDICT: argues against design-system-bootstrap as a separate skill *for this project class*, but does NOT exercise the from-scratch path the skill is built for.

The arc (`2026-06-02-design-system-integration.md` → `2026-06-05-kill-design-system-layer.md`, D-033):
- **`/design-system-bootstrap` was deliberately NOT run.** "The skill generates a fresh token file + seed components and explicitly does not migrate an existing system; this project already had a complete hand-authored `--primary` cascade... Rex confirmed." So the one project where it could have run declined it — because a Claude Design handoff already supplied a complete system.
- What got integrated was a **reference layer** (extracted CSS, `ui_kits/`, 21-page `preview/` gallery, a path-scoped rule).
- It was **killed** once the Phase 2 static rewrite (`2026-06-03-static-rewrite.md`, D-023) retired the React kit the layer was attached to. By 2026-06-05 the shipping `index.html` was fully self-contained and "loads nothing from the standalone design-system files." ~32 files culled.
- **The kill was complete and correct.** `design-system.md` surviving in `.claude/rules/` is intended — it was *retargeted* (`paths: index.html` only) to govern the inlined `<style>` tokens, preserving every live invariant (`--primary` cascade, `.qv` scope, never-hardcode). Not orphaned.

Lesson: a *separate* design-system layer earned nothing for a single-artifact prototype and became dead weight. The token system that survived lives inline. This is real evidence against a separate bootstrap skill for this class — but it's one project, and one where the from-scratch path never ran. The evidence indicts "separate reference layer," not "bootstrap from nothing." The backlog item "verify design-system-bootstrap actually triggers and produces usable output" is therefore **still unmet** — qventus declined the skill, so it remains unvalidated end-to-end.

### 3. Chain composition — VERDICT: manual hand-offs, not orchestration; and a naive `/idea-to-product` would have *harmed* this project.

- prd-creator and context-engineering ran as two discrete manual invocations in one session (`2026-06-02-prd-and-scaffold.md`); design-system-bootstrap was never run.
- A naive orchestrator that auto-ran all three would have run bootstrap here and **clobbered the real hand-authored tokens.** For this project the third link required a human "integrate vs bootstrap" judgment an orchestrator couldn't safely automate.
- Hand-off friction was mild: the design-system integration was parked at scaffold time and became "the next call" (`PARKING_LOT.md`); a real permission-classifier snag blocked the first `.claude/rules/` write (treated as self-modification, needed explicit approval) — sequencing wouldn't fix that.
- **Net for the `/idea-to-product` candidate:** this is a *cautionary* data point, not support. The prd→scaffold sequence was smooth; the genuine friction was a judgment call. If an orchestrator is built, it MUST branch on "skip bootstrap if a system already exists." This tempers (does not kill) the candidate-A case that the Squirreled stall made.

### 4. Scaffold structural fidelity + drift

- **High fidelity.** `AGENTS.md` matches the template shape (Primary constraints / Commands / What this is / Vocabulary lock / Decisions log / When-in-doubt table / Path-scoped rules / Before-you-respond). All expected `docs/` present. Modular 4-rule shape. The scaffold absorbed a full React→static stack rewrite without breaking — a stronger endorsement than any single rule citation.
- **Shape variant: AGENTS.md-primary.** qventus is `CLAUDE.md = @AGENTS.md` with a substantive `AGENTS.md` — the *inverse* of this repo (`AGENTS.md = @CLAUDE.md`, substantive `CLAUDE.md`). Both are legitimate skill variants; worth being explicit in the skill about which is canonical vs. a choice. Connects to agent-process brief item (5) (harness-condition the session-start AGENTS read on `rule_shape`).
- **No hooks installed.** The skill emits `settings.json` with `block-env-commit` (always) + gated `block-deploy-cli`/`block-worktree`. qventus has **none** — only `settings.local.json` with a hand-grown 2-entry allowlist (`git rev-list`, `git ls-remote`). A real 33-session project enforced worktree/env/deploy rules as **prose only** — and the **visual-confirmation gate was violated once** (`2026-06-05-section5-flow-polish.md`: committed before Rex's confirmation, caught only when he asked "are you going to let me check it?"). Evidence that prose gates leak — mild support for the on-demand-hooks decision and hooks-by-default — but the project shipped fine without them, so not urgent.
- **`launch.json` + the allowlist are hand-added**, not skill-emitted. The dev command (`python3 -m http.server 8000`) is captured in AGENTS.md but the launch config + permission allowlist grew by hand. Direct support for agent-process brief item (2): seed `permissions.allow` from the captured `{{dev/check/test_cmd}}` + a launch shell.

### 5. session-start filename-sort bug — confirmed defect, still unfixed in the skill (and in THIS repo).

qventus hit it on 2026-06-05: four same-day `2026-06-05-*` retros, the command's filename sort surfaced the alphabetically-last one and "reported stale context" (`2026-06-05-prd-slim-recipes-and-cleanup.md`). qventus fixed its **local** command to pick the latest retro by **git add-history** instead of filename. The skill template `claude-commands/session-start.md.template` **still says "sort by filename date"** — and so does *this* repo's `.claude/commands/session-start.md` (latent; today's single-retro case happened to sort correctly). **#1 backport candidate.** Connects to agent-process brief item (1) (timestamped-H1 retro convention is the other half of this fix — qventus solved it via selection, the brief solves it via naming; they should land together).

## What was verified

- **Retro findings are citation-backed**, each to a named qventus retro with a quoted sentence (subagent report retained in session context).
- **Structural claims verified by direct reads**, not inference: read qventus `AGENTS.md`, `CLAUDE.md` (11 bytes, `@AGENTS.md`), all 4 rules, `session-start.md`, `settings.local.json`, `launch.json`; diffed against the skill's `session-start.md.template` and `claude-settings.json.template`.
- **Deploy-absence triple-confirmed** across rule + PRD + ROADMAP, not a single source.

## What was NOT done / honest misses

- **Read-only; nothing changed in qventus or the skill.** No template fixes applied this session — the post-mortem is the deliverable; fixes are separate scoped sessions (the filename-sort backport is ≤3 files and ready to go next).
- **design-system-bootstrap end-to-end still unvalidated.** qventus declined it, so its from-scratch path has zero real-project evidence. Backlog item stays open.
- **Did not re-run the qventus session-start command or live-fire anything** — this was a documentation audit, not a behavior test; the validation contract's live-fire bar doesn't apply to a read-only post-mortem.
- **One project, two pivots.** Strong but singular. The design-system and orchestrator conclusions rest on a project with an atypical pre-existing design system; flagged as such, not generalized.

## Next session

- **Backport the session-start retro-selection fix** (filename-sort → git-history) into `templates/claude-commands/session-start.md.template`, `examples/output-small/`, and **this repo's own `.claude/commands/session-start.md`**. Pair it with the agent-process brief item (1) timestamped-H1 convention. ≤3 files, ready.
- **agent-process brief item (2)** (seed `permissions.allow` + launch shell) now has direct qventus evidence — promote when starting a harness session.
- The `/idea-to-product` orchestrator case is *tempered, not killed*: if built, it must branch "skip bootstrap if a design system already exists."
- For the deploy-shell pilot and design-system-bootstrap validation: both need a **new deploy-targeted, bootstrap-from-scratch** project. qventus can't supply either.
