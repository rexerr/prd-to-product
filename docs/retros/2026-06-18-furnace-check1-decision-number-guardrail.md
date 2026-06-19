# Retro — 2026-06-18 23:43 CDT — furnace Check 1 decision-number guardrail (sub-case 1a)   (13th session of the day)

## What was completed

Landed the n=2 stale-decision-number guardrail the [plan-review rehost retro](2026-06-18-plan-review-rehost.md) flagged as out-of-scope and deferred. Single directed change, Rex-gated agent-config.

- **`skills/furnace-plan/SKILL.md`** — added preflight **Check 1 sub-case 1a**: string-equality & decision-number claims must re-grep the source (`docs/DECISIONS.md`, plus the trial-ledger for earmarked numbers) **at the moment of writing** and quote both sides from *that* read, not an earlier-in-session grep. Cites the D-040→D-042 collision as its failure mode (per the "every rule cites its failure mode" architecture rule).
- **`skills/furnace-plan/trial-ledger.md`** — added the `--- preflight tightened 2026-06-18 ---` divider the ledger legend (line 24) mandates whenever the preflight changes, so the before/after bucket trend stays legible.
- **`BACKLOG.md`** — closed the pre-registered "second bucket-1 string/equality miss" earmark (marked Landed, with the honest bucket-2 caveat) and updated the forward-pointer in the plan-review bullet that referenced this task.

Commit [`80a863b`](https://github.com/rexerr/prd-to-product/commit/80a863ba7617801e53046d3515e01ae9bb1c0cc9) (code) + this retro.

## What was verified — and how

- **Landing-surface evidence checked, not assumed.** Re-grepped before deciding: both observed collisions (D-018→D-020, D-040→D-042) were furnace-authored plans; the by-hand decision path has **zero** observed collisions (D-021 logged cleanly by hand). So a CLAUDE.md always-loaded standing-step would fix an unobserved failure mode — rejected on the repo's own "cite the failure mode" + anti-sprawl (CF-01) grounds. Chose furnace Check 1.
- **The task's own premise re-verified at source (ate the dogfood).** The task asserted the trial-ledger legend "already earmarks a second bucket-1 string-equality miss." Grepped it: the earmark actually lives in `BACKLOG.md:10`, not the ledger legend — minor misattribution, substance real. And the D-040 collision is logged **bucket-2** (read-but-stale/TOCTOU; rows 86/88, `Round | Bucket` columns confirmed), not the strict bucket-1 the trigger names. Recorded the caveat in BACKLOG rather than overstating that "second bucket-1" fired.
- **Doc cross-references re-read after editing** (per CLAUDE.md "Verification before claiming done", doc tier): re-read the SKILL.md preflight block — 1a sits between Check 1 and Check 2, does not renumber 2/3/4, and its `docs/DECISIONS.md` / `trial-ledger.md` paths are correctly project-relative (the skill runs cross-project via the global symlink).
- **Not verified / out of tier:** no live furnace-plan run exercised 1a — this is prose config, not a hook or template substitution, so live-fire isn't the verification tier. First real proof comes the next time `/furnace-plan` authors a plan that writes a D-NNN. Self-verified; no independent subagent used (small prose change).

## What the bucket-2 finding sharpened

The collision being bucket-2 (planner *did* grep, result went stale by write time) is why 1a's load-bearing clause is **"re-read at write time"** (the TOCTOU fix), not just the pre-registered "quote both sides" (which addressed the CF-03 line-72 string miss). Folding both was correct; "quote both sides" alone would have missed this n=2 instance.

## Deviations / misses

- **Double-push.** Rex's instruction was literally "commit and push and /end-session", so the code commit pushed *before* the retro existed — this retro is a second commit. The end-session skill warns against exactly this double-push; here it was the directed order, not waste from forgetting, but worth naming.
- **No new D-NNN.** Judged this an experiment-internal preflight tightening, already governed by the furnace-trial BACKLOG item (D-020 lineage) — not a binding cross-tool constraint needing its own decision. If that's wrong, it's a one-line add (and 1a now governs how to number it safely).

## Failure tag

**none** — clean execution of a directed, pre-scoped change; the two judgment calls (landing surface, bucket-2 caveat) were surfaced to Rex, not silently resolved.

## Open / next

- **Gated on Rex:** confirm the landing-surface call (furnace Check 1, not CLAUDE.md) and the no-D-NNN judgment, if either is contestable.
- **Next to pick up:** the deferred items from the plan-review rehost retro are unchanged — Rex to deploy `skills/plan-review.zip` to Cowork + smoke-test; then **Plan 2** (subagent-reviewer loop in furnace-plan) in a fresh `/furnace-plan` session.
- **First live proof of 1a** arrives whenever the next furnace-authored plan writes a D-NNN — watch whether Cowork still catches a decision-number drift (would mean 1a isn't being executed) or the class goes quiet.
