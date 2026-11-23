#!/bin/sh
# A file of the user's (a sheet, an export) stays on their own machine. This script is run there,
# by the user, outside the project's VM: it prints the file's shape and never a cell, and it finds
# where a value of the file has been written down, saying where and never what.
#
#   source.sh describe FILE        the file's columns, how many rows, what kind of cell each column holds
#   source.sh scan FILE FOLDER     each place in FOLDER where a value of FILE is written: the file, the line
#                                  and the column the value is from. Exit 1 when any is found.
#
# Reads delimited text (.csv, .tsv, .txt). Exit 3 with a line starting "REFUSED" when it cannot
# read the file: a file that could not be read is never reported as "nothing found".
set -u

say() { printf '%s\n' "$*"; }
refuse() { say "- REFUSED: $*"; exit 3; }

# Reads one delimited file. With mode=describe prints its shape; with mode=values prints, for every
# cell worth looking for, its column's name, a tab, and the cell in lower case.
READ='
function cells(line, out,    n, i, c, cell, quoted) {
  n = 0; cell = ""; quoted = 0
  for (i = 1; i <= length(line); i++) {
    c = substr(line, i, 1)
    if (quoted) {
      if (c != "\"") cell = cell c
      else if (substr(line, i + 1, 1) == "\"") { cell = cell "\""; i++ }
      else quoted = 0
    } else if (c == "\"") quoted = 1
    else if (c == sep) { out[++n] = cell; cell = "" }
    else cell = cell c
  }
  out[++n] = cell
  return quoted ? -1 : n
}
function kind(cell) {
  if (cell ~ /^[-+]?[0-9][0-9., ]*%?$/ || cell ~ /^[-+]?[^0-9A-Za-z ]?[0-9][0-9.,]*$/) return "number"
  if (cell ~ /^[0-9][0-9]?[0-9]?[0-9]?[-\/.][0-9][0-9]?[-\/.][0-9][0-9]?[0-9]?[0-9]?([ T][0-9:.]+)?$/) return "date"
  return "text"
}
# A value worth looking for: one that would tell a reader something of the file. Not a short word
# or a small number, which any text holds by chance.
function telling(cell) {
  if (kind(cell) == "number") return (cell ~ /[.,]/ && length(cell) >= 4) || length(cell) >= 5
  return length(cell) >= 5
}
{ sub(/\r$/, "") }
NR == 1 {
  sub(/^\357\273\277/, "")
  if (sep == "") { t = gsub(/\t/, "\t"); s = gsub(/;/, ";"); c = gsub(/,/, ","); sep = (t > c && t >= s) ? "\t" : (s > c ? ";" : ",") }
  columns = cells($0, name)
  if (columns < 0) { broken = NR; exit }
  next
}
$0 == "" { next }
{
  n = cells($0, cell)
  if (n < 0) { broken = NR; exit }
  rows++
  for (i = 1; i <= columns; i++) {
    value = (i <= n) ? cell[i] : ""
    gsub(/^[ \t]+|[ \t]+$/, "", value)
    if (value == "") continue
    filled[i]++
    if (!((i, value) in seen)) { seen[i, value] = 1; different[i]++ }
    k = kind(value)
    kinds[i] = (kinds[i] == "" || kinds[i] == k) ? k : "mixed"
    if (mode == "values" && telling(value)) print name[i] "\t" tolower(value)
  }
}
END {
  if (broken) { print "BROKEN " broken; exit }
  if (mode != "describe") exit
  printf "- rows: %d, columns: %d\n", rows, columns
  for (i = 1; i <= columns; i++)
    printf "- column %d \"%s\": %s, %d filled, %d different\n", i, name[i], (kinds[i] == "" ? "empty" : kinds[i]), filled[i], different[i]
}'

readable() {
  [ -n "${1:-}" ] || refuse "no file was named"
  [ -f "$1" ] && [ -r "$1" ] || refuse "the file $1 cannot be read"
  case "$1" in
    *.xlsx|*.xlsm|*.xls|*.ods|*.numbers) refuse "$(basename "$1") is a workbook: save the sheet as CSV and name that file" ;;
    *.csv|*.tsv|*.txt) ;;
    *) refuse "$(basename "$1") is not delimited text (.csv, .tsv, .txt)" ;;
  esac
}

separator() { case "$1" in *.tsv) printf '\t' ;; *) printf '' ;; esac; }

describe() {
  readable "${1:-}"
  out=$(awk -v mode=describe -v sep="$(separator "$1")" "$READ" "$1") || refuse "the file $1 could not be read"
  case "$out" in
    "BROKEN "*) refuse "a cell of $(basename "$1") spans more than one line (near line ${out#BROKEN }): save it without line breaks inside cells" ;;
  esac
  say "- source: $(basename "$1") (read where it is; no cell is printed, only the names of its columns)"
  say "$out"
}

scan() {
  readable "${1:-}"
  [ -d "${2:-}" ] || refuse "the folder ${2:-} cannot be read"
  values=$(awk -v mode=values -v sep="$(separator "$1")" "$READ" "$1") || refuse "the file $1 could not be read"
  case "$values" in "BROKEN "*) refuse "a cell of $(basename "$1") spans more than one line: it cannot be scanned for" ;; esac
  for tool in find grep xargs awk; do
    command -v "$tool" >/dev/null 2>&1 || refuse "this machine has no $tool, so nothing could be scanned"
  done
  # Every text file of the folder but what git keeps for itself; the values go in by the
  # environment, so no value is ever an argument or a file on disk.
  found=$(cd "$2" && find . -type f ! -path './.git/*' ! -path '*/.git/*' -exec grep -Il . {} + 2>/dev/null | sed 's|^\./||' | sort \
    | VALUES="$values" xargs awk '
      BEGIN {
        n = split(ENVIRON["VALUES"], lines, "\n")
        for (i = 1; i <= n; i++) { tab = index(lines[i], "\t"); if (tab) { column[i] = substr(lines[i], 1, tab - 1); value[i] = substr(lines[i], tab + 1) } }
      }
      {
        line = tolower($0)
        for (i = 1; i <= n; i++) {
          if (value[i] == "") continue
          rest = line; at = 0
          while ((p = index(rest, value[i])) > 0) {
            before = (at + p == 1) ? "" : substr(line, at + p - 1, 1)
            after = substr(line, at + p + length(value[i]), 1)
            if (before !~ /[a-z0-9]/ && after !~ /[a-z0-9]/) {
              key = FILENAME SUBSEP FNR SUBSEP column[i]
              if (!(key in said)) { said[key] = 1; printf "- %s line %d: a value of column \"%s\"\n", FILENAME, FNR, column[i] }
              break
            }
            at += p; rest = substr(line, at + 1)
          }
        }
      }' 2>/dev/null)
  if [ -n "$found" ]; then
    say "$found"
    say "- $(say "$found" | wc -l | tr -d ' ') place(s) hold a value of $(basename "$1"): each is rewritten with an invented value, or allowed by the user in so many words"
    exit 1
  fi
  say "- no value of $(basename "$1") is written in $2"
}

case "${1:-}" in
  describe) describe "${2:-}" ;;
  scan) scan "${2:-}" "${3:-}" ;;
  *) sed -n '5,7p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
