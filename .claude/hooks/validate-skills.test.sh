#!/usr/bin/env bash
# Unit tests for validate-skills.sh — drives every branch with fixture skills.
# Run: bash .claude/hooks/validate-skills.test.sh   (exit 0 = all pass)
# Harness adapted from hooks/write-guard.test.sh: different dir, asserts the
# hook's EXIT CODE (2=block / 0=allow) rather than JSON, sends a *command*
# payload, and writes real SKILL.md fixtures into a temp SKILLS_DIR.
HERE=$(cd "$(dirname "$0")" && pwd)
HOOK="$HERE/validate-skills.sh"
ROOT=$(mktemp -d)
pass=0; fail=0
trap 'rm -rf "$ROOT"' EXIT

payload() { printf '{"tool_input":{"command":"%s"}}' "$1"; }

newdir() { mktemp -d "$ROOT/skills.XXXXXX"; }

run() { # label expect-rc cmd skills_dir
  local label=$1 expect=$2 cmd=$3 dir=$4 rc
  printf '%s' "$(payload "$cmd")" | SKILLS_DIR="$dir" bash "$HOOK" >/dev/null 2>&1; rc=$?
  if [ "$rc" -eq "$expect" ]; then pass=$((pass+1)); printf 'PASS  %-52s -> rc=%s\n' "$label" "$rc"
  else fail=$((fail+1)); printf 'FAIL  %-52s -> got rc=%s want %s\n' "$label" "$rc" "$expect"; fi
}

echo "=== validate-skills.sh unit tests ==="

# valid set -> allow
D=$(newdir); mkdir -p "$D/a" "$D/b"
printf -- '---\nname: a\ndescription: A.\n---\nbody\n' > "$D/a/SKILL.md"
printf -- '---\nname: b\ndescription: B.\n---\nbody\n' > "$D/b/SKILL.md"
run "valid set -> allow" 0 "git commit -m x" "$D"

# empty dir -> allow (fail-open guard)
D=$(newdir)
run "empty skills dir -> allow (fail-open)" 0 "git commit -m x" "$D"

# missing line-1 fence -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '\n---\nname: a\ndescription: A.\n---\n' > "$D/a/SKILL.md"
run "no line-1 fence -> block" 2 "git commit -m x" "$D"

# name only in body, no frontmatter -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '# Title\nname: a\ndescription: A.\n' > "$D/a/SKILL.md"
run "name only in body, no frontmatter -> block" 2 "git commit -m x" "$D"

# opening fence, no closing fence -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '---\nname: a\ndescription: A.\nbody no closing fence\n' > "$D/a/SKILL.md"
run "opening fence, no closing fence -> block" 2 "git commit -m x" "$D"

# empty description -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '---\nname: a\ndescription: \n---\n' > "$D/a/SKILL.md"
run "empty description -> block" 2 "git commit -m x" "$D"

# name:value with no space -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '---\nname:a\ndescription: A.\n---\n' > "$D/a/SKILL.md"
run "name:value no space -> block" 2 "git commit -m x" "$D"

# leading tab in frontmatter -> block
D=$(newdir); mkdir -p "$D/a"
printf -- '---\nname: a\n\tdescription: A.\n---\n' > "$D/a/SKILL.md"
run "leading tab in frontmatter -> block" 2 "git commit -m x" "$D"

# duplicate name across two skills -> block
D=$(newdir); mkdir -p "$D/a" "$D/b"
printf -- '---\nname: dup\ndescription: A.\n---\n' > "$D/a/SKILL.md"
printf -- '---\nname: dup\ndescription: B.\n---\n' > "$D/b/SKILL.md"
run "duplicate name -> block" 2 "git commit -m x" "$D"

# non-commit command with bad fixtures present -> allow (scoping)
D=$(newdir); mkdir -p "$D/a"
printf -- 'garbage no frontmatter\n' > "$D/a/SKILL.md"
run "non-commit (ls) with bad fixture -> allow" 0 "ls -la" "$D"

echo "=== $pass passed, $fail failed ==="
[ $fail -eq 0 ]
