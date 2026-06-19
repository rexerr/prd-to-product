# Retro — 2026-06-18 23:34 CDT — plan-review rehost + host-agnostic rewrite (Plan 1 of 2)   (12th session of the day)

## What was completed

Long design conversation → `/furnace-plan` → 3 Cowork review rounds → execution. Shipped **Plan 1** of a 2-plan effort to bring the Cowork `plan-review` skill under version control and prepare it for a future Claude Code subagent reviewer.

- **Rehosted** `plan-review` from the unbacked-up Cowork plugin bundle into `skills/plan-review/SKILL.md` (verbatim capture first, [D-042](../DECISIONS.md)). Deploy path = ZIP-upload to Cowork (it's a Cowork skill; `~/.claude/skills/` is Claude-Code-only — confirmed against Anthropic skill docs + the open sync feature requests).
- **Host-agnostic rewrite** — output now returns to "the plan loop" by either path (Cowork-paste or subagent-orchestrator); generalized the synced-folder / revise-box mechanics; trigger phrases left verbatim.
- **Decision section** — "Questions for me" → "Open decisions — for the plan loop, not this chat", conformed to **C-16** ([D-031](../DECISIONS.md)): stakes + proof + recommendation + options, so forks are answerable for a non-engineer. Added a finding-vs-open-decision **disjointness rule** to protect the trial-ledger bucket signal.
- Produced `skills/plan-review.zip` (gitignored) for Rex to upload.

## Failure this session

- **Tag:** bad substitution (stale codebase facts — caught by Cowork, not by me or the furnace preflight; corrected in-session).
- **Name the artifact:**
  1. **Decision-number drift.** The first plan asserted the new decision was `D-040`; my "next = D-041" was checked against a grep that went stale mid-session (CF-13 consumed D-041 *after* my read). Cowork caught both; the real number was `D-042`. See `trial-ledger.md` rows dated 2026-06-19 ~04:08/04:14 UTC.
  2. **Incomplete host-bound passage list.** Phase 2a's first draft listed ~4 Cowork-bound lines; a full grep sweep found 9 (missed L3 trigger description, L116, several `synced` uses), and the verification grep as first written would have RED-flagged L3 — an edit-list-vs-grep contradiction Cowork flagged.
- **Tool or agent?** Agent judgment both times — asserting from a stale/partial read instead of a fresh grep at the moment of writing.
- **Does it generalize?** Yes, and #1 is now at **n=2**: the [furnace-plan migration retro](2026-06-17-furnace-plan-migration.md) flagged the identical "stale D-018→D-020 id" collision. Rule of Two met.
- **→ The change it demands:** a **standing "re-grep the decision number immediately before writing the entry" step** in the decisions-log discipline (candidate: CLAUDE.md "Decisions log" or the furnace-plan preflight Check 1, as a named string/equality-claim sub-case — which the trial ledger already earmarked as the "second bucket-1 string-equality miss" trigger). Logged here for the next furnace-plan pass to land; not done this session (out of Plan 1 scope).

## Files changed

- `skills/plan-review/SKILL.md` — new (verbatim capture, then host-agnostic rewrite). Commits `2c78199` (capture) + `153ac3f` (rewrite).
- `docs/DECISIONS.md`, `docs/DECISIONS_ACTIVE.md`, `BACKLOG.md` — D-042 + mirror + marker bump + furnace-item note (`75ed576`, date fix `c4ef9a6`).
- `.gitignore` — exclude the deploy zip (`f06e978`).
- `skills/furnace-plan/trial-ledger.md` — swept Cowork's review-round appends (`5345c12`).

## Key decisions made

- [D-042](../DECISIONS.md) — plan-review hosted + versioned in-repo (full rationale there; mirrors D-020 with a ZIP-upload deploy + no-Claude-Code-surface twist).
- Sign-off resolved: ledger `Reviewer` column **deferred to Plan 2** (no consumer until the subagent exists).

## Open items

- **Deploy (Rex):** upload `skills/plan-review.zip` via Cowork → Settings → Skills; confirm it *updates* (not duplicates); run `/plan-review` on a real plan to confirm the new "Open decisions" section + ledger logging still fire. Only this proves the deployed skill works — not runnable from Claude Code.
- **Plan 2 (separate session):** build the subagent-reviewer loop in `furnace-plan` (read-from-disk handoff, read-only fence + verify-landed-tree, G-11 engineered blindness) + add the ledger `Reviewer` column (`cowork` | `cc-subagent`) + pair-by-plan tally rule. This evolves D-018's writer carve-out (planner still never writes; a distinct reviewer subagent may).
- **Decisions-number standing-step fix** (from Failure above) — fold into the next furnace-plan pass.

## Next session

- If deploying/validating: no skill needed, just the Cowork upload + smoke test.
- If building Plan 2: open with `/furnace-plan` (it self-modifies `furnace-plan` — agent-config change, Rex-gated).
