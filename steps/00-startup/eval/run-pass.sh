#!/bin/sh
# Run inside the evaluation VM, from the repository's root: one pass of every scenario.
#   sh steps/00-startup/eval/run-pass.sh MODEL RUNS NAME CEILING_USD
# Leaves NAME.json and one transcript per run under /tmp/results.
set -eu
model=$1; runs=$2; name=$3; ceiling=$4
mkdir -p /tmp/results/traces
cd "$(dirname "$0")/plugin"
env -u BASH_ENV -u CLAUDE_ENV_FILE claude plugin eval . --model "$model" --runs "$runs" --ablation none \
  --scaffold --allow-tools Bash Write Edit --no-publish --trust-plugin --max-cost-usd "$ceiling" --keep-temp \
  --output-dir "/tmp/results/$name" --json "/tmp/results/$name.json" >/dev/null 2>&1 || true
python3 - "$name" <<'PY'
import json, os, shutil, sys
name = sys.argv[1]
d = json.load(open("/tmp/results/" + name + ".json"))
for case in d["cases"]:
    for i, run in enumerate(case["arms"]["with"]):
        top = run["tracePath"].split("/out/")[0]
        os.system("chmod 700 " + top + " 2>/dev/null")
        try:
            shutil.copy(run["tracePath"], "/tmp/results/traces/%s-%s-%d.jsonl" % (name, case["name"], i))
        except OSError as error:
            print("no transcript:", case["name"], i, error)
        os.system("chmod -R u+rwX " + top + " 2>/dev/null; rm -rf " + top)
print(name, "cost", round(d["costUsd"], 4), "partial", d.get("partial"))
PY
