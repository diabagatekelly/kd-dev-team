#!/bin/sh
# Which planning stage comes next, by the documents that exist in the project's planning folder.
#
#   stage.sh report            print the folder, the documents found and the next stage; changes nothing
#   stage.sh remember FOLDER   record FOLDER as this project's planning folder (asked once per project)
#
# The folder is remembered outside the project, in the plugin's own data folder, keyed by the
# project's root. Exit 3 with a line starting "REFUSED" when it cannot go on.
set -u

say() { printf '%s\n' "$*"; }
refuse() { say "- REFUSED: $*"; exit 3; }

root=$(git rev-parse --show-toplevel 2>/dev/null) || root=$(pwd -P)
store="${CLAUDE_PLUGIN_DATA:-$HOME/.kd-dev-team}/planning-folders"

inside() { case "$1" in /*|[A-Za-z]:*) say "$1" ;; *) say "$root/$1" ;; esac; }

remember() {
  [ -n "${1:-}" ] || refuse "no folder was named"
  [ -d "$(inside "$1")" ] || refuse "the folder $1 does not exist in $root"
  mkdir -p "$(dirname "$store")" || refuse "cannot write to $(dirname "$store")"
  [ -f "$store" ] || : > "$store"
  awk -F'\t' -v r="$root" '$1 != r' "$store" > "$store.new" && printf '%s\t%s\n' "$root" "$1" >> "$store.new" \
    && mv "$store.new" "$store" || refuse "cannot write to $store"
  say "- planning folder: $1 (recorded for $root)"
}

# One line per stage, in pipeline order: its name, then the document that shows it was done.
# A stage from "slice" on is read in the latest slice's folder.
stages() {
  cat <<'STAGES'
problem|problem.md
scope|scope.md
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

report() {
  folder=""
  [ -f "$store" ] && folder=$(awk -F'\t' -v r="$root" '$1 == r {print $2}' "$store" | tail -1)
  if [ -z "$folder" ]; then say "- planning folder: not chosen yet for this project"; return 0; fi
  dir=$(inside "$folder")
  if [ ! -d "$dir" ]; then say "- planning folder: $folder (chosen earlier for this project) no longer exists"; return 0; fi
  say "- planning folder: $folder (chosen earlier for this project)"
  slice=$(cd "$dir" && ls -d slice-[0-9]* 2>/dev/null | sort | tail -1)
  slice=${slice:-slice-001}
  found=""; missing=""; next=""; disorder=""
  while IFS='|' read -r name document; do
    case "$document" in SLICE/*) document="$slice/${document#SLICE/}" ;; esac
    case "$document" in
      */) [ -n "$(ls "$dir/$document" 2>/dev/null)" ] && there=yes || there=no ;;
      *) [ -f "$dir/$document" ] && there=yes || there=no ;;
    esac
    if [ "$there" = yes ]; then
      found="${found:+$found, }$name ($document)"
      [ -z "$missing" ] || disorder="${disorder}- out of order: $name ($document) exists but nothing was found for: $missing
"
    else
      missing="${missing:+$missing, }$name"
      [ -n "$next" ] || next=$name
    fi
  done <<STAGES
$(stages)
STAGES
  say "- found: ${found:-no planning document}"
  [ -z "$disorder" ] || printf '%s' "$disorder"
  say "- next stage by the documents: ${next:-none left: every planning document of $slice exists}"
}

case "${1:-}" in
  report) report ;;
  remember) remember "${2:-}" ;;
  *) sed -n '4,5p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
