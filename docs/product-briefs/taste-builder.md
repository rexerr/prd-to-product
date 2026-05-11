# Working brief: Taste Builder

A web app that turns saving references into a training loop for aesthetic judgment — not just a better Pinterest. The library is a side effect; the product's actual value is the forced-interpretation moment during capture and the patterns that surface over time.

This is the seed for prd-creator. It's deliberately incomplete; the interview is supposed to fill the gaps.

## What it is

A reflective practice disguised as a reference tool. You save a reference (upload, URL, mobile capture) and the system asks 1–3 short interpretation prompts before it lands in your library: *what do you like about this, what business context would this fit, what makes it feel contemporary or durable or premium or cheap.* Over weeks, the system surfaces your patterns — recurring motifs, color bias, composition tendencies, anti-patterns (what you consistently reject). It can also run *contrast sessions* — pull 8 references you've saved and ask "which of these is trend-chasing vs timeless," "which reason matters most" — to sharpen judgment, not just preserve it.

The output isn't a library. It's a *taste profile*: a personal record of recurring patterns, contradictions, and blind spots that doubles as a promptable "style language" for future projects.

## Who it's for

Designers early in career who are trying to develop point of view, not just collect inspiration. Freelancers defining their aesthetic to differentiate. Brand designers who need to build direction faster on new projects by pulling from a personal pattern library instead of starting cold. Solo-tool only in V1.

## The core problem

Designers save references constantly. The saves become a graveyard. The act of saving *feels* like learning but it isn't — pattern recognition only compounds if there's a forcing function on the moment of capture that turns passive collection into active observation. There's no tool today that does this. Pinterest, IG saves, Dribbble likes are storage. The fix isn't better search; it's making the save *do* something.

## Rough shape of the experience

Three modes, not one.

- **Capture.** Upload an image / paste URL / mobile capture → 1–3 interpretation prompts → tags (AI-suggested, user-edited) → image lands in library. Interpretation is the unskippable part; tags are convenience.
- **Library.** Grid view, filter and search by tag and by interpretation. Storage is the floor; engagement should push users past it.
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
- **Naming.** Working name "Taste Builder" is loaded and may signal aesthetic-bro vibe. Alternatives floated: Point of View, Pattern Library, Aesthetic Memory, Reference Coach, Design Judgment Trainer. Defer the call until later but capture for the PRD.
- **Stack.** Next.js + Vercel is the natural fit and matches the build-defaults pilot's deploy-shell Phase 1. Confirm during PRD.
- **What "done with V1" looks like.** Personal use only, or share with 2–3 designer friends as a beta?

## Validation purpose for this repo

Beyond being a real product, this brief is the input that exercises the `prd-creator` → `context-engineering` → real-build chain end-to-end. It's the first deployed-app validation since the build-defaults pilot shipped. Expect signal on:

- Does prd-creator's interview surface the right questions from this brief?
- Does Phase 1 deploy-shell (per build-defaults pilot item 1) actually get followed?
- Does the BACKLOG / ROADMAP split feel right in a real session, or does it create friction?

## Source

This conversation, 2026-05-11. Neighbor ideas worth keeping warm: Taste Genome (the analysis-layer evolution of this product), Vibe-to-System Compiler (downstream — taste library → design system primitives).
