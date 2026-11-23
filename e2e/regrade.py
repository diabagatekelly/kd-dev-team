#!/usr/bin/env python3
"""Grade runs that were already made, again, with the checks as they stand now. No model, no cost.

A check that failed a good answer is corrected and then has to be shown right. Running the
scenario again costs money and a new set of answers; grading the kept transcripts again costs
nothing and uses the very answers the check got wrong. It also shows, before anything is run,
what a new or changed check would have said of every run on record.

The free checks are graded as the tool grades them: a pattern on the last message, on a file the
run left, or on the transcript; whether a file exists; how often a tool was used. A file is what
the scenario started with, changed by the run's Write and Edit calls.

Usage: python3 -I regrade.py PLUGIN TRACES NAME
    PLUGIN   a stage's built plugin (its evals/ folder holds each scenario's case.yaml)
    TRACES   the folder of kept transcripts, named NAME-<scenario>-<run>.jsonl
"""
import json
import pathlib
import re
import sys


def graders(case):
    """A scenario's name and its checks, from the case file this repository's builders write."""
    name, checks = "", []
    for line in case.read_text(encoding="utf-8").splitlines():
        if line.startswith("name: "):
            name = line[6:].strip()
        elif line.startswith("  - {"):
            checks.append(json.loads(line[4:]))
    return name, checks


def replay(record, files):
    """What a run said last, the files it left (those it started with, changed by its Write and
    Edit calls) and its tool calls, from the tool's own record of it."""
    files, last, calls = dict(files), "", []
    for line in record.splitlines():
        try:
            message = json.loads(line).get("message") or {}
        except ValueError:
            continue
        if message.get("role") != "assistant" or not isinstance(message.get("content"), list):
            continue
        for part in message["content"]:
            if part.get("type") == "text":
                last = part.get("text") or last
            elif part.get("type") == "tool_use":
                given = part.get("input") or {}
                calls.append((part.get("name"), json.dumps(given)))
                path = str(given.get("file_path") or "")
                key = next((known for known in files if path.endswith("/" + known) or path == known), None)
                if part.get("name") == "Write":
                    files[key or path] = given.get("content") or ""
                elif part.get("name") == "Edit" and key is not None:
                    old, new = given.get("old_string") or "", given.get("new_string") or ""
                    files[key] = files[key].replace(old, new) if given.get("replace_all") else files[key].replace(old, new, 1)
    return last, files, calls


def file_named(files, path):
    return next((text for known, text in files.items() if known == path or known.endswith("/" + path)), None)


def passes(check, last, files, calls, record):
    """Whether one free check passes; None for a kind of check this script does not know."""
    kind = check.get("type")
    if kind == "file_exists":
        return file_named(files, check["path"]) is not None
    if kind == "tool_used":
        pattern = check.get("input_match")
        used = sum(1 for name, given in calls
                   if name == check["tool"] and (pattern is None or re.search(pattern, given)))
        return check.get("min", 0) <= used <= check.get("max", float("inf"))
    if kind == "regex":
        target = check.get("target")
        if target == "last_message":
            text = last
        elif target == "trace":
            text = record
        elif isinstance(target, dict) and target.get("source") == "file":
            text = file_named(files, target["path"])
            if text is None:    # a file that was never written fails every check on it, as the tool has it
                return False
        else:
            return None
        found = re.search(check["pattern"], text, re.I if "i" in check.get("flags", "") else 0) is not None
        return found != (check.get("match") == "not_contains")
    return None


def started_with(case_folder):
    project = case_folder / "project"
    return {path.relative_to(project).as_posix(): path.read_text(encoding="utf-8", errors="replace")
            for path in project.rglob("*") if path.is_file()} if project.is_dir() else {}


def regrade(plugin, traces, name):
    """For each scenario, each kept run's failed checks: {scenario: [[names of failed checks], ...]}."""
    out = {}
    for case in sorted((plugin / "evals").glob("*/case.yaml")):
        scenario, checks = graders(case)
        runs = sorted(traces.glob(f"{name}-{scenario}-*.jsonl"), key=lambda path: int(path.stem.rsplit("-", 1)[1]))
        for run in runs:
            record = run.read_text(encoding="utf-8", errors="replace")
            last, files, calls = replay(record, started_with(case.parent))
            out.setdefault(scenario, []).append(
                [check["name"] for check in checks if passes(check, last, files, calls, record) is False])
    return out


if __name__ == "__main__":
    plugin, traces, name = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
    result = regrade(plugin, traces, name)
    runs = sum(len(found) for found in result.values())
    print(f"{name}: {sum(1 for found in result.values() for failed in found if not failed)} of {runs} runs pass "
          f"the checks as they stand")
    for scenario, found in result.items():
        for number, failed in enumerate(found):
            if failed:
                print(f"  {scenario} run {number}: {', '.join(failed)}")
