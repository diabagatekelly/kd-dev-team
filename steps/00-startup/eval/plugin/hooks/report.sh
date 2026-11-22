#!/bin/sh
# Hands the session the startup report of the made-up machine it was started on.
report="/tmp/startup-reports/$(pwd -P | tr '/ ' '__')"
[ -f "$report" ] || exit 0
sed "s|@STARTUP@|${CLAUDE_PLUGIN_ROOT}/startup|g" "$report"
