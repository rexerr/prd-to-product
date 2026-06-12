# Retro — 2026-06-12 09:15 CDT — CLAUDE.md slim via progressive disclosure (item E)   (2nd session of the day)

## What was completed

- **Shipped E** (harness-proposals item, promotion evidence met in the 1st session of the day): this repo's CLAUDE.md slimmed **158→135 lines / 1,836→1,181 words (−36%)**. Design: every binding rule stays inline as a one-liner *with* its failure-mode citation (the repo invariant); rationale, history, and attribution cut to plain markdown pointers at content that already existed (D-009 in `docs/DECISIONS.md`, retro conventions in `docs/retros/README.md`, autonomy/memory rationale in `docs/agent-process-brief.md`). Zero new docs files. **`@include` rejected, not just unverified** — imports load content into context, which defeats slimming; the OpenAI TOC shape uses read-on-demand links.
- **Devils-advocate pass before shipping** (D-009 calibration: reversible prose → DA, not council; run as a fresh subagent to avoid self-grading — second live exercise of the F heuristic after the 1st session's fan-out). Verdict REVISE, 8-item punch list, all applied. Headline catch: the draft cut the four council fork examples while claiming D-009 carried them — D-009 verifiably does not; restored inline. The DA's diagnosis generalized: the cuts had removed *examples* while keeping *principles*, and examples are the trigger-recognition mechanism that binds behavior under pressure. Other restorations: "(or equivalent multi-perspective stress-test)" (required by D-009's own portability reasoning), the product-code enumeration in architecture rule 3, force-push/deleting-work in the gated list, proactive duplicate-memory deletion, `/rewind`'s working-tree mechanism.
- **Honest close-out framing (DA punch-list item 8):** the cited bars (~100-line TOC, 120-line cap, <150 words always-loaded) were **not met and are structurally unreachable** under the every-rule-cites-its-failure-mode invariant (~17 inline rules). Recorded in BACKLOG as *dilution mitigated, not solved*, and as a harmless reversible tidy-up on external-convergence evidence — not an observed-failure fix; the failure-tag log has never recorded instruction dilution (which is also the one failure class the instrument can't self-observe).
- **Verification:** live CLAUDE.md diffed byte-identical against the DA-reviewed draft; all 14 cross-referenced paths checked and resolve.
- **Side thread:** Rex's file-delivery preferences captured to auto-memory (Claude-local UI behavior, correct side of the where-facts-live cut): review artifacts staged in-repo with relative md links (side previewer works; `SendUserFile` cards are dead ends), HTML always `open`ed in his browser (in-app viewer buggy with animations).

## Failure this session

- **none** — with one near-miss worth logging: the first slim draft committed a **bad substitution** (cut content while asserting it was relocated; the relocation target didn't contain it). Caught by the DA subagent *as designed*, before anything touched the repo. Evidence for the DA-before-shipping calibration, and for fresh-subagent review over self-review.

## Files changed

- `CLAUDE.md` — slimmed per above (Rex-gated self-edit, explicitly approved this session).
- `BACKLOG.md` — item 39: E marked shipped with the honest framing; kill-watch line reconciled (E no longer a pending guardrail).
- `docs/retros/2026-06-12-claude-md-slim.md` — this retro.

## Key decisions made

- No D-NNN: the slim is reversible prose; the markdown-only invariant, all D-001…D-010 constraints, and every binding rule survive verbatim-or-terser. The one design call worth remembering: **pointers carry rationale; examples stay inline** — relocating trigger examples is the failure mode, not the fix.

## Open items

- Standing gated items unchanged: the two `.claude/` self-edits (settings.json permission seed; session-start AGENTS.md step), plan-review mining run (Workflow opt-in), `block-deploy-cli.sh`/`block-worktree.sh` stdin fixes with remediation-text enrichment.
- If lost-context ever recurs in the tag log, the kill-watch now reads "consider deepening E beyond the 36% trim" — deeper cuts would have to confront the failure-mode-invariant trade explicitly.

## Next session

- E is closed; In-progress items remain validation-blocked (deploy-shell needs a live-URL project; BACKLOG-scaffolding consolidation needs a post-change scaffold or a deliberate dog-food-evidence ship decision). The latter is the only one workable without an external project — if Rex wants motion, that's the candidate.
