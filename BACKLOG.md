# Backlog — prd-to-product

A single **kanban board** of every open unit of work — one row per unit, read whole at session start. **The board *is* the roadmap:** sort by `Seq` within a lane to see order; there is no separate roadmap file. Full context to *act* lives in the linked `tickets/<slug>.md`, brief, or `D-NNN` — never inline here ([D-048](docs/DECISIONS.md#d-048) / [D-054](docs/DECISIONS.md#d-054)). Card convention: [`tickets/README.md`](tickets/README.md).

Read this at session start alongside the most recent retro in [`docs/retros/`](docs/retros/).

## Board

One row per live unit: **Item · Type · Lane · Seq · Tags · Gloss · Refs**. Lanes are the kanban columns (see Format). `Seq` orders the actionable lanes — so the next item to pick up is just the lowest `Seq`; `—` elsewhere. The `Gloss` says in plain English what each item is. Done rows leave the board — their card is archived to [`tickets/archive/`](tickets/archive/).

<!-- TAGS · max 2 per row · two axes only — the render validates rows against this list and flags unknowns:
gate:  what must happen before it moves — council · furnace · rule-of-2 · needs-decision · blocked-on-<x>
area:  which part of the system — scaffold · generator · render · skill · skill-templates · docs · crib · mine · furnace-plan · prd-creator · dsb · build-defaults
-->

| Item | Type | Lane | Seq | Tags | Gloss | Refs |
|---|---|---|---|---|---|---|
| Crib adoption (residual) | chore | watching | — | area:crib, gate:rule-of-2 | Folding lessons mined from other repos into ours — waves 1–3 done; re-enters only on a new mine. | [crib plan](docs/cribs-adoption-roadmap.md), [D-059](docs/DECISIONS.md#d-059) |
| CF-22 family router (`/which-skill`) | feature | watching | — | gate:rule-of-2, area:skill | A helper that picks the right skill for a task — build only once skill-picking actually misfires (logged) or the family opens to a 2nd author. | [D-059](docs/DECISIONS.md#d-059) |
| C-01/C-02 furnace mechanical primitives | feature | watching | — | gate:furnace, area:furnace-plan | Two safety checks for the plan-authoring tool — build when a dropped requirement bites or the furnace opens to a 2nd author. | [D-062](docs/DECISIONS.md#d-062) |
| `/mine` hardening candidates | feature | watching | — | gate:rule-of-2, area:mine | Two possible upgrades to the `/mine` skill — held until a second real need shows up. | [retro](docs/retros/2026-06-22-mine-audit-and-dsb-text-wrap.md) |
| [furnace-trial](tickets/furnace-trial.md) | research | watching | — | area:furnace-plan | A measurement experiment on the planning tool — paused; resume only if a real question needs the data. | [D-052](docs/DECISIONS.md#d-052) |
| Ledger-sweep hook | feature | watching | — | gate:rule-of-2, area:furnace-plan | An auto-guard so the Cowork measurement file never gets swept into the wrong commit — build on a 2nd accident. | [D-018](docs/DECISIONS.md#d-018) |
| Build-defaults pilot item 1 (deploy-shell) | feature | watching | — | area:build-defaults | Scaffold a deploy-ready shell first — done when a live-URL project exercises it. | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 5 (check/test pre-commit) | feature | watching | — | area:build-defaults | A pre-commit test gate for scaffolded projects — queued behind item 1. | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 6 (defer abstraction) | feature | watching | — | area:build-defaults | Guidance to not over-abstract early — queued behind items 1 and 5. | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 2 (vertical slice) | feature | watching | — | area:build-defaults | Build one end-to-end slice before going wide — queued behind earlier items. | [brief](docs/build-defaults-brief.md) |
| Build-defaults item 3 (test-first for logic) | feature | watching | — | area:build-defaults | Write tests first for real logic — queued behind earlier items. | [brief](docs/build-defaults-brief.md) |
| `stack_summary_one_line` row missing (`stack=other + deploy_target=none`) | fix | watching | — | gate:rule-of-2, area:generator | A missing summary row for one project-type combo — add when it's seen a second time (one seen). | [decisions](skills/context-engineering/generator/decisions.md) |
| Skill ecosystem gaps (Thariq 9-category) | research | watching | — | area:skill | Eight kinds of skill we don't have yet — build one only when its absence causes a real failure. | — |
| Chain auto-compose | feature | watching | — | area:skill | An orchestrator that chains the skills together automatically — only if hand-offs start getting dropped. | [D-014](docs/DECISIONS.md#d-014) |
| Brownfield context-drift | chore | watching | — | area:scaffold | Old scaffolded projects drift from current standards — fix by hand unless a change must sweep all at once. | [D-013](docs/DECISIONS.md#d-013) |
| Token-adopt for Claude Design bundles | feature | watching | — | gate:rule-of-2, area:dsb | Auto-adopt design tokens from a Claude Design handoff — revisit on a 2nd real bundle. | [D-044](docs/DECISIONS.md#d-044) |
| Harness-proposals kill-watch | research | watching | — | area:docs | Watching whether parked harness ideas earn revival — decide after ~10 sessions of retro failure-tags. | [council](docs/council/council-transcript-2026-06-09-harness-proposals.md) |
| On-demand hook scaffolds in the skill | feature | watching | — | gate:rule-of-2, area:generator | Optional hook scaffolds the skill could emit — waiting on a real failure mode. | — |
| [Pressure-test behavior-shaping prose](tickets/pressure-test-behavior-prose.md) | research | watching | — | area:skill | Test whether behavior-shaping wording actually changes the agent — needs ≥3 trials/condition (0/2). | [handoff](docs/superpowers-context-engineering-handoff.md) |
| [Superpowers liftables](tickets/superpowers-liftables.md) | chore | watching | — | area:skill | Four small ideas borrowed from the Superpowers project — fold in on the next relevant edit. | [handoff](docs/superpowers-context-engineering-handoff.md) |
| animations.dev skill-craft patterns | chore | watching | — | area:skill-templates | Skill-writing patterns from animations.dev — fold in on the next template edit. | [reference](docs/animation-taste-reference.md) |
| [Scaffold-level superpowers candidates](tickets/scaffold-superpowers-candidates.md) | chore | watching | — | area:scaffold | Scaffold ideas from Superpowers — pick up in the next big template session. | [handoff](docs/superpowers-context-engineering-handoff.md) |
| [Harness-batch liftables](tickets/harness-batch-liftables.md) | chore | watching | — | area:docs | Four batched process ideas — fold each in when its trigger file is next touched. | [retro](docs/retros/2026-06-12-harness-batch-review.md) |
| [/decision command](tickets/decision-command.md) | feature | watching | — | gate:rule-of-2, area:skill | A slash-command to log decisions — build only if doing it by hand misfires twice. | [D-021](docs/DECISIONS.md#d-021) |
| Concurrency / parallel-exploration for UI | decision | watching | — | area:docs | Decided NOT to build parallel-exploration mode — read the brief before ever re-proposing. | [brief](docs/concurrency-mode-brief.md) |
| Loop-graduation guidance for scaffolded projects | feature | watching | — | gate:rule-of-2, area:scaffold | Teach scaffolded projects when/how to safely run an unattended agent loop — add when one adopts a loop and the gap bites. | [mine](docs/mined/2026-06-24-loops-article.md) |
| Soften external-audience framing in live docs ([D-069]) | chore | backlog | — | area:docs | Reword a few docs that quietly assume an external audience, now that D-069 says the audience is Rex — on next incidental edit, not a sweep. | [D-069](docs/DECISIONS.md) |
| Rough-render-before-the-gauntlet working policy | chore | backlog | — | area:docs | Flesh out a "show a cheap rough render before any heavy review (furnace/Cowork/council/build)" working policy for when Rex asks for a mockup, and decide where it lives (likely global CLAUDE.md) — discuss in a new session; evidence so far is goal-drift n=2. | [retro](docs/retros/2026-06-26-kanban-schema-and-render-redesign.md) |
| [OPTIONAL-marker gating in scaffolded verification rule](tickets/optional-marker-gating.md) | feature | backlog | — | area:generator | Fix how an optional verification rule is gated in the scaffold — settle block-vs-line first. | [D-041](docs/DECISIONS.md#d-041) |
| Flat-shape rule parity sweep | chore | watching | — | gate:rule-of-2, area:scaffold | The flat and modular scaffold shapes have a small wording gap — sweep all parity gaps together on the 3rd. | [D-067](docs/DECISIONS.md) |
| [/session-start rewrite (Appendix-A)](tickets/session-start-rewrite.md) | chore | backlog | — | area:docs | Slim down the session-start command — only if it gets bloated. | [brief](docs/agent-process-brief.md) |
| [Modular-shape example output tree](tickets/modular-example-output-tree.md) | feature | backlog | — | area:scaffold | A worked example of the modular scaffold shape — build when modular work picks up. | [council](docs/council/council-report-2026-06-08.html) |
| [Agent-teams scaffold guidance](tickets/agent-teams-scaffold-guidance.md) | feature | backlog | — | area:scaffold | Guidance for multi-agent project structure — add when a scaffolded project needs it. | — |
| [README install loop symlinks `context-engineering-audit`](tickets/readme-install-symlink-cea.md) | fix | backlog | — | area:docs | The README's install steps wrongly symlink an audit doc — fix when it confuses a fresh clone. | [D-019](docs/DECISIONS.md#d-019) |
| AGENTS.md-canonical flip (this-repo half) | chore | backlog | — | area:docs | Make AGENTS.md the canonical file (not CLAUDE.md) in this repo — generator half already done. | [D-047](docs/DECISIONS.md#d-047) |
| `solutions/` scar-tissue library + CF-05 | decision | watching | — | area:docs | Decided NOT to build a "past mistakes" library — revisit only as a scaffold-emit for high-error project types, or if a 2nd scan finds a hidden pattern. | [D-063](docs/DECISIONS.md#d-063) |
| [Skill injection by project type](tickets/skill-injection-by-project-type.md) | feature | blocked | — | gate:needs-decision, area:skill | Auto-add the right skills based on project type — blocked on deciding plugin vs vendored delivery. | — |
| DSB HTML supplement | feature | icebox | — | area:dsb | An optional HTML supplement for the design-system skill — shelved indefinitely. | [D-012](docs/DECISIONS.md#d-012) |
| Candidate future products (3 briefs) | research | icebox | — | area:docs | Three possible future product ideas — revisit after Taste Builder is validated. | [briefs](docs/product-briefs/) |

## Done

See [`docs/retros/`](docs/retros/) for the session-by-session record, and [`tickets/archive/`](tickets/archive/) for archived cards. Skill-build Phases 1–4 (2026-05-10) and continuous-mode sessions (2026-05-10 → 2026-05-11) are recorded there.

## Format

`BACKLOG.md` is a **thin always-loaded kanban board** ([D-048](docs/DECISIONS.md#d-048) / [D-054](docs/DECISIONS.md#d-054)). The board is the only work-tracking surface — no separate roadmap file; the roadmap is the board sorted by `Seq`.

**Columns:**

- **Item** — the unit of work (links its `tickets/<slug>.md` card when one exists).
- **Type** — one word: `feature` · `chore` · `decision` · `research` · `fix` · `spike`.
- **Lane** — the kanban column (see below).
- **Seq** — order within the actionable lanes (`active`/`next`); the next item to pick up is the lowest `Seq`. `—` elsewhere. There is no per-item "next action" column — `Seq` answers *which item is next*, the linked card answers *how*.
- **Tags** — **max 2**, two axes only: `gate:` (what must happen before it moves) and `area:` (which part of the system). Allowed values live in the `<!-- TAGS -->` comment above the board; the render validates against them.
- **Gloss** — one plain-English line saying what the item *is* (and, for parked items, the trigger that un-parks it). The deliberate readability exception to one-line-terseness ([D-069](docs/DECISIONS.md) — optimize for Rex's clarity); a label, **not** inline reasoning (that stays in the card/brief/`D-NNN`).
- **Refs** — pointers to the card, brief, or `D-NNN`/retro that hold the *why* and the operational detail.

**Lanes** (the `Lane` column — the kanban columns):

- `active` — being worked **this session**.
- `next` — queued and ready to pick up; `Seq` orders it.
- `watching` — parked on a **named trigger** (in the gloss); fires when the trigger trips, not on a schedule.
- `backlog` — real work, not yet queued.
- `blocked` — can't proceed until a dependency clears (the gloss names it).
- `icebox` — someday/maybe; deliberately not soon.

**Rules:**

- **One line per row.** The context to *act* lives in the linked `tickets/<slug>.md`, brief, or `D-NNN`/retro — never inline. The `Gloss` is a one-line plain-English label, not an exception to this. A fat row is a rule violation, not a deferral.
- **A row earns a ticket card only when it has working context to act on.** Icebox/thin rows stay a single line + pointer to an existing detail store (a brief, council, tracker, or `D-NNN`). Don't spawn empty cards.
- **`Seq` orders the actionable lanes** (`active`/`next`) — a suggested order Rex curates; `—` for `watching`/`backlog`/`blocked`/`icebox`.
- **Tags stay within the `<!-- TAGS -->` vocabulary, max 2 per row.** A new value earns its place in the comment block first; the render flags anything off-list.
- **Retire, don't re-accrete.** A resolved row's card is `git mv`'d to [`tickets/archive/`](tickets/archive/) (archive, don't delete) via the `/end-session` retirement ritual; the row leaves the board. Done rows do not return.
- **New idea → a new row**, lane `icebox` or `backlog`. It earns a card when you start it.

## Cross-references

- Project rules: [`CLAUDE.md`](CLAUDE.md).
- Active decisions: [`docs/DECISIONS_ACTIVE.md`](docs/DECISIONS_ACTIVE.md).
- Decisions log: [`docs/DECISIONS.md`](docs/DECISIONS.md).
- Ticket convention: [`tickets/README.md`](tickets/README.md).
- Lifecycle pattern: [`docs/briefs/living-document-lifecycle-brief.md`](docs/briefs/living-document-lifecycle-brief.md).
- Session retros: [`docs/retros/`](docs/retros/).
