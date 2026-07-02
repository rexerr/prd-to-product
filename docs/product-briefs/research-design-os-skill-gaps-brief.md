# Harness change brief — skill-gap tracking as a child of the living-document lifecycle

Paste into Claude Code (plan mode). This is a scoped proposal, and it is explicitly **queued behind** the in-flight context-lifecycle ticket. Do not implement until that lands. Plan it, show me scope, then implement under the normal workflow once the parent pattern exists.

---

## Context, what we're doing and why

I run client engagements that are design, research, synthesis, and prototyping work, not software products. I want to run these as Claude Code projects using this repo's context-engineering harness, the same way I run code projects, so each engagement gets a disciplined CLAUDE.md, sane document structure, and context-thrift conventions instead of an ad hoc pile of notes.

This is a new project archetype for the harness. Context-engineering was built to scaffold code projects, so a lot of what it emits assumes code. A research-and-design engagement has different shapes, a research corpus, disposable test stimulus, a durable client handoff, calls and sessions. The first real instance is a client product-design and validation engagement starting soon, and I'm going to scaffold it with context-engineering and watch where the harness fits and where it doesn't.

The plan is build-bespoke-then-harvest. Run the harness on a real engagement, capture every place it helped or got in the way, and only later use that evidence to decide whether context-engineering needs a research-and-design mode. To make that possible, every project of this type needs to capture what worked and didn't about the skills, as a byproduct of the work.

## Why this brief changed

An earlier version of this proposed an append-only `SKILL-GAPS.md`, a single file that only grows. That is the exact anti-pattern the context-lifecycle ticket is curing, a living registry with no retirement step that bloats the always-loaded set. So this is now framed as a **child instance of the living-document-lifecycle pattern** that ticket establishes, not a standalone mechanism. It must not ship before that parent pattern exists, and it must conform to it.

One framing point so we don't overbuild. This is self-instrumenting, not self-improving. The loop does not close automatically. The harness reliably produces the evidence; I close the loop later by driving a scoped change through Claude Code. No autonomous self-modification of the skill.

## The change, conformed to the lifecycle pattern

A skill gap is an **event** — it happened at a moment and is immutable. Per the lifecycle doctrine, events are solved by dated per-file folders (the retro/audit shape), not by a growing registry. The set of **open, not-yet-harvested** gaps is the only registry-shaped part, and it stays a thin index that shrinks as gaps are acted on.

So, three pieces, all reusing mechanisms the parent ticket will already have built:

1. **Gap findings as an event log.** Each gap is a dated entry in the established event-log mechanism. Decide at build time whether that is a dated per-file folder (e.g. `docs/skill-gaps/YYYY-MM-DD-<slug>.md`) or a tagged entry in the existing retro stream, since a skill gap is essentially a retro observation about the tooling rather than the session. Pick whichever the lifecycle ticket makes cheapest; do not invent a third mechanism.
2. **A thin index of open gaps** that points to the findings and shrinks as they're harvested, following the same thin-index discipline as the new BACKLOG and DECISIONS_ACTIVE.
3. **Harvest folded into the retirement ritual.** The `/end-session` retirement step gains one line, a harvested gap (acted on via a scoped skill change) is demoted out of the open index. No separate harvest loop, no bespoke ritual. It rides the one being built.

## Scope of this task

- Extend what context-engineering emits so a newly scaffolded project includes the skill-gap event-log location, the thin open-gaps index, and the CLAUDE.md rule below.
- Reuse the parent ticket's mechanisms (event-log folder convention, thin-index discipline, the `/end-session` retirement ritual). This task adds a new *application* of the pattern, it does not add new machinery.
- This fits the generator's remit, it writes context files, shape not content.
- Record a short `docs/DECISIONS.md` entry, since this changes what the generator always emits; mirror a one-liner to `DECISIONS_ACTIVE.md` if binding.
- Keep the emitted CLAUDE.md rule terse, every future project pays for it in context.
- Verify against the example output trees the way generator changes are normally verified.

## Explicitly out of scope, do not build these yet

- No append-only single-file ledger (the retired anti-pattern).
- No `/log-gap` routine, no cold-read review ritual, no aggregation or triage engine, no eval/benchmark wiring.
- No change to the markdown-only invariant or any architecture rule.
- Do not start before the context-lifecycle ticket lands. If asked to, stop and flag the dependency.

If the plan grows past "one more application of the existing pattern," that's the signal it's drifting. Stop and flag it.

## Content to emit, CLAUDE.md rule

```markdown
## Track skill gaps (self-instrumenting)

When a scaffolding or workflow skill produces something you must correct, replace,
or work around, record it as a dated gap finding (the event-log mechanism) and add
a line to the open-gaps index, in the moment — a workaround you didn't log is a
finding thrown away. Log wins too. The retirement ritual demotes a gap once it's
been acted on through a scoped skill change. These notes are evidence for improving
the harness later, not an automatic loop.
```

The gap finding itself should carry: date/phase, the skill and what it was asked to do, what it produced, a verdict (kept / partial / wrong / missing / over-generated), and what I did instead plus the implication for the harness. Treat that schema as a starting point the first real engagement will revise, which is why it isn't hardwired deeper than the rule.

## Notes for your plan

- This is a product change to the harness, run through the normal scope-gated workflow; self-modification of the harness is gated on me regardless, so show me the plan first.
- It is reversible (one emitted rule plus a folder convention that reuses existing machinery), so it does not need a council. The heavier harvest/triage engine, if ever proposed, is the costly fork where a council is worth recommending.
- Dependency, hard: this is a child of the context-lifecycle ticket. It conforms to that pattern and ships after it, never before.
- Connect it to the existing pattern in your reasoning, this gap log is to skills what retros are to sessions, and it's one more instance of the living-document-lifecycle shape, alongside context-lifecycle, docs-structure, and repo-miner-output.
