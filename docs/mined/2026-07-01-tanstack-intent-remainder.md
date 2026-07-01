# Mine — TanStack/intent (remainder) — 2026-07-01

- **Source:** [github.com/TanStack/intent](https://github.com/TanStack/intent) — CLI for library maintainers to generate, validate, and ship Agent Skills alongside npm packages.
- **Pinned:** `f9269e5349f1d716eba1012bda39df5bc7bbfeff` (same SHA as the [2026-06-30 mine](2026-06-30-tanstack-intent.md); shallow clone `docs/mined/repos/intent/`, gitignored). MIT.
- **Lens:** same as the prior mine — Lens A = our skill-authoring + validation discipline; Lens B = the shipped `context-engineering` scaffold.
- **Scope of THIS mine (the remainder):** everything the 2026-06-30 pass deliberately skipped — the full test suite (29 files, 12.4k lines), the per-agent hook adapters + install machinery, the unread commands (install/scaffold/setup/stale/support/exclude/meta/load/list), scanner/fs-cache/walk internals, skills/resolver, the docs set, and — the sleeper — the **eval harness** (`evals/intent-discovery/`) and benchmarks. Motivation: the CE-plugin remainder proved test suites are the densest IP layer; this run confirmed it a second time.
- **Now exhausted:** with both passes, the repo is substantively covered.

## How this mine ran

Three blind readers over disjoint slices (test suite · CLI/hooks/install mechanics · core internals + docs + eval harness), each given house facts + the combined dedup inventory (prior intent mine + CE-plugin mines) as facts, never valuations, forbidden to Write. 17 load-bearing citations spot-checked in the main session against the pinned clone — **all confirmed**.

**Taxonomy correction:** the prior mine recorded the eval graders' failure taxonomy as 6-way. The corpus type is **13 classes** (`corpus/tasks.ts:15-28`), adding `instruction-ignored`, `wrong-surface`, `command-unknown`, **`late-load`** (loaded guidance *after* editing — a distinct, host-relevant failure shape), `final-output-only`, **`context-saturation`**, and `prompt-too-vague`.

## Findings by landing surface (adopted 2026-07-01; citations relative to the clone)

### IR-1 — The prose-experiment methodology, shipping · code-grounded · → pressure-test ticket (the headline adoption)

`evals/intent-discovery/` is a working instance of the experiment our pressure-test ticket describes — measuring whether ambient guidance prose changes agent behavior:

- **Condition lattice with a diagnostic ceiling arm.** Six conditions (`no-intent` → `plain-docs` → `current-intent` → `mapped-intent` → `hooked-intent` → `explicit-intent-control`), each with `countsTowardAutonomousScore`; the explicit-instruction arm is `false` — it exists only as a ceiling check, excluded from the headline score (`corpus/conditions.ts:1-26`). Prompt explicitness is a *separate* 0–4 dimension; level 4 is hard-excluded from autonomous scoring (`conditions.ts:42-44`). What-the-prose-says and how-explicit-the-user-was are isolated variables.
- **Prose materialized from production code, never hand-copied.** The harness imports `buildIntentSkillsBlock` from the shipped package and writes the *actual* guidance block into the fixture workspace (`harness/setup-intent-condition.ts:3-7,128-138`) — the measured prose cannot drift from the product. Host analog: inject the real SKILL.md under test, not a paraphrase.
- **Calibrate the grader before trusting a run.** Every corpus task carries an `expected` block including its expected *failure class*; the committed suite asserts the graders reproduce those expectations on hand-written known-outcome transcripts (`corpus/tasks.ts:30-35`, `intent-discovery.eval.ts:59-62`). The saved-transcript tier regression-tests the measuring instrument, not the agent.
- **Two failure channels, never confused.** "Harness integrity failures fail the eval. Product findings such as reference-only behavior … are recorded as diagnostic failures, not passing scores" (`README.md:52`); live assertions check only `runnerStatus === 'completed'` + evidence presence.
- **pass@k / pass^k aggregation** over repeated runs (`bin/summarize-results.mjs:83-106`) — pass^k ("every run succeeded") is the reliable-not-lucky metric; per-condition rate table + failure-class histogram. Concurrency pinned to 1 with a *measured* reason (parallel calls on one account contended upstream ~2×, `README.md:29`).
- **LLM judge quarantined.** "You must not decide whether Intent was invoked; that is provided by deterministic scores" (`bin/llm-judge.mjs:83`); annotations land in a separate file, "it never changes deterministic scores" (`README.md:33`); mandated `unknown` option.
- **Anti-contamination guards, tested.** Prose mention ≠ invocation (`parseIntentCommand('I would run intent load …')` → undefined); user-prompt mentions can't count as evidence; the gate's own deny message is tested to be un-parseable by the grader (`harness-capture.eval.ts:178-210`, `intent-hooks.eval.ts:94-97`) — the instrument cannot feed its own signal.
- **Three-tier runner:** saved transcripts (grader calibration) → fake-runner command backend validating the *capture pipeline* at zero live cost (`live-copilot-harness.eval.ts:50-99`) → live agent runs; a missing live backend surfaces as `runnerStatus: 'unsupported'`, never a silent skip.
- **Fixture corpus as declared manifest**, integrity-tested (declared files exist; each task's fixture covers its expected skill areas), copy-on-use isolation with a byte-identity check on the source (`corpus/fixtures.ts`, `fixture-corpus.eval.ts:12-41`, `harness-capture.eval.ts:238-256`).

**Honest limits (verified):** the corpus is tiny (3 saved transcripts, 5 live tasks) and its committed suite proves grader correctness, not agent behavior; `plain-docs` is defined in data but a no-op in the live apparatus (`setup-intent-condition.ts:29-31`); explicitness levels 0–4 declared, only 2 and 4 used; live tier is Copilot-only. The *design* transfers; the runner would be rebuilt on scripted Claude Code sessions.

### IR-2 — Codex blocking hooks: confirmed shipping · code-grounded · → on-demand-hook-scaffolds row

Not just feasible — implemented: `.codex/hooks.json` project/user targets (`src/hooks/adapters.ts:50-59`), same `SessionStart` + `PreToolUse` events, matcher includes `apply_patch` (`policy.ts:14`), deny envelope byte-identical in shape to Claude's. Portability detail: Codex lacks `${CLAUDE_PROJECT_DIR}`, so the hook command is `node "$(git rev-parse --show-toplevel)/.intent/hooks/intent-codex-gate.mjs"` (`install.ts:482`). Copilot's degradation axis is **scope and event granularity, not block-vs-guide** (user-scope only, no matchers, bare envelope). Design choices to weigh, not copy: their emitted gate is deliberately **fail-open** (`catch {} … process.exit(0)`, `install.ts:85-90`) — availability over enforcement, the opposite posture to our D-006 write-guard; hooks carry `statusMessage` + `timeout` UX affordances ours don't set; gate state lives in tmpdir (OS cleanup silently re-locks). The deny reason is command-free by design and tested to be un-parseable as an unlock — see IR-4.

### IR-3 — Version-stamp + upgrade advisory on emitted files · code-grounded · → brownfield-drift row

Generated workflow files carry `# intent-workflow-version: N`; `support.ts:28-53` compares against the current `INTENT_CHECK_SKILLS_WORKFLOW_VERSION = 3` and emits "Intent workflow update available: run `npx @tanstack/intent@latest setup` to refresh" when behind; silent when current or absent; advisories are excluded from `--json` output. A mechanism for a scaffolded project to *know* its emitted files predate the current skill — the detection half our brownfield row lacks. **Verified caveat:** their loop isn't closed — `setup` skips existing files, so the advisory points at a command that won't actually refresh (the user must delete first). Adopt the stamp+advisory shape, not the broken refresh.

### IR-4 — Prose-lock craft from the test suite · code-grounded · → skill-authoring-upgrades row + consolidation

- **Negative-space assertions dominate**: generated text tested for what it must NOT contain — local/absolute paths (`not.toContain('/home/sarah')`), legacy vocabulary, out-of-scope flags, CLI banner/help chrome in agent-consumed output (`load` stdout must never match `/^Usage:/m` — the consumer is a context window). Grep-shaped, runner-free.
- **Byte-exact golden blocks**: the whole generated managed block asserted with `toBe()` against one inline string, deterministic sort pinned (`install-writer.test.ts:121-167`).
- **Deny-reason self-reference trap**: the gate's error text is fed back through the parser and asserted un-matchable (`hooks.test.ts:99-102`) — a guard against a hook's own message triggering the behavior it polices.
- **"Agent fakes the ritual" cases**: `echo intent load …` must NOT unlock the gate; a real load in an or-chain must; a `#`-comment mention must not (`hooks-install.test.ts:453-507`). The emitted script is live-fired as a subprocess in the suite — our manual live-fire contract, automated (`:323-358`).
- **Emitter/detector round-trip**: formatter output must pass its own recognizer, and a paraphrase must fail it (`skill-paths.test.ts:129-152`).
- **Auto-fixer non-destruction checklist** (`cli.test.ts:1971-2248`): `--check` writes nothing (byte-identical after); CRLF + body bytes preserved exactly; trailing YAML comments survive; partial failure corrupts nothing; second run byte-identical (idempotent). The complete list of ways a markdown auto-fixer silently destroys files.
- **Unicode-lookalike traps in trust grammar**: `' * '` (NBSP-wrapped star) rejected as wildcard (`skill-sources.test.ts:222-230`); identity from directory path, never the frontmatter claim; symlink-escape and `..`-hint traversal rejected.
- **N-surface parity**: one trust fixture asserted across all four exposure surfaces (list/load/install/stale) — seam-parity generalized from two ends to N (`integration/source-policy-surfaces.test.ts`); → chain-handoff audit row.

### IR-5 — Typed config key: the Deploy-Config-block pattern, shipped · code-grounded · → project-setup Seq 1

`IntentConfig { version, repo, docs, requires? }` in package.json (`shared/types.ts:5-10`): declared config consulted first, detection is the fallback (`project-setup.ts:110-169`) — including a `version` field on the config block itself. Companion autonomy principle in the scaffold prompt: "Gather this context yourself (do not ask the maintainer — agents should never ask for information they can discover)" (`scaffold.ts:18-19`) — reinforces the adopted CE-1 intake upgrade. Also Seq-1-relevant: template copy is skip-if-exists with per-file "Already exists" reporting; workspace detection spans four manifest dialects with warn-and-continue on malformed config; `edit-package-json` detects and preserves the existing file's indent style.

### IR-6 — /mine hardening adds · code-grounded · → /mine-hardening row

- **Tripwire-file technique**: to prove untrusted code was never executed, plant a candidate whose `index.js` writes a marker file, then assert the marker does not exist after the operation (`scanner.test.ts:1300-1355`, "A candidate package whose code must never be executed during discovery"). Subprocess + filesystem, no runner needed.
- **Grader-calibration-first** (from IR-1): before trusting any verification agent's grades, run it against known-outcome cases.
- **Audience redaction proven by whole-serialization scan**: `JSON.stringify(result)` must not contain the hidden name — no field can leak it (`core.test.ts:278-307`).

### IR-7 — Docs-craft datum · code-grounded · → docs-craft row

The generated/hand-written split is real here and sharper than our banked version: typedoc-generated API reference is **kept out of the repo entirely** (build output, `scripts/generate-docs.ts`); everything committed is hand-written orientation + per-command reference following a rigid template in which **exact runtime strings are the documented contract** — every CLI page quotes verbatim status lines and error strings, cross-checked accurate against the error-code enum. The doc doubles as a testable contract and an agent-greppable error index. Their `verify-links.ts` treats a link resolving *outside the docs root* as its own error class — a small possible complement to `check-live-links.py` (noted, not proposed).

### IR-8 — Consolidation-pass inputs

- **INSTALL_PROMPT anti-hallucinated-success rules** (`install/command.ts:21-122`): "Do not report success until a file was created or updated, or an existing mapping block was confirmed." / "Do not stop after discovery… the task is incomplete until this file exists and contains the managed block." / "Verify the target file before your final response." — our verification-before-done discipline encoded in a shipped agent-executed prompt; plus a 12-mapping cap with ask-first.
- **Residual-risk-sibling pattern** (#153): the regression test and its predicted adjacent failure ("second symlink hop") authored together, both also pinning a secondary symptom (`scanner.test.ts:201-366`). Extends reproduce-before-fix: capture the sibling while the failure is fresh.
- **Real-tooling repro when synthetic can't go red** (#119): "A synthetic `.pnp.cjs` with a no-op `setup()` does not reproduce that, so this uses a real Yarn install… the exact invocation from the report"; CI-vs-local skip policy pinned in code so the regression always surfaces on CI (`integration/pnp-berry-corepack.test.ts:15-62`).
- **Asymmetric failure polarity**: subtractive config (excludes) fails open as safe no-ops; additive-trust config (allowlist) fails closed — one malformed entry rejects the whole list, no partial allowlist; `absent` ≠ `empty` ≠ explicit, each with its own pinned notice (`skill-sources.test.ts`, `source-policy.test.ts:27-29,143-178`).
- **Generated templates pinned THIN**: shipped workflow files must contain CLI calls and must NOT contain inline logic (`workflow-review.test.ts:222-247`) — emitted artifacts delegate to the versioned tool so consumer copies don't fossilize logic.
- **JSON-config ownership by artifact filename**: where marker comments can't live, own-script-name regex over command fields is the ownership marker; reinstall surgically replaces only own entries, and a `note` field *mentioning* the script must not count (`hooks-install.test.ts:147-311`).
- **Runtime-lookup sentinel**: emitted comments instruct agents to re-resolve paths per session — "Do not copy the resolved path into this file." — with stable-path rules rejecting absolute/`..`/store-internal paths (`skills/paths.ts:30-68`); the rule-class "never freeze resolved paths into always-loaded docs."

## Record-only (no action)

- **No uninstall**: the tool writes into `~/.claude/settings.json`, `~/.codex/hooks.json`, `~/.copilot/hooks/hooks.json` and ships no removal command (`cli.ts:161`; zero `uninstall` hits in src) — the anti-pattern to avoid for anything managing `~/.claude`.
- **Hand-authored prose is the least-tested artifact**: the four meta-skills doing the actual generation work are pinned only for existence, frontmatter presence, and a 1000-line cap (`skills.test.ts`) — the inverse of a prose-product workspace's need; validates the pressure-test ticket's priority.
- **Per-run in-memory cache as the alternative to invalidation contracts**: intent's fs-cache lives for one command invocation, persists nothing, caches errors too, and surfaces hit/read stats in `--debug` — over-read instead of over-invalidate (`fs-cache.ts:41-74`). The counterpoint to CE's carefully-invalidated persistent cache.
- **Static-discovery invariant names its enforcement + sole exception in the file header** (`scanner.ts:1-4`: "…never executes discovered package code… Enforced by the `intent/static-discovery` ESLint rule") — our rules-cite-failure-mode grammar extended with "cite the enforcement."
- **Stale-review PR body is a structured agent prompt** with "Do not auto-generate skills." as its first decision rule and required maintainer questions — drift detector proposes, human+agent disposes (`staleness/workflow-review.ts:103-173`).
- npm-keyword-as-registry (`docs/registry.md:9`); coverage-ignores carry reason strings (auditable out-of-scope decisions); README/CONTRIBUTING template rot (badges, phantom `examples/` dir) — even disciplined repos rot at the edges docs-first.

## Dedup

Adds-to (not re-minted): Codex hook scoping (now implementation-confirmed); STOP gates (scaffold.ts's whole 3-phase flow is human-gated between artifacts); audience trust-routing (auto-detected via `INTENT_AUDIENCE`/`detectAgent()`, gates disclosure — "Hidden skill sources are not revealed in agent sessions"); manifest-path-safety (meta.ts arg traversal guard); validate.ts item (failure messages are themselves tested artifacts, incl. "Why this failed:" CI section); fake-CLI harness (new detail: the fake runner validates the capture pipeline, not judgment); seam-parity (N-surface variant); guidance.ts verifier (rejects legacy schema keys during migration; managed-block search order AGENTS.md → CLAUDE.md → .cursorrules → copilot-instructions, existing block anywhere wins; prepend-at-top placement with attention-budget tip). The prior mine's 6-way taxonomy corrected to 13 classes (see above).
