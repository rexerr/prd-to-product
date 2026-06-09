#!/usr/bin/env bash
# write-guard.sh — D-005 non-destructive write guard, enforced as a PreToolUse hook.
#
# PURPOSE. The generator skills (design-system-bootstrap, context-engineering,
# prd-creator) must never silently overwrite a hand-authored file (the qventus
# near-miss: a fresh tokens.css clobbering a real one). The prose guard in each
# skill's generator/decisions.md asks the agent to diff-and-confirm — but prose
# the agent can drop under context pressure is not enforcement. This hook is the
# enforcement: it intercepts Write/Edit on a file that existed BEFORE the run and
# forces a non-forgeable user decision (interactive) or a safe skip (headless).
#
# WHY A HOOK, NOT A LEDGER. An earlier design had the hook exit 2 and tell the
# agent to record its own consent token — but the agent (the entity under
# pressure) could self-consent. permissionDecision:"ask" forces the native
# permission dialog, which the agent cannot answer for the user. That is the only
# non-forgeable primitive. (Verified on 2.1.138/2.1.165 — see hooks/README.md.)
#
# ARMING / DORMANCY. The guard is GLOBAL (fires on every Write/Edit) but DORMANT
# unless a skill armed THIS session: it looks up a sentinel keyed by the payload's
# session_id. session_id is the safety key — a different project is a different
# session, so the guard never wedges unrelated work. TTL is GC only.
#
# RUN-OWNED SET. "Pre-run" = "existed before the run" — NOT "exists now", which
# would self-block a generator editing a file it just created (Write-then-Edit).
# The hook records run-created files in <session>.owned itself; a missing/empty
# owned set fails SAFE (existing files fall through to the gate, never to allow).
#
# All scoping lives HERE, in the script (the block-env-commit.sh pattern). The
# settings.json entry is a bare matcher "Write|Edit|MultiEdit".

set -u
# Override only for tests; production always resolves under the real home dir.
STATE_DIR="${WRITE_GUARD_STATE_DIR:-${HOME}/.claude/state/write-guard}"

payload=$(cat)

# --- extract a top-level JSON string field (no jq dependency, like the env hook) ---
json_str() {
  printf '%s' "$payload" \
    | grep -oE "\"$1\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" \
    | head -1 \
    | sed -E "s/^\"$1\"[[:space:]]*:[[:space:]]*\"(.*)\"$/\1/"
}

session_id=$(json_str session_id)
file_path=$(json_str file_path)
permission_mode=$(json_str permission_mode)

# No session id -> we have no safety key -> the guard cannot be armed -> allow.
[ -z "$session_id" ] && exit 0

sentinel="$STATE_DIR/${session_id}.sentinel"
owned="$STATE_DIR/${session_id}.owned"

# --- Ladder step 1: dormancy gate (session-keyed; refresh-on-match; age-reap others) ---
# Refresh THIS session's state FIRST so an actively-used-but-idle session never
# ages out (the 2B idle-disarm bug). Then GC strictly stale files from any
# session — the just-touched current files have a fresh mtime and survive.
if [ -f "$sentinel" ]; then
  touch "$sentinel" "$owned" 2>/dev/null     # refresh; creates an empty owned if absent (harmless)
  find "$STATE_DIR" -maxdepth 1 -type f \( -name '*.sentinel' -o -name '*.owned' \) -mtime +1 -delete 2>/dev/null
else
  # Not armed for this session -> dormant. Opportunistically GC stale orphans.
  [ -d "$STATE_DIR" ] && find "$STATE_DIR" -maxdepth 1 -type f \( -name '*.sentinel' -o -name '*.owned' \) -mtime +1 -delete 2>/dev/null
  exit 0
fi

# --- Ladder step 2: control-path exemption (guard's own state must never self-gate) ---
case "$file_path" in
  "$STATE_DIR"/*) exit 0 ;;
esac

# No path to evaluate -> nothing to guard.
[ -z "$file_path" ] && exit 0

# --- Ladder step 3: fresh create -> run-owned, allow ---
# PreToolUse fires BEFORE the write, so a to-be-created file is legitimately absent.
if [ ! -e "$file_path" ]; then
  printf '%s\n' "$file_path" >> "$owned" 2>/dev/null
  exit 0
fi

# --- Ladder step 4: already run-owned -> allow (fixes the self-block) ---
if grep -qxF -- "$file_path" "$owned" 2>/dev/null; then
  exit 0
fi

# --- Ladder step 5: unfilled scaffold marker -> allow (never customized) ---
if grep -qE '<!-- (PARAMETERIZE|OPTIONAL):' "$file_path" 2>/dev/null; then
  exit 0
fi

# --- Ladder step 6: pre-run, hand-authored -> GATE ---
# Mode branch (evidence-locked): CLAUDE_CODE_ENTRYPOINT is the only reliable
# interactive/headless signal (/dev/tty is "no" even in the desktop app;
# permission_mode is "auto" interactively / "default" headless — neither
# discriminates). Headless SDK entrypoints start with "sdk". Fail toward deny:
# unknown/empty entrypoint or bypassPermissions -> deny (never hang, never clobber;
# headless auto-denies an "ask" anyway as a backstop).
entrypoint="${CLAUDE_CODE_ENTRYPOINT:-}"
if [ -z "$entrypoint" ] || [ "${entrypoint#sdk}" != "$entrypoint" ] || [ "$permission_mode" = "bypassPermissions" ]; then
  decision="deny"
else
  decision="ask"
fi

# JSON-escape the path for the reason string (paths rarely contain " or \, but be safe).
esc=$(printf '%s' "$file_path" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')
reason="\\\"${esc}\\\" existed before this generator run (hand-authored). Per D-005, show a diff and get explicit overwrite/skip consent (default skip). This is a skip — do not retry this write."

printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":"%s"}}\n' "$decision" "$reason"
exit 0
