# Intake flow

The interview that produces a PRD. Run the clusters in order. Do not dump every question at once. Read this file when the skill triggers.

## How to run a cluster

Every cluster follows the same shape. Do not skip steps.

1. Ask the cluster's questions. Up to three per call. Free-text fills ask one at a time. Branching questions offer two to four options, never more. When the cluster 0 source material already covers a question, do not ask it cold. Present a draft answer drawn from that material for the user to confirm or edit (the full rule is in cluster 0). Ask cold only where the material is thin or silent.
2. Capture the answers verbatim into a running scratch buffer the user does not see. Do not paraphrase prematurely.
3. Sweep for open questions before closing the cluster. Ask the user "anything you do not yet know about <cluster topic> that would change the build." Capture each into the running open-questions list.
4. Sweep for decisions before closing the cluster. If the user stated something that locks a future choice ("we are using Vercel," "single-user no auth"), assign a draft `D-NNN` ID and append to the running decisions list. Do not ask permission to capture, and do not narrate the draft ID to the user (no "that's D-002"). Just capture, and review the numbered list in cluster 5.
5. Summarize what was captured in two or three sentences. Wait for the user to correct or confirm before moving to the next cluster.

**User-facing copy is natural language.** Never name internal scaffolding in what you say to the user. No "cluster 0" or "cluster 3", no "as source material", no draft decision-ID narration while capturing. The cluster numbers and draft `D-NNN` IDs are yours, not the user's. Confirmed decision IDs appear to the user only at the cluster 5 read-back and in the written PRD, where they are part of the deliverable. **Failure it prevents:** the user sees how the sausage is made instead of a conversation, which reads as the skill not having understood them.

## Cluster 0: source material

**Always run first.** Do not skip even when the user pasted a brief earlier in the conversation. The lesson from context-engineering Pass 1.7 is that silently absorbing pasted context produces worse PRDs than asking anyway.

**Check the working directory first.** Before asking, the generator checks the working directory and `docs/` for candidate source files: `BRIEF.md`, `brief.md`, `*-brief.md`, `IDEA.md`. This is a detection aid, not silent absorption: offer what you find, never read it before the user confirms, and make no claim about a found file's age or recency.

- **One candidate found.** Offer it without reading it yet: "I see `docs/brief.md` in this project, read it as your source material? (yes / point me at another file / none)." On yes, treat it as the "User has source material" branch below. The offer *is* the source-material question; do not also ask the generic question.
- **Multiple candidates.** List them and ask which to use, or none.
- **None found.** Ask the generic question:

> Before we start, do you have a working brief, research dump, transcript, message thread, or notes you want me to read first. Paste, link, or tell me there's none.

Three branches:

- **User has source material.** Read it. State a one-paragraph summary of what you found, describing what the material contains. Do not speculate about when it was written or how recent it is (no "this was written a while ago," no "your thinking may have moved on since") unless the material itself states a date you can cite. Then, for each later cluster the material covers, draft that cluster's answer from the material and present the draft for the user to confirm, edit, or correct, rather than asking the user to state it cold. Where the material is thin or silent on a cluster, ask that cluster's questions cold. This is the line between three behaviors, and only the third is right: silently absorbing the material and moving on without showing the user is wrong (it produces shallow PRDs, the context-engineering Pass 1.7 lesson); asking cold for things the material already answers is also wrong (it makes the user re-state work they already did, and reads as if you did not read it); drafting from the material and presenting every draft for explicit edit is right, because nothing is absorbed without the user seeing it and signing off.
- **User has none.** Acknowledge. Move on.
- **User wants to skip the interview entirely and let you draft from material alone.** Decline. Explain that this skill's value is the interview; if they want a one-shot draft from material, they should write it themselves. Then offer to run the interview anyway.

Close cluster 0 with a natural-language hand-off, not a cluster label. For example: "Ready to start. First, the quick pitch, who it is for, and why it exists. Confirm to proceed."

## Cluster 1: elevator pitch

The opening shot. Combines the brief's clusters 1 and 2 (pitch plus user plus problem) because the three are tightly coupled and asking them separately produces repetition.

Ask in this order, one question at a time:

1. "In one paragraph, what is this product. Lead with what it does, then who it is for, then why it exists."
2. "Who specifically is the V1 user. Concrete role, not 'everyone who needs X.' If there is more than one user type, name each."
3. "What are these users currently doing instead. The workaround they will abandon when this exists."

Capture into: product summary, target users, core problem.

Sweep for open questions. Sweep for decisions. Summarize and confirm.

## Cluster 2: main workflow

The happy path. One numbered list, each step one sentence.

Ask:

> Walk me through the V1 happy path. What does the user do, step by step, the first time the product works for them. Three to seven steps is typical.

If the user produces fewer than three steps or more than ten, push back. Three is usually too thin (probably missing setup or output), more than ten is usually two workflows that need to be split.

Sweep for open questions on edge cases: "What happens if step N fails. Capture as open question or as out of scope, your call." Sweep for decisions. Summarize and confirm.

## Cluster 3: scope

V1 in, V1 out, deferred. Combines the brief's clusters 3 and 7 because users naturally produce in-scope and out-of-scope items in the same breath.

Ask, one question per call:

1. "What is V1. Bullet list of capabilities, each one checkable."
2. "What did you consider for V1 and explicitly cut. The cuts matter as much as the inclusions."
3. "What is V2 or later. Things you want to build but not now."

Distinguish carefully. "We will figure it out later" goes in deferred capabilities, not out of scope. Out of scope is a rejected capability for V1 that may or may not come back.

Sweep for open questions. Sweep for decisions. Summarize and confirm.

## Cluster 4: architecture and stack

What is decided about how this gets built. The user is not designing new architecture here; they are stating what they have already chosen.

Ask, one question per call:

1. "What is the stack. Framework, deploy target, key services, third-party APIs, databases."
2. "What integrations does V1 require. Auth providers, payment, email, AI APIs, anything external."
3. "What is the AI surface, if any. Where in the product does an LLM call happen, and what does it produce."

If the user has not made a choice on a stack item, do not push them to choose. Capture the question into open questions and move on.

Sweep for open questions. Sweep for decisions. Summarize and confirm.

## Cluster 5: decisions consolidation

Review the running decisions list captured across clusters 1 through 4. This cluster does not collect new decisions; it confirms and assigns final IDs.

1. State the running list back to the user, formatted as `D-001` through `D-N` with statement plus rationale for each.
2. For each, ask the user to confirm, edit, or drop. Do this as a single batch read-back, not one decision at a time, since the user is reviewing not deciding.
3. Ask: "Anything else you have already committed to that I missed."
4. Renumber if any were dropped. The final list has no gaps.

This is the only cluster where you re-state captured material before closing. The decisions list is load-bearing for the context-engineering hand-off.

## Cluster 6: brand and voice (optional)

Skip if the product is purely backend, dev tooling with no user-facing copy, or the user explicitly waves it off.

Ask, one question per call:

1. "Who reads or hears this product's voice. Concrete audience segments."
2. "Three to five tone attributes. Each one a single word or short phrase plus a one-line definition. Examples beat principles."
3. "Any vocabulary the product locks. Terms with a canonical name plus old or alternate names that should not be used."
4. "Any patterns to avoid. Tone, words, framings the brand explicitly does not do."

Track the volume. Three or fewer total items across all four questions means the content lands inline as an appendix in the PRD. More than three means the content lands in a sibling `BRAND.md`. The decision logic in `decisions.md` makes the call.

Sweep for open questions. Summarize and confirm.

## Cluster 7: success criteria and testing decisions

Concrete done-when statements, then how V1 gets verified. Each success criterion is checkable. If the user cannot answer concretely, the unanswered version goes in open questions, not in success criteria.

Ask, one question per call:

1. "What does V1 success look like. Concrete metrics, behaviors, or events. 'Ten users complete the workflow without help' is checkable. 'Users find it intuitive' is not. List two to five."
2. "How will you know V1 actually works, and what counts as a good test here. Name the external behaviors to verify, which parts of the system matter most, and any prior art you will model tests on. Not test code, just the testing decisions. If V1 ships no automated tests, say so and how you will verify instead."

Push back on vibes-criteria. "Feels good" → "what specifically would feel bad, and how would you know." Convert to checkable or capture as open question.

Capture into: success criteria, testing decisions. "No automated suite, verified by a manual pass over the validation window" is a valid testing decision, not a blank. If the user names no verification approach at all, capture "verification approach undecided" as an open question rather than leaving the testing decisions section empty.

Sweep for open questions. Summarize and confirm.

## After all clusters

State the proposed PRD outline. In the outline you show the user, name the sections, not the cluster numbers (track which cluster filled which section for yourself). Name every section that will be skipped and why. Confirm the placement choice for the brand and voice content (inline appendix vs sibling file).

Wait for explicit user confirmation before writing files. If `docs/PRD.md` or `docs/BRAND.md` already exists, flag it here — it will be shown as a diff for overwrite/skip consent at write time (default skip), never silently replaced (per `decisions.md` "Non-destructive write guard"). Then run `decisions.md` to determine final emission and write the PRD, applying the write guard to every target.
