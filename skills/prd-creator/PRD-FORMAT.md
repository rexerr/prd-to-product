<!-- Authority: this file is the single source of truth for the PRD's body-shape — the section skeleton (names + order) and the failure-cited rules for each section's content and style. On any conflict between a thin restatement elsewhere (the template's loaded cues, SKILL.md's file-list mention) and this file, THIS FILE WINS. Diff it against examples/small/PRD.md to verify shape. Adopted via CF-29 / D-052. -->

# PRD-FORMAT — shape contract for `PRD.md`

What lives where: `SKILL.md` routes; `templates/PRD.md.template` is the **loaded** artifact at generation, carrying the `PARAMETERIZE` markers plus thin operative cues that must fire while a PRD is written; **this file** is the reference authority — the canonical skeleton + the full failure-cited rules, diffable against the example. `principles.md` holds the *why*; this file holds the *what*.

## Canonical section skeleton

**12 always-emitted core sections, in order**, then **2 OPTIONAL** sections (allowed-absent, never required). This is the **ordering authority** — do not re-list section order anywhere else.

```
# <project name>                 H1: project name only — no tagline, no version suffix
## Product summary               core 1
## Target users                  core 2
## Core problem                  core 3
## Main workflow                 core 4
## Version 1 scope               core 5
## Out of scope                  core 6
## Deferred capabilities         core 7
## Architecture and stack        core 8
## Decisions already made        core 9
## Open questions                core 10
## Success criteria              core 11
## Testing decisions             core 12
## Brand and voice               OPTIONAL — inline appendix; omit when a sibling BRAND.md exists or no material
## Supporting documents          OPTIONAL — include when a sibling BRAND.md, external research, or other named sources exist
```

**Position-aware placement (the rationale lives in `principles.md`).** The U-shaped attention curve penalizes the middle, so the load-bearing pieces sit at the ends: top = product summary, target users, core problem; bottom = open questions, success criteria, supporting documents. Middle = scope, workflow, architecture, decisions, deferred. If the PRD grows past V1, new sections go in the middle; the top and bottom anchors stay.

## Per-section shape rules

One line each — what each section must contain. (These have thin operative restatements in the loaded template; this file is authoritative on conflict.)

- **Product summary** — one paragraph, three to five sentences. Lead with what the product does, then who it is for, then why it exists. No marketing voice.
- **Target users** — name the V1 user concretely; if more than one type, list each with a one-line role. List who it is built for in V1, not everyone who might benefit.
- **Core problem** — what these users struggle with and what they do instead. One or two paragraphs. Cite the workaround so the problem is checkable.
- **Main workflow** — numbered steps through the V1 happy path, each one sentence. No error states or edge cases (those go in V1 scope or open questions).
- **Version 1 scope** — what V1 ships; a bullet list, each item checkable. "Single-user, no auth" is checkable; "simple onboarding" is not.
- **Out of scope** — explicit cuts; each item names a capability considered and rejected for V1. "We'll figure it out later" goes in deferred capabilities, not here.
- **Deferred capabilities** — V2-and-later candidates; each points forward to a future version, not a "maybe never" (a "maybe never" is an out-of-scope cut).
- **Architecture and stack** — what is decided about how it gets built: stack, deploy target, key services, third-party dependencies. Prose plus a short bullet list. Capture decisions already made; open architectural questions go in open questions. Obeys "No volatile code locations" below.
- **Decisions already made** — a numbered seed list: each decision an ID (`D-001`..`D-N`), a one-line statement, a one-line rationale. The context-engineering skill lifts this into `DECISIONS.md` at scaffold time. Do not duplicate this section into a sibling file at PRD time.
- **Open questions** — questions that would change the build if answered differently. A question that changes no decision does not belong here.
- **Success criteria** — concrete done-when statements, each checkable. If the user cannot answer one concretely, capture the unanswered version in open questions instead.
- **Testing decisions** — names what a *good test* is, not test code: the external behaviors to verify, which parts of the system matter most, any prior art the tests model. If V1 ships no automated suite, say so and name how V1 is verified instead. Always emitted; if no approach was named, state that verification is undecided and cross-reference open questions. A decision record, not a test plan.
- **Brand and voice** *(OPTIONAL)* — inline appendix when cluster 6 produced three or fewer items and the user chose inline. If a sibling `BRAND.md` was emitted, omit this and link to it from Supporting documents.
- **Supporting documents** *(OPTIONAL)* — include when there is a sibling `BRAND.md`, an external research dump, prior product docs, or other named sources the reader should know about.

## Style rules — house style for the PRD

Each carries the failure it prevents.

- **Sentence-case headers.** H1 for the document title; H2 for canonical sections; H3 for subsections only when the section has more than one distinct piece. No H4 or deeper. *Failure it prevents: Title Case and deep nesting drift per-PRD, so the corpus reads as several house styles instead of one.*
- **No em dashes.** Use commas, periods, or parentheses. *Failure: em dashes are the house tell of un-edited AI prose.*
- **No Oxford commas.** *Failure: inconsistent series punctuation across PRDs.*
- **No colons in titles.** *Failure: "Feature: subtitle" headers fight the sentence-case rule and bloat the table of contents.*
- **AP style.** *Failure: ad-hoc capitalization/number/abbreviation choices diverge between PRDs.*
- **Specific over generic.** "Approve and skip are the only triage actions" beats "Triage should be simple." *Failure: a generic line reads as filler and changes no reader's understanding.*
- **Cite specific files, sources, or prior decisions when describing constraints.** "Per D-003 we ship on Vercel" beats "We ship on Vercel." *Failure: an uncited constraint can't be traced or checked.*
- **Every paragraph earns its tokens.** If a sentence does not change a reader's understanding, cut it. *Failure: padding buries the load-bearing lines.*

## Content conventions — what goes in the sections

Each carries the failure it prevents.

- **Imperatives, not principles, in scope and decisions.** "V1 ships single-user, no auth" is a decision; "Keep V1 simple" is not. If a statement cannot be checked, rewrite it until it can. *Failure: an uncheckable principle reads as a decision but commits the build to nothing.*
- **Out of scope is a list of explicit cuts, not a vague boundary.** Each item names what was considered and rejected for V1. *Failure: a vague boundary doesn't actually cut anything; the scope creeps back.*
- **Deferred capabilities point forward.** Each item is a V2-or-later candidate, not a "maybe never" (which belongs in out of scope). *Failure: "maybe never" items masquerading as a roadmap inflate the forward plan.*
- **Open questions name what would change the build.** A question that does not change a decision belongs in a discussion thread, not the PRD. *Failure: decision-irrelevant questions dilute the ones that gate the build.*
- **Success criteria are concrete.** "10 users complete the workflow without help" beats "users find it intuitive." If a criterion can't be made concrete, capture it as an open question. *Failure: an unmeasurable criterion can never be marked done.*
- **No volatile code locations in the PRD.** Do not pin implementation file paths, line numbers, or verbatim code; they go stale on the first rename and the PRD rots silently while reading as accurate. One carve-out: inline a short prototype-derived snippet only when it encodes a decision more precisely than prose can — a state machine, schema, reducer, or type shape — trimmed to the decision-rich part. Citing a decision or named source doc by reference is fine; the ban is on volatile code, not on references. *Failure it prevents: a PRD that pinned `app/api/route.ts:42` or pasted a component becomes wrong on the first rename, and the reader cannot tell the stale line from the live ones.*
- **Testing decisions name what a good test is, not test code.** State the external behaviors to verify, which parts matter most, and any prior art the tests model. If V1 ships no automated suite, that is itself a testing decision: say so and name how V1 is verified instead. *Failure: a pasted test plan goes stale; a decision record about what to verify does not.*

## Hand-off contract with context-engineering (load-bearing)

The output PRD is the input to the context-engineering skill's cluster 0. Two pieces are load-bearing.

- **Named sections.** Context-engineering extracts product summary, target users, core problem, and architecture overview *by section name* using the canonical names above. Do not rename sections to a project's local idiom; add subsections under the canonical names instead. *Failure: a renamed section is invisible to the downstream extractor.*
- **Numbered decision seed list.** "Decisions already made" uses `D-001`, `D-002`, … one per decision with a one-line rationale — the format `DECISIONS.md` will absorb. The seed list is not a duplicate of `DECISIONS.md` (which doesn't exist yet at PRD time); it is the source context-engineering draws from when scaffolding it. *Failure: an unnumbered or differently-shaped list can't be lifted cleanly.*
