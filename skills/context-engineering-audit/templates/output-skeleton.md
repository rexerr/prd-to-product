# Output skeleton — context-engineering audit report

The shape every audit report should fill. Read this when you are about to write the report — not at invocation. Copy the skeleton into the audited project's `docs/context-audit-YYYY-MM-DD.md` and fill the placeholders.

The six sections are mandatory. The seventh (Comparison to prior audit) is conditional — include only if the project already has a `docs/context-audit-*.md` from an earlier date.

Headings below should be used verbatim. Sub-buckets and table columns should not be reshaped.

---

## Skeleton — copy from here down

```markdown
# Context audit — YYYY-MM-DD

Comparison of `<project>`'s AI-context structure against the standard scaffolded by `/Users/rexc/Sites/prd-to-product/skills/context-engineering/`. This project was <hand-built | scaffolded by the skill | mixed>; the audit catalogs the divergences and does not prescribe fixes. Decisions on what to act on are deferred to follow-up sessions.

Source-of-truth precedence applied throughout: when a project file says something the skill doesn't, the project wins for this project. Drift is flagged for visibility, not for overwrite.

<If a prior audit exists, add a line naming it and stating that §7 below carries the comparison.>

---

## 1. Inferred intake answers

What the skill's intake flow would have asked, and the best inference from reading the project.

| Key | Inferred value | Source of inference |
|---|---|---|
| `project_name` | <value> | <where it came from> |
| `stack` | `<nextjs \| react-vite \| node-cli \| python \| other>` | <evidence> |
| `deploy_target` | `<vercel \| netlify \| cloudflare \| fly \| railway \| manual \| none>` | <evidence> |
| `deploy_target_has_cli_conflict` | **<true \| false>** | <reasoning> |
| `stack_has_client_server_split` | **<true \| false>** | <evidence> |
| `stack_has_ui` | **<true \| false>** | <evidence> |
| `uses_visual_confirmation_gate` | **<true \| false>** | <evidence> |
| `visual_confirmer_name` | <name or null> | <evidence> |
| `ai_surface_count` | **<integer>** | <evidence: rule files, API routes> |
| `voice_and_tone` | **<true \| false>** | <evidence> |
| `design_shape` | **`<basic_styling \| tokens_with_linter \| none>`** | <evidence> |
| `apply_design_heuristics` | **<true \| false>** | <evidence> |
| `include_product_rules` | **<true \| false>** | <evidence> |
| `include_parking_lot` | **<true \| false>** | <evidence> |
| `include_decisions_active` | **<true \| false>** | <evidence> |
| `include_future` | **<true \| false>** | <evidence> |
| `codex_usage` | **`<regular \| occasional \| none>`** | <evidence> |
| `enforce_rules_as_hooks` | **<true \| false \| unknown>** | <evidence; flag if unknown> |
| `external_skill_references` | <list or none> | <evidence> |

**Modular vs flat shape.** State which the project uses and which the decision logic in `decisions.md` would have produced for these intake values. If they match, say so. If they don't, that's drift to call out in §3.

**Open questions worth confirming with the user:** numbered list of any intake value where the inference was ambiguous.

---

## 2. Missing files

What the skill would emit that doesn't exist in this project. Each is named with its load-bearing or cosmetic classification.

### Load-bearing

**`<missing file 1>`** — <what it is in the canonical scaffold>. **Failure mode the file prevents:** <cite the principle from `principles.md` or `decisions.md` with line numbers>. **Evidence the failure mode applies here:** <quote or summarize the project's own prose that cites this failure mode, or note its absence>.

**`<missing file 2>`** — <same shape>.

### Cosmetic / structural

**`<missing file>`** — <what it is>. <One sentence: cosmetic now because <reason>; would become load-bearing if <condition>>.

### Not missing — correctly omitted or in a different place

**`<file or pattern>`** — <intake value that gates it; confirmation that the project's choice matches>.

---

## 3. Present but drifted

Files that exist but diverge from what the skill would emit.

### <Drift item 1 — short descriptive title>

**What the skill specifies** (cite `principles.md:LL` or `decisions.md:LL`): <the standard, paraphrased>.

**What the project has:** <what's actually there, quoted or summarized>.

**Judgment: <intentional | accidental | borderline>.** <One paragraph: what makes you think this is intentional/accidental? Cite evidence from the project's prose, ROADMAP, retros, or other files. Apply the project-autonomy clause: if the project's choice contradicts the skill, the project wins for that project — flag the divergence, don't recommend overwriting.>

### <Drift item 2>

<Same structure.>

### Other forms of drift

<Small drifts that don't merit a full subsection — bullet list with one-paragraph notes each.>

- **<short title>** — <one-paragraph note>.

---

## 4. Present and correct

Files and structures that match what the skill would emit. No attention needed.

- **`<file or pattern>`** — <one-line note on what it is and why it's correct>.
- **`<file or pattern>`** — <note>.

---

## 5. Open questions for the post-audit discussion

Items the audit surfaced that need a decision the audit can't make on its own.

1. **<short title>** — <the question, what answer would unblock action, which audit sections it ties back to>.
2. **<short title>** — <…>.

---

## 6. Notes on what was *not* checked

What this audit deliberately did not assess.

- The actual *content quality* of rules, PRD, ARCHITECTURE — this audit checks structural conformance only.
- Whether the rules will hold up under pressure. The skill cites the AGENTS.md study finding that prose rules degrade compliance versus harness-enforced hooks; that risk applies to anything flagged in §5.
- <Project-specific exclusions, e.g., "tests because none exist yet," "deployment pipeline because the project is pre-deploy.">
- <Anything else the auditor consciously skipped.>

---

## 7. Comparison to prior audit — watch items

<Include this section only if a prior `docs/context-audit-*.md` exists. Otherwise delete the heading.>

The watch items from `<prior-audit-filename>`:

1. **<watch item 1 from prior audit>** — <how this audit's evidence updates the item: confirms, rules out, or surfaces a new shape>.
2. **<watch item 2>** — <…>.
3. **<watch item 3>** — <…>.

<Optionally close with: any new failure-mode classes this audit surfaced that the prior didn't, or any positive divergences worth naming.>
```

---

## How to fill the skeleton

Three rules for filling:

1. **Every drift in §3 carries a judgment.** "Drifted but no judgment" is not an acceptable entry — if you cannot say whether the drift is intentional, accidental, or borderline, write "borderline" and explain what evidence would resolve it.
2. **Every load-bearing miss in §2 cites both the failure mode and the project-side evidence.** A miss without project evidence is speculation; a miss without failure-mode citation is unmoored from the standard.
3. **§5 names questions, not recommendations.** "Should we add hooks?" is a question. "Add hooks before Phase 1" is a recommendation and belongs in a follow-up session, not the audit.

If the audit produces zero entries in §3 or §5, double-check — both reference audits produced multiple entries in each, and a project with zero drift is rare enough to warrant re-reading the project files before declaring it.
