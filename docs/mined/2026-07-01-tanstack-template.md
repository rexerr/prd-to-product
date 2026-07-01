# Mine — TanStack/template — 2026-07-01

- **Source:** [github.com/TanStack/template](https://github.com/TanStack/template) — "a starting point for new TanStack libraries" (README.md:40).
- **Pinned:** `22ed1944be1c7ba89194a85815163eb378097414` (shallow clone, `docs/mined/repos/template/`, gitignored)
- **License:** MIT (Copyright 2025 Tanner Linsley)
- **Lens:** Track 2 of the [project-setup handoff](../handoffs/project-setup-system-handoff.md) — the trio scaffolds *context + rules* but not *stack / security / audits / tests*; this repo was flagged the **strongest foundation candidate** ("adopting/forking it may be most of the foundation answer"). Two sub-lenses: **A** — this workspace's own tooling; **B** — what the `context-engineering` scaffold should produce for a downstream project.

## How this mine ran

Three independent reader agents over disjoint slices (foundation/config · CI/automation · adoption-story/structure), each given only the neutral host-project lens — **not** the author's prior — so any convergence would be unbiased. All three converged: **library-authoring scaffold, not an app starter.** Every code-grounded keeper was then re-checked directly against the clone (file contents = ground truth); all survived, including the two easiest-to-get-wrong claims — the negative "no vuln/secret scanning" claim and the Node-pin defect.

## The headline — the handoff's prior is FALSIFIED

`TanStack/template` is a scaffold for authoring an open-source **library/package**, not an app-foundation starter. Settled verbatim by the files:

- `README.md:40` — *"TanStack Template is a starting point for new TanStack libraries. Replace this README content with product-specific copy before release."*
- `docs/overview.md:3` — *"This is a template for creating new TanStack libraries."*
- `TEMPLATE_GUIDE.md:3` — *"This template provides a complete TanStack library setup... Follow these steps to create a new library."*

The shipped "product" is a publishable npm package — a `Template` class + `createTemplate()` over `@tanstack/store`, with per-framework adapter hooks (`useTemplate` React, `createTemplateSignal` Solid) and matching `*-devtools` packages. It stands up `tsdown` + Changesets + TypeDoc + npm-publish CI + `size-limit` + a core/adapter split — **publishing machinery a downstream app never uses.** The **name collision** ("template") seeded the wrong prior. Net for the Seq-1 project-setup decision: **drop "fork TanStack/template" from the option space**; the app-foundation question stays open — the thing to actually read is a TanStack **Start/Router app** starter, not this.

## Findings

### F-1 — A sound foundation = an *enumerated set of orthogonal CI gates*, each catching one failure class · code-grounded (Lens B) · ADOPTED

**Source:** `package.json:29` — `test:ci` = `lint:all && nx run-many --targets=test:sherif,test:knip,test:docs,test:lib,test:types,build`. A "green" build is a named enumeration of orthogonal checks: lint · `sherif` (dep-version consistency across packages) · `knip` (dead code / unused deps) · `test:docs` (doc-link check, `scripts/verify-links.ts`) · `test:lib` (unit tests) · **`test:types` (type-checking as a first-class gate)** · `build` (which ends in `size-limit`, `package.json:11,47-52`).

**Why it matters:** this is the mine's real yield. A sound foundation here isn't "has tests" — it's a *named set of gates each catching a distinct failure class* (dep drift, dead code, doc rot, type regressions, bundle bloat, supply-chain). That maps almost 1:1 onto the dimensions the trio omits (stack strictness, security, audits, tests), **and it fits this repo's existing "every rule cites its failure mode" idiom** — the scaffold could emit a `test:ci`-style gate list per project type, each gate annotated with the failure it prevents. Likely the spine of the "compose don't freeze" connective layer. **Caveat:** this is a *library* gate set; an *app* foundation swaps `size-limit`/provenance for runtime/env/deploy gates — so the connective layer needs per-type gate sets, not one list.

**Landed as:** a note into the [project-setup handoff](../handoffs/project-setup-system-handoff.md) §6 Track 2 (design input to Seq 1); enriches Build-defaults item 5 (check/test pre-commit gate).

### F-2 — Security can be scoped *light*: even a mature foundation skips vuln/secret scanning · code-grounded (Lens B) · ADOPTED (→ row)

**Source (all verified present):** `.npmrc:1` `provenance=true` (npm build-provenance attestation); `pnpm-workspace.yaml:8` `onlyBuiltDependencies: [esbuild]` (allowlist of packages permitted to run install scripts — blocks arbitrary postinstall, a real attack vector); `.github/workflows/pr.yml:57` `fail-on-downgrade: true` (blocks a PR silently rolling a dependency backward); `.github/renovate.json` (`schedule:weekly`, `group:allNonMajor`, `:automergeMinor`, `:approveMajorUpdates`, `:maintainLockFilesMonthly`); `autofix.yml:29` pins a third-party action to a full commit SHA. **Verified absent:** no CodeQL / Snyk / `npm audit` / secret-scanning / Dependabot anywhere in `.github/`.

**Why it matters:** the whole "security" posture of a mature published library is **provenance + install-script allowlist + SHA-pinned actions + Renovate** — *not* vuln/secret scanning. That usefully **bounds** how heavy the connective layer's security dimension needs to be, and gives a concrete, ~20-line default set the scaffold could recommend. Renovate is the single highest-leverage "maintenance runs without me" artifact in the repo (minor-automerge, majors human-gated — matches Rex's reversibility instincts).

**Landed as:** board row — *Supply-chain + dep-automation scaffold defaults* (`backlog`, `area:build-defaults`).

### F-3 — The toolchain-pin agreement defect · code-grounded (Lens B) · ADOPTED (→ row)

**Source:** `.nvmrc:1` pins Node `24.8.0`; `.npmrc:2` `use-node-version=24.14.1` — **two different pinned Node versions in the same repo.** A real drift bug in the source template (verified).

**Why it matters:** concrete motivation for a scaffold-emitted check — if a scaffolded project pins a toolchain version in more than one file (`.nvmrc` / `.npmrc` / CI matrix), emit a check that they agree. Cheap, evidence-backed.

**Landed as:** board row — *Toolchain-pin agreement check* (`backlog`, `area:scaffold`).

### F-4 — Verified adoption ritual (placeholder tokens + files-to-update checklist) · code-grounded (Lens A/B) · HELD (gate:rule-of-2)

**Source:** `TEMPLATE_GUIDE.md:7-13` — a fixed rename vocabulary (`template`/`Template`/`TEMPLATE` → your names) plus an 8-area "Files to Update" checklist (`:16-66`); `README.md:40` — a self-marking *"Replace this README before release"* NOTE-in-place. Adoption is **fork + manual find-and-replace**, honor-system, no rename script.

**Why held:** a genuinely portable "now make this yours" handoff pattern — and this workspace could improve on it (dry-run-diff *verified* substitution instead of honor-system). But single-source and not yet needed. Park until a 2nd need surfaces.

### Dedup / dropped (no action)

- **`scripts/verify-links.ts`** — direct overlap with our `scripts/check-live-links.py`. Theirs is a hard CI gate (`test:docs`) with no retro/point-in-time skip; ours deliberately skips dated retros/council/archive and is on-demand by design. **Ours is better-scoped for this repo. No change** (the "promote to CI gate" idea was already considered and declined in `CLAUDE.md`).
- **`knip` for this workspace (Lens A)** — no `package.json` deps to drift; low value here. Dropped.
- **`copy:readme` fan-out (`package.json:20`)** — named as an *anti-pattern* our no-mirroring rule already forbids; TanStack accepts README duplication because npm needs one per published package, a non-published skills repo should not. Confirmation, not action.
