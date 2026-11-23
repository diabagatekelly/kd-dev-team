#!/bin/sh
# Hands the session the startup report of the made-up machine it was started on.
report="/tmp/startup-reports/$(pwd -P | tr '/ ' '__')"
[ -f "$report" ] || exit 0
data="${CLAUDE_PLUGIN_DATA:-$HOME/.kd-dev-team}"
[ ! -f "$(pwd -P)/.cache/kd-data/planning-folders" ] || data="$(pwd -P)/.cache/kd-data"
sed -e "s|@STARTUP@|${CLAUDE_PLUGIN_ROOT}/startup|g" -e "s|@DATA@|$data|g" "$report"
