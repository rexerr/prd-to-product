# Retro — 2026-06-19 09:30 CDT — docs structure & artifact-output routing (research + parking)   (6th session of the day)

## What this session was

Rex asked whether the project's `docs/` sprawl is a real problem, whether it matters to Claude Code, and whether folder discipline should be baked into the skill's scaffolded rules. It evolved into a design conversation about how `context-engineering` should route docs + skill-generated artifacts, then a `deep-research` run to validate the design — which surfaced a tool bug mid-flight.

## What was done

1. **Audited the repo's docs IA.** Found the routing rule already exists in CLAUDE.md ("Where new docs go") but was added reactively, with 18 of 22 root-level `docs/*.md` grandfathered (moving them breaks ~75–90 cross-refs). `.claude/rules/` doesn't exist here (Rex confirmed: keep CLAUDE.md, don't adopt a rules dir — over-engineering for a single-dev repo).
2. **Traced the artifact-routing question to a real mechanism.** Confirmed the `llm-council` skill writes to a generic `<outputs>` with default filenames; this repo's tidy `docs/council/` exists because *this repo's routing rule steered it*, not the skill (proof: early bare-default `council-*.html` next to later steered ones).
3. **Captured the design + parked it.** Wrote [`docs/briefs/docs-structure-and-artifact-routing-brief.md`](../briefs/docs-structure-and-artifact-routing-brief.md) and a BACKLOG pin (sibling to the Context-lifecycle item).
4. **Ran `deep-research`** on the routing/IA question. The workflow's search/fetch/verify stages completed (21 claims survived 3-vote adversarial verification, 4 refuted); the **final synthesis agent infinite-looped** on a schema-validation failure. Stopped it, salvaged the verified-claim set from the synthesis agent's input prompt, and hand-synthesized the report: [`research/docs-structure-artifact-routing-research-2026-06-19.md`](../../research/docs-structure-artifact-routing-research-2026-06-19.md).
5. **Wired research into brief + BACKLOG** (it confirms the design).
6. **Diagnosed the `deep-research` bug**, found its source is app-bundled (not on disk — two sessions produced byte-identical scripts), so could not fix upstream. Captured diagnosis + salvage recipe as an auto-memory ([`deep-research-synthesis-loop-bug.md`](../../../../.claude/projects/-Users-rexc-Sites-prd-to-product/memory/deep-research-synthesis-loop-bug.md)).

## What was verified (concrete, not "looks correct")

- **Cross-references resolve** — checked both directions: brief→research (`../../research/…`) and research→brief (`../docs/briefs/…`) both resolve on disk; BACKLOG links to both files confirmed present. (Per CLAUDE.md "Verification before claiming done" for doc changes.)
- **The bug is real and located** — read the persisted workflow script: `REPORT_SCHEMA` requires `summary`/`findings`/`caveats` ([line 72](../../../../.claude/projects/-Users-rexc-Sites-prd-to-product/df0952b9-607c-4c43-b81a-ee417b55d9f7/workflows/scripts/deep-research-wf_e4dcea6d-c87.js)); the synthesis `agent()` retries on schema-mismatch without a ceiling and never returns null, so the `if (!report)` salvage (lines 319-330) is unreachable in this failure mode. Confirmed the loop empirically: 207 assistant turns / 106 tool-results in one agent `.jsonl`, last event repeating `must have required property 'summary'`; journal frozen 30 min while the agent file grew.
- **Source-unreachable claim verified** — exhaustive search of `~/.claude`, app bundle, and plugins found only throwaway per-run copies; two sessions' generated scripts byte-identical (`diff -q` → IDENTICAL).
- **Research salvage is faithful** — the report is synthesized from the intact verified-claim set (the synthesis agent's own input), not re-derived; refuted claims preserved for transparency.

## What was NOT verified / remains

- The research's headline ("folder structure doesn't help agent retrieval") rests on a **refuted** claim (0-3) — that's "no evidence for," not "proof against." Flagged as such in the report.
- The design is **confirmed by research but not decided or built.** No `context-engineering` template change made. No `D-NNN` logged (this is a parked pre-decision, not a binding call yet).
- The `deep-research` bug is **not fixed** — only documented. Durable fix is Anthropic-side.

## Failure this session

- **Tag:** none (of bad-substitution / scope-creep / lost-context / goal-drift) — but a real **monitoring near-miss** worth recording.
- **The artifact:** after launching the background `deep-research`, I told Rex "I'll be notified when it completes, sit tight" and then stayed passive. The run had gone into a runaway loop, and I only investigated after Rex prodded **twice** ("you seem to be stuck", then "something is wrong"). My first liveness check even *misread* the symptom — I saw the agent file growing and called it "actively synthesizing, not stuck," when it was a retry loop appending failure after failure. The user caught the problem before I did.
- **→ The change it demands:** for long-running background work, don't equate "harness will notify on completion" with "it's healthy." Proactively sample liveness (file growth *and* journal progress *and* what the newest agent is actually doing — turn count / last event type), and distinguish "file growing" from "file making progress." A growing transcript with a frozen orchestrator journal is a loop signal, not a health signal. This is a habit change, not a repo rule — over-encoding it as a guardrail would be the ceremony-accretion the failure-tag instrument exists to prevent. Logged here; promote to a rule only if a second monitoring miss lands (Rule of Two).

## Handoff

- **Gated on Rex:** (1) decide whether to build the confirmed design into `context-engineering` (scope-gate + likely `D-NNN` when promoted); (2) optionally file the `deep-research` synthesis-loop bug to Anthropic — the only durable fix.
- **Uncommitted work in tree** (this session did not ask to commit/push, so nothing was committed): new brief, new research report, new retro, BACKLOG pin edits, two memory files. Say the word and I'll stage all of it as one commit + push.
- **Single next thing:** if picking this up, it's a Rex decision — "build it or leave it parked," not more research. The brief's "Proposed next step" lists the concrete 3-part build.
