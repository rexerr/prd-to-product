# Retro — 2026-06-30 16:36 CDT — No-hooks allowlist gap (emission + reporting) — (3rd session of the day)

Follow-on after shipping slice 2c. Picked up the small `area:generator` backlog row logged this morning, then closed a related reporting gap Rex asked for. Two small commits.

## What was completed

- **Emission fix** ([4f07802](https://github.com/rexerr/prd-to-product/commit/4f07802)). The generator's emission manifest gated `.claude/settings.json` on `enforce_rules_as_hooks == true` ([`generator/decisions.md`](../../skills/context-engineering/generator/decisions.md):247), contradicting the same file's `:367` carve-out and the template's `//permissions` note (both say emit a permissions-only file when hooks are opted out). A no-hooks scaffolded project therefore lost its seeded read-only allowlist entirely. Changed the manifest row to `always` (hooks block stays conditional, drops when off) and reconciled the two prose spots (`:26`, `:342`) so the contradiction can't be re-read in. Retired the backlog row.
- **Reporting gap** ([1ece1a6](https://github.com/rexerr/prd-to-product/commit/1ece1a6)). The post-gen report ([`output-summary.md`](../../skills/context-engineering/generator/output-summary.md)) mentioned `settings.json` only under the conditional "Hooks (if enabled)" item, so a hooks-opted-out project never heard about its permissions-only file. Added an always-shown "Permissions allowlist" bullet; tightened the Hooks bullet to "the `hooks` block in `settings.json`" for consistency with the emission fix.

## Verification

- **Emission:** grepped all four spec references after editing — manifest row now `always`; `:26`/`:342`/`:367` + template `//permissions` note all agree (ships always, hooks block conditional). Confirmed no surviving `settings.json ... == true` emission gate. Red→green trace: before, a no-hooks project reading `:247` skips `settings.json` → allowlist lost; after, it emits and drops the hooks block per the notes → permissions-only file.
- **Reporting:** re-read the two bullets; leak-grep clean (no `cluster-N`/`Q-label`/`state-map` in the new report text); `check-live-links` 0/115 broken both times.
- **Did not cover:** no live end-to-end scaffold run of a `enforce_rules_as_hooks == false` project (no fixture for that shape; the repo has no runner). The fix is a spec-consistency fix verified by cross-reference agreement, not by generating a no-hooks tree. If a no-hooks scaffold is ever run, that's the real-world confirmation — and a candidate hooks-off fixture if the shape recurs.

## Failure this session

- **Tag: none.** No failure reached a commit. Minor note: the reporting gap was something I spotted and flagged while doing the emission fix (offered it as optional rather than silently expanding scope) — Rex took it. Surfacing-not-absorbing worked as intended.

## Open items

- **No `enforce_rules_as_hooks == false` regression fixture** exists. Not built (single instance, no runner); revisit if the no-hooks path breaks again or a second no-hooks need appears.
- Board `next` lane is empty after this and the 2c retirement.

## Next session

- Nothing queued. Next work is Rex's pick from `backlog`/`watching`. No residual from this work.
