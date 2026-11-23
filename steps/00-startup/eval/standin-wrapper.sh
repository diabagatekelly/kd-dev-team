#!/bin/sh
# Installed in the evaluation VM under each stood-in tool's name. In a folder a scenario was
# set up in, it answers as that scenario's made-up machine; anywhere else it is the real tool.
# A command that steps out of the project first (`cd "$TMPDIR"; ...`) is still on that machine:
# the folder it came from is looked in too.
me=$(basename "$0")
key=""
for start in "$(pwd -P)" "${OLDPWD:-}"; do
  d=$start
  while [ -n "$d" ]; do
    if [ -d "$d/.cache/machine" ]; then key="$d/.cache/machine"; break 2; fi
    [ "$d" = / ] && break
    d=$(dirname "$d")
  done
done
if [ -n "$key" ]; then
  if [ -e "$key/absent/$me" ]; then echo "$me: command not found" >&2; exit 127; fi
  STANDIN_STATE="$key" exec sh "${STANDIN_HOME:-/opt/standin}/$me" "$@"
fi
here=$(cd "$(dirname "$0")" && pwd)
old_ifs=$IFS; IFS=:
for folder in $PATH; do
  if [ "$folder" != "$here" ] && [ -x "$folder/$me" ]; then IFS=$old_ifs; exec "$folder/$me" "$@"; fi
done
echo "$me: command not found" >&2; exit 127
