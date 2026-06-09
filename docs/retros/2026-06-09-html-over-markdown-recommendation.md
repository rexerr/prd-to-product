# Retro — 2026-06-09 11:08 CDT — HTML-over-markdown investigation + open-decisions sweep   (7th session of the day)

## What this session did

Two things, both documentation-only (no code, no templates, no skill changes):

1. **Ran the long-parked HTML-over-markdown investigation** to a written recommendation memo. Grounded it in real sources rather than re-summarizing the brief — Thariq's gallery, his GitHub repo, his Anthropic article, plus a rebuttal for the opposing case.
2. **Cleared the "Open decisions from prior roadmap" block** in BACKLOG with Rex deciding each.

## HTML investigation — outcome

Memo: [`docs/html-over-markdown-recommendation.md`](../html-over-markdown-recommendation.md). Key findings:

- The thesis is strongest for **spatial/interactive** content (diffs, call-graphs, design systems with live swatches). Thariq's own driver is *human attention* ("feeling in the loop"), not agent correctness.
- Thariq's gallery/repo give **no guidance** on the questions that actually matter for our skills (canonical-vs-derived, diff-noise, when-not-to-use). The rebuttal is the only source engaging those costs.
- **The crux:** our outputs are repo artifacts that the *agent reads at session start AND humans review*. The decision splits by which artifact is canonical.

Recommendations:
- **`context-engineering`** — unchanged (markdown is non-negotiable; agent parses it).
- **`prd-creator`** — stay markdown canonical; HTML only ever an optional *derived* export. `PRD.md` is the agent's session-start source of truth; HTML-as-canonical breaks readability + makes diffs unreviewable.
- **`design-system-bootstrap`** — the one ripe, low-risk case: an HTML *supplement* for the descriptive design-system doc (live swatches, type scale, component previews). Canonical stays the **CSS token file**, so the agent-readability/which-is-canonical objections don't apply. Claude Design ships as HTML for the same reason.

Gating recorded: D-001 requires a `D-NNN` before any emit; D-009 council threshold may apply if scope grows past the DSB descriptive doc. Three open questions left for Rex (commit-vs-gitignore the HTML doc; replace-vs-supplement; council-or-solo on the narrow DSB case).

## Open-decisions sweep — what Rex decided

- **HTML output (skills)** → investigated; **adopt-decision still open**, parked at "documented, awaiting go." Rex chose to document the plan only, no work.
- **Verification skill** → **SKIP** (resolved). The CLAUDE.md prose contract + dry-run-against-`examples/` already cover it; a `verify` skill exists in the ecosystem; no failure pile-up. Removed from open-decisions, recorded here.
- **Agent-teams guidance** → **re-filed** as a future scoped Backlog investigation. The old "watch upstream" condition has partly triggered — the harness now ships first-class `Agent`/`Workflow` orchestration. Real question is now "should `context-engineering` scaffold subagent/workflow guidance," which is its own investigation. Connected to the existing "Skill injection by project type" domain-layer item.
- **On-demand hook scaffolds** → **reaffirmed deferred**. Write-guard hook covers the high-value class; Rule-of-Two not met.

## Verification

- Documentation-only change → applied the doc-change contract (re-read, confirm cross-references resolve). Memo ↔ brief ↔ BACKLOG links all resolve; D-NNN references (D-001/D-005/D-006/D-009) exist in `DECISIONS_ACTIVE.md`.
- Scope: 4 files (1 new memo, 1 new retro, brief Status, BACKLOG), all docs, well under limits. No markdown-only invariant changed — this is a plan, not a switch, so D-001 is not triggered by writing it.

## Misses / honest notes

- **The recommendation is not a decision.** The DSB supplement is recommended but unbuilt and ungated by a `D-NNN`; nothing ships until Rex answers the three open questions and a decision is recorded.
- **The DSB "canonical stays CSS" claim should be re-confirmed against the actual DSB output** before building — the memo asserts the CSS token file is the machine-read source of truth; verify that holds in the skill's current generator before treating the HTML doc as safely "just human-facing."

## Handoff

- **Next on HTML:** Rex answers the 3 open questions in the memo → record a `D-NNN` (and run a council if scope exceeds the DSB descriptive doc per D-009) → only then scope the DSB template change.
- **Still open from earlier (unchanged):** `block-deploy-cli.sh` / `block-worktree.sh` stdin fix; auto-detect-input finding; DSB from-scratch validation needs a real project; build-defaults deploy-shell still needs a live-URL project.

## Commit / push

The HTML memo + brief Status + BACKLOG resolutions + this retro, committed together on `main`. No push unless asked.
