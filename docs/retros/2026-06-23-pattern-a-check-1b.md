# Retro — 2026-06-23 ~18:25 CDT — Pattern-A furnace grounding fix (Check 1b) shipped   (7th session of the day)

`/furnace-plan`'d and shipped the Pattern-A fix from D-063: the furnace preflight's Check 1 verified *that* a read happened, not that it was broad/granular/forward enough to **ground the claim** (n=9+, hidden by per-session micro-splitting). Added **Check 1b** to the furnace skill and ported a generalized analog into the `context-engineering` scaffold's verification rule (both shapes + `output-small`). Top board row, cleared.

## What was completed

- **`skills/furnace-plan/SKILL.md`** — new **Check 1b** ("ground each claim at the breadth, granularity, and forward-reach it asserts") inserted between 1a and Check 2; numbering verified 1 → 1a → 1b → 2.
- **Scaffold, both shapes** — one generalized bullet ("A check must match the scope of the claim it grounds") added to "Verification before claiming done" in `claude-rules-flat-AGENTS.md.template` and `claude-rules-modular/session-discipline.md.template`. No furnace/internal vocabulary leaked (grep-verified RED).
- **`examples/output-small/AGENTS.md`** — collapsed-form clause appended to the Verification bullet; consistency-checked against the flat template.
- **No new `D-NNN`** — executes already-logged D-063; not mirrored (no new binding rule beyond D-063's recorded scope).
- **Scope:** 4 product files, < 20 lines new content. The multi-file count is the port-back discipline (skill + both shapes + fixture move together).

## Process — the furnace caught its own author committing the exact bug it fixes

This is the session's headline. While *authoring the plan to fix Pattern A*, I committed a textbook Pattern-A miss: I proposed an Edit 5 writing a tightening-divider to `trial-ledger.md`, on the inference that "a prior Claude-Code session wrote the 1a divider" — an inference I never grounded, because I'd read only the divider region (lines 95–106), not the **header** (line 5: *"Claude Code … never writes here"*). A too-narrow read that didn't ground its claim.

- **The blind `Explore` reviewer caught it** (Should-consider 1) → I read the header, **dropped Edit 5**, and rerouted the divider to Cowork via sign-off S-1.
- **Cowork then logged my miss to the trial ledger** as a bucket-1 cc-subagent catch, verbatim: *"A too-narrow read (header unread): the exact Pattern-A class this plan fixes."*
- **Cowork's own catch** (the cowork row): the first-draft scaffold failure mode was near-tautological — fixed by embedding a concrete instance ("a green test over one of five call sites still ships the four-site claim untested"), matching the sibling bullet's vivid-instance style.

So the fix was validated by the failure it targets, observed live in three independent layers (blind reviewer → Cowork → the ledger). Strong evidence the loop works as designed.

## Failure this session

- **Tag: lost context** (narrow read → ungrounded claim). The Edit-5 / divider-author miss above. **Tool or agent?** Agent — the header was readable from the start; I scoped the read to the divider and inferred the rest. **Does it generalize?** It *is* Pattern A, now fixed in-product by this very session's Check 1b — the rule that would have forced the broader read. No new guardrail minted; the fix is the guardrail. The honest note: the furnace's *existing* Check 1 should arguably have caught it too, which is exactly why 1b exists (Check 1 passes on "a read happened"; 1b is what demands the read be wide enough). Self-consistent.

## Verification — what it did and didn't cover

- **Re-read + grep, all green:** furnace numbering contiguous (1/1a/1b/2 at SKILL.md:34/38/42/46); no internal-vocab leak in either scaffold bullet; output-small clause present (1 match); `git status` shows only the 4 product files as my writes.
- **Independent checks:** blind `Explore` reviewer (read-only, withheld reasoning) pre-ExitPlanMode; Cowork `/plan-review` post-approval. Both fed only artifact + criteria. Not self-graded.
- **Did NOT cover:** the 1b *divider* is not written — S-1 is open, awaiting Rex's "say the word" to have Cowork append it (ledger line 32 says a tightening *owes* a divider; line 5 says only Cowork may write it). The scaffold change is not exercised by a real scaffolded project (no test runner; consistency-checked only).
- **Ledger sweep:** Cowork's 3-row append swept into a dedicated commit, scoped to `trial-ledger.md` only (D-018 / CLAUDE.md sweep rule).

## Open / next

- **S-1 (open, Rex's call):** want the 1b instrument-generation divider in the trial-ledger? If yes, it's Cowork's write (it offered) — not a Claude-Code session's.
- Board: Pattern-A row clears. Next `next`-lane item is the group-5 in-repo dogfood self-edit loose end (agent-process upgrades).
