# LLM Council Transcript — prd-to-product Harness Proposals
**Date:** 2026-06-09

## Framed question
Rex runs `prd-to-product`, a single-developer, markdown-only Claude Code skill-development workspace (chiefly the `context-engineering` skill that scaffolds AI-coding project context files but never product code), governed by a strict CLAUDE.md (hard scope limits, direct-on-main, "every rule cites its failure mode," a markdown-only invariant, and D-009: recommend a council only at genuine costly+irreversible forks, don't over-apply it). Claude reviewed five first-party Anthropic Claude Code blog posts plus secondary/influencer content and produced 8 proposals:
- **A** — Cowork/non-Claude-Code agents stay read-only on the repo without explicit permission
- **B** — name the laziness/bias/drift failure taxonomy in principles.md
- **C** — verifier-subagent-per-rule + skeptic pass for generated rule files
- **D** — /freeze + /careful session-scoped hooks
- **E** — slim CLAUDE.md via progressive disclosure
- **F** — subagent "need output or conclusion?" heuristic + verification-subagent prompts
- **G** — explicit /compact-vs-/clear guidance
- **H** — keep CLAUDE.md static for prompt-cache stability

Which proposals earn their place vs add ceremony, what's missing, and is the synthesis sound for a single-dev markdown repo or over-engineering imported from a large-team API-product context?

---

## Anonymization mapping (used for the peer-review round)
```
A → The Veteran
B → The Stranger
C → The Long View
D → The Skeptic
E → The Architect
```

---

## Advisor responses (de-anonymized)

### The Skeptic
Most of this synthesis is sound, but the framing buries the real risk: the synthesis itself becoming the project. Eight proposals from one blog-reading session, against a CLAUDE.md that already runs to thousands of words with a D-009 anti-ceremony rule, is the exact failure D-009 exists to prevent. You are about to council-and-decision-log your way into the very over-engineering you're asking about. The cheap-adopt tags are doing suspicious work. H is the only one with a hard mechanical payoff, and even that assumes Claude Code caches your CLAUDE.md per-project in a way you've verified — the blog describes Anthropic's own infra, not your local harness. Verify the cache actually breaks on edit before writing a rule to prevent it. If you can't measure it, it's cargo cult. B and F add named vocabulary; vocabulary that doesn't change behavior is decoration — if you can't name the failure mode, B and F don't qualify by your own bar. C is a trap: per-rule verifier + skeptic pass, token-heavy, for a single-dev markdown repo with hand-written example-tree regression. Cut it. The thing missed: who maintains this? Every rule added is a rule the next session must read, honor, and not contradict. Adopt H, maybe G and A. Reject the rest until a real failure earns them.

### The Architect
B, F, H earn their place because they cost a line and prevent a real failure. A is a genuine safety gap — Cowork writing your repo unsupervised is exactly the irreversible-outward-facing class your own rules gate. Adopt those four. Now the reframe: you are optimizing the wrong variable. The question isn't "which of 8 blog-derived improvements do I adopt" — it's "what is the actual failure rate of my current harness, and which proposal moves it?" You have zero instrumentation on that. C and D are the tell: per-rule verifier subagents and a skeptic pass are the canonical large-team, high-traffic answer — defense-in-depth against thousands of untrusted invocations. You have one invocation, yourself, who can read the diff. Sledgehammer for a thumbtack. D's /freeze and /careful guard against a driver you trust; your scope limits and direct-on-main already cover that. Simplest first move that proves the right variable: before adopting C/D/E, log the next ten sessions' actual failures — bad substitution, scope creep, lost context — one retro line each. If goal-drift and unverified rules don't appear, C and D answer a question your repo never asked. E is the one deliberate item worth a real cut, but drive it from that log too. Adopt A/B/F/H now; instrument; let the log earn C/D/E or kill them.

### The Stranger
Most of the load-bearing words here would stop a normal person cold: "harness," "subagent," "progressive disclosure," "prompt-cache stability," "goal drift taxonomy." Who is affected? One person, Rex, plus future-Rex reading his own CLAUDE.md next month. There are no teammates, no API consumers, no traffic. Every proposal justified by scale (C's verifier swarm, the skeptic pass, H's prompt-cache pennies) solves a problem Rex does not have. The blog authors are protecting a product used by millions; Rex is protecting an afternoon. The hidden assumption: because Anthropic does it, it's a practice — rather than a cost they can amortize that Rex cannot. H optimizes cache hits on a file one person loads a few times a day — invisible saving. C spends tokens to verify markdown Rex can read in thirty seconds. What survives the naivety test: D (/freeze, /careful) and A, because they map to a real fear — an agent wrecking files. G is cheap, fine. The thing missed: nobody asked whether Rex's current CLAUDE.md is already too long for him to follow — E hints at it but treats it as caching, not comprehension. The real risk isn't under-engineering; it's adding eight more rules to a file already straining one human's attention.

### The Long View
Single-dev markdown repos don't fail in three years because Rex picked the wrong eight proposals. They fail because the harness accreted ceremony until editing it felt like work, and Rex quietly stopped — or worse, an agent kept "improving" the meta-layer while the actual skills aged. That's the second-order risk the synthesis is blind to, because it's importing the failure modes of a 50-engineer API product onto a workspace with one human and no traffic. What compounds: the skills being genuinely useful, and CLAUDE.md staying legible enough that Rex trusts it. What depreciates: every tactic tuned for prompt-cache economics and multi-agent token budgets at Anthropic's scale (C, F's verifier-subagents, H's cache framing). Prompt-cache stability (H) saves nothing measurable; adopting it as a rule is cargo-cult — a constraint whose failure mode you'll never experience, violating "every rule cites its failure mode." Cut it. Adopt only what reduces future cognitive load: A (real — Cowork can touch the repo), E (slimming compounds), G (one sentence, prevents real context loss). Defer everything else until a concrete failure demands it. The discipline that ages well is saying no to your own tooling.

### The Veteran
B (failure taxonomy) and H (static CLAUDE.md) are the only two that survive contact with reality unconditionally — B because naming a failure is what your invariant already demands, H because it costs one line. The pattern I've watched fail repeatedly: importing the scaled-team playbook into a solo repo. C and D are exactly that. C — verifier-subagent per rule plus a skeptic pass — is the "defense in depth" instinct that makes sense when twelve engineers push to a shared harness. You are one person who reads his own diffs; a skeptic subagent per rule is ceremony that, on attempt three, gets silently skipped because it doesn't pay for its latency. If you ever feel the need, that's a signal your dry-run-against-output-small contract has a gap — fix that instead. D (/freeze, /careful) solves a multi-agent-stomping problem you mostly don't have on direct-on-main solo; the honest exception is Cowork, which is why A is worth it and D mostly isn't. A is the one genuinely-new thing, not imported: a second non-Claude agent now touches the repo. E and G are housekeeping — do them when you next touch CLAUDE.md anyway, not as a project. F is half-real: the conclusion-vs-artifact heuristic is worth one line; the verification-subagent prompt library is C's ceremony in a smaller coat — skip it. Verdict: B, H, A, the cheap half of F. Defer E/G. Kill C/D. 60% sound, 40% scaled-context cosplay.

---

## Peer review (de-anonymized)

**Vote tally — Strongest:** The Architect ×5.
**Vote tally — Biggest blind spot:** The Architect ×3, The Stranger ×1, The Skeptic ×1.

### What the council collectively missed
- **The proposals are entangled, not a separable menu.** E (slim) pulls against B/F/G (add lines); H (freeze) conflicts with E/G (edit). Scored as a coupled set, even the minimalist verdict grows CLAUDE.md. — flagged by The Skeptic & The Long View
- **Provenance contamination.** The eight proposals were self-generated by Claude reading Anthropic's own marketing blogs, biasing the set toward Anthropic-shaped solutions; the alternatives Rex didn't get are invisible. — flagged by The Veteran
- **No deletion / sunset clause.** All five argued over what to ADD; none proposed a cut, on a file two advisors already call too long. — flagged by The Architect
- **The D-009 meta-irony.** This is a reversible markdown-prose decision; D-009 says don't council routine reversible work — yet here a council was convened, and no advisor noticed they ARE that over-application. — flagged by The Stranger, The Long View & The Veteran
- **H's cache premise is unverified.** The "timestamp churn breaks the prefix" claim describes Anthropic's infra, not Rex's local harness. — flagged by The Stranger, The Veteran & The Architect

### Individual reviews

**Reviewer — The Skeptic**
- Strongest: The Architect — converts the abstract dispute into a falsifiable test (instrument ten sessions; let data earn or kill C/D/E).
- Biggest blind spot: The Stranger — warns about attention overload but never engages the proposals' mechanics, so can't say which items are worth the cost.
- All missed: The proposals are mutually entangled, and this very council on a reversible decision is the routine work D-009 says not to council.

**Reviewer — The Stranger**
- Strongest: The Architect — names the root cause (zero instrumentation) and proposes a cheap test.
- Biggest blind spot: The Architect — accepts H on an unverified timestamp-churn claim about the local harness.
- All missed: This is the D-009 fork that should have triggered a council + scope-check before drafting; all five treat the proposals as a fixed menu rather than questioning the bundling.

**Reviewer — The Long View**
- Strongest: The Architect — converts disagreement into a decision procedure backed by evidence.
- Biggest blind spot: The Skeptic — flags synthesis-as-project but never asks whether the current CLAUDE.md is already too long to hold in attention.
- All missed: The adoption decision is itself a D-009 fork candidate; proposals interact (E vs B/F/G; H vs E/G) and weren't scored as a coupled set.

**Reviewer — The Veteran**
- Strongest: The Architect — names the missing variable and a cheap empirical test.
- Biggest blind spot: The Architect — asserts the timestamp-churn premise as fact when it's unverified for the local harness.
- All missed: Provenance integrity — a self-generated list from a vendor's marketing content is a contaminated input set; and the council didn't size whether the exercise clears its own D-009 bar.

**Reviewer — The Architect**
- Strongest: The Architect — names the meta-error and gives a concrete cheap test.
- Biggest blind spot: The Architect — adopts H on an unverified mechanical claim.
- All missed: This review IS a D-009 genuine-fork event recommended without the council its own rule demands; and no one proposed a deletion or sunset clause, so even minimalist verdicts grow the file.

---

## Chairman synthesis

### Recommendation headline
Adopt the four cheap, failure-naming proposals (A, B, H, and the one-line half of F), defer E/G to your next CLAUDE.md edit, and kill C/D — but first instrument ten sessions, because this council is itself the D-009 over-application it's evaluating.

### Where the council agrees
Unusually strong convergence. **Kill C and D** — all five flag them as imported large-team defense-in-depth against many untrusted invocations; Rex is one person reading his own diffs, and existing scope limits + the dry-run-against-`output-small` contract already cover the failure. **Adopt A** — Cowork writing the repo unsupervised is the one genuinely new fact, not imported from any blog. **B and the cheap half of F** earn their line; cut F's verification-subagent prompt library (C's ceremony in a smaller coat). **E and G are housekeeping**, not a project. And the whole synthesis is partly scaled-context cosplay — importing a 50-engineer API product's failure modes onto a one-human, zero-traffic repo.

### Where the council clashes
Only **H** (static CLAUDE.md for cache stability). Architect/Veteran adopt it as one free line; Skeptic/Long View reject it as cargo cult violating "every rule cites its failure mode"; Stranger rejects it as an invisible saving. Resolves once you see the adopters assert an unverified premise — four of five reviews caught that the cache claim describes Anthropic's infra, not Rex's local harness. H isn't free if it's false.

### Blind spots the council caught
Entanglement (E vs B/F/G/H; the set grows the file either way); provenance contamination (proposals self-generated from Anthropic's blogs); no deletion/sunset clause proposed; and the D-009 meta-irony that this council is itself the over-application the rule warns against.

### The recommendation
Adopt A, B, H-conditionally, and the one-line half of F. Defer E and G to your next incidental CLAUDE.md edit. Kill C and D outright. Treat this as the last time you council a decision this reversible. You're optimizing the wrong variable — you have zero instrumentation on your harness's actual failure rate, so C/D/E answer questions your repo may never have asked. A responds to a new fact (Cowork). B and the F half cost a line and satisfy an invariant you hold. H gets a conditional yes only after you verify the cache actually breaks on edit locally. Don't let the synthesis become the project; one retro line per session tells you whether goal-drift, bad substitution, or lost context actually occur. When you next open CLAUDE.md, your first edit should be a cut.

### The one thing to do first
Add one line to your retro template — "failure this session: [bad substitution / scope creep / lost context / none]" — and log it for the next ten sessions. Let that log earn or kill C/D/E. Everything else (A, B, the F half) folds in whenever you next touch CLAUDE.md; nothing here justifies a dedicated editing session today.

### Council alignment
| Advisor | Position | Core argument |
|---|---|---|
| The Skeptic | Adopt H only, maybe A/G | Most proposals are decoration; verify the cache claim before writing any rule, and beware the synthesis becoming the project. |
| The Architect | Adopt A/B/F/H, instrument rest | You have zero data on actual failure rate; log ten sessions and let the log earn or kill C/D/E. |
| The Stranger | Adopt A/D/G only | Every scale-justified proposal solves a problem one person protecting an afternoon does not have. |
| The Long View | Adopt A/E/G, defer rest | The repo dies from accreted ceremony, not wrong picks; adopt only what reduces future cognitive load. |
| The Veteran | Adopt B/H/A, cheap F | Sixty percent sound, forty percent scaled-context cosplay; kill C/D as solo-repo defense-in-depth. |

---

## Disposition (Rex + Claude, 2026-06-09)

Acted on the council the same session:
- **DONE** — retro "Failure this session" tag instrument (template + CLAUDE.md pointer), commit `4fb6a57`. This is the Architect's "one thing to do first."
- **KILLED** — C (verifier-per-rule swarm) and H (static-CLAUDE cache rule; premise unverified for the local harness and the saving is imperceptible solo — dropped rather than verified, since verification costs more than H could ever save).
- **DEFERRED to the next incidental CLAUDE.md / principles edit, no dedicated session** — A, B, the one-line half of F, E, G. Parked in `BACKLOG.md` with a 10-session kill-watch on C/E driven by the new failure log.
- **ALREADY PARKED** — D, as the "on-demand hook scaffolds" open decision in `BACKLOG.md`; council independently reaffirmed the defer.
- **Meta-lesson** — this council was itself a D-009 over-application (reversible markdown prose). For reversible-but-fuzzy calls, reach for `devils-advocate` (cheap) before `llm-council`; reserve the council for the costly+irreversible forks D-009 names.
