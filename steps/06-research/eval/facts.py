#!/usr/bin/env python3
"""Count which known facts a research document holds.

The key is a JSON file kept apart from this repository when it comes from a real project:
{"a-fact's-name": "a pattern that finds it"}. A fact counts as held when its pattern is found in
any of the documents, whatever the case. The patterns are loose, so the count is a guide and a
close call is read.

Usage: python3 -I facts.py KEY.json DOCUMENT...     (one line a fact, then the count)
       python3 -I facts.py KEY.json --runs FOLDER... (a run a folder: how many runs hold each fact)
"""
import json
import pathlib
import re
import sys


def held(key, text):
    """The names of the key's facts whose pattern is found in the text."""
    return [name for name, pattern in key.items() if re.search(pattern, text, re.I)]


def across(key, runs):
    """{fact: in how many runs it is held}, for runs given as texts."""
    found = [set(held(key, text)) for text in runs]
    return {name: sum(name in one for one in found) for name in key}


def read(paths):
    return "\n".join(pathlib.Path(path).read_text(encoding="utf-8", errors="replace") for path in paths)


def main(arguments):
    key = json.loads(pathlib.Path(arguments[0]).read_text(encoding="utf-8"))
    if arguments[1] == "--runs":
        runs = [read(sorted(pathlib.Path(folder).glob("*.md"))) for folder in arguments[2:]]
        counts = across(key, runs)
        for name, count in counts.items():
            print(f"{count} of {len(runs)}  {name}")
        total = sum(counts.values())
        print(f"held: {total} of {len(key) * len(runs)} ({100 * total // max(1, len(key) * len(runs))}%); "
              f"in every run: {sum(count == len(runs) for count in counts.values())} of {len(key)}")
    else:
        found = held(key, read(arguments[1:]))
        for name in key:
            print(("held     " if name in found else "missing  ") + name)
        print(f"held: {len(found)} of {len(key)}")


if __name__ == "__main__":
    main(sys.argv[1:])
