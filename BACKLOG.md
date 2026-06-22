# Backlog — prd-to-product

A single **kanban board** of every open unit of work — one row per unit, read whole at session start. **The board *is* the roadmap:** sort by `Seq` within a lane to see order; there is no separate roadmap file. Full context to *act* lives in the linked `tickets/<slug>.md`, brief, or `D-NNN` — never inline here ([D-048](docs/DECISIONS.md#d-048) / [D-054](docs/DECISIONS.md#d-054)). Card convention: [`tickets/README.md`](tickets/README.md).

Read this at session start alongside the most recent retro in [`docs/retros/`](docs/retros/).

## Board

One row per live unit: **Item · Lane · Seq · Next · Refs**. Lanes are the kanban columns (see Format). `Seq` orders the actionable lanes; `—` elsewhere. Done rows leave the board — their card is archived to [`tickets/archive/`](tickets/archive/).

| Item | Lane | Seq | Next | Refs |
|---|---|---|---|---|
| [plan-review rehost](tickets/plan-review-rehost.md) | next | 1 | First live `cc-subagent` run on a real furnace plan; confirm Cowork transcribes | [D-043](docs/DECISIONS.md#d-043) |
| [/repo-miner](tickets/repo-miner-skill.md) | next | 2 | Build the engine as a lightweight playbook; wire lens A now | [D-022](docs/DECISIONS.md#d-022) |
| Crib adoption (Wave 2) | next | 3 | S4 DSB (G-19); solo CF-07 | [crib plan](docs/cribs-adoption-roadmap.md) |
| Agent-process & context-harness upgrades | next | 4 | Residual: the group-5 in-repo dogfood self-edit loose end | [brief](docs/agent-process-brief.md) |
| Invariant/semantic output checks | next | 5 | OPEN: no-jargon-leak + provenance-grounded checks (write-guard done) | [council](docs/council/council-report-2026-06-08.html) |
| [Docs structure & artifact routing](docs/briefs/docs-structure-and-artifact-routing-brief.md) | next | 6 | Rex decision: build the routing rule + narrow intake Q (research done, confirms design) | [research](research/docs-structure-artifact-routing-research-2026-06-19.md) |
| [furnace-trial](tickets/furnace-trial.md) | watching | — | Paused 2026-06-21; resume only if a real question needs the per-reviewer data | [D-052](docs/DECISIONS.md#d-052) |
| Build-defaults pilot item 1 (deploy-shell) | watching | — | Promote to Done when a live-URL project exercises the deploy-shell | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 5 (check/test pre-commit) | watching | — | Pilot pending item 1's real-project evidence | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 6 (defer abstraction) | watching | — | Pilot pending items 1, 5 | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 2 (vertical slice) | watching | — | Pilot pending items 1, 5, 6 | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 3 (test-first for logic) | watching | — | Pilot pending earlier items | [brief](docs/build-defaults-brief.md) |
| `stack_summary_one_line` row missing (`stack=other + deploy_target=none`) | watching | — | Add on 2nd instance (one seen) | [decisions](skills/context-engineering/generator/decisions.md) |
| Skill ecosystem gaps (Thariq 9-category) | watching | — | Promote one only on a real failure (8 uncovered) | — |
| Chain auto-compose | watching | — | Escalate to `/idea-to-product` orchestrator only if soft handoffs observed dropped | [D-014](docs/DECISIONS.md#d-014) |
| Brownfield context-drift | watching | — | Fix old projects by hand; revisit only if a change must sweep all at once | [D-013](docs/DECISIONS.md#d-013) |
| Token-adopt for Claude Design bundles | watching | — | Revisit on a 2nd real bundle (Rule of Two) | [D-044](docs/DECISIONS.md#d-044) |
| Harness-proposals kill-watch | watching | — | After ~10 sessions read retro failure-tags; revive C / deepen E only if tags recur | [council](docs/council/council-transcript-2026-06-09-harness-proposals.md) |
| On-demand hook scaffolds in the skill | watching | — | Pending a real failure mode (Rule-of-Two not met) | — |
| [Pressure-test behavior-shaping prose](tickets/pressure-test-behavior-prose.md) | watching | — | Verify CLAUDE-auto-load assumption; ≥3 trials/condition before the counter moves (0/2) | [handoff](docs/superpowers-context-engineering-handoff.md) |
| [Superpowers liftables](tickets/superpowers-liftables.md) | watching | — | Fold a/b/c/d into the next incidental edit of the relevant file | [handoff](docs/superpowers-context-engineering-handoff.md) |
| animations.dev skill-craft patterns | watching | — | Fold into the next incidental skill-template edit | [reference](docs/animation-taste-reference.md) |
| [Scaffold-level superpowers candidates](tickets/scaffold-superpowers-candidates.md) | watching | — | Next substantive context-engineering template session | [handoff](docs/superpowers-context-engineering-handoff.md) |
| [Harness-batch liftables](tickets/harness-batch-liftables.md) | watching | — | Fold a/b/c/d into incidental edits on their named triggers | [retro](docs/retros/2026-06-12-harness-batch-review.md) |
| [/decision command](tickets/decision-command.md) | watching | — | Build only if by-hand decision-logging misfires twice (Rule of Two) | [D-021](docs/DECISIONS.md#d-021) |
| Concurrency / parallel-exploration for UI | watching | — | PINNED — not building; clone-or-branch first. **Read the brief before re-proposing** | [brief](docs/concurrency-mode-brief.md) |
| One-board model → context-engineering scaffold | watching | — | After dogfooding here, port the proven board via a D-009 council | [D-054](docs/DECISIONS.md#d-054) |
| [OPTIONAL-marker gating in scaffolded verification rule](tickets/optional-marker-gating.md) | backlog | — | Settle block-vs-line gating, then move universal sentence + logic bullet outside the gate | [D-041](docs/DECISIONS.md#d-041) |
| [/session-start rewrite (Appendix-A)](tickets/session-start-rewrite.md) | backlog | — | Only if `/session-start` bloat bites | [brief](docs/agent-process-brief.md) |
| [Modular-shape example output tree](tickets/modular-example-output-tree.md) | backlog | — | Build as structural assertions (not byte-diff) when modular work picks up | [council](docs/council/council-report-2026-06-08.html) |
| [Agent-teams scaffold guidance](tickets/agent-teams-scaffold-guidance.md) | backlog | — | Promote when a scaffolded project needs multi-agent structure | — |
| [README install loop symlinks `context-engineering-audit`](tickets/readme-install-symlink-cea.md) | backlog | — | Fix on a fresh-clone confusion (contradicts D-019) | [D-019](docs/DECISIONS.md#d-019) |
| AGENTS.md-canonical flip (this-repo half) | backlog | — | Generator half done (D-047); flip this repo's own CLAUDE/AGENTS shape | [D-047](docs/DECISIONS.md#d-047) |
| Build `solutions/` scar-tissue library | backlog | — | Unblocks crib CF-05 | [crib plan](docs/cribs-adoption-roadmap.md) |
| [Skill injection by project type](tickets/skill-injection-by-project-type.md) | blocked | — | Resolve the source-dependent promotion mechanic (plugin vs vendored) first | — |
| DSB HTML supplement | icebox | — | Deferred indefinitely; trigger did not fire at cat-tracker (no hand-built preview) | [D-012](docs/DECISIONS.md#d-012) |
| Candidate future products (3 briefs) | icebox | — | Revisit after Taste Builder validation | [briefs](docs/product-briefs/) |

## Done

See [`docs/retros/`](docs/retros/) for the session-by-session record, and [`tickets/archive/`](tickets/archive/) for archived cards. Skill-build Phases 1–4 (2026-05-10) and continuous-mode sessions (2026-05-10 → 2026-05-11) are recorded there.

## Format

`BACKLOG.md` is a **thin always-loaded kanban board** ([D-048](docs/DECISIONS.md#d-048) / [D-054](docs/DECISIONS.md#d-054)). The board is the only work-tracking surface — no separate roadmap file; the roadmap is the board sorted by `Seq`.

**Lanes** (the `Lane` column — the kanban columns):

- `active` — being worked **this session**.
- `next` — queued and ready to pick up; `Seq` orders it.
- `watching` — parked on a **named trigger**; fires when the trigger trips (not on a schedule).
- `backlog` — real work, not yet queued.
- `blocked` — can't proceed until a dependency clears (the `Next` names it).
- `icebox` — someday/maybe; deliberately not soon.

**Rules:**

- **One line per row.** The context to *act* lives in the linked `tickets/<slug>.md`, brief, or `D-NNN`/retro — never inline. A fat row is a rule violation, not a deferral.
- **A row earns a ticket card only when it has working context to act on.** Icebox/thin rows stay a single line + pointer to an existing detail store (a brief, council, tracker, or `D-NNN`). Don't spawn empty cards.
- **`Seq` orders the actionable lanes** (`active`/`next`) — a suggested order Rex curates; `—` for `watching`/`backlog`/`blocked`/`icebox`.
- **Retire, don't re-accrete.** A resolved row's card is `git mv`'d to [`tickets/archive/`](tickets/archive/) (archive, don't delete) via the `/end-session` retirement ritual; the row leaves the board. Done rows do not return.
- **New idea → a new row**, lane `icebox` or `backlog`. It earns a card when you start it.

## Cross-references

- Project rules: [`CLAUDE.md`](CLAUDE.md).
- Active decisions: [`docs/DECISIONS_ACTIVE.md`](docs/DECISIONS_ACTIVE.md).
- Decisions log: [`docs/DECISIONS.md`](docs/DECISIONS.md).
- Ticket convention: [`tickets/README.md`](tickets/README.md).
- Lifecycle pattern: [`docs/briefs/living-document-lifecycle-brief.md`](docs/briefs/living-document-lifecycle-brief.md).
- Session retros: [`docs/retros/`](docs/retros/).
