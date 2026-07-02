# Building out the system — design-research engagements as Claude Code projects

A brief on what we're building, why, and in what order. This is the orienting document; the detail lives in the other files it points to, kept thin on purpose.

---

## What the system is

A repeatable way to run client engagements that are design, research, synthesis, and prototyping work, not software, as Claude Code projects. Each engagement gets a disciplined CLAUDE.md, a sane document structure, named routines, and context-thrift conventions, so the work compounds across sessions instead of restarting from memory every time. Theragen Sync 3.0 is the first instance. The reusable version gets harvested out of it later, not designed up front.

## The one idea everything hangs on

Build bespoke, then harvest. You can't abstract a reusable harness from zero runs, so the move is to run a real engagement, capture what works and doesn't, and let that evidence define the reusable pattern. This is the same sequence prd-to-product already uses, earn a guardrail from a logged failure rather than designing it from imagination. It also keeps you from the trap that's shown up repeatedly in this thread, building the meta-system is more fun and has no deadline, while the engagement is real and starts July 1. The engagement is the forcing function. The system is the byproduct.

## The shape of a project

Three kinds of artifact, each with a different discipline, because collapsing them is the main design error:

- Research (calls, sessions, synthesis) wants rigor. Cite the session, separate evidence from interpretation, capture is one-shot.
- Stimulus (storyboards, throwaway prototypes used as test props) wants speed. Build fast, multiple variations, disposable.
- Handoff (the high-fidelity dev-ready spec) wants precision. Versioned, careful, the thing the client pays for.

Folder map, CLAUDE.md, and the engagement-specific rules are in `theragen-sync3-starter.md`. Ground-truth content is in `context/` (engagement-brief, people, constraints). Work tracking stays a thin BACKLOG index, with the fuller `tickets/` plus retirement convention inherited from prd-to-product when it ports over, not hand-built in parallel.

## Routines, and where they live

Most routines are invoked by hand, so they're manual-only (`disable-model-invocation: true`), which means they cost nothing in context until you type them. You can have a lot of them.

- Engagement routines (project-local `.claude/skills/`): `/ingest-call`, `/ingest-session`, `/synthesize`, `/prototype-brief`. Drafted, in `commands/`.
- Personal routines (user-level `~/.claude/skills/`, so they ride along to every project): `/capture`, `/next`, `/smallest-step`, `/focus`, `/welcome-back`. These attack the actual bottleneck, starting, and aren't Theragen-specific.

Commands and skills are now the same mechanism in Claude Code; author new ones as skills for the extra features, leave existing command files alone.

## Design principles that shape it

Tuned for procrastination and the symptoms you described, because a system that fights your brain goes stale by week three.

- Kill the blank page. Every routine drafts first and lets you react. Editing is cheaper to start than creating.
- One next action, not a board. The default surface is a single line, not twelve cards.
- Push, not pull. Briefings and the postcard come to you; things off-screen stop existing.
- Make time visible. Elapsed and remaining, on dependencies and deadlines.
- Re-entry over guilt. The dead man's switch is a gentle "welcome back, here's the one thing," not a scold. Shame becomes another reason to avoid the repo.

## Build sequence

Phase 0, now, before the engagement starts:
- Stand up `theragen-sync3/` from the starter, drop in the `context/` files and the thin BACKLOG.
- Put the four engagement routines in the project's `.claude/skills/`, manual-invoke.
- Put the five personal routines at user level. Build these first, `/capture` and `/next` especially, they're the daily wins and prove the habit fastest.
- Confirm with Theragen how recorded session data should be handled. Precedent exists (AI was used last round), so this is a one-line check, not a blocker. De-identify upstream of the tool regardless, the AI only ever sees notes you've already stripped.
- Do not build the dashboard, the postcard, or the skill-gaps mechanism yet.

Phase 1, early engagement (Align):
- Use it. Ingest calls, seed `research/prior/` from the Nov/Dec research, keep BACKLOG thin.
- Keep an informal running note of where the harness and routines fit and don't. That's the raw material for the harvest, even before the formal mechanism exists.

Phase 2, as needs prove themselves (Develop, Validate):
- Add `/standup`, the generated dashboard, and `/postcard` only when you feel the friction each removes. The dashboard is generated from current files every time, never maintained, so it can't go stale.

Phase 3, harvest (after Theragen, or after one more):
- Feed the captured gaps into context-engineering improvements, scope-gated through Claude Code.
- Decide, from evidence, whether context-engineering needs a dedicated research-and-design mode. That mode is the reusable harness.

## Dependencies and sequencing

- The skill-gaps self-instrumenting step ships after the in-flight context-lifecycle ticket lands and conforms to its pattern (event-log findings, thin open-gaps index, harvest folded into `/end-session`). Details in `harness-skill-gaps-brief.md`. Do not build it ahead of the parent ticket.
- Theragen inherits the `tickets/` plus retirement convention when the context-engineering port brings it over. Until then, thin BACKLOG and archive done items.
- Using context-engineering to scaffold Theragen gives you the disciplined shell, not the bespoke content. Hand-fill the content (already drafted), and log every place the code-built harness misfits a research project. That gap list is the spec for the harness.

## What not to build yet

- No reusable harness designed up front. Harvest it from Theragen.
- No heavy self-improvement engine, no aggregation or triage loop, no eval tooling. The thin convention now, the proven mechanism later.
- No dashboard before `/capture` and `/next`. Prove the habit before the cockpit.
- No parallel ticket system in Theragen. Inherit the proven one.

If a build step starts growing past "one thin thing," that's the signal it's drifting into the yak. Stop and check it against this brief.

## Governance

- Cowork advises; Claude Code implements under your scope gate. Changes to the harness, the skills, or prd-to-product go through that gate, and self-modification of agent config is gated on you regardless.
- Reversible prose changes don't need a council. The costly, hard-to-reverse forks (the context-engineering port, a heavier harvest loop) are where a council is worth recommending first.
- Patient data stays de-identified and out of the tool until stripped. Medical client, real people, your own notes shouldn't become a liability.

## First three moves

1. Stand up `theragen-sync3/` from the starter and the `context/` set.
2. Build `/capture` and `/next` at user level and actually use them this week.
3. Send Theragen the one-line session-data-handling question so it's settled before Align.

Everything else waits until the work asks for it.
