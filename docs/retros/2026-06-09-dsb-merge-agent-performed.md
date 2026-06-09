# Retro — 2026-06-09 07:31 CDT — DSB merges are agent-performed, not handed to the user (D-007)   (1st session of the day)

## What this session did

Started as "what's next on our list?" (rec: prd-creator intake.md pass) but pivoted when Rex caught a real boundary error while reviewing last session's write-guard work: design-system-bootstrap's `merge` paths told the agent to **emit a snippet/merge-note and ask the user to apply it by hand** — inverting "you approve, I apply" into "I hand you a snippet, you do the editing."

Fixed it. Logged as **D-007**. The agent now performs skill-defined merges itself and shows a diff for confirm; it never hands the user a snippet.

Deliverables (6 files, +27/−9):
- [`skills/design-system-bootstrap/generator/decisions.md`](../../skills/design-system-bootstrap/generator/decisions.md) — rewrote the rule-file `merge` branch; added a `globals.css` merge subsection; updated the per-template table rows + the "What the generator never writes" file list.
- [`output-summary.md`](../../skills/design-system-bootstrap/generator/output-summary.md) — `(snippet — apply by hand)` → `(merged with consent)`, enumeration widened to the full merge set.
- [`principles.md`](../../skills/design-system-bootstrap/principles.md) — fixed a stale "not yet enforced by a hook" clause (superseded by D-006) + added `globals.css` to the merge set.
- [`SKILL.md`](../../skills/design-system-bootstrap/SKILL.md) — merge-set enumeration + "agent performs it" framing.
- [`DECISIONS.md`](../DECISIONS.md) D-007 + [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md) mirror.

## The investigation that mattered most (before any edit)

Rex's framing was that he might have been *misunderstood* last session — that his annoyed "if I want to change the design that's my prerogative" got encoded into a rule telling the agent it *can't* edit. Two findings settled it:
1. **Grep for "prerogative"/approve-apply across all docs: zero hits.** His pushback was NOT written into any rule. The misread he feared didn't happen.
2. **`git log -S "apply it manually"`: the behavior is from the initial commit (`3fea33c`), not last session.** Last session's D-005 only re-blessed pre-existing design. So "how bad did you mess up our efforts?" → the honest answer was "not in the way you fear; this is old design, and it's a ~5-file correction."

Disentangling the three easily-conflated things up front kept the answer honest: (1) write-guard never-clobber = correct, keep; (2) the snippet-to-user merge = the actual bug; (3) the agent-config self-edit gate = a separate harness guardrail, not mine to remove.

## Design tightened over four review rounds with Rex (none of the first drafts survived intact)

Each round caught a real gap the prior draft glossed:
1. **Safety-model shift made explicit.** The old merge never touched the file (safe by construction). The new merge `Edit`s the protected pre-run file class — so it now *rides the D-006 hook* (interactive `ask` + headless `deny`). No-clobber is preserved by the hook on the Edit, not by "refusing to write." Cited the probe (Edit `deny` honored, #37210 not live) so the move onto the Edit path is verified, not hoped.
2. **Merge semantics specified, not "merge nicely."** Fenced block (`<!-- design-system-bootstrap:start/end -->`), EOF-append-then-update-in-place, framed as *positionally additive, not semantic reconcile*; tailwind = `theme.extend`-append-only; globals.css = all three pieces (`tokens.css` `@import`, font imports, `@tailwind` directives).
3. **`globals.css` was a third backwards path** I'd have missed — my first verification grep only caught "apply by hand," not "emit a merge note." Folded it in and broadened the grep.
4. **`globals.css` insert position is not optional** — CSS silently drops a mid-file `@import`, so the pieces *prepend above existing rules*; "never reordering" was the wrong framing.
5. **Under-listing the merge set** — `output-summary` and `principles.md`/`SKILL.md` named only "rule + tailwind." Widened every enumeration to include `globals.css`.

## Verified — with evidence

- Residual-pattern grep (`apply it manually|apply by hand|snippet for merge|emit a merge note|asks the user to apply|merge-snippet`) across DSB → **zero hits**.
- `principles.md` no longer contains "not yet enforced".
- Both rewritten merge paths (rule branch + globals subsection) state **both** the interactive diff-confirm **and** the headless-skip branch (grep: 3 interactive / 3 headless mentions).
- Concrete semantics present: fence markers, end-of-file, `theme.extend`, "top of the file, above existing rules", "positionally additive".
- New `../../hooks/README.md` cross-ref in `principles.md` resolves.
- `git diff --stat skills/*/examples/` **empty** — no golden-tree impact (merge paths fire only against pre-existing customized files; the example tree is fresh output).

## Deviations from the approved plan (faithful to its spirit)

- Plan listed `SKILL.md:66` and `principles.md:100`'s merge-*scope* statement as "not changing." I edited **both** to add `globals.css` to the merge set — leaving "only rule + tailwind" would have re-created the exact under-listing inconsistency Rex flagged for `output-summary`/`DECISIONS_ACTIVE`. Net 6 files instead of 5; still well under the feature gate.

## Honest ceiling (carried into D-007)

The merge is **positionally** safe (deterministic insert + the D-006 hook gating the Edit), **not semantically reconciling** — if a user has inline hand-written rules, the fenced block lands alongside them and the diff surfaces the overlap for the user to resolve. Interactive-only: headless runs skip the merge (D-006 functional ceiling). If a future Claude Code version regresses Edit-`deny` (#37210), the merge's safety on the Edit path falls back to prose — re-run the probe + `hooks/write-guard.test.sh`.

## Handoff — what remains

- **The prd-creator intake.md pass + invariant checks** (the original "what's next" rec) remains queued and untouched — resume next session. Four findings aggregate into one `intake.md` file: "ask anyway" overcorrection, vocabulary leak, temporal hallucination, auto-detect input; plus the missing `## Gotchas` section in `prd-creator/SKILL.md`.
- **Not yet exercised live:** an interactive DSB run over a real pre-existing customized `globals.css` / rule file — the mechanism is specified and verified by inspection, but the merge itself hasn't run end-to-end. Will happen naturally next time the skill runs against a real project.
- Not committed-and-pushed — committed to `main` only (the task didn't ask to push).
