#!/bin/sh
# Which planning stage comes next, by the documents that exist in the project's planning folder.
#
#   stage.sh report            print the folder, the documents found and the next stage; changes nothing
#   stage.sh remember FOLDER   record FOLDER, inside the project, as its planning folder (asked once per
#                              project); the folder is made if it is not there
#
# The folder is remembered outside the project, in the plugin's own data folder, keyed by the
# project's root. Exit 3 with a line starting "REFUSED" when it cannot go on.
set -u

say() { printf '%s\n' "$*"; }
refuse() { say "- REFUSED: $*"; exit 3; }

root=$(git rev-parse --show-toplevel 2>/dev/null) || root=$(pwd -P)
# A session runs the commands this script prints in a shell of its own, which is not told where the
# plugin keeps its data: each printed command carries it.
SELF="sh \"$(cd "$(dirname "$0")" && pwd)/stage.sh\""
[ -z "${CLAUDE_PLUGIN_DATA:-}" ] || SELF="CLAUDE_PLUGIN_DATA=\"$CLAUDE_PLUGIN_DATA\" $SELF"
store="${CLAUDE_PLUGIN_DATA:-$HOME/.kd-dev-team}/planning-folders"

inside() { case "$1" in /*|[A-Za-z]:*) say "$1" ;; *) say "$root/$1" ;; esac; }

remember() {
  [ -n "${1:-}" ] || refuse "no folder was named"
  # Given by its full path: the folder inside the project. Both paths are read the way this shell
  # writes them, since a full path on Windows may come as C:/... where the shell says /c/...
  case "$1" in /*|[A-Za-z]:*)
    above=$(cd "$(dirname "$1")" 2>/dev/null && pwd -P) && here=$(cd "$root" 2>/dev/null && pwd -P) || above=""
    case "${above:+$above/$(basename "$1")}" in "$here"/?*) full="$above/$(basename "$1")"; set -- "${full#"$here"/}" ;; esac ;;
  esac
  case "$1" in /*|[A-Za-z]:*|..|../*|*/..|*/../*) refuse "the planning folder is a folder inside the project: $1 is not" ;; esac
  mkdir -p "$(inside "$1")" || refuse "cannot make the folder $1 in $root"
  mkdir -p "$(dirname "$store")" || refuse "cannot write to $(dirname "$store")"
  [ -f "$store" ] || : > "$store"
  awk -F'\t' -v r="$root" '$1 != r' "$store" > "$store.new" && printf '%s\t%s\n' "$root" "$1" >> "$store.new" \
    && mv "$store.new" "$store" || refuse "cannot write to $store"
  say "- planning folder: $1 (recorded for $root)"
}

# One line per stage, in pipeline order: its name, then the document that shows it was done.
# A document is found by its name; the number before it is its place in the order the
# folder's documents were made. A stage from "slice" on is read in the latest slice's folder.
stages() {
  cat <<'STAGES'
problem|problem.md
scope map|scope-map*.md
requirements|requirements.md
research|research/
slice|SLICE/slice.md
questions|SLICE/questions.md
answers|SLICE/answers.md
tests of open facts|SLICE/open-facts.md
design|SLICE/design.md
screens|SLICE/screens.md
stack and repository|SLICE/stack.md
readiness|SLICE/readiness.md
the owner's list|SLICE/owner-list.md
STAGES
}

# The latest numbered entry of that name in a folder, or nothing.
numbered() { (cd "$1" 2>/dev/null && ls -d [0-9][0-9][0-9]_$2 2>/dev/null | sort | tail -1) | sed 's|/$||'; }

# The number the next document takes: one past the highest in the folder and its slices.
next_number() {
  (cd "$dir" && ls -d [0-9][0-9][0-9]_* slice-[0-9]*/[0-9][0-9][0-9]_* 2>/dev/null) \
    | sed 's|.*/||' | awk '{n = substr($0, 1, 3) + 0; if (n >= max) max = n + 1} END {printf "%03d\n", max}'
}

# The requirements as a list to check off (decision 23): how many items, how many checked, and
# any item the acceptance criteria could not point to. An item is a line "- [ ] **its-name**: ...".
count() {
  awk -v title="$2" '
    /^[ \t]*[-*] \[[ xX]\]/ {
      items++; line = $0; sub(/^[ \t]*[-*] \[/, "", line)
      if (substr(line, 1, 1) != " ") checked++
      rest = substr(line, 3); sub(/^[ \t]*/, "", rest); name = ""
      if (substr(rest, 1, 2) == "**") { rest = substr(rest, 3); end = index(rest, "**"); if (end > 1) name = substr(rest, 1, end - 1) }
      sub(/:$/, "", name)
      if (name !~ /^[a-z0-9]+(-[a-z0-9]+)*$/) nameless = nameless (nameless == "" ? "" : ", ") "line " NR
      else if (++seen[name] == 2) twice = twice (twice == "" ? "" : ", ") name
    }
    END {
      printf "- requirements (%s): %d items, %d checked\n", title, items, checked
      if (nameless != "") print "- a requirement with no short name of its own: " nameless
      if (twice != "") print "- a requirement\047s name used more than once: " twice
    }' "$1"
}

report() {
  folder=""
  [ -f "$store" ] && folder=$(awk -F'\t' -v r="$root" '$1 == r {print $2}' "$store" | tail -1)
  if [ -z "$folder" ]; then
    say "- planning folder: not chosen yet for this project"
    say "- to record the folder the user names (it is made if it is not there): $SELF remember FOLDER"
    say "  then read the documents again: $SELF report"
    return 0
  fi
  dir=$(inside "$folder")
  if [ ! -d "$dir" ]; then say "- planning folder: $folder (chosen earlier for this project) no longer exists"; return 0; fi
  say "- planning folder: $folder (chosen earlier for this project)"
  slice=$(cd "$dir" && ls -d slice-[0-9]* 2>/dev/null | sort | tail -1)
  slice=${slice:-slice-001}
  number=$(next_number)
  found=""; missing=""; next=""; disorder=""
  while IFS='|' read -r name document; do
    case "$document" in SLICE/*) under="$slice/"; document=${document#SLICE/} ;; *) under="" ;; esac
    is=$(numbered "$dir/$under" "${document%/}")
    case "$document" in
      */) [ -n "$is" ] && [ -n "$(ls "$dir/$under$is" 2>/dev/null)" ] && there=yes || there=no; is="$is/" ;;
      *) [ -n "$is" ] && there=yes || there=no ;;
    esac
    if [ "$there" = yes ]; then
      found="${found:+$found, }$name ($under$is)"
      [ -z "$missing" ] || disorder="${disorder}- out of order: $name ($under$is) exists but nothing was found for: $missing
"
    else
      missing="${missing:+$missing, }$name"
      [ -n "$next" ] || next="$name (its document: $folder/$under${number}_$(say "$document" | sed 's/\*//'))"
    fi
  done <<STAGES
$(stages)
STAGES
  say "- after a stage is finished, read the documents again: $SELF report"
  say "- a file of the user's (a sheet, an export) is never opened here: the user runs, in a terminal on their own"
  say "  machine, this plugin's \`sh startup/source.sh describe FILE\`, and pastes what it prints"
  say "- found: ${found:-no planning document}"
  list=$(numbered "$dir" "requirements.md")
  [ -z "$list" ] || count "$dir/$list" "$list"
  [ -z "$disorder" ] || printf '%s' "$disorder"
  if [ -n "$next" ]; then say "- next stage by the documents: $next"; return 0; fi
  # A slice fully planned goes to the build; whether it is done is decided at a check-in when
  # its work is merged (decision 23), which is not built yet.
  say "- every planning document of $slice exists"
  say "- next stage by the documents: none, $slice is planned and ready to build"
}

case "${1:-}" in
  report) report ;;
  remember) remember "${2:-}" ;;
  *) sed -n '4,6p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
