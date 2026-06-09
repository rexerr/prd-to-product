#!/usr/bin/env bash
# Unit tests for write-guard.sh — exercises every ladder branch with mock payloads.
# Run: bash hooks/write-guard.test.sh   (exit 0 = all pass)
HERE=$(cd "$(dirname "$0")" && pwd)
HOOK="$HERE/write-guard.sh"
ROOT=$(mktemp -d)
export WRITE_GUARD_STATE_DIR="$ROOT/state"
SID="sess-AAA"
pass=0; fail=0
trap 'rm -rf "$ROOT"' EXIT

reset() { rm -rf "$ROOT/state" "$ROOT/files"; mkdir -p "$ROOT/state" "$ROOT/files"; }
arm()   { : > "$ROOT/state/$1.sentinel"; }
payload() { # tool file session mode
  printf '{"session_id":"%s","permission_mode":"%s","hook_event_name":"PreToolUse","tool_name":"%s","tool_input":{"file_path":"%s","content":"x"}}' "$3" "$4" "$1" "$2"
}
run() { # label expect tool file session mode entrypoint
  local label=$1 expect=$2 out rc got
  out=$(printf '%s' "$(payload "$3" "$4" "$5" "$6")" | CLAUDE_CODE_ENTRYPOINT="$7" bash "$HOOK"); rc=$?
  if   printf '%s' "$out" | grep -q '"permissionDecision":"ask"';  then got=ask
  elif printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then got=deny
  elif [ -z "$out" ] && [ $rc -eq 0 ]; then got=allow
  else got="??($rc)"; fi
  if [ "$got" = "$expect" ]; then pass=$((pass+1)); printf 'PASS  %-50s -> %s\n' "$label" "$got"
  else fail=$((fail+1)); printf 'FAIL  %-50s -> got=%s want=%s\n' "$label" "$got" "$expect"; fi
}

echo "=== write-guard.sh unit tests ==="
reset; printf 'hand\n' > "$ROOT/files/hand.css"
run "dormant: not armed -> allow"                 allow Write "$ROOT/files/hand.css" "$SID" auto claude-desktop
reset; arm other; printf 'hand\n' > "$ROOT/files/hand.css"
run "armed for other session -> allow"            allow Write "$ROOT/files/hand.css" "$SID" auto claude-desktop
reset; arm "$SID"
run "control-path -> allow"                       allow Write "$ROOT/state/$SID.owned" "$SID" auto claude-desktop
reset; arm "$SID"
run "fresh create -> allow"                       allow Write "$ROOT/files/new.css" "$SID" auto claude-desktop
grep -qxF "$ROOT/files/new.css" "$ROOT/state/$SID.owned" && { pass=$((pass+1)); echo "PASS  fresh create recorded in .owned"; } || { fail=$((fail+1)); echo "FAIL  fresh create NOT recorded in .owned"; }
reset; arm "$SID"; printf 'mine\n' > "$ROOT/files/mine.css"; printf '%s\n' "$ROOT/files/mine.css" > "$ROOT/state/$SID.owned"
run "in-owned (run created) -> allow"             allow Edit "$ROOT/files/mine.css" "$SID" auto claude-desktop
reset; arm "$SID"; printf '<!-- PARAMETERIZE: x -->\n' > "$ROOT/files/scaf.md"
run "scaffold marker -> allow"                    allow Write "$ROOT/files/scaf.md" "$SID" auto claude-desktop
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/hand.css"  # .owned absent
run "FAIL-SAFE missing .owned + existing -> ask"  ask  Write "$ROOT/files/hand.css" "$SID" auto claude-desktop
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"
run "hand-authored + desktop -> ask"              ask  Edit "$ROOT/files/tokens.css" "$SID" auto claude-desktop
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"
run "hand-authored + sdk-cli (headless) -> deny"  deny Edit "$ROOT/files/tokens.css" "$SID" default sdk-cli
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"
run "hand-authored + empty entrypoint -> deny"    deny Edit "$ROOT/files/tokens.css" "$SID" default ""
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"
run "hand-authored + bypassPermissions -> deny"   deny Edit "$ROOT/files/tokens.css" "$SID" bypassPermissions claude-desktop
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"; touch -t 202501010000 "$ROOT/state/$SID.sentinel"
run "idle sentinel refreshed -> still gates"      ask  Edit "$ROOT/files/tokens.css" "$SID" auto claude-desktop
[ -f "$ROOT/state/$SID.sentinel" ] && { pass=$((pass+1)); echo "PASS  idle sentinel survived (refresh-on-match)"; } || { fail=$((fail+1)); echo "FAIL  idle sentinel reaped"; }
reset; arm "$SID"; printf 'hand\n' > "$ROOT/files/tokens.css"
run "MultiEdit hand-authored + desktop -> ask"    ask  MultiEdit "$ROOT/files/tokens.css" "$SID" auto claude-desktop

echo "=== $pass passed, $fail failed ==="
[ $fail -eq 0 ]
