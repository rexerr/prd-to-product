# Working brief: Taste Builder

A web app that turns saving references into a training loop for aesthetic judgment — not just a better Pinterest. The library is a side effect; the product's actual value is the forced-interpretation moment during capture and the patterns that surface over time.

This is the seed for prd-creator. It's deliberately incomplete; the interview is supposed to fill the gaps.

## What it is

A reflective practice disguised as a reference tool — *and* a working corpus designers mine for client deliverables. You save a reference (upload, URL, mobile capture) and the system asks 1–3 short interpretation prompts before it lands in your library: *what do you like about this, what business context would this fit, what makes it feel contemporary or durable or premium or cheap.* Over weeks, the system surfaces your patterns — recurring motifs, color bias, composition tendencies, anti-patterns (what you consistently reject). It can also run *contrast sessions* — pull 8 references and force ranking ("which of these is trend-chasing," "which reason matters most") — to sharpen judgment, not just preserve it.

The dual purpose matters. **Personal mode** is the long-tail reflective practice that builds the corpus. **Client mode** is when you mine that corpus for a real project: a designer starting a luxury skincare brand pulls references from their own years-deep library, generates a "style language" from 12 selected pieces, and walks into a kickoff with a personal point of view instead of a blank Pinterest search.

The output isn't a library. It's a personal *canon* — recurring patterns, contradictions, anti-patterns — that's both a record of how you see and a working tool for billable work.

## Who it's for

Designers early in career who are trying to develop point of view, not just collect inspiration. Working freelancers and in-house designers who need to walk into client kickoffs with a personal canon instead of starting from a blank board. Brand designers who build direction faster by pulling from accumulated patterns. Anyone whose taste is part of what they sell. Solo-tool only in V1 — no shared libraries, no team collaboration.

## The core problem

Designers save references constantly. The saves become a graveyard. The act of saving *feels* like learning but it isn't — pattern recognition only compounds if there's a forcing function on the moment of capture that turns passive collection into active observation. There's no tool today that does this. Pinterest, IG saves, Dribbble likes are storage. The fix isn't better search; it's making the save *do* something.

## Rough shape of the experience

Four modes, not one.

- **Capture (personal).** Upload / paste URL / mobile capture → 1–3 interpretation prompts → tags (AI-suggested, user-edited) → reference lands in library. Interpretation is the unskippable part; tags are convenience. This is the slow, reflective default.
- **Capture (client).** Same flow but minimum friction — fast-save into a named project board, interpretation optional or deferred. Recognizes that a designer mid-client-deadline doesn't have time for the full prompt set.
- **Library.** Grid view, filter and search by tag and by interpretation. Storage is the floor; engagement should push users past it.
- **Project boards.** Slices of the library scoped to a specific client engagement. A reference can live in the universal library *and* in N project boards. Each board can generate a "style language" — a promptable description of shared traits across selected references — for use in kickoff decks, AI image gen, or brand-direction conversations.
- **Contrast and profile.** Periodic prompts that pull 8 references and force ranking ("which of these is trend-chasing"). A profile view that surfaces patterns ("you've saved 12 references with [specific trait], you avoid [specific trait]") — phrased with specificity, never as horoscope.

## What this is NOT

- Not a public reference feed or social product. No discovery from strangers in V1.
- Not collaboration / shared libraries. Single-user.
- Not AI image generation. The library is *real references*, not synthesized ones.
- Not a scraper from other tools. User uploads or pastes.
- Not portfolio / case-study presentation. That's a different product.
- Not a Claude skill. The training-loop value only compounds across months of sustained engagement, which a one-shot skill session can't deliver.

## Real risks worth naming upfront

- **Users may want storage, not reflection.** The product is more interesting than what most users will actively choose to do. V1 has to seduce engaged users into the reflective practice while still being usable as plain storage if they don't engage. If we make interpretation friction-heavy, lazy users churn. If we make it skippable, the differentiator dies. The friction calibration is the hardest UX call in the product.
- **Personal-mode and client-mode friction mismatch.** Personal mode wants slow, deep interpretation. Client mode wants fast-save under deadline pressure. Same library, different friction. If we apply personal-mode rigor everywhere, the client flow is unusable on a Tuesday afternoon. If we make everything skippable to keep client mode fast, the personal-mode differentiator dies. The split has to be deliberate.
- **Pattern surfacing can become aesthetic astrology.** "You tend toward boldness" is horoscope. "You've saved 12 references with high-contrast color palettes and architectural typography" is observation. The product is dead if users sense it's generating poetry instead of evidence. Specificity over phrasing.
- **Visual analysis in Claude is imperfect.** Auto-tagging will be wrong sometimes. The product has to make editing tags / interpretations cheap and not feel like work the user is doing for the AI.
- **"Taste" is a loaded word.** May or may not survive to the public name; brief uses it as the working term.

## Open questions for the interview

These are where prd-creator should focus.

- **Auth.** Required, magic-link only, or no-auth-solo-tool first? (Affects DB, hosting cost, whether deploy is even meaningful in V1.)
- **Image storage.** Cloud (S3 / R2 / Cloudflare Images) vs self-host vs hybrid. Cost model matters — designers save *a lot* of images, and that's the dominant cost driver.
- **AI tagging and interpretation.** Which model (Claude, Gemini, GPT-4 vision)? What's the seed tag taxonomy? Does the user own / edit the taxonomy or does it auto-evolve? How are interpretation prompts authored — preset library, AI-generated per image, or both?
- **When does forced interpretation happen?** At capture (high friction, high depth) or in batch sessions later (lower friction, may never happen)? Or both — one quick prompt at capture, optional deep-dive in a weekly "review session"? This is the central UX call.
- **Mobile capture.** Native iOS, PWA, share-sheet target, or browser-only? "I saw this on my phone" is the dominant capture moment for many designers.
- **Profile / pattern-surfacing scope in V1.** Is the taste profile a V1 feature or an unlock at N references saved? Specificity threshold for surfaced patterns to avoid astrology mode?
- **Project boards in V1.** The client-work mining path is the difference between "tool I use for self-improvement" (gets abandoned in week 3) and "tool I use on billable work" (sticky). Project boards probably land V1, not V2 — confirm scope in PRD. Style-language extraction (turning 5–20 selected references into a promptable description) is the natural next feature; could be V1 or V1.5.
- **Naming.** Working name "Taste Builder" is loaded. The candidates split along positioning lines: *personal-practice register* (modest, honest about behavior) — **Taste Journal**, **Squirreled**, Reps; *client-work register* (professional, working-tool) — **Throughline**, Atelier, **Taste Refinery**. Almost no name fits both registers cleanly. Best path: pick the load-bearing differentiator (personal practice) and let the client-work flow be a use case of that name. Current finalists: Taste Journal (safest, modest), Squirreled (most distinctive, personality risk), Throughline (most professional, hardest to use casually). Backup options preserved for the PRD: Point of View, Pattern Library, Aesthetic Memory, Atelier, Squint, Reps. Defer the final call but capture the registers for the PRD interview.
- **Stack.** Next.js + Vercel is the natural fit and matches the build-defaults pilot's deploy-shell Phase 1. Confirm during PRD.
- **What "done with V1" looks like.** Personal use only, or share with 2–3 designer friends as a beta?

## Validation purpose for this repo

Beyond being a real product, this brief is the input that exercises the `prd-creator` → `context-engineering` → real-build chain end-to-end. It's the first deployed-app validation since the build-defaults pilot shipped. Expect signal on:

- Does prd-creator's interview surface the right questions from this brief?
- Does Phase 1 deploy-shell (per build-defaults pilot item 1) actually get followed?
- Does the BACKLOG / ROADMAP split feel right in a real session, or does it create friction?

## Source

This conversation, 2026-05-11. Neighbor ideas worth keeping warm: Taste Genome (the analysis-layer evolution of this product), Vibe-to-System Compiler (downstream — taste library → design system primitives).
