#!/bin/sh
# The audit switch: whether a record of the session is kept, and where.
#
#   audit.sh [on|off] [REPOSITORY]   print the switch and where the record is kept
#
# Off unless the user chose on. With on, the record is kept in a folder on the user's own
# machine unless they named a repository of their own. Exit 3 on any other word: a record
# is never started, or dropped, on a guess.
set -u

say() { printf '%s\n' "$*"; }
case "$(say "${1:-off}" | tr 'A-Z' 'a-z')" in
  off|false|no|0|"") say "audit: off" ;;
  on|true|yes|1)
    if [ -n "${2:-}" ]; then say "audit: on; the record is kept in the repository $2"
    else say "audit: on; the record is kept in ${CLAUDE_PLUGIN_DATA:-$HOME/.kd-dev-team}/audit"; fi ;;
  *) say "- REFUSED: the audit option is '$1', neither on nor off"; exit 3 ;;
esac
