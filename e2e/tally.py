#!/usr/bin/env python3
"""Count one pass of a stage from the tool's own result: runs that pass every check, runs that
pass every check but those of form (named `form-...`: what nothing tells a bare model to write),
the cost, and each run's failed checks by name. No model, no cost.

Usage: python3 -I tally.py RESULT.json [RESULT.json ...]
"""
import json
import pathlib
import sys


def tally(result):
    """(runs, runs passing every check, runs passing all but the checks of form, cost,
    [(case, run, [failed checks])]) for one result of `claude plugin eval`."""
    runs = passed = held = 0
    failures = []
    for case in result.get("cases", []):
        for number, run in enumerate(case.get("arms", {}).get("with", [])):
            failed = [grader["name"] for grader in run.get("graders", []) if not grader.get("passed")]
            if run.get("error") and not failed:
                failed = ["the run itself: " + str(run["error"])[:80]]
            runs += 1
            passed += not failed
            held += all(name.startswith("form-") for name in failed)
            if failed:
                failures.append((case.get("name", "?"), number, failed))
    return runs, passed, held, round(result.get("costUsd") or 0.0, 2), failures


if __name__ == "__main__":
    for path in sys.argv[1:]:
        runs, passed, held, cost, failures = tally(json.loads(pathlib.Path(path).read_text(encoding="utf-8")))
        print(f"{pathlib.Path(path).stem}: {passed} of {runs} pass every check; {held} of {runs} but for form; ${cost}")
        for case, number, failed in failures:
            print(f"  {case} run {number}: {', '.join(failed)}")
