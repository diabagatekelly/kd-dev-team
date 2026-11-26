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
# The page reader is in the plugin's research folder, beside this script's own.
PAGE="python3 \"$(cd "$(dirname "$0")" && pwd)/../research/page.py\""
# The script that draws a slice's questions is beside it.
QUESTIONS="python3 \"$(cd "$(dirname "$0")" && pwd)/../questions/questions.py\""
# And the one that says which questions no answer settles yet, and draws the answers.
ANSWERS="python3 \"$(cd "$(dirname "$0")" && pwd)/../answers/answers.py\""
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

# One line per stage, in pipeline order (decision 36): its name, then the document that shows it
# was done. A document is found by its name; the number before it is its place in the order the
# folder's documents were made. The slice stage has two: the set of slices, then the chosen
# slice's own, in the folder of that slice's number in the set. Every stage after it is read there.
stages() {
  cat <<'STAGES'
problem|problem.md
scope map|scope-map*.md
requirements|requirements.md
the set of slices|slices*.md
slice|SLICE/slice.md
approach|SLICE/approach.md
research|SLICE/research/
questions|SLICE/questions/
security|SLICE/security.md
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

# What the chosen slice's own document says it needs from outside: "none" where the first line
# under that heading is the word alone, "some" for anything else, nothing where it has no such heading.
NEEDS='
/^#+[ \t]/ { inside = tolower($0) ~ /needs? from outside/; next }
inside && !said { line = $0; gsub(/[`*_ \t\r]/, "", line); if (line == "") next; said = 1; print (tolower(line) ~ /^none\.?$/ ? "none" : "some") }'

# What the requirements list says of outside systems and lasting things: "none" where the first
# line under that heading is the word alone, "some" for anything else, nothing where it does not say.
INVENTORY='
/^#+[ \t]/ { inside = tolower($0) ~ /outside systems and lasting things/; next }
inside && !said { line = $0; gsub(/[`*_ \t\r]/, "", line); if (line == "") next; said = 1; print (tolower(line) ~ /^none\.?$/ ? "none" : "some") }'

# The approach, counted (its condition 19). Lines that start with "@" are for this script: how many
# needs still wait for the user, how many decisions commit to something, how many things "Committed
# to" lists. The rest is the list research starts from: a line a thing, with the document it gets.
APPROACH='
function trim(s) { gsub(/^[ \t\r]+|[ \t\r.]+$/, "", s); return s }
/^#+[ \t]/ { inside = tolower($0) ~ /committed to/; next }
{ line = $0; gsub(/[`*]/, "", line); line = trim(line) }
tolower(line) ~ /^decision:/ {
  sub(/^[^:]*:[ \t]*/, "", line); low = tolower(line)
  if (low ~ /^waiting/) waiting++; else if (low ~ /^(committed|fixed by a limit)/) commits++
  next
}
inside && $0 ~ /^[ \t]*[-*][ \t]/ {
  sub(/^[-*][ \t]+/, "", line); if (tolower(line) ~ /^(none|nothing)$/) next
  name = line; address = "no address given"; need = ""
  if (match(line, /https?:\/\/[^ \t,)>]+/)) address = substr(line, RSTART, RLENGTH)
  if (match(line, /:[ \t]/)) name = substr(line, 1, RSTART - 1)
  if (match(line, /,? for /)) need = trim(substr(line, RSTART + RLENGTH))
  file = tolower(name); gsub(/[^a-z0-9]+/, "-", file); gsub(/^-|-$/, "", file)
  listed++; printf "  - %s%s (its documentation: %s; its document: @RESEARCH@%s.md)\n", name, (need == "" ? "" : ", for " need), address, file
}
END { print "@waiting " waiting + 0; print "@commits " commits + 0; print "@listed " listed + 0 }'

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

# The set of slices, counted (the slice stage's condition 22), and whether a coming-back is due
# (its conditions 14 and 15). Read, in this order: the requirements; every earlier version of the
# set; the set; each slice's own document; what the tracker says of merged work and open issues.
# Lines that start with "@" are for this script; the rest are the report's.
LEDGER='
function trim(s) { gsub(/^[ \t\r]+|[ \t\r]+$/, "", s); return s }
function plain(s) { gsub(/[`*]/, "", s); return trim(s) }
function slug(s) { s = plain(s); return match(s, /^[a-z0-9]+(-[a-z0-9]+)*/) ? substr(s, 1, RLENGTH) : "" }
function criterion(s) { s = plain(s); sub(/:$/, "", s); gsub(/[ \t]*\/[ \t]*/, " / ", s); return trim(s) }
function add(list, more, sep) { return list (list == "" ? "" : sep) more }
function due_line(text) { due = due "  - " text "\n" }
kind == "requirements" {
  # A question still open under "Not yet confirmed": a line of a list that starts at the margin.
  if ($0 ~ /^#+[ \t]/) { unconfirmed = tolower($0) ~ /not yet confirmed/; next }
  if (unconfirmed && $0 ~ /^([-*]|[0-9]+[.)])[ \t]/) questions++
  if ($0 !~ /^[ \t]*[-*] \[[ xX]\]/) next
  line = $0; sub(/^[ \t]*[-*] \[/, "", line); done = substr(line, 1, 1) != " "
  name = slug(substr(line, 3))
  if (name != "" && !(name in item)) { item[name] = 1; checked[name] = done; items[++items_n] = name }
  next
}
kind == "earlier" || kind == "set" {
  line = $0
  while (match(line, /#[0-9]+/)) { placed[substr(line, RSTART + 1, RLENGTH - 1) + 0] = 1; line = substr(line, RSTART + RLENGTH) }
  if (kind == "earlier" || $0 !~ /^[ \t]*\|/) next
  n = split($0, cell, "|")
  for (i = 1; i <= n; i++) cell[i] = plain(cell[i])
  if (!table) {
    c_number = c_items = c_state = 0
    for (i = 2; i <= n; i++) {
      low = tolower(cell[i])
      if (low == "#") c_number = i; else if (low ~ /^items?$/) c_items = i; else if (low ~ /^state$/) c_state = i
    }
    if (c_number && c_items && c_state) table = 1
    next
  }
  if (cell[c_number] !~ /^[0-9]+$/) next
  s = cell[c_number] + 0; rows[++rows_n] = s; low = tolower(cell[c_state])
  if (low ~ /^built/) { state[s] = "built"; built_n++ }
  else if (low ~ /^chosen/) { state[s] = "chosen"; chosen_n++; chosen_all = add(chosen_all, "slice " s, ", "); if (!chosen) chosen = s }
  else if (low ~ /^open/) { state[s] = "open"; open_n++ }
  else { state[s] = "?"; unknown = add(unknown, "slice " s, ", ") }
  m = split(cell[c_items], each, ",")
  for (i = 1; i <= m; i++) {
    name = slug(each[i]); if (name == "") continue
    covers[name] = add(covers[name], s, " ")
    if (!(name in item)) stray = add(stray, name " (slice " s ")", ", ")
  }
  next
}
kind == "slice" {
  if ($0 ~ /^#+[ \t]/) { criteria = tolower($0) ~ /criteri/; next }
  if (!criteria || $0 !~ /^[ \t]*[-*] (\[[ xX]\] )?\*\*/) next
  line = $0; sub(/^[^*]*\*\*/, "", line); id = criterion(substr(line, 1, index(line, "**") - 1))
  number += 0; holds[number, id] = 1; held[number] = add(held[number], id, "\t"); held_n[number]++
  name = id; sub(/ \/ .*$/, "", name)
  if (!(name in item)) nameless[number] = add(nameless[number], "line " FNR, ", ")
  next
}
kind == "work" {
  n = split($0, field, "\t")
  if (field[1] == "issue") { issues[++issues_n] = field[2] + 0; title[field[2] + 0] = field[3]; next }
  if (field[1] != "merged") next
  names = trim(field[3]); s = chosen
  if (match(tolower(names), /^slice[ \t]*[0-9]+[ \t]*:/)) {
    s = substr(names, 1, RLENGTH); gsub(/[^0-9]/, "", s); s += 0; names = substr(names, RLENGTH + 1)
  }
  m = split(names, each, ",")
  for (i = 1; i <= m; i++) {
    id = criterion(each[i]); if (id == "") continue
    if (id !~ / \/ /) { if (id in item) outright[id] = add(outright[id], "#" field[2], ", "); else lost = add(lost, id " (#" field[2] ")", ", "); continue }
    if (s != "" && (s, id) in holds) { named[s, id] = 1; if (index(", " by[s] ",", ", #" field[2] ",") == 0) by[s] = add(by[s], "#" field[2], ", ") }
    else lost = add(lost, id (s == "" ? "" : " of slice " s) " (#" field[2] ")", ", ")
  }
  next
}
END {
  if (!table) {
    print "- the set of slices (" set ") has no table this script can read: its columns are # | Slice | Items | Builds on | State"
    print "@table 0"; exit
  }
  printf "- slices (%s): %d %s, %d built, %d chosen, %d open\n", set, rows_n, (rows_n == 1 ? "slice" : "slices"), built_n, chosen_n, open_n
  if (unknown != "") print "- a slice whose state is not built, chosen or open: " unknown
  if (chosen_n > 1) print "- more than one slice is chosen: " chosen_all " (the first is read)"
  for (i = 1; i <= items_n; i++) if (!(items[i] in covers)) homeless = add(homeless, items[i], ", ")
  if (homeless != "") print "- a requirement in no slice: " homeless
  if (stray != "") print "- a slice names an item the requirements do not hold: " stray
  if (chosen && held_n[chosen]) {
    printf "- slice %d (%s): %d %s\n", chosen, document, held_n[chosen], (held_n[chosen] == 1 ? "criterion" : "criteria")
    if (nameless[chosen] != "") print "- a criterion that names no item of the requirements: " nameless[chosen]
  }
  # What merged work builds: a slice, when every criterion of its document is named.
  for (r = 1; r <= rows_n; r++) {
    s = rows[r]; now[s] = state[s]; if (state[s] == "built" || !held_n[s]) continue
    n = split(held[s], each, "\t"); got = 0; missing = ""
    for (i = 1; i <= n; i++) if ((s, each[i]) in named) got++; else missing = add(missing, each[i], ", ")
    if (got == n) { now[s] = "built"; any_built = 1; due_line("slice " s " is built by merged work (" sorted(by[s]) "): mark it built in " folder "/" set) }
    else if (got) print "- merged work (" sorted(by[s]) ") names " got " of the " n " criteria of slice " s ": not built yet, so nothing is marked or checked for it; still to come: " missing
  }
  if (lost != "") print "- merged work names what no slice\047s document holds: " lost
  all_built = rows_n > 0; all_marked = rows_n > 0
  for (r = 1; r <= rows_n; r++) { if (now[rows[r]] != "built") all_built = 0; if (state[rows[r]] != "built") all_marked = 0; else any_built = 1 }
  all_checked = 1; were_checked = 1
  for (i = 1; i <= items_n; i++) {
    name = items[i]; if (checked[name]) continue
    were_checked = 0
    n = split(covers[name], each, " "); whole = n > 0
    for (j = 1; j <= n; j++) if (now[each[j]] != "built") whole = 0
    if (whole) due_line("every slice of " name " is built: check its box in " folder "/" list)
    else if (name in outright) due_line("merged work names " name " as complete (" outright[name] "): check its box in " folder "/" list)
    else all_checked = 0
  }
  for (i = 1; i <= issues_n; i++) if (!(issues[i] in placed)) waiting = add(waiting, "#" issues[i] " \"" title[issues[i]] "\"", ", ")
  if (waiting != "") due_line("open issues not placed yet (each is placed, by its number, in " folder "/" set "): " waiting)
  if (due != "") {
    if (all_built && all_checked && !(all_marked && were_checked)) {
      if (questions) due_line("with those, every slice cut so far is built, and " questions (questions == 1 ? " question" : " questions") " of the list " (questions == 1 ? "is" : "are") " not yet confirmed: the activity is not done, and the requirements stage takes them next")
      else due_line("with those, every slice is built and every requirement checked: the activity is done")
    }
    printf "- a coming-back to the slices is due:\n%s", due
  }
  print "@table 1"; print "@chosen " chosen; print "@open " open_n + 0; print "@due " (due != "")
  print "@built " any_built + 0; print "@done " (all_marked && were_checked && items_n > 0); print "@unchecked " unchecked(); print "@questions " questions + 0
}
function unchecked(    i, n) { for (i = 1; i <= items_n; i++) if (!checked[items[i]]) n++; return n + 0 }
# "#13, #12" as "#12, #13": the pull requests in the order they were opened.
function sorted(list,    n, each, i, j, t) {
  n = split(list, each, ", ")
  for (i = 2; i <= n; i++) for (j = i; j > 1 && substr(each[j], 2) + 0 < substr(each[j - 1], 2) + 0; j--) { t = each[j]; each[j] = each[j - 1]; each[j - 1] = t }
  list = ""; for (i = 1; i <= n; i++) list = add(list, each[i], ", ")
  return list
}'

# What the ledger says of one thing this script needs, from its "@" lines.
told() { printf '%s\n' "$ledger" | awk -v key="@$1" '$1 == key { print $2 }'; }

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
  if [ ! -d "$dir" ]; then
    say "- planning folder: $folder (chosen earlier for this project) no longer exists"
    say "- to record the folder the user names (it is made if it is not there): $SELF remember FOLDER"
    say "  then read the documents again: $SELF report"
    return 0
  fi
  say "- planning folder: $folder (chosen earlier for this project)"
  number=$(next_number)
  list=$(numbered "$dir" "requirements.md")
  set=$(numbered "$dir" "slices*.md")
  ledger=""; chosen=""; slice=""
  if [ -n "$set" ]; then
    # The tracker is asked only once there is a set: nothing is checked off or placed before it.
    work=$(sh "$(dirname "$0")/tracker.sh" work 2>/dev/null) && unread="" || unread=yes
    [ -z "$unread" ] || work=""
    set -- kind=requirements
    [ -z "$list" ] || set -- "$@" "$dir/$list"
    set -- "$@" kind=earlier
    for earlier in $(cd "$dir" && ls -d [0-9][0-9][0-9]_slices*.md 2>/dev/null | sort); do
      [ "$earlier" = "$set" ] || set -- "$@" "$dir/$earlier"
    done
    set -- "$@" kind=set "$dir/$set" kind=slice
    for each in $(cd "$dir" && ls -d slice-[0-9]* 2>/dev/null | sort); do
      own=$(numbered "$dir/$each" "slice.md")
      [ -z "$own" ] || set -- "$@" "number=${each#slice-}" "$dir/$each/$own"
    done
    # The chosen slice is known only once the set is read: its document is named afterwards.
    ledger=$(printf '%s\n' "$work" | awk -v set="$set" -v list="$list" -v folder="$folder" -v document="@DOCUMENT@" "$LEDGER" "$@" kind=work -) \
      && [ -n "$ledger" ] || refuse "the set of slices ($folder/$set) could not be read by this script"
    chosen=$(told chosen)
    [ -z "$chosen" ] || slice=$(printf 'slice-%03d' "$chosen")
  else
    slice=$(cd "$dir" && ls -d slice-[0-9]* 2>/dev/null | sort | tail -1)
    slice=${slice:-slice-001}
  fi
  found=""; missing=""; next=""; disorder=""; needs=""; approach=""; counted=""; skipped=""; research=""
  rfolder=""; stale=""; qfolder=""; qstate=""; adone=""
  own=""; [ -z "$slice" ] || own=$(numbered "$dir/$slice" "slice.md")
  [ -z "$own" ] || needs=$(awk "$NEEDS" "$dir/$slice/$own")
  while IFS='|' read -r name document; do
    case "$document" in
      SLICE/*) [ -n "$slice" ] || continue; under="$slice/"; document=${document#SLICE/} ;;
      *) under="" ;;
    esac
    is=$(numbered "$dir/$under" "${document%/}")
    case "$document" in
      */) [ -n "$is" ] && [ -n "$(ls "$dir/$under$is" 2>/dev/null)" ] && there=yes || there=no; is="$is/" ;;
      *) [ -n "$is" ] && there=yes || there=no ;;
    esac
    case "$name" in
      approach)
        if [ "$there" = yes ]; then
          approach="$under$is"
          counted=$(awk "$APPROACH" "$dir/$approach")
          # A need the user has not decided keeps the approach as the next stage, in the same document.
          if [ "$(say "$counted" | awk '$1 == "@waiting" { print $2 }')" != 0 ]; then
            missing="${missing:+$missing, }$name"
            [ -n "$next" ] || next="approach (its document: $folder/$approach, corrected in place: $(say "$counted" | awk '$1 == "@waiting" { print $2 }') of its needs still waiting for the user's decision)"
            continue
          fi
        elif [ "$needs" = none ]; then
          # Nothing to compare and nothing to commit to: the stage is not done and not missing.
          skipped="- approach: not needed, slice ${chosen:-${slice#slice-}} needs nothing from outside ($under$own)"
          continue
        fi ;;
      research)
        # Research, counted (its condition 17): a document a thing committed to, under the name the
        # approach's list gives it, and the states of the lasting things unless the requirements name none.
        # The folder is the one already there, written in or not; research is written from once it holds something.
        [ -z "${is%/}" ] || rfolder="$under${is%/}"
        [ "$there" = yes ] && research="$under$is"
        wanted=$(say "$counted" | grep -v '^@' | sed 's|.*@RESEARCH@\(.*\))$|\1|')
        inventory=""; [ -z "$list" ] || inventory=$(awk "$INVENTORY" "$dir/$list")
        [ "$inventory" = none ] || wanted="$wanted states.md"
        owed=""
        for file in $wanted; do
          [ -n "$rfolder" ] && [ -f "$dir/$rfolder/$file" ] || owed="${owed:+$owed, }$file"
        done
        if [ -n "$rfolder" ]; then
          for file in $(cd "$dir/$rfolder" && ls *.md 2>/dev/null); do
            case " $(say $wanted) " in *" $file "*) ;; *) [ "$file" = states.md ] || stale="$stale $file" ;; esac
          done
        fi
        if [ -z "$(say $wanted)" ]; then
          skipped="${skipped:+$skipped
}- research: not needed, nothing is committed to and the requirements name no lasting thing ($list)"
          continue
        elif [ -n "$owed" ]; then
          missing="${missing:+$missing, }$name"
          if [ -n "$research" ]; then
            [ -n "$next" ] || next="research (its document: $folder/$rfolder/, still to write there: $owed)"
          elif [ -n "$rfolder" ]; then
            [ -n "$next" ] || next="research (its document: $folder/$rfolder/, to write there: $owed)"
          else
            [ -n "$next" ] || next="research (its document: $folder/$under${number}_research/, to write there: $owed)"
          fi
          continue
        fi
        there=yes ;;
      questions)
        # The questions, counted: kept.md is the session's (or skipped.md, the user's word), and
        # questions.md is drawn from it by script. They are done only while the drawing carries the
        # mark of the documents as they stand: the slice, the approach, research, and kept.md.
        [ -z "${is%/}" ] || qfolder="$under${is%/}"
        qstate=none; sstate=none; basis=kept.md
        [ -z "$qfolder" ] || [ -f "$dir/$qfolder/kept.md" ] || basis=skipped.md
        if [ -n "$qfolder" ] && [ -f "$dir/$qfolder/$basis" ]; then
          qstate=kept
          if [ -f "$dir/$qfolder/questions.md" ]; then
            # The security pass writes security.md beside it, and the questions are drawn again with
            # it: the mark is then of that file too, after the others.
            marked() { (cd "$dir" && { cat "$slice/$own"; [ -z "$approach" ] || cat "$approach"
                      [ -z "$rfolder" ] || for file in $(cd "$rfolder" && LC_ALL=C ls *.md 2>/dev/null); do cat "$rfolder/$file"; done
                      cat "$qfolder/$basis"; [ -z "$1" ] || cat "$qfolder/security.md"; }) 2>/dev/null | cksum | awk '{ print $1 }'; }
            qstate=stale
            if grep -q "drawn from: $(marked "") " "$dir/$qfolder/questions.md"; then
              qstate=drawn; [ ! -f "$dir/$qfolder/security.md" ] || sstate=written
            elif [ -f "$dir/$qfolder/security.md" ] && grep -q "drawn from: $(marked with) " "$dir/$qfolder/questions.md"; then
              qstate=drawn; sstate=drawn
            fi
          fi
        fi
        if [ "$qstate" = drawn ]; then
          there=yes
          [ "$basis" = kept.md ] || skipped="${skipped:+$skipped
}- questions: skipped at the user's word ($qfolder/skipped.md); what needs no judgement is drawn, and the skipping is for the owner's list"
        else
          missing="${missing:+$missing, }$name"
          at="$folder/${qfolder:-$under${number}_questions}/"
          case "$qstate" in
            none) owes="to write there: kept.md; questions.md is then drawn from it" ;;
            kept) owes="$basis is written there; questions.md is still to be drawn from it" ;;
            *) owes="to draw again: a document of the slice, or $basis, changed after questions.md was drawn; kept.md is looked at again only for what the change brings or removes" ;;
          esac
          [ -n "$next" ] || next="questions (its document: $at, $owes)"
          continue
        fi ;;
      security)
        # The security pass, counted: security.md beside kept.md, and the questions drawn again
        # with it. Nothing is said of it before the questions are drawn.
        if [ "${qstate:-none}" = drawn ] && [ "$sstate" = drawn ]; then
          found="${found:+$found, }security ($qfolder/security.md)"
          ! grep -qi "^skipped at the user's word" "$dir/$qfolder/security.md" || skipped="${skipped:+$skipped
}- security: skipped at the user's word ($qfolder/security.md); every fixed question is drawn, and the skipping is for the owner's list"
        else
          missing="${missing:+$missing, }$name"
          if [ "${qstate:-none}" = drawn ] && [ -z "$next" ]; then
            [ "$sstate" = written ] && owes="security.md is written there; the questions are still to be drawn again with it" \
              || owes="to write there: security.md; the questions are then drawn again with it"
            next="security (its document: $folder/$qfolder/security.md, $owes)"
          fi
        fi
        continue ;;
      answers)
        # The answers, counted: answers.md is the session's, and answered.md is drawn from it by
        # script once every question is settled. They are done only while that drawing carries the
        # mark of the questions and the answers as they stand.
        if [ "$there" = yes ]; then
          answered="$under${is%_answers.md}_answered.md"
          if [ -f "$dir/$answered" ] && grep -q "drawn from: $( (cat "$dir/$qfolder/questions.md" "$dir/$under$is") 2>/dev/null | cksum | awk '{ print $1 }') " "$dir/$answered"; then
            found="${found:+$found, }answers ($under$is)"
            adone="$under$is"
            continue
          fi
          [ -f "$dir/$answered" ] && owes="to draw again: the questions or the answers changed after $answered was drawn; only what the change brings is answered" \
            || owes="written in, and not yet drawn: the questions no answer settles are still to answer"
          missing="${missing:+$missing, }$name"
          [ -n "$next" ] || next="answers (its document: $folder/$under$is, $owes)"
          continue
        fi ;;
    esac
    if [ "$there" = yes ]; then
      found="${found:+$found, }$name ($under$is)"
      [ -z "$missing" ] || disorder="${disorder}- out of order: $name ($under$is) exists but nothing was found for: $missing
"
    else
      missing="${missing:+$missing, }$name"
      [ -z "$next" ] || continue
      case "$name" in
        "the set of slices")
          next="slice (its document: $folder/${number}_slices.md, the set of slices; once the user has chosen one, its own document: $folder/slice-NNN/$(say "$number" | awk '{ printf "%03d", $1 + 1 }')_slice.md, NNN the slice's number in the set)" ;;
        slice) next="slice (its document: $folder/$under${number}_slice.md${chosen:+, the criteria of slice $chosen})" ;;
        *) next="$name (its document: $folder/$under${number}_$(say "$document" | sed 's/\*//'))" ;;
      esac
    fi
  done <<STAGES
$(stages)
STAGES
  say "- after a stage is finished, read the documents again: $SELF report"
  say "- a file of the user's (a sheet, an export) is never opened here: the user runs, in a terminal on their own"
  say "  machine, this plugin's \`sh startup/source.sh describe FILE\`, and pastes what it prints"
  say "- found: ${found:-no planning document}"
  [ -z "$list" ] || count "$dir/$list" "$list"
  if [ -n "$ledger" ]; then
    own=""; [ -z "$slice" ] || own=$(numbered "$dir/$slice" "slice.md")
    printf '%s\n' "$ledger" | grep -v '^@' | sed "s|@DOCUMENT@|$slice/$own|"
    [ -z "$unread" ] || say "- whether a coming-back to the slices is due is not known: the tracker could not be read"
    if [ "$(told table)" = 1 ]; then
      if [ "$(told built)" = 1 ]; then
        versions=$(cd "$dir" && ls -d [0-9][0-9][0-9]_slices*.md 2>/dev/null | wc -l)
        say "- a changed set is a new document, the earlier one left as it is: $folder/${number}_slices-v$(printf '%03d' $((versions + 1))).md"
      else
        say "- a changed set is corrected in place ($folder/$set): no slice is built from it yet"
      fi
    fi
  fi
  [ -z "$disorder" ] || printf '%s' "$disorder"
  if [ -n "$ledger" ] && [ -z "$missing" ] || { [ -n "$ledger" ] && [ -z "$chosen" ]; } || [ "$(told due)" = 1 ]; then
    # Past the set, what comes next is the set's to say before the documents'.
    if [ "$(told table)" = 0 ]; then
      say "- next stage by the documents: slice (the set is to be written as that table, in $folder/$set)"; return 0
    elif [ "$(told due)" = 1 ]; then
      say "- next stage by the documents: slice, the coming-back (before anything else is planned)"; return 0
    elif [ "$(told done)" = 1 ] && [ "$(told questions)" != 0 ]; then
      say "- next stage by the documents: requirements (every slice cut so far is built, and $(told questions) questions of $folder/$list are not yet confirmed: their answers may add to the list, and the activity is not done before them)"; return 0
    elif [ "$(told done)" = 1 ]; then
      say "- next stage by the documents: none: every slice of this activity is built and every requirement checked; which row of the scope map is the next \"now\" is the user's to say"; return 0
    elif [ -z "$chosen" ] && [ "$(told open)" != 0 ]; then
      say "- next stage by the documents: slice (the user chooses where to start; the chosen slice's own document: $folder/slice-NNN/${number}_slice.md, NNN its number in the set)"; return 0
    elif [ -z "$chosen" ]; then
      say "- next stage by the documents: slice (every slice of the set is built and $(told unchecked) of the requirements are not checked: the set does not cover the list)"; return 0
    fi
  fi
  [ -z "$skipped" ] || say "$skipped"
  if [ -n "$approach" ]; then
    commits=$(say "$counted" | awk '$1 == "@commits" { print $2 }'); listed=$(say "$counted" | awk '$1 == "@listed" { print $2 }')
    [ "$commits" = "$listed" ] || say "- the decisions of $approach commit to $commits and its \"Committed to\" lists $listed: research starts from that list, so the two must agree"
    if [ -n "$research" ]; then
      say "- a changed approach is a new document, the earlier one left as it is: $folder/$slice/${number}_approach.md"
      for file in $stale; do
        say "- no longer stands, its thing is not committed to in $approach: $folder/$rfolder/$file (it is left as it is, but for a first line to be added that says so)"
      done
    else
      say "- a changed approach is corrected in place ($folder/$approach): no research is written from it yet"
    fi
  fi
  case "$next" in
    research*)
      if [ -n "$approach" ] && [ "$listed" != 0 ]; then
        say "- to research, committed to in $folder/$approach:"
        say "$counted" | grep -v '^@' | sed "s|@RESEARCH@|$folder/${rfolder:-$slice/${number}_research}/|"
      elif [ -n "$approach" ]; then
        say "- nothing is committed to in $folder/$approach: no outside system is researched"
      fi ;;
  esac
  case "$next" in
    approach*|research*|answers*)
      say "- a page of documentation is read with: $PAGE fetch URL --to $folder/$slice/pages"
      say "  and every quote written from one is then looked for in its saved page: $PAGE check $folder/$slice/pages DOCUMENT"
      kept=$(ls "$dir/$slice/pages"/*.txt 2>/dev/null | wc -l | tr -d ' ')
      [ "$kept" = 0 ] || say "- $kept pages are already kept in $folder/$slice/pages, read from their copies: $PAGE kept $folder/$slice/pages" ;;
  esac
  case "$next" in
    security*)
      say "- what kept.md lists and the documents name: $QUESTIONS things $folder/$slice"
      say "  the questions are drawn again with security.md by script, never written by hand: $QUESTIONS draw $folder/$slice" ;;
    answers*)
      say "- the questions no answer settles yet, sixty at a time: $ANSWERS next $folder/$slice"
      say "  what the answers still need looked up in the research, together: $ANSWERS lookups $folder/$slice"
      say "  the answers are checked and drawn by script once none is left: $ANSWERS draw $folder/$slice" ;;
    questions*)
      say "- what a question may apply to, and the library's kinds: $QUESTIONS things $folder/$slice"
      say "  the questions of a kind, every kind read, four or five at a time: $QUESTIONS library KIND KIND ..."
      say "  the questions are drawn from kept.md by script, never written by hand: $QUESTIONS draw $folder/$slice" ;;
    *)
      # The answers stay the place a decision of the owner's is recorded, whatever stage is next.
      [ -z "$adone" ] || say "- a decision the owner takes on their list is recorded in $folder/$adone, and the answers drawn again: $ANSWERS draw $folder/$slice" ;;
  esac
  if [ -n "$next" ]; then say "- next stage by the documents: $next"; return 0; fi
  # A slice fully planned goes to the build; it is built when merged work names its criteria.
  say "- every planning document of slice ${chosen:-${slice#slice-}} exists"
  say "- next stage by the documents: none, slice ${chosen:-${slice#slice-}} is planned and ready to build"
}

case "${1:-}" in
  report) report ;;
  remember) remember "${2:-}" ;;
  *) sed -n '4,6p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
