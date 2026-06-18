# Retro — 2026-06-18 09:05 CDT — MCP/connector token audit, skill prune, AB- crib tracker, repo-miner fork resolution   (3rd session of the day)

## What was completed

- **Token-cost audit** of MCPs / plugins / skills. Established the live mechanics: MCP tool *schemas* are deferred (not in context until fetched); what's always-on is the tool-name index + server-instruction blocks + skill/agent descriptions (~10–15k tokens, cached after first turn). Found the bloat is **claude.ai account-level connectors** (~20+), not local config — `~/.claude.json` has zero local MCP servers and the registry reports zero "installed."
- **Pruned 8 never-used local skills** from `~/.claude/skills/` (6 vercel/deploy symlinks + `humanizer` + `make-pages-interactive`), evidence-based off the `skillUsage` log. Filesystem op, not a repo change; all restorable (symlink sources intact; both real dirs have clean GitHub remotes).
- **Harvested** the `engineering`/`design`/`data` connector skill bundles (read-only subagent fan-out, returned drafts) into a reference doc **before disconnecting**, since the source is non-re-fetchable.
- **Converted the harvest into the `AB-` crib tracker** + wired it into the roadmap + BACKLOG (4th crib lane).
- **Resolved the repo-miner A/B fork** via `/devils-advocate` and recorded it on the BACKLOG item.
- Connector disconnect itself is user-side and was in progress through the session (Webflow, Adobe, Gmail, Notion, Drive, Granola, Calendar, Spark, Paste, Figma-dup, brand-voice/data bundles all dropped).

## Failure this session

- **Tag:** none (work product sound and verified) — with one logged near-miss.
- **Name the artifact.** Near-miss: I framed this session as "a live run of your planned `/repo-miner` process" and offered to log it as "evidence that the pipeline works" — but `/repo-miner` does not exist; it was a *manual* hand-run of the idea. Rex caught it ("but we didnt run repo-miner. did we?"). Corrected in-conversation and the BACKLOG note now says so explicitly.
- Lesson→change jump:
  - **Tool or agent?** Agent judgment — a loose process-claim (describing an analogue as the actual thing), not a tooling gap.
  - **Does it generalize?** It's a class (overstating what was done), but adjacent to existing coverage: the harness already guards *output* claims ("never claim success because the code looks correct," `C-22` claim vocabulary). This was a *narration-of-process* claim, caught immediately, zero downstream cost.
  - **→ The change it demands:** none. A new rule against process-overclaim would be a guardrail against a failure that hasn't recurred (the anti-pattern the retro instrument exists to avoid). If process-overclaim shows up again in the tag log, revisit then.

## Files changed

See commits this session (newest first): `e74cf0d` (A/B fork resolution), `2d921aa` (repo-miner refinements), `438f958` (AB- tracker + roadmap/BACKLOG wiring), `ed64b57` ([harness-domain-notes.md](harness-domain-notes.md) creation). New durable artifacts: [`cribs-from-claude-skill-bundles.md`](../cribs-from-claude-skill-bundles.md) and [`harness-domain-notes.md`](../harness-domain-notes.md) (frozen, non-re-fetchable source-of-record for the `AB-` lane).

## Key decisions made

- **`AB-` is the 4th crib lane.** Creating an inventory tracker is not itself a `D-NNN` (consistent with how the DG/CF lanes were added — `D-022` ratified the lifecycle, not each tracker). Thin yield by design: only `AB-01` (mobile type), `AB-02` (data type), `AB-03` (per-type repro, extends `CF-03`) survived the rule-#3 fit-triage; the bulk declined-on-fit as downstream content.
- **Repo-miner A/B fork resolved** (recorded in [BACKLOG](../../BACKLOG.md), not promoted to `D-NNN` — it's a conditional plan, not a binding constraint). One shared engine, two lenses; build a playbook not a skill; wire proven A now; defer B until a real hand-run; B likely folds into a `context-engineering` extension.

## Open items

- **Connectors:** finish the UI disconnect against the session's cut-list (user-side).
- **`AB-01`/`AB-02`** are council-gated Big Rocks (generator-scope expansion, `D-009`) — do not build without a council.
- **Crib work** standing next item is still **Wave 1** (per BACKLOG); the repo-miner *playbook* is its own queued build.

## Next session

- Open with [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md). Pick either the top **Wave 1** crib (cheap adoption) or the **repo-miner playbook** (build the shared engine as a doc, wire A). Both are sub-300-line tasks; neither needs a council.
