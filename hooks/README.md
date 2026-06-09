# `hooks/` — kit-level enforcement hooks

These hooks guard **the generator skills themselves** while they run. They are NOT
the `block-*.sh` hooks that `context-engineering` scaffolds *into* generated
projects (those live in `skills/context-engineering/templates/claude-hooks/`).
This directory is dev tooling for *this* kit, installed once into the operator's
`~/.claude/`.

## `write-guard.sh` — D-005 non-destructive write enforcement

Turns the prose "non-destructive write guard" (D-005, in each skill's
`generator/decisions.md`) into an enforced one. A `PreToolUse` hook on
`Write|Edit|MultiEdit` that, **only while a generator run is armed**, refuses to
let a write land on a file that **existed before the run** without a non-forgeable
user decision.

### Decision ladder (all scoping in-script)

1. **Dormancy gate** — looks up `~/.claude/state/write-guard/<session_id>.sentinel`
   (session_id from the payload). Not armed for *this* session → allow. `session_id`
   is the safety key (a different project = a different session = dormant). The
   sentinel is refreshed on every matched call so a long, idle-then-resumed run
   never ages out; a generous TTL (~1 day) only GCs orphaned sentinels.
2. **Control path** — writes under the state dir are exempt.
3. **Fresh create** (path absent on disk) → record in `<session_id>.owned`, allow.
4. **Run-owned** (path in `.owned`) → allow. This is what lets a generator edit a
   file it created earlier in the same run. A missing/empty `.owned` matches
   nothing, so existing files fall through to the gate — **fail-safe, never open.**
5. **Unfilled scaffold** (`<!-- PARAMETERIZE:` / `<!-- OPTIONAL:` marker present) → allow.
6. **Pre-run, hand-authored** → gate. Interactive → `permissionDecision: "ask"`
   (native dialog the agent cannot answer for the user). Headless / `bypassPermissions`
   / unknown → `permissionDecision: "deny"` (D-005 default-skip; never hangs, never clobbers).

### Interactive vs headless

Detection is by **`CLAUDE_CODE_ENTRYPOINT`**: an SDK/headless entrypoint starts with
`sdk` (e.g. `sdk-cli`) → `deny`; anything else (`claude-desktop`, `cli`, …) → `ask`.
`/dev/tty` and `permission_mode` were tested and rejected as signals (both read the
same in the desktop app as in `claude -p`). Verified on Claude Code 2.1.138 / 2.1.165:
`deny` is honored for Write and Edit in `default` and `acceptEdits`; a headless `ask`
auto-resolves to a deny (does not hang); the interactive `ask` dialog offers only
allow-once (no "for session" option, so one approval can't neuter the guard).

### The arming contract (what the skills must do)

A generator skill arms the guard at run start and disarms at run end, using its own
session id (`$CLAUDE_CODE_SESSION_ID` equals the payload `session_id` for a real,
non-nested session):

```bash
# run start (arm) — use Bash, not the Write tool, so it bypasses the guard's own matcher
mkdir -p ~/.claude/state/write-guard
: > ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel

# run end (disarm)
rm -f ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel \
      ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".owned
```

A forgotten disarm is harmless (keyed by a dead session id → dormant for every other
session; GC'd by TTL). A forgotten **arm** means no enforcement for that run — that is
the one unprotected residual; the prose guard is the backstop.

### Install (operator, once)

`write-guard.sh` must be **executable** (a non-exec hook exits 126 → Claude Code treats
it as a non-blocking error and *allows* the tool). Wire it globally:

```jsonc
// ~/.claude/settings.json
{ "hooks": { "PreToolUse": [
  { "matcher": "Write|Edit|MultiEdit",
    "hooks": [ { "type": "command", "command": "<path>/hooks/write-guard.sh" } ] }
] } }
```

`MultiEdit` is included for forward-compat; it is not a tool in 2.1.138.

**Install gotchas (learned the hard way):**
- The script must be **executable** — a non-exec hook exits 126, which Claude Code treats as a non-blocking error and **allows** the tool. `chmod +x`.
- Editing `~/.claude/settings.json` via an **agent Edit tool is reverted** by the harness (it protects agent self-edits to config). Apply the hooks key by a **direct file write** (or have the user edit it), with the user's explicit consent. The desktop app itself does *not* revert a direct write (verified persistent).
- Verify an install by `permission_denials`, **not** by file state — a file can be "unchanged" for unrelated reasons (the agent didn't attempt it; an Edit-needs-prior-Read block fired first).

### Honest ceiling

Enforced for the pre-run hand-authored class. Bypassable only by global permission-skip
modes (`--dangerously-skip-permissions`). Headless runs **cannot update a pre-existing
file at all** (they `deny`) — they are non-destructive *because* they are update-incapable
on existing files, restricted to greenfield work. Not yet distribution-portable (lives in
the operator's `~/.claude/`, not the shipped skill).

### Test

`bash hooks/write-guard.test.sh` — 15 mock-payload assertions across every branch.
