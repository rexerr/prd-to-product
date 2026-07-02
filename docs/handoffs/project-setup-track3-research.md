# Track-3 research — Project-setup system (compose candidates + gaps)

**Written:** 2026-07-01 · **Feeds:** [`project-setup-system-handoff.md`](project-setup-system-handoff.md) §6 Track 3 · **Status:** research finding, not a decision.

Track 3 asked: what already exists, as **maintained, composable capabilities**, for a project-setup layer (stack standup → secure → audit → test → deploy)? Framed by what Track 1 exposed ([findings](project-setup-track1-findings.md)). Prioritized 2025-2026-current, widely-adopted options.

**Method note:** the bundled `/deep-research` harness failed on its schema layer (the known synthesis/scope schema bug). Salvaged via a direct 5-agent web-research fan-out (one per track), each returning cited findings; synthesis below is the main session's. Reader citations beyond the headline claims accepted on reader authority.

## Headline

**The market sells every *capability*; nobody sells the *glue*.** Each trio hole has strong, externally-maintained, CLI/config-driven tooling. This decisively confirms "compose, don't freeze" — the layer is a composition problem, not authorship. The whitespace is the per-project-type **composition + verification glue** for an agent-driven setup — exactly the thin layer we'd own.

## Compose candidates per hole (all maintained; ★ = first-party)

| Hole | Compose candidates | Notes |
|---|---|---|
| **Expo/RN standup** | ★`create-expo-app --template default@sdk-57` (Expo Router + TS pre-wired); `rn-new --nativewind` automates NativeWind's fiddly 7-step wiring; Obytes template / Ignite as pre-composed all-in-ones | `@latest` still pins SDK 54 — must pass the template flag. NativeWind **v4 needs Tailwind v3** (v4 errors); v5 is pre-release. |
| **Expo/RN deploy** | ★EAS Build / Submit / Update / Workflows | First-party, config-file-driven (`eas.json`, `.eas/workflows/*.yml`). 2026 pattern = fingerprint-gated OTA-vs-native. Paid beyond free tier. |
| **iOS standup** | XcodeGen (YAML, single-maintainer, simplest) or Tuist (Swift manifests + caching, company-backed, team-scale) | Project-as-code kills `.xcodeproj` merge pain. XcodeGen for simple/automatable; Tuist for modular. |
| **iOS toolchain** | xcodes (install Xcode) + mise (`.mise.toml` + `.xcode-version` pin) | **Deadline to encode: Xcode 26+ required for ASC uploads from 2026-04-28.** |
| **iOS signing/submit** | Fastlane match + ASC API key (flexible, self-hostable) **or** Xcode Cloud (low-setup, Apple-locked, 25 free hrs/mo, metered) | **Fastlane maintenance risk** — Google-owned but under-resourced (issue #29713 "Is this project dead?", ~545 open issues). A real fork, not a default. |
| **Tests (JS/TS)** | Vitest (new default, zero-config TS/ESM); **Playwright `npm init playwright --gha`** = harness + CI workflow in one shot (best self-scaffolder found) | Pin the non-interactive `--gha` flag (under-documented). |
| **Tests (RN)** | `jest-expo` + `@testing-library/react-native`; **Maestro** for E2E (over Detox) | Preset exists, but no scaffolder — `package.json` wired by hand. |
| **Tests (Swift)** | Swift Testing (Xcode 16+) for unit; XCTest for UI/perf | **Headless CI actively broken on Xcode 26** (fastlane `scan` freeze #29714; failure-parsing regressions #29799) — corroborates seance's PTY wall as an *industry* condition. |
| **Security (bounded set)** | GitHub push protection + Dependabot alerts (free defaults) · Gitleaks (CI) · Renovate (minor-automerge/majors-gated) · Semgrep (private) / CodeQL (public) · SHA-pin Actions + **zizmor** | The realistic small-team job: don't fight the free defaults, add 2-3 OSS gates, stop. SBOM/SLSA/Snyk = defer until compliance/scale. |

## Genuine gaps a thin layer must fill itself

1. **Version reconciliation** — Expo SDK vs `@latest`, NativeWind↔Tailwind majors. A judgment step no tool owns.
2. **"No test framework → install one"** — GitHub's CI recommender detects the *language* but stops at "run your test command"; nothing cross-stack detects the *absence* of a harness and bootstraps it.
3. **Sequencing** — stack → design-system-wiring → backend → deploy gates (the Track-1 §finding-1 problem).
4. **Credentials/accounts** — Apple/Google accounts, ASC API keys, match storage repo, first App Store Connect app record. Inherently manual, Rex-gated (propose config, never author credentials).
5. **The "verify it ran" gate** — packaged for app scaffolding by no one.

## Two patterns to steal (each maps onto an existing board row)

- **cruft's linked-template model** — keeps scaffolded projects *bound* to their source template: `cruft update` propagates template improvements into existing projects as reviewable diffs; `cruft check` (CI) flags drift. Near-exact fit for our **"port self-improvements back to the skill"** rule + the **Brownfield context-drift** board row — the propagation mechanism we've lacked. Every other scaffolder is fire-and-forget.
- **The verify-it-ran ladder** — weakest→strongest: config-presence → idempotent re-derivation (Ansible/Terraform "no changes" = convergence proof) → exit-code gating → **`doctor`-style probe suites** (flutter/npm/brew doctor: real probe per concern + per-check pass/fail + remediation hint) → **Terraform `check`-block live assertions** (hit the endpoint, assert 200). For **sequencing**, GitHub Actions **`needs:` gates dependents on *success*, not completion** — fusing verification and sequencing into one DAG. Directly answers the Track-1 constraint "verify must route to the capable actor."

## Per-project-type variation — the delivery-decision evidence

For the blocked [Skill injection by project type](../../BACKLOG.md) row (plugin-vs-vendored, [D-009](../DECISIONS_ACTIVE.md) fork):

- **Scaffolder variation models, weakest→most-extensible:** interactive prompts over a *closed* set (create-t3-app) → composable generators + template-by-example (Plop, Turborepo `turbo gen`) → **plugin ecosystem + composable generators (Nx — richest)**. cruft adds linked-template drift management on top.
- **AI-agent variation is context injection, not file templating** — Claude Code **plugins/marketplaces** (GA'd Oct 2025: skills + commands + hooks + MCP bundled, distributed via `marketplace.json`) and Cursor `.cursor/rules/*.mdc`. If our product is installable skills, the right mechanism is a **marketplace of composable skills** with prompts as the thin front-door for choosing *which* to apply — Nx's extensibility philosophy, applied to context rather than code.

## Forks for the council (now with named options)

1. **Starter lane per stack** — RN: official-minimal + à-la-carte vs Obytes all-in vs Ignite. iOS: XcodeGen vs Tuist.
2. **iOS submission** — Fastlane (flexible, under-maintained substrate) vs Xcode Cloud (low-setup, Apple-locked, metered). Costly + hard to reverse.
3. **Delivery** — Claude Code plugin/marketplace vs vendored skills (the blocked row).
4. **Build vs compose the glue** — how much of the verify/sequence layer we author vs borrow (cruft, doctor-pattern, `needs:` DAG).

## Next

Council the four forks above on the combined Track-1 + Track-3 evidence, per [D-009](../DECISIONS_ACTIVE.md).
</content>
