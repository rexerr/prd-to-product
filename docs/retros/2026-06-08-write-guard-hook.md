# Retro — 2026-06-08 23:26 CDT — write-guard PreToolUse hook: D-005 enforced (D-006)   (9th session of the day)

## What this session did

Built the **load-bearing closure** the prior session (8th, D-005) explicitly deferred: a PreToolUse hook that *enforces* the non-destructive write guard, turning the qventus clobber class from "mitigated by prose" into "enforced (interactive) / refused (headless)." Logged as **D-006**.

Deliverables:
- [`hooks/write-guard.sh`](../../hooks/write-guard.sh) — global PreToolUse `Write|Edit|MultiEdit` guard (~120 lines, all scoping in-script, the `block-env-commit.sh` pattern).
- [`hooks/write-guard.test.sh`](../../hooks/write-guard.test.sh) — 15 mock-payload assertions, all pass.
- [`hooks/README.md`](../../hooks/README.md) — model, arming contract, install, honest ceiling.
- Skill integration: the "Non-destructive write guard" section in all three `generator/decisions.md` now carries the **arming contract** + an "enforced" framing; DSB + context-engineering SKILL.md gotchas upgraded.
- D-006 in `DECISIONS.md` + `DECISIONS_ACTIVE.md`; BACKLOG council item narrowed to the remaining (b) invariant checks.

The work was **probe-first**: an empirical Step-1 probe (a throwaway debug hook driven by nested `claude -p` + Rex's interactive desktop run) settled every load-bearing unknown before any script logic was written. That sequencing is what kept the "enforced" claim honest.

## Design (after four review rounds with Rex)

Each round caught a real defect; the final design is none of the first three drafts:
1. **`ask`, not exit-2-plus-token.** An exit-2 + agent-written consent ledger is *forgeable* — the agent under pressure self-consents. `permissionDecision:"ask"` forces the native dialog the agent cannot answer. This is the only non-forgeable primitive.
2. **Interactive-`ask` / headless-`deny` mode branch.** `ask` would deadlock a headless orchestrator — so headless → `deny` (default-skip; never hangs, never clobbers). Signal = `CLAUDE_CODE_ENTRYPOINT` (`sdk-*` = headless).
3. **Hook-maintained run-owned set, not a skill-declared snapshot.** Guards files that *existed before the run*; run-created files are auto-tracked and freely re-editable (fixes the self-block). A missing owned-set fails **safe** (gate), never open.
4. **Session-keyed dormancy, refresh-on-match, age-reap-only.** `session_id` is the safety key (a different project = a different session = dormant, so the global hook never wedges unrelated work); no concurrent-session sweep; an idle-then-resumed run is refreshed, not disarmed.

## Verified — with evidence

**Probe (Claude Code 2.1.138 headless + 2.1.165 interactive desktop), all gates PASS** — full record folded in from `/tmp/wg-findings.md`:
- `permissionDecision:"deny"` **honored for Write AND Edit** in `default` and `acceptEdits` (bugs #37210 / the feared acceptEdits-4th-bug **not live**).
- Headless `ask` **auto-resolves to a deny — does NOT hang** (#9026/#64271 not live on the `claude -p` path); so misdetecting headless is doubly-safe.
- Interactive `ask` **surfaces a real dialog** offering **allow-once only** — no "for session" option, confirmed by a per-file re-prompt (Rex's run) → one approval cannot neuter the guard.
- Signal = **`CLAUDE_CODE_ENTRYPOINT`** (`sdk-cli` headless / `claude-desktop` interactive). `/dev/tty` and `permission_mode` **tested and rejected** (both read identically in the desktop app and headless).
- `payload.session_id` == `$CLAUDE_CODE_SESSION_ID` (non-nested) → the arming mechanism works.
- **MultiEdit is not a tool in 2.1.138** (matcher keeps it as harmless forward-compat).

**Hook:** 15/15 unit assertions (every ladder branch + fail-safe + idle-refresh + cross-session + mode branch). **True end-to-end through real Claude Code:** a pre-run `hand.css` overwrite was **blocked** (in `permission_denials`, file unchanged, agent quoted the D-005 reason) while fresh-create + run-owned re-edit passed and `.owned` was maintained.

**Skill edits:** `git diff --stat skills/*/examples/` **empty** (zero emitted-output drift — the guard is generator behavior, not emitted content); all new cross-references resolve.

## Misses / deviations (the important part)

- **Two false-positive "it works" reads, both caught by checking `permission_denials` instead of file state.** (1) An early end-to-end run showed `hand.css` unchanged and I nearly called it a deny — it was actually the agent *not attempting* step 3. (2) A later run was unchanged because the **hook wasn't executable** (exit 126 → Claude Code treats it as a non-blocking error and **allows** the tool); `hand.css` was untouched only because the Edit-needs-prior-Read precondition blocked it first. **Lesson: file-state is a misleading success signal for a guard; assert on `permission_denials`. And the hook MUST be `chmod +x` — that's now in README + the install step.**
- **The "enforced" claim was kept scoped, not inflated.** Per the prior session's lesson (overclaiming D-005), D-006 states the headless **functional** ceiling plainly: an unattended run can never *update* a pre-existing file (it `deny`s), so it is non-destructive *because* it is update-incapable — the `/idea-to-product` gate is cleared for the **clobber-safety class only**, not "the orchestrator's full job runs unattended."

## Honest ceiling (carried into D-006)

Enforced for the pre-run hand-authored class. Bypassable only by `--dangerously-skip-permissions` (not by `[y]s` — no for-session option exists for hook-`ask`). **Not distribution-portable:** the hook lives in the operator's `~/.claude/` and is installed by hand; a shipped plugin would install it at plugin-install time. Unprotected residual: a generator that forgets to arm (prose is the backstop); a forgotten owned-set fails safe.

## Handoff — what remains

- **Step 5 (gated, not yet done):** wire `~/.claude/settings.json` to point a `PreToolUse` `Write|Edit|MultiEdit` matcher at `hooks/write-guard.sh`, and `chmod +x` it. This is a self-edit of Rex's agent config — **needs his explicit OK**; built and staged, not installed. Until installed, the arming in the skills is a harmless no-op and the prose guard is the only protection.
- **Live-fire after install:** the interactive `ask` path is already proven; after global install, confirm concurrency (two armed sessions don't disarm each other), idle-refresh, and a real `design-system-bootstrap` run over a hand-authored `tokens.css`.
- **Still open (separate):** (b) invariant/semantic checks (no-jargon-leak, provenance-grounded) — the council's "a day" layer; the `block-deploy-cli`/`block-worktree` + `"if"`-field item (left unchanged pending Rex's independent `"if"` verification — claude-code-guide says `"if"` IS official, which would change that item's premise); distribution-portability of this hook.
- **Do not build `/idea-to-product`** until the hook is installed *and* a distribution story exists — the gate is cleared only for the clobber-safety class.
