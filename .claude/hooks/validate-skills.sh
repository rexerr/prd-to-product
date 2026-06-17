#!/usr/bin/env bash
# Hook: Validate skill frontmatter before a commit.
# Reason: a SKILL.md with malformed frontmatter silently fails to load, and two
# skills sharing a `name` shadow each other. Prose in CLAUDE.md can't guarantee
# this; a hook can. Blocks `git commit` (exit 2) when any skills/*/SKILL.md is
# malformed. Crib C-27 / decision D-017.
#
# Scoping lives HERE, in the script (same pattern as block-env-commit.sh). The
# settings.json matcher is a bare "Bash", so this runs on EVERY Bash call and
# its exit-0 path is the common path. Do NOT add an `if` filter in settings.json.
#
# Mechanism: extract the command with jq when available, fall back to the raw
# payload otherwise (a blocking guard must never disarm because jq is missing).
# The commit match is anchored at command-word position so prose merely
# mentioning "git commit" does not trigger validation.
#
# Validation is STRUCTURAL + cheap-syntactic, NOT a full YAML parse (v1
# narrowing, D-017): line-1 `---` fence, a closing `---` fence, non-empty
# name:/description: inside the frontmatter block, name uniqueness,
# space-after-colon, and no leading tabs. Unbalanced quotes, bad nesting, and
# full YAML semantics are NOT validated.
#
# Known limitations: validates the working tree, not the staged blob (minor
# TOCTOU); gates the agent's commits, not manual terminal commits. Fails OPEN
# when no SKILL.md is found, so a missing skills/ never locks out commits.

payload=$(cat)

# --- Is this a git commit? Otherwise allow (the common path). ---
if command -v jq >/dev/null 2>&1; then
  cmd=$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null)
else
  cmd=$payload
fi
printf '%s' "$cmd" | grep -Eq '(^|[|&;])[[:space:]]*git[[:space:]]+commit' || exit 0

# --- Collect skill files; fail OPEN if none (commit-lockout guard). ---
SKILLS_DIR="${SKILLS_DIR:-${CLAUDE_PROJECT_DIR:-.}/skills}"
shopt -s nullglob
files=( "$SKILLS_DIR"/*/SKILL.md )
[ ${#files[@]} -eq 0 ] && exit 0

errors=()
names=()
namefiles=()
tab=$(printf '\t')

for f in "${files[@]}"; do
  # line 1 must be the opening fence
  if [ "$(sed -n '1p' "$f")" != "---" ]; then
    errors+=("$f — frontmatter must open with '---' on line 1")
    continue
  fi
  # closing fence = first '---' after line 1; block if there is none
  close=$(awk 'NR>1 && $0=="---"{print NR; exit}' "$f")
  if [ -z "$close" ]; then
    errors+=("$f — no closing '---' fence (frontmatter unterminated)")
    continue
  fi
  # frontmatter block = lines 2 .. close-1
  block=$(sed -n "2,$((close-1))p" "$f")

  # leading-tab indentation is invalid YAML
  if printf '%s\n' "$block" | grep -Eq "^${tab}"; then
    errors+=("$f — frontmatter uses leading tabs")
  fi

  # name: present, space after colon, non-empty, unique
  name_line=$(printf '%s\n' "$block" | grep -E '^name:' | head -1)
  if [ -z "$name_line" ]; then
    errors+=("$f — missing 'name:' in frontmatter")
  elif ! printf '%s' "$name_line" | grep -Eq '^name:[[:space:]]'; then
    errors+=("$f — 'name:' needs a space after the colon")
  else
    name_val=$(printf '%s' "$name_line" | sed -E 's/^name:[[:space:]]*//; s/[[:space:]]*$//')
    if [ -z "$name_val" ]; then
      errors+=("$f — 'name:' is empty")
    else
      dupfile=""
      i=0
      while [ $i -lt ${#names[@]} ]; do
        [ "${names[$i]}" = "$name_val" ] && { dupfile="${namefiles[$i]}"; break; }
        i=$((i+1))
      done
      if [ -n "$dupfile" ]; then
        errors+=("$f — duplicate name '$name_val' (also in $dupfile)")
      else
        names+=("$name_val")
        namefiles+=("$f")
      fi
    fi
  fi

  # description: present, space after colon, non-empty
  desc_line=$(printf '%s\n' "$block" | grep -E '^description:' | head -1)
  if [ -z "$desc_line" ]; then
    errors+=("$f — missing 'description:' in frontmatter")
  elif ! printf '%s' "$desc_line" | grep -Eq '^description:[[:space:]]'; then
    errors+=("$f — 'description:' needs a space after the colon")
  else
    desc_val=$(printf '%s' "$desc_line" | sed -E 's/^description:[[:space:]]*//; s/[[:space:]]*$//')
    [ -z "$desc_val" ] && errors+=("$f — 'description:' is empty")
  fi
done

if [ ${#errors[@]} -gt 0 ]; then
  {
    echo "BLOCKED: skill frontmatter validation failed (D-017). Fix before committing:"
    i=0
    while [ $i -lt ${#errors[@]} ]; do echo "  - ${errors[$i]}"; i=$((i+1)); done
  } >&2
  exit 2
fi
exit 0
