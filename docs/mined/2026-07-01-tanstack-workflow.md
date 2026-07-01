# Mine — TanStack/workflow — 2026-07-01

- **Source:** [github.com/TanStack/workflow](https://github.com/TanStack/workflow) — "Type-safe durable execution for TypeScript. Workflows are async functions that pause, persist to an append-only log, and resume after approvals, webhooks, timers, or restarts."
- **Pinned:** `602cdec439876335168d96f5443c0dc59e4cc436` (shallow clone, `docs/mined/repos/workflow/`, gitignored)
- **License:** MIT (Tanner Linsley / TanStack)
- **Lens:** Track 2 project-setup. Prior was *"likely tangential (durable-execution runtime)."* Two blind readers (what-it-is/orchestration relevance · craft/template-reuse delta) tested that prior against the files. Lens **A** = our tooling; **B** = scaffold output.

## Verdict — the "tangential" prior is REFUTED (for orchestration), CONFIRMED (for project-setup)

workflow is a headless durable-execution **runtime library**, not a setup tool — its deploy adapters (`workflow-vercel|cloudflare|netlify|railway`) are thin runtime-hosting shims that wake already-deployed code (`docs/guide/runtime-model.md:91-92`), **not** deploy setup. So for the Seq-1 project-setup gap it is genuinely weak. **But** it carries the maintainers' own design docs (`research/AI_ORCHESTRATION_INTEGRATION.md`, `research/PRIOR_ART_AI_ORCHESTRATION.md`) showing this engine is the durability substrate under a TanStack **AI-agent orchestrator** (`defineAgent`/`defineOrchestrator`/`defineRouter`, `AI_ORCHESTRATION_INTEGRATION.md:9`) — a near-exact prior-art match for our parked **chain-auto-compose** idea. The lightweight-pass prior would have missed this entirely.

## Findings

### W-1 — Chain-auto-compose has strong external prior art · code-grounded (Lens A) · ADOPTED (→ folded into Chain-auto-compose row)

**Source:** `research/AI_ORCHESTRATION_INTEGRATION.md:9` (refactor the AI orchestrator to sit on the durable engine); `docs/overview.md:33-34` (append-only event log is source of truth; state is *derived* by replay, never persisted); `docs/concepts/primitives.md:84-97` + `docs/concepts/replay-and-resume.md:59-107` (`ctx.approve({title})` pauses until a human resolves it, returning `{approved, feedback}`; resume appends `APPROVAL_RESOLVED` and re-runs; idempotent `stepId`/`signalId` so duplicate delivery no-ops; version routing so a paused run resumes on the version it started).

**What transfers (the model, not the code):** when chain-auto-compose is picked up, spec its state on this pattern — **log each hand-off; derive chain progress by replay; model approvals as durable pauses; make resume idempotent** — rather than inventing one. Read `research/AI_ORCHESTRATION_INTEGRATION.md` in full first. **What does NOT transfer:** the TS engine's replay-determinism contract (`ctx.now()`/`ctx.uuid()`, side-effects only in `ctx.step`) — our chains are markdown skills + a JS harness invoking Claude Code sessions, non-deterministic by nature. Import the concepts, not the dependency.

### W-2 — `zizmor` GitHub-Actions security scan · code-grounded (Lens B) · ADOPTED (→ folded into supply-chain-defaults row)

**Source:** `.github/workflows/zizmor.yml:1` ("GitHub Actions Security Analysis", `permissions: {}` default-deny). A net-new gate over the base template — scans the workflows themselves for supply-chain/permission issues. Extends the bounded supply-chain security set already captured from template + gstack.

### W-3 — Docs-craft patterns · mixed · ADOPTED (→ watching row, gate:rule-of-2)

Three net-new-over-base-template docs patterns, single-source so parked under rule-of-two:

- **Generated-reference + thin hand-written orientation layer (`code-grounded`)** — `docs/reference/` is 100% typedoc-generated with source backlinks; a *separate* hand-written `docs/api/index.md` explains which package to start with and why, and links to (never edits) the generated set. Completes our "generated docs regenerated not hand-edited" rule with its missing half: keep a thin hand-orientation layer over the generated dump.
- **`research/` status-column disposition table (`soft`)** — `research/README.md:3` declares "**Not maintained as living docs** — treat as historical context," and the index carries a **"Status of recommendations"** column tracking each note's fate ("Candidate 2 won.", "Shipped.", "Forward-looking"). A one-line disposition per point-in-time artifact — directly usable for our `docs/council/` · `docs/brainstorms/` · `docs/mined/` archives (and portable to a scaffolded project's research archive). Resonant with our point-in-time-records carve-out + D-048 retirement ritual.
- **Self-epistemic comparison doc (`code-grounded`)** — `docs/comparison.md:27,30` ships a "TanStack signal" column self-tagging each row **differentiator / table-stakes / non-goal** and an explicit rule: "when public documentation does not clearly support a first-class claim, the cell is marked partial." A rare doc that cites its own epistemics (echoes "every rule cites its failure mode"). An optional scaffolded doc type.

### Dedup / dropped (no action)

- **Base-template foundation** — the enumerated `test:ci` gate list, `nx affected`, knip/sherif/size-limit, changesets, `verify-links.ts` (identical script), placeholder-token adoption ritual, SHA-pinned actions + `permissions: {}` — all **already mined from [TanStack/template](2026-07-01-tanstack-template.md)**; workflow inherits them unchanged. Not re-proposed.
- **`adapter-roadmap.md` demand-gated expansion rule** ("don't add the next store adapter until an existing one has proven the missing requirement") — *confirms* our existing guardrail-restraint / rule-of-two, no new rule.
- **Deploy-doc content (`soft`)** — `docs/guide/deployment.md:333-357` failure model + checklist + "migrations belong to app deploy not the cron path" — folded as a content note under the Deploy Configuration row, not a standalone item.
