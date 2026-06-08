Close out the session cleanly. Follow the session-discipline rules in CLAUDE.md and the retro convention (`docs/retros/README.md`).

1. **Restate** in one short block: what was done, what was **verified** — concrete evidence (dry-run substitution diffed against `examples/output-small/`, hook payload tests, or re-read cross-references for doc changes — see CLAUDE.md "Verification before claiming done"), not "the code looks correct" — and what remains.

2. **Update the docs the work changed.** Tick / move completed items in `BACKLOG.md` (In progress → resolved go to a retro, not back into the file). Log any significant decision in `docs/DECISIONS.md`, and mirror a one-liner into `docs/DECISIONS_ACTIVE.md` if it imposes a binding constraint not visible from the code.

3. **Retro — only if the session was non-trivial** (skip one-line tweaks; avoid retro-spam). Get the time with `date "+%Y-%m-%d %H:%M %Z"`, then write `docs/retros/YYYY-MM-DD-topic.md` with a timestamped, session-numbered H1 (`# Retro — YYYY-MM-DD HH:MM TZ — [topic]   (Nth session of the day)`). Be honest about misses, deviations, and what verification did and did not cover.

4. **Commit + push as ONE commit** (only when the task asked to commit/push). Stage code + retro + doc updates together and push once — never push the code, then push the retro as a second commit (that double-push is the waste the retro exists to prevent). Paste the resulting commit URL: `https://github.com/rexerr/prd-to-product/commit/<sha>`.

5. **Hand off.** List anything still gated on Rex and the single next thing to pick up.
