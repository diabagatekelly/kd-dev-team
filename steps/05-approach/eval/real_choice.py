#!/usr/bin/env python3
"""Count an approach against a key written before it: of the statements an earlier record rested a
choice on, which the approach's table holds as a quote from the candidate's own site, which it
states with no quote, and which it does not hold; and how many cells of each candidate's row say
the pages read do not say. No model. The key names real things and is kept outside this repository.

A key: {"sites": {candidate: its site}, "statements": {name: {"candidate": ..., "pattern": ...}}}

Usage: python3 -I real_choice.py KEY.json APPROACH.md [APPROACH.md ...]
"""
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("page", HERE.parents[2] / "research/page.py")
page = importlib.util.module_from_spec(spec)
spec.loader.exec_module(page)
NOT_SAID = re.compile(r"not said|not stated|does not say|no mention", re.I)


def rows(text, candidate):
    """The cells of each table row whose first cell names the candidate, without that first cell."""
    out = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
        if cells and re.search(re.escape(candidate), cells[0], re.I):
            out += cells[1:]
    return out


def count(text, key):
    """({statement: "quoted" | "unquoted" | "absent"}, {candidate: cells that say the pages do not say})."""
    found, silent = {}, {}
    for candidate, site in key["sites"].items():
        silent[candidate] = sum(1 for cell in rows(text, candidate) if NOT_SAID.search(cell))
    for name, statement in key["statements"].items():
        site = key["sites"][statement["candidate"]]
        result = "absent"
        for cell in rows(text, statement["candidate"]):
            if not re.search(statement["pattern"], cell, re.I):
                continue
            own = any(site in address for _, address in page.PAIR.findall(cell))
            result = "quoted" if own else ("unquoted" if result == "absent" else result)
            if own:
                break
        found[name] = result
    return found, silent


if __name__ == "__main__":
    key = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    for path in sys.argv[2:]:
        found, silent = count(pathlib.Path(path).read_text(encoding="utf-8", errors="replace"), key)
        tally = {kind: sum(1 for result in found.values() if result == kind) for kind in ("quoted", "unquoted", "absent")}
        print(f"{path}: of {len(found)} statements, {tally['quoted']} quoted from the candidate's own site, "
              f"{tally['unquoted']} stated with no quote, {tally['absent']} not in the table; cells that say the pages "
              f"do not say: {', '.join(f'{candidate} {number}' for candidate, number in silent.items())}")
        for name, result in found.items():
            if result != "quoted":
                print(f"  {result}: {name}")
