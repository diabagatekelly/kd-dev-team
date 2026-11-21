#!/bin/sh
# The one report a session is given at its start: the machine, the tracker, the documents.
# Changes nothing. A part that cannot read its tool says REFUSED and the rest still comes.
set -u

HERE=$(cd "$(dirname "$0")" && pwd)
refused=0
part() {
  printf '\n%s\n' "$1"; shift
  sh "$@" 2>&1
  [ $? -eq 0 ] || refused=1
}

printf '%s\n' "kd-dev-team: startup report" \
  "Read by script at the start of this session; nothing was installed or changed."
part Machine "$HERE/machine.sh" inspect
part Tracker "$HERE/tracker.sh"
part Documents "$HERE/stage.sh" report
[ "$refused" -eq 0 ] || printf '\n%s\n' "Startup could not read everything: see REFUSED above."
exit 0
