#!/usr/bin/env python3
"""List the settings a build reads from its environment, and which the plan never names.

  settings_inventory.py SOURCE_DIR PLAN_DIR

A plan can only decide what happens to a malformed or missing setting it
knows about. A build is free to introduce settings the plan never named
(a port, an address), and those are where "the value is wrong and nobody
decided what happens" lives. This reads the source for environment
lookups and the plan for each name. No model.

It finds names written literally (`process.env.NAME`, `process.env["NAME"]`,
`os.environ["NAME"]`, `os.getenv("NAME")`, `os.environ.get("NAME")`) and
reports a lookup whose name is built at run time as a pattern it cannot
resolve, so that one is looked at by a person and not silently missed.
"""
import json
import os
import re
import sys

SOURCE_SUFFIXES = (".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py")
SKIPPED_DIRS = {"node_modules", ".git", "dist", "build", "coverage", "__pycache__", ".venv"}
_NAME = r"([A-Za-z_][A-Za-z0-9_]*)"
_LITERAL = [
    re.compile(r"process\.env\." + _NAME),
    re.compile(r"process\.env\[\s*[\"']" + _NAME + r"[\"']\s*\]"),
    re.compile(r"os\.environ\[\s*[\"']" + _NAME + r"[\"']\s*\]"),
    re.compile(r"os\.environ\.get\(\s*[\"']" + _NAME + r"[\"']"),
    re.compile(r"os\.getenv\(\s*[\"']" + _NAME + r"[\"']"),
]
_ANY_LOOKUP = re.compile(r"process\.env\s*\[|os\.environ\s*\[|os\.environ\.get\(|os\.getenv\(")


def read_lookups(text):
    """Return (names read literally, lines with a lookup whose name is computed)."""
    names, computed = set(), []
    for number, line in enumerate(text.splitlines(), start=1):
        rest = line
        for pattern in _LITERAL:
            for match in pattern.finditer(line):
                names.add(match.group(1))
            rest = pattern.sub("", rest)
        # What is left after the literal lookups are taken out is computed.
        if _ANY_LOOKUP.search(rest):
            computed.append((number, line.strip()))
    return names, computed


def scan_source(root):
    """Every setting name the source reads, with where; and every computed lookup."""
    where, computed = {}, []
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIPPED_DIRS)
        for name in sorted(files):
            if not name.endswith(SOURCE_SUFFIXES):
                continue
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8", errors="replace") as handle:
                names, lines = read_lookups(handle.read())
            shown = os.path.relpath(path, root)
            for setting in names:
                where.setdefault(setting, []).append(shown)
            computed += [f"{shown}:{number}: {line}" for number, line in lines]
    return where, computed


def named_in_plan(plan_root, names):
    """Which of the names appear, as whole words, anywhere in the plan's text files."""
    text = []
    for folder, dirs, files in os.walk(plan_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIPPED_DIRS)
        for name in sorted(files):
            if name.endswith((".md", ".html", ".txt")):
                with open(os.path.join(folder, name), encoding="utf-8", errors="replace") as handle:
                    text.append(handle.read())
    whole = "\n".join(text)
    return {name for name in names if re.search(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])", whole)}


def report(where, computed, in_plan):
    return {
        "settings_read_by_the_build": len(where),
        "named_in_the_plan": sorted(name for name in where if name in in_plan),
        "never_named_in_the_plan": {name: where[name] for name in sorted(where) if name not in in_plan},
        "lookups_with_a_computed_name": computed,
    }


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    where, computed = scan_source(argv[0])
    result = report(where, computed, named_in_plan(argv[1], where))
    json.dump(result, sys.stdout, indent=1)
    print()
    return 1 if result["never_named_in_the_plan"] or computed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
