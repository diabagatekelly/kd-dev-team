#!/bin/sh
# Installed in the evaluation VM under each stood-in tool's name. In a folder a scenario was
# set up in, it answers as that scenario's made-up machine; anywhere else it is the real tool.
me=$(basename "$0")
d=$(pwd -P); key=""
while [ -n "$d" ]; do
  candidate="/tmp/standin/by-dir/$(printf '%s' "$d" | tr '/ ' '__')"
  if [ -d "$candidate" ]; then key=$candidate; break; fi
  [ "$d" = / ] && break
  d=$(dirname "$d")
done
if [ -n "$key" ]; then
  if [ -e "$key/absent/$me" ]; then echo "$me: command not found" >&2; exit 127; fi
  STANDIN_STATE="$key" exec sh "/opt/standin/$me" "$@"
fi
here=$(cd "$(dirname "$0")" && pwd)
old_ifs=$IFS; IFS=:
for folder in $PATH; do
  if [ "$folder" != "$here" ] && [ -x "$folder/$me" ]; then IFS=$old_ifs; exec "$folder/$me" "$@"; fi
done
echo "$me: command not found" >&2; exit 127
