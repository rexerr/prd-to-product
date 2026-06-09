# Retro — 2026-06-09 08:20 CDT — Claude Design handoff: fidelity test + double council (no build)   (2nd session of the day)

## What this session did

Investigated whether the kit should ingest **Claude Design handoff bundles** (Rex's shifted workflow: design in Claude Design → export a bundle → feed to the kit). Used a real bundle, `the-council/spikes/claude-design/`, as **reference only — no changes made to that project**. Ran the question through a fidelity test and two LLM Council sessions. **Outcome: build nothing this session; clear handoff for a follow-up session.**

This was decision/research work, not code. No skills were modified. The only repo artifacts are docs (a brief, a fidelity-test record, two council report/transcript sets).

## The arc (each step changed the answer)

1. **Initial read + my recommendation:** a new sibling skill `design-handoff-adopt` (inverse of design-system-bootstrap). Wrote [`docs/design-handoff-adopt-brief.md`](../design-handoff-adopt-brief.md) proposing it.
2. **Council #1** ([report](../council/council-report-2026-06-09-design-handoff.html)) **rejected the new skill unanimously.** Verdict: decompose by repeatability — only token transcription is mechanical; reconciliation is human; component recreation is the bundle's own README's job. Don't add a 4th non-composing node. Run a fidelity test first.
3. **Rex's correction:** the "multiple aesthetics" I'd fed the council was largely a **theme picker** (`tweaks-panel.jsx`, `body.twilight`, runtime colorways) + 3 distinct product surfaces — not competing directions. I had over-conflated three different things into one "reconciliation is hard" risk. Owned it; theming is mechanical.
4. **Fidelity test** ([`docs/design-handoff-fidelity-test.md`](../design-handoff-fidelity-test.md)): transcribed the real bundle's `:root` into our two-tier `tokens.css`. Result: **value-lossless (40/40 tokens verbatim — oklch, easings, rgba, scalars) but structurally non-isomorphic** — DSB's scale-first template *fabricates* shades, can't hold 6 fonts in 3 slots, has no tier for 5 categorical accents / `--crt` / a toggle. The Skeptic's "fidelity trap" was real but precisely scoped to the *scale-first template*, not CSS-vars-as-such.
5. **Council #2 (final audit)** ([report](../council/council-report-2026-06-09-audit.html)): unanimous **defer**, then the peer review caught the advisors overreaching — the valuable part.

## The verdict (chairman, audit)

- **Keep killed:** the 4th skill *and* a DSB "adopt mode." Settled twice.
- **Don't build the token-adopt command yet** — not because it's a dangerous importer (it's a *saved prompt* against a static bundle you own), but because at **N=1 you can't separate a shipped theme from tweak-tool scratch**, so you'd hardcode a schema you can't validate. Cheap to write later → deferring costs nothing. Promote on **bundle #2** (Rule of Two).
- **The gap every advisor missed (peer review):** "reference the bundle, don't transcribe" is right for the *kit* and a **fiction for the product** — a Claude Design bundle is a disposable prototype export; the real app needs tokens **in its own repo** to build. Correct move there is a one-time **`cp`** of the tokens into the product repo (lossless values make a literal copy safe), with the bundle staying the source of record for component recreation. **That `cp` is a product-side action in the real app's repo — NOT a change to this kit.**

Net: kill two, defer one (cheaply), and the only "ship now" is product-side (not in this repo).

## Misses / notes

- **I over-conflated the multi-aesthetic input** when framing council #1 (theme picker vs distinct surfaces vs competing directions all lumped together). Rex caught it; the correction materially sharpened council #2. Lesson: when feeding a council, separate "intended product variants" from "design alternatives" explicitly.
- **The council killed my own opening proposal twice** — good evidence the council earns its keep, and a caution against shipping a first instinct.
- `the-council` was touched **read-only**; the `/tmp/council-fidelity/` transcription was scratch (not in the repo) — its findings live in the fidelity doc.

## Handoff — for the NEXT session (system-improvement work Rex deferred)

The decision is made; these are the follow-ups, none done this session per Rex's "new session" call:
1. **Log D-008** in `DECISIONS.md` (+ `DECISIONS_ACTIVE.md` mirror): kit stance = no adopt-skill, no DSB mode, no command now; Claude Design bundles stay authoritative; one-time `cp` into the product repo; revisit a token-adopt command only on a **2nd real bundle**.
2. **Reconcile [`design-handoff-adopt-brief.md`](../design-handoff-adopt-brief.md)** — add a header marking it **superseded by the 2026-06-09 audit** (it proposed the rejected skill; its own status line already says "pre-decision," so it's not misleading, but a pointer to the verdict is owed).
3. **BACKLOG entry:** "token-adopt command — deferred to bundle #2 (Rule of Two); see fidelity test + audit." Promotion trigger = a 2nd real Claude Design bundle.
4. **Tailwind-default note** for Claude-Design-sourced input (default vanilla CSS-vars, never Tailwind translation) — small, only if/when the adopt path is ever built.
5. Open question for that session: does the kit want a tiny **"adopt a Claude Design bundle" guidance doc** (observation log, not a tool) so bundle #2 is re-derived against a recorded baseline? The fidelity doc is the start of that baseline.

## Commit / push

This session's artifacts (brief, fidelity test, two council sets, this retro) committed and pushed alongside the earlier D-007 fix. No changes to `the-council`. No skill changes.
