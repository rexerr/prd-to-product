# Context-drift audit — `field-society-demo` (pilot #2)

**Date:** 2026-06-13 · **Type:** one-off, read-only, by-hand (brownfield audit pilot #2)
**Target:** `/Users/rexc/Sites/field-society-demo` — **not a git repo, scaffold-only** (no `package.json` / no app code; AGENTS.md + `.claude/` + `docs/` only), single-agent (no `.codex/`/`.agents/`), last touched ~2026-05-09/10.
**Method:** same as pilot #1 — diff against the current `context-engineering` modular standard, then classify each gap by KIND.

> This is pilot #2. Its job is to test whether the classification rubric from pilot #1 (epost) is **stable across project kinds**. The cross-pilot synthesis at the bottom is the load-bearing output — it's the evidence for the `/audit-context` build decision.

> Note: the project already contains a prior hand-audit, `docs/context-audit-2026-05-10.md`. The drift need recurs even within a single project — supporting evidence that this is ongoing maintenance, not one-time cleanup.

---

## Headline

A clean, correct **earlier-generation** modular scaffold — right AGENTS→CLAUDE pointer shape, 7 well-formed `paths:`-scoped rule files, per-decision `DECISIONS_ACTIVE` curation, vocabulary lock, complete `docs/` set. It's *younger and thinner* than epost: more of the agent-process layer is missing, but it's also **not yet a real project** (no git, no code), which flips several classifications relative to epost.

**Raw diff: ~13 gaps. After classification: 6 worth backporting, 2 judgment, 5 not-drift / N/A / premature.**

---

## Classification

| # | Gap vs. current standard | Status | Kind | Recommend |
|---|---|---|---|---|
| 1 | Retro convention: timestamped H1 + session-of-day | older plain date-topic; **zero retros written yet** | **A — improvement** | **Backport** (README edit only; no existing retros to preserve — cheapest possible). |
| 2 | Autonomy "run to done" charter | ABSENT | **A — improvement** | **Backport.** One section in `session-discipline.md`. |
| 3 | `/compact` vs `/clear` + `/rewind` guidance | ABSENT | **A — improvement, cheap** | **Backport.** |
| 4 | "Read before you write" + "Checkpoint between phases" sections | **both ABSENT** (epost had them) | **A — improvement** | **Backport.** Two of the three sections the skill names as systematically-missed. Cheap. |
| 5 | `/end-session` (or `/session-end`) command | ABSENT entirely (only `session-start.md`) | **A — improvement** | **Backport.** The bookend is standard now; cheap to add. |
| 6 | "Where facts live — memory vs. repo" note | ABSENT | **A/B — improvement, LOWER fit** | Backport-optional. **Lower value than in epost:** field-society is single-agent (no Codex), so the survives-a-tool-switch driver is weak; only the Claude-auto-memory-vs-repo cut applies. |
| 7 | "Every rule cites its failure mode" | PARTIAL (strong in git/session rules; thin in product/voice/AI) | **B — quality** | Backfill opportunistically. |
| 8 | `permissions.allow` seeded | PARTIAL — only 2 historical `mkdir` grants, no working allowlist | **B — minor, partial applicability** | Low priority; no `package.json` so no check/build seeds apply, and not git so git-status seed is moot — only the read-only core (grep/rg/find/ls/cat) would help. |
| 9 | Council-recommend note | ABSENT | **B — minor for solo** | Optional. |
| 10 | Agent-failure taxonomy as retro tag | ABSENT | **B — adopt only if wanted** | Optional. |
| 11 | Enforcement hooks (env-commit / deploy-CLI / worktree) | ABSENT | **C — PREMATURE, not a gap** | **Skip.** No git, no `.env`, no code, no deploy → nothing to guard *yet*. (Contrast epost: there `block-env-commit` was a real gap because epost has git + `.env.local`.) |
| 12 | Non–Claude-Code-agents-read-only rule | ABSENT | **C — N/A** | **Skip.** No other agent surface exists (no Codex). (Contrast epost: there it was an *intentional opposite policy*; here it's simply inapplicable — **same checklist item, different non-actionable reason**.) |
| 13 | README.md at root | ABSENT | **C — not drift** | **Skip.** The generator never emits a README ("writes shape, not content"); absence is correct, not drift. |
| — | Project is **not under git** | — | **Project-readiness, NOT context-drift** | Flag separately. `git-and-deploy.md` + the commit/push/visual-gate chain are aspirational-as-written until `git init`. This is "project not set up," not "context drifted from standard" — a different category the audit happens to surface. |

---

## Cross-pilot synthesis (epost #1 vs field-society #2) — the real finding

**The "safe backport" tier is rubric-STABLE.** Six items classified identically across both projects with the same recommendation: timestamped retro convention, autonomy charter, `/compact`-vs-`/clear`, the missing session-discipline sections, `/end-session` bookend, and (with a fit caveat) the memory note. These are **project-agnostic improvements** — a skill could recommend them with confidence.

**But the judgment tier FLIPS on project facts, not on the checklist.** Three items got different classifications across the two projects, every flip driven by a project property:

| Checklist item | epost (#1) | field-society (#2) | What drove the flip |
|---|---|---|---|
| Enforcement hooks | real gap (`block-env-commit` worth it) | premature / skip | **has git + `.env`** vs none |
| Memory "where facts live" | high fit (backport) | low fit (optional) | **multi-agent (Codex)** vs single-agent |
| Non-Claude-read-only rule | intentional opposite policy (don't touch) | N/A — no other agent (skip) | **Codex writes on purpose** vs no Codex at all |

The flips cluster on a small set of **project-profile dimensions**: `{under-git, multi-agent-surfaces, has-product-code, has-secrets/.env, has-deploy-target}`. Read those five facts first and the judgment-tier classification falls out almost mechanically.

**Implication for `/audit-context`:** the pilots now define its shape. It is NOT "diff a checklist" — that over-reports ~2× and mis-fires on intentional divergences. It is **(1) read a 5-field project profile → (2) diff the checklist → (3) gate/classify each gap by the profile.** The safe-backport tier is stable enough to automate; the judgment tier is automatable *only because* the flips reduce to profile facts. Two data points were enough to surface the five dimensions; a third would mostly confirm, not extend.

---

## Open decisions (for Rex)

**(a) Fix field-society-demo?** It's a not-under-git scaffold-only demo — lowest stakes of the three. Recommend **defer** (same as epost): the 6 Tier-A backports are captured above if ever promoted. If the project ever gets `git init` + real code, re-run and the hook/permissions items move from premature to live.

**(b) Does `/audit-context` earn building — now with 2 data points?** The build decision is now *designable*: the profile-gated three-step shape above is concrete. Recommendation options below.
