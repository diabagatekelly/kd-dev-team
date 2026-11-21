#!/usr/bin/env python3
"""Make, split, check and render the questions a triage kept (no model).

  answers.py make TRIAGE.json LIBRARY.json > cells.json
      one empty cell per (question kept, thing it applies to)
  answers.py split CELLS.json PARTS OUT_DIR
      cut the cells into PARTS files, a question's cells kept together
  answers.py check CELLS.json ANSWERED.json [ANSWERED.json ...]
      every cell answered once, nothing added, dropped or altered,
      and every cell that leans on a dependency carries a source
  answers.py render ANSWERED.json [...] > tables.md
      the answers as the tables the matcher reads
  answers.py count ANSWERED.json [...]
      how many of each tag and kind, and what would reach the owner
"""
import collections
import json
import os
import sys

TAGS = ("DECIDED", "PLAN SILENT", "CONTRADICTS DOCS", "IMPOSSIBLE")
KINDS = ("fact", "owner", "planner")
GIVEN = ("cell", "entry", "action", "thing", "failure", "question")
TO_FILL = ("kind", "tag", "says", "source")


def make(triage, library):
    """A cell for each thing each kept question must be answered for."""
    entries = {entry["id"]: entry for entry in library}
    cells = []
    for row in triage:
        if row["relevant"] is not True:
            continue
        entry = entries[row["id"]]
        for number, thing in enumerate(row["applies_to"], start=1):
            cells.append({
                "cell": f"{entry['id']}.{number:02d}", "entry": entry["id"], "action": entry["action"],
                "thing": thing, "failure": entry["failure"], "question": entry["question"],
                "kind": "", "tag": "", "says": "", "source": "",
            })
    return cells


def split(cells, parts):
    """Cut into `parts` lists of near-equal size without splitting a question."""
    groups, order = {}, []
    for cell in cells:
        if cell["entry"] not in groups:
            order.append(cell["entry"])
        groups.setdefault(cell["entry"], []).append(cell)
    out = [[] for _ in range(parts)]
    for entry in order:
        min(out, key=len).extend(groups[entry])
    return [part for part in out if part]


def problems(expected, answered):
    """Why the answered cells cannot stand for the cells that were handed out."""
    found, seen = [], {}
    for cell in answered:
        name = cell.get("cell")
        if name in seen:
            found.append(f"{name}: answered twice")
        seen[name] = cell
    wanted = {cell["cell"]: cell for cell in expected}
    for name in wanted:
        if name not in seen:
            found.append(f"{name}: missing")
    for name, cell in seen.items():
        if name not in wanted:
            found.append(f"{name}: not one of the cells")
            continue
        for field in GIVEN:
            if cell.get(field) != wanted[name][field]:
                found.append(f"{name}: {field} was changed")
        if cell.get("tag") not in TAGS:
            found.append(f"{name}: tag is {cell.get('tag')!r}")
        if cell.get("kind") not in KINDS:
            found.append(f"{name}: kind is {cell.get('kind')!r}")
        if not str(cell.get("says", "")).strip():
            found.append(f"{name}: says is empty")
        needs_source = cell.get("tag") == "CONTRADICTS DOCS" or (
            cell.get("kind") == "fact" and cell.get("tag") in ("DECIDED", "PLAN SILENT"))
        if needs_source and not str(cell.get("source", "")).strip():
            found.append(f"{name}: leans on a dependency but gives no source")
    return found


def render(answered):
    """One table per question, a row per thing it was answered for."""
    lines = ["# The library's questions, answered for this slice", "",
             "Every cell has an id and one tag: DECIDED, PLAN SILENT, CONTRADICTS DOCS or IMPOSSIBLE.", ""]
    current = None
    for cell in answered:
        if cell["entry"] != current:
            current = cell["entry"]
            lines += ["", f"## {cell['entry']} ({cell['action']}): {cell['failure']}", "",
                      "| id | for | tag | what the plan says, or what would go wrong here | rests on |", "|---|---|---|---|---|"]
        clean = lambda text: " ".join(str(text).split()).replace("|", "/")
        lines.append(f"| {cell['cell']} | {clean(cell['thing'])} | {cell['tag']} | {clean(cell['says'])} | {clean(cell['source'])} |")
    return "\n".join(lines) + "\n"


def count(answered):
    """Sizes a person would care about."""
    tags = collections.Counter(cell["tag"] for cell in answered)
    open_cells = [cell for cell in answered if cell["tag"] in ("PLAN SILENT", "CONTRADICTS DOCS")]
    return {
        "cells": len(answered),
        "tags": {tag: tags[tag] for tag in TAGS},
        "open": len(open_cells),
        "open_by_kind": dict(collections.Counter(cell["kind"] for cell in open_cells)),
        "open_questions_for_the_owner": len({cell["entry"] for cell in open_cells if cell["kind"] == "owner"}),
        "marked_for_a_test": sum(1 for cell in answered if str(cell["source"]).startswith("NEEDS A TEST")),
    }


def _load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def _all(paths):
    return [cell for path in paths for cell in _load(path)]


def main(argv):
    if len(argv) == 3 and argv[0] == "make":
        json.dump(make(_load(argv[1]), _load(argv[2])), sys.stdout, indent=1, ensure_ascii=False)
        print()
        return 0
    if len(argv) == 4 and argv[0] == "split":
        os.makedirs(argv[3], exist_ok=True)
        for number, part in enumerate(split(_load(argv[1]), int(argv[2])), start=1):
            with open(os.path.join(argv[3], f"cells-{number}.json"), "w", encoding="utf-8") as handle:
                json.dump(part, handle, indent=1, ensure_ascii=False)
            print(f"cells-{number}.json: {len(part)} cells")
        return 0
    if len(argv) >= 3 and argv[0] == "check":
        found = problems(_load(argv[1]), _all(argv[2:]))
        print("\n".join(found) if found else "ok")
        return 1 if found else 0
    if len(argv) >= 2 and argv[0] == "render":
        sys.stdout.write(render(_all(argv[1:])))
        return 0
    if len(argv) >= 2 and argv[0] == "count":
        json.dump(count(_all(argv[1:])), sys.stdout, indent=1)
        print()
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
