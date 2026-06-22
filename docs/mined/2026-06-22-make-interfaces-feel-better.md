# Mine — make-interfaces-feel-better — 2026-06-22

- **Source:** https://github.com/jakubkrehel/make-interfaces-feel-better
- **Pinned:** `384562064fcdd99778fcbafd8729626fe6aab02f`
- **License:** MIT per README; **no `LICENSE` file in repo** (GitHub classifier reports none — declared-not-filed)
- **Lens:** skill-development workspace — skill *craft* (how this skill is written), not its UI-tip *content* (design/visual mining is out of `/mine`'s scope)

> **Status: RESOLVED 2026-06-22.** One finding adopted; the rest declined as already-covered or conflicting. See Outcome.

## Outcome (post-analysis)

Mined through three lenses, then cross-checked against the two skills that would consume the content (`design-system-bootstrap`, and `frontend-er` at `~/Sites/frontend-er`):

- **`frontend-er` already covers ~9 of the source's 11 UI details** — often verbatim (optical alignment names play-triangles too) and better-reasoned (easing-by-role, `prefers-reduced-motion`, perf floor in `references/motion.md` + SKILL §6/§8). The source is a subset.
- **DSB already ships** font-smoothing, reduced-motion, and motion tokens in `globals.css` / `tokens.css`.
- **Conflict, not graft:** the source's pure-black 3-layer "shadow-as-border" recipe contradicts `frontend-er` §6 ("tint shadows toward the background; pure-black looks pasted on" + no-ghost-card). Declined.
- **Adopted (1):** `text-wrap: balance` on headings / `pretty` on body — a genuine gap in DSB's `globals.css` (frontend-er enforces it at build time, but DSB-scaffolded projects never see that). Landed in `skills/design-system-bootstrap/templates/globals.css.template` + the `output-small` example. No `D-NNN` (small additive default, not an invariant change).
- **Declined / deferred:** shadow-as-border token (conflict, above); image outlines (niche + mild tension with the anti-"pasted-on" instinct); the concentric border-radius *formula* is the one real gap left — a `frontend-er` §6 follow-up (separate repo), not DSB.
- **`MIFB-01`** (review-coverage checklist) — left Proposed, Rule-of-Two not met.

Net: a mature workspace got one two-line graft from a popular-but-introductory source — the dedup discipline working as designed.

## Headline

Near-zero net-new adoptable. This is the **most-overlapping possible source**: a UI-craft *skill*, mined into a repo that already mined one ([`docs/animation-taste-reference.md`](../animation-taste-reference.md), from Emil Kowalski's animations.dev skill). Both the craft patterns and the design-engineering content were already captured there. The honest yield is **1 borderline craft crib + 1 Rule-of-Two pointer**; everything else *confirms an existing call and adds nothing* — cited below, not re-minted.

## Findings

### Lens-A crib (our tooling)

| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
|---|---|---|---|---|---|
| MIFB-01 | **Review skill closes with a literal coverage checklist** — a review-shaped skill ends with a checkbox list mirroring its own principles, so the agent self-audits that it considered every one before reporting. (Source: `SKILL.md` lines 126–141, "Review Checklist".) | A review skill silently skips a principle it knows about — coverage looks complete because no omission is visible. | investigate | `docs/skill-md-template.md`; any review-shaped skill | **Proposed — borderline, Rule-of-Two NOT met.** Adjacent to the already-held "Gotchas bottom-anchored" + structured-output-contract patterns; adopt only if a 2nd independent instance appears OR a live review skill actually drops a principle. |

### Lens-B pointer (host-project — NOT adoptable content)

| Item | Lane | Seq | Next | Refs |
|---|---|---|---|---|
| DSB motion-defaults layer | watching | — | **2nd instance now seen** — this source's animation content (enter/stagger/exit, icon-anim values, easing) is a second candidate body of design-engineering content after `animation-taste-reference.md` Part 2. Rule-of-Two threshold for *deciding whether to build a DSB motion-defaults layer* may be met. Route to a human decision — `/mine` cannot adopt this (design/visual content, out of scope). | [animation-taste-reference](../animation-taste-reference.md) |

### Confirms-existing — cited, deliberately NOT re-minted

- **Anti-example output contract** (`SKILL.md` 100–124, "Review Output Format" — Before/After table, "omit empty tables, they add noise"). *Weaker* instance of `animation-taste-reference.md` Part 1 #1, which also shows the explicit "Wrong format (never do this)" block this source lacks. No new crib.
- **Trigger-saturated description** (`SKILL.md` frontmatter packs ~15 trigger phrases + auto-fire). A fresh real-world *instance* of the trigger-saturation anti-pattern already documented (`animation-taste-reference.md` Part 1 #2, "observed not theorized"). Evidence for the existing call, not a new one.
- **Exact value + failure rationale** ("always `scale(0.96)`, never below `0.95` — anything below feels exaggerated"; identical pattern on icon-anim values, image-outline colors). This *is* the project's own invariant "every rule cites its failure mode" (CLAUDE.md). External convergent validation — same role as the animation-taste-reference note on Kowalski's "taste has logical reasons." Not a crib.
- **Runtime dependency-branch instruction** ("check `package.json` for `motion`/`framer-motion`; if present use Motion, else CSS cross-fade — don't add a dep"). Adjacent to the harness-probe install pattern (`animation-taste-reference.md` Part 1 #5) and to context-engineering's stack detection. Generic, already in the project's vocabulary. Not a crib.

## Verification ledger

Every keeper tiered by ground truth (engine step 5):

- **MIFB-01** — *structural claim* about the source's own text → verified by reading `SKILL.md` 126–141. The claim is "this skill does X," which is checkable; whether the pattern *helps our skills* is the open question that keeps it at `investigate`.
- **All UI/taste content** (concentric radius, `text-wrap: balance` ≤6 lines, `scale(0.96)`, antialiasing, etc.) — **soft claims** about browser behavior and visual taste. The source *is* the claim; there is no project ground truth to check them against. They could only ever enter as time-boxed experiments with kill conditions — and they're out of `/mine`'s scope anyway. None promoted to "verified fix."

## Provenance / safety

- Web source treated as untrusted; quoted, not followed. No embedded instructions acted on.
- Shallow clone cached at gitignored `docs/mined/repos/make-interfaces-feel-better/` (regenerable; not committed). Guard verified before clone.
- License caveat above (MIT declared, no file) matters if any snippet were ever lifted verbatim — but nothing here proposes lifting content, only observing craft.
