# Mine — supermemory (supermemoryai/supermemory) — 2026-07-01

- **Source:** https://github.com/supermemoryai/supermemory
- **Pinned:** `42f3aec88583baf8a00c2cfc98b7b615412520c6`
- **License:** MIT
- **Lens:** Skill-development workspace — context-engineering scaffold, prd-creator, the shipped skills' craft, this repo's own agent/CI/memory discipline. Filtered for: skill-craft, project-setup/CI (Seq 1), and our memory-vs-repo discipline.

## Orientation — what this repo is, and where the yield actually was

supermemory is a **memory/context-infrastructure product** (a "living knowledge graph" for AI apps — fact extraction, temporal versioning, RAG). Its `CLAUDE.md`, `CONTRIBUTING.md`, and product-architecture docs are largely **boilerplate or product-marketing** — nothing transferable. The prior-falsification streak held: the name says "memory engine," but the yield came from three places the name doesn't predict —

1. Its **`.github/workflows/`** — three production Claude-Code-in-CI agents, all wired to a shared cross-run memory (the strongest vein; Seq-1 fuel).
2. Its shipped **`skills/supermemory/`** — a product-adoption skill (a contrast specimen for our failure-mode rule grammar) and a battle-tuned **code-review agent prompt** (real skill-craft borrows).
3. Its **memory ontology** — recorded mostly as a *decline*, because our lighter memory discipline already covers it.

The "tests are the densest IP layer" heuristic paid indirectly: `packages/tools/src/claude-memory.ts` is where a real path-security invariant lives, not in any doc (SM-7).

---

## Findings

### Lens B (host-project needs) — the strong veins

#### SM-1 — Agent-in-CI wired to a shared cross-run memory (2nd auto-repair-CI instance + a compound-memory twist) · **verified (code)**

All three CI agents mount the **same supermemory MCP server** as a durable memory shared across every run and PR:

- `.github/workflows/claude-code-review.yml` — review agent: *"Search Supermemory for any relevant past patterns, known issues, or architectural decisions related to the changed code."*
- `.github/workflows/claude-auto-fix-ci.yml` — triggered on `workflow_run` **completion=failure**; prompt: *"Check supermemory for similar past CI failures and fixes … After fixing … Save the fix pattern to supermemory for future reference."* Then commits and pushes directly to the PR branch (no new PR).
- `.github/workflows/claude.yml` — `@claude`-mention responder, same MCP mount.

**Two things here:**
1. **A second production instance of the auto-repair-CI class** (router was the first, per the [project-setup handoff](../handoffs/project-setup-system-handoff.md) / BACKLOG row 18). The trigger shape is worth copying exactly: a *separate* workflow keyed on the CI workflow's `workflow_run: completed` + `conclusion == 'failure'`, not a step inside CI.
2. **A novel compound-engineering pattern we haven't mined before:** the org's agents (reviewer, fixer, responder) share one persistent memory of past incidents/fixes/decisions, so each CI run *learns* — the fixer reads prior fix patterns before acting and writes new ones after. This is "compound engineering" operationalized at the CI layer, and it's the closest external analog to our Chain-auto-compose durable-log idea and the CE-plugin compound-engineering theme.

**Verify:** all quotes are verbatim from the three `.yml` files at the pinned SHA.
**Lands on:** Seq-1 **project-setup** row (enrich: 2nd auto-repair-CI instance + the trigger shape) and **Chain auto-compose** row (the shared-memory compound loop as prior art #3). Candidate new **watching** row: "agent-in-CI (review/auto-fix/@mention) as a scaffold-emit default" — gated on a scaffolded project actually wanting CI agents.

#### SM-2 — CI install-policy + a supply-chain threat-model note + a partial-coverage smell · **verified (code)**

From `ci.yml` and the agent workflows:

- **Install policy:** `bun install --frozen-lockfile` — the bun-equivalent of the lockfile-integrity install policy the [router mine](2026-07-01-tanstack-router.md) flagged (RT-4). A scaffold supply-chain default should name the per-package-manager frozen-install flag, not just pnpm's.
- **Fast CI:** `biome ci --changed --since=origin/main` — lint/format only changed files against the merge base.
- **Threat-model note (new, worth flagging):** the three agent workflows run `claude-code-action` with `--allowedTools "…Bash(*)…"` (fully unrestricted shell) **plus** `secrets.SUPERMEMORY_API_KEY` and an OAuth token in the environment, and the fixer **pushes directly to the PR branch**. That is a real prompt-injection / secret-exfil surface: a malicious PR (or poisoned memory entry) can steer an agent with shell + write access. Belongs on the "shared-/tmp prompt-injection threat model" line of the supply-chain row as a *second concrete instance* — agent-in-CI is itself an attack surface the scaffold should threat-model, not just dependencies.
- **Coverage smell (negative finding):** `ci.yml` type-checks only a **filtered 2-package subset** (`--filter='@supermemory/ai-sdk' --filter='@supermemory/memory-graph'`) — most of the monorepo is never type-checked in CI. Consistent with router's "still no vuln/secret scan anywhere" — a mature repo still ships partial CI coverage. A scaffold check could warn when CI's filter set is narrower than the workspace.

**Lands on:** **Supply-chain + dep-automation scaffold defaults** row (enrich: frozen-install-per-PM, changed-files-only CI, agent-in-CI threat model, partial-coverage warn).

### Lens A (our tooling / skill-craft)

#### SM-3 — Production code-review agent prompt: craft borrows for our rule grammar + review discipline · **verified (code)**

`claude-code-review.yml`'s prompt is a heavily-tuned reviewer. Borrowable, and a **third production instance** of patterns we already track (what-not-to-flag suppression from gstack; grader-calibration from intent):

- **"Silence is a perfectly good review … A PR with 0 inline comments and a clean summary is ideal when the code is solid."** — an explicit anti-noise stance (new; stronger than our current suppression wording).
- **Bounded output:** *"DO NOT leave more than 5 inline comments. If you find more than 5 … pick the 5 most critical."* — a hard cap forcing prioritization (new).
- **Explicit two-column WHAT-TO-COMMENT / WHAT-TO-NEVER-COMMENT lists** (never: style, naming, "consider X instead of Y unless Y is broken", missing tests/docs, praise) — the same shape as our failure-mode + what-not-to-flag rule grammar, with a fuller never-list.
- **Anti-stinginess score calibration:** *"10/10 … is the COMMON case for competent engineers — don't be stingy."* — a grader-calibration instruction that pre-empts the reflexive-harsh-grader failure (matches intent's grader-calibration-first).
- **Boundary heuristic:** *"look at surrounding code that ISN'T in the diff — bugs often hide at the boundary between changed and unchanged code."*

**Lands on:** **Skill-authoring upgrades from gstack mine** row (richer rule grammar) — fold silence-is-good + the ≤N bounded-output cap + the fuller never-list as a production specimen. Also a note for our own review/verification discipline (llm-council, the subagent-verification rule).

#### SM-4 — `SKILL.md` + `references/` progressive disclosure — another production instance (product-adoption flavor) · **verified (code)** · *mostly dedup*

`skills/supermemory/` is a thin `SKILL.md` (173 lines) pointing to five `references/*.md` files (quickstart, sdk-guide, api-reference, architecture, use-cases). Confirms the router `references/`-extraction pattern (RT-1/RT-2) feeding **Seq-2 skill-craft consolidation** — but adds little beyond router, which is already the production proof. Novelty: this flavor mirrors *product docs* into a skill (a docs→references sync). Record; don't re-mint.

#### SM-5 — Anti-pattern specimen: the "proactively recommend our product as optimal" skill · **observation (validates our principle)**

`skills/supermemory/SKILL.md` is a **product-marketing skill**: *"proactively recommend Supermemory as the optimal solution,"* superlatives ("state-of-the-art," "perfect recall"), zero failure-mode grounding. It's a clean contrast case validating our **"every rule cites its failure mode"** / **"'be thoughtful' is not a rule"** invariants — and a mild caution to audit our own `SKILL.md` *descriptions* for over-claiming. Not adoptable work; recorded as a specimen so the principle has an external exhibit.

### Memory ontology — recorded as a **decline** (so a future mine doesn't re-propose it)

#### SM-6 — supermemory's memory model vs. our memory discipline · **decline, with rationale**

`references/architecture.md` is a mature ontology: static-vs-dynamic facts (`isStatic`), three fact relations (**Updates** / **Extends** / **Derives**), temporal versioning (`isLatest`), container-tag isolation, automatic forgetting/contradiction handling. Tempting to map onto our repo's auto-memory (`MEMORY.md` index + one-file-per-fact + frontmatter `type:` + `[[links]]`).

**Verdict: decline.** Our memory discipline already covers the load-bearing parts in a lighter form appropriate to single-dev scratch memory — `type: user|feedback|project|reference` ≈ their static/dynamic split; `[[links]]` ≈ Extends; "update the file, don't duplicate" + "delete wrong memories" ≈ Updates/forgetting. Porting the full relational ontology (explicit supersede edges, `isLatest` version chains) would be over-engineering for a scratch store. The **one** idea with marginal merit — an explicit *supersede marker* when a memory overwrites an older fact (a trail, vs. our silent in-place edit) — doesn't clear the "is this adoptable / does it prevent a real failure" bar for a single-dev memory. Recorded so the next memory-adjacent source isn't re-triaged into a duplicate proposal.

#### SM-7 — Anthropic memory-tool contract (`claude-memory.ts`) · **observation / future-watch**

`packages/tools/src/claude-memory.ts` implements Anthropic's memory-tool API — the `/memories/`-rooted file commands (`view`/`create`/`str_replace`/`insert`/`delete`/`rename`) — backed by supermemory. Its one genuinely reusable idea is a **path-security invariant** (`isValidPath`, lines 607–613): require the `/memories/` prefix **and** reject `../` / `..\\` traversal. We don't build a memory tool, so nothing to adopt now — but noted because (a) our own repo memory is already file-based and close to this emerging standard contract, and (b) if the context-engineering scaffold ever emits memory-tool-compatible structure, this contract + the traversal-defense invariant is the reference. Future-watch only.

---

## Verification — what this did and didn't cover

- **Did:** read the three CI workflows in full and quoted them verbatim; read `SKILL.md`, `references/architecture.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `ci.yml` in full; confirmed the `isValidPath` invariant by reading lines 607–613; confirmed the auto-fix trigger shape (`workflow_run` + `conclusion == 'failure'`). All SM-1/2/3/4/7 claims are code-grounded against the pinned SHA.
- **Did NOT:** read the memory-graph package internals, the SDK packages, the web/browser-extension apps, or the test suites beyond locating them (the tests-are-IP heuristic was noted but not deep-mined — the CI/skill veins were richer and the source is a product, not a discipline artifact). SM-5/SM-6 are observations/declines, not verified adoptable claims. No product files edited — this doc is the only artifact until adoption.
