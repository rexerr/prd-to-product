# Retro — 2026-06-11 18:47 CDT — DSB motion layer shipped   (2nd session of the day)

## What was completed

- **The DSB motion-defaults layer landed end-to-end.** The BACKLOG candidate (source: [`docs/animation-taste-reference.md`](../animation-taste-reference.md) Part 2, the Emil Kowalski extract) was half-landed as uncommitted edits to `intake.md` Q5d/Q5e and `tokens.css.template`; this session propagated it through every downstream surface and wired the two known gaps.
- **Rex's scope calls (asked up front):** seed components get hover easing only (no `:active` press feedback); the Q7c "Reduce, don't eliminate" strategy gets real template emission now.
- **What shipped:**
  - `tokens.css.template` + `intake.md` (the pre-existing edits, ridden along): fixed `--ease-*` bank (9 curves), six semantic easing tokens (`default`/`enter`/`exit`/`spring` parameterized; `hover`/`linear` fixed), snappy 120/200/280, mellow 150/250/300, ≤300ms product-UI rule, Expressive easing set, >300ms custom-value flag.
  - `globals.css.template`: the always-emitted reduced-motion block became three `reduced_motion_strategy`-gated variants — `disable` (0.01ms block), `reduce_dont_eliminate` (duration tokens remap to fast tier, spring neutralized — works because components only reference semantic tokens), `ignore` (no block).
  - `decisions.md`: two new OPTIONAL keys (`reduced_motion_disable`/`reduced_motion_reduce`, mutually exclusive, derived from Q7c) + the derived `motion_tokens` rule string rewritten (hover easing for hover/color, instant for keyboard-initiated and 100+/day actions, spring as accent only).
  - `output-summary.md`: new flag — Q7c "ignore" surfaces the accessibility-gap warning (makes the decisions.md cross-claim true; not in the plan's file list, 2 lines).
  - `DESIGN_SYSTEM.md.template`: motion section rewritten — instant row, duration bands, six-token easing table, exits-~20%-faster and paired-elements rules.
  - Seed components ×3 (template + output-small copies): hover/focus transitions switched `--motion-easing-default` → `--motion-easing-hover`.
  - `principles.md`: motion-pairs convention updated to the new default curve + bank→semantic structure rationale.
  - `transcript-medium.md`: mellow values 180/280/440 → 150/250/300. (small quotes no values; large's custom 240/180 already conforms: ≤300ms, exit faster.)
  - `examples/output-small/` regenerated: tokens.css (280ms slow, bank, six semantic tokens), globals.css (strategy comment), rule-file motion line, DESIGN_SYSTEM.md motion paragraph.

## Failure this session

- **none.** One honest note: `generator/output-summary.md` wasn't in the approved plan's file list — editing decisions.md introduced a claim ("output summary repeats the intake warning") that needed a 2-line home there. In-scope completion, not creep, but named here so the tag stays honest.

## Files changed

18 files, ~115 insertions / 51 deletions — inside the 300-line feature gate. All under `skills/design-system-bootstrap/` except `BACKLOG.md` and this retro.

## Key decisions made

- **Components reference only semantic easing tokens, never the `--ease-*` bank** (failure prevented: tempo change becomes a component sweep instead of a token-file edit). Recorded in `principles.md`.
- **Reduce-don't-eliminate remaps tokens instead of zeroing transitions** — motion stays as feedback under `prefers-reduced-motion`, stops being spectacle.
- **Not a D-009 fork** — reversible template/prose work, markdown-only invariant untouched; no council. The motion-strengthens-HTML-supplement note stays parked with the HTML memo (Rex-gated).
- The stale "No bounce, no spring" line in the example rule file (never in the derived mapping) replaced by the actual derived string.

## Verification

- **Stale-value sweep:** repo-wide grep for the old curves (`0.4, 0, 0.2, 1` family), 320ms/440ms, old mellow values — zero hits in the skill.
- **Bank parity:** `diff` of `--ease-*` lines, template vs `output-small/tokens.css` — identical.
- **OPTIONAL gating dry-run:** both reduced-motion blocks verified contiguous (comment + `@media` block, no internal blank lines) so the drop rule cleanly emits exactly one (or zero, on "ignore"); output-small carries the disable variant with its strategy comment, matching emission.
- **Snappy/standard substitution check:** output-small motion values match a fresh substitution of the new template against transcript-small's answers (120/200/280 + standard curves).
- **Tailwind path:** confirmed unaffected — components use Tailwind's own `transition-*` utilities and the config template's "Motion: not extended" note stands.
- **Doc contract:** cross-references in BACKLOG edit and this retro resolve.

## Open items

- Tailwind-path motion extension remains deliberately out of scope (recorded in `tailwind.config.tokens.ts.template`).
- The shipped motion layer is live evidence for the pending DSB HTML-supplement decision (BACKLOG "Open decisions"; Rex-gated, needs a D-NNN).
- animations.dev Part 1 skill-craft patterns still parked for the next incidental skill-template edit (BACKLOG).

## Next session

- Rex's stated plan from the 1st session today stands: a batch of additional external resources to review. The review → park-with-triggers pattern converged twice on the same items; this session promoted one of them (motion layer) — convergence-as-promotion-evidence worked exactly as designed.
