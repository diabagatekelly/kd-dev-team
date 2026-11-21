#!/bin/sh
# Hands the session the startup report of the made-up machine it was started on.
key="$(pwd -P)/.cache/machine"
[ -f "$key/report.txt" ] || exit 0
sed "s|@STARTUP@|${CLAUDE_PLUGIN_ROOT}/startup|g" "$key/report.txt"
