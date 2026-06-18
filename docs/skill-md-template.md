# SKILL.md structure template

Extracted from [paraschopra/make-pages-interactive](https://github.com/paraschopra/make-pages-interactive)'s SKILL.md as a reference for evaluating our own skills (`context-engineering`, `prd-creator`, `design-system-bootstrap`, `context-engineering-audit`).

Not a binding spec. A pattern to compare against. Where our SKILL.md files diverge, the divergence should be deliberate, not accidental.

---

## The shape

```markdown
---
name: <kebab-case-skill-name>
description: <one paragraph: what it does, when to trigger, trigger phrases inline>
---

# <Human-readable name>

<One-paragraph orientation: what this skill does, what kind of input it expects,
what kind of output it produces. Name the failure mode it prevents if there is one.>

## When to invoke

User says any of:
- "<exact trigger phrase>" → **<Flow name>**
- "<exact trigger phrase>" → **<Flow name>**
- "<exact trigger phrase>" → **<Flow name>**

<Optional: "Do not activate on" list — phrases that look similar but mean
something else. Cite what the user probably wants instead.>

## <Flow 1 name> flow

1. **<Imperative step, bolded lead-in.>** <Detail.>
   ```
   <exact command, including flags>
   ```
2. **<Next step.>** <Detail, including what to check and how to branch.>
   - <Branch condition> → <action>
   - <Branch condition> → <action>
3. **<Next step.>** <…>

## <Flow 2 name> flow

<Same shape. One section per distinct flow the trigger list referenced.>

## On <reentry / edge case>

<If the skill can be invoked in a state where prior work exists, describe the
state check and what to do. Example from make-pages-interactive: "On startup in
a directory that already has feedback".>

## Files in this skill

\`\`\`
~/.claude/skills/<skill-name>/
├── SKILL.md
├── README.md
├── <other top-level files>
└── <subdirs>/
    └── <…>
\`\`\`

## Gotchas

- <Failure mode 1 + the specific reason it bites.>
- <Failure mode 2 + the specific reason it bites.>
- <Failure mode 3 + the specific reason it bites.>
```

---

## Patterns worth copying

**1. Trigger phrases mapped to flows, not just listed.**
`make-pages-interactive` lists each trigger phrase with `→ **Flow name**` next to it. Means the agent doesn't have to infer which procedure applies — the routing is explicit in the trigger table. Our `context-engineering/SKILL.md` lists triggers and a single "When triggered" procedure; that's fine when there's one flow, but if any of our skills grow a second flow (e.g. an "update" or "audit" path on top of a "scaffold" path), copy this routing pattern.

**2. Numbered steps with the exact command in a fenced block.**
No prose-only instructions. Every imperative step in `make-pages-interactive` has either an exact bash invocation or an exact decision rule. Reduces the chance the agent improvises a flag. Our `context-engineering` procedure has this for the generator flow; check `prd-creator` and `design-system-bootstrap` for prose-only steps and convert them.

**3. Branch conditions written as bullet lookups, not nested if-trees.**
Step 3 of the setup flow handles "port in use" with three explicit bullets — "matches → reuse", "different → ask or increment", "no response → free". The agent doesn't have to interpret nested logic. If our skills have multi-branch decision points (intake answers driving template selection in `context-engineering`), prefer this style over paragraphs.

**4. "Do not activate on" list right next to the activation list.**
Our `context-engineering/SKILL.md` already has this (`"scaffold a Next.js app"`, `"create a CLAUDE.md"`, `"set up a project"`). Worth verifying every skill has at least 2-3 near-miss phrases listed. Stops false-positive activations.

**5. Self-cleaning long-running processes.**
`lib/server.py` records its parent PID, polls every 5s, exits when reparented to PID 1. Plus a 10-min idle timeout. If any of our skills ever spawns a daemon (a watcher, a dev server, a monitor), copy this pattern — abandoned background processes are the kind of thing that's invisible until a user has 12 of them running.

**6. Idempotent + reversible scripts.**
`scripts/inject.py <dir>` and `scripts/inject.py <dir> --remove`. Same script handles forward and reverse. Re-running forward is safe. Pattern applies any time `context-engineering` scaffolds files into an existing project — every emitter should be idempotent, and ideally reversible. Matches our "generator scaffolds shape, not content" invariant in CLAUDE.md.

**7. "Gotchas" section bottom-anchored.**
Three load-bearing failure modes, each one sentence, each citing the specific cause. Matches our principles-must-cite-failure-modes invariant. Every SKILL.md should have this section if there are non-obvious ways to misuse the skill.

**8. Invocation mode by the two-load cut.**
Whether a skill sets `disable-model-invocation: true` is governed by the two-load model — context-load (model-invoked descriptions sit in the window every turn) vs cognitive-load (user-invoked skills are indexed only by the human's memory). Narrow/heavyweight explicit-invoke tools (`furnace-plan`, `frontend-er`) go user-invoked to protect the window; broadly-useful auto-firing skills (the `context-engineering`/`prd-creator`/`design-system-bootstrap` chain) stay model-invoked. The binding rule lives in [`DECISIONS.md`](DECISIONS.md) D-034 — this is the example, not the spec.

---

## How our existing skills compare

Quick audit prompts — not a verdict, just questions to ask when next touching each file:

- `skills/context-engineering/SKILL.md` — has trigger list, has "do not activate", has numbered procedure. Missing: explicit "Gotchas" section, flow-routing on triggers (only one flow today). If we add an audit or update flow, route triggers explicitly.
- `skills/prd-creator/SKILL.md` — re-read against this template. Are trigger phrases mapped to flows? Are steps numbered with exact commands? Is there a "Gotchas" section?
- `skills/design-system-bootstrap/SKILL.md` — same audit. Plus: confirm it doesn't write product code (per CLAUDE.md architecture rule).
- `skills/context-engineering-audit/SKILL.md` — same audit.

If any divergence from the patterns above is deliberate, that's fine — but it should be deliberate.
