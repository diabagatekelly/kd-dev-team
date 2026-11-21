#!/usr/bin/env python3
"""Check a triage of the library and measure what it kept (no model).

  triage_check.py LIBRARY.json COVERAGE_RUNS_DIR PLAN TRIAGE.json [TRIAGE.json ...]

A triage says, per library entry, whether its question matters for one
slice. The measure: of the defects later found in that slice which the
coverage judges tied to a library entry, for how many did the triage
keep at least one of those entries? A defect whose entries were all
dropped could not have been caught by anything built on the triage.

COVERAGE_RUNS_DIR/run<n>/out.json are the coverage judge's runs
([{plan, id, class, entries}], class F, P or X); PLAN picks the slice.
"""
import collections
import json
import os
import sys


def problems(library_ids, triage):
    """Why a triage cannot be used: every entry once, the fields as asked."""
    found, seen = [], set()
    for row in triage:
        name = row.get("id")
        if name in seen:
            found.append(f"{name}: judged twice")
        seen.add(name)
        if name not in library_ids:
            found.append(f"{name}: not an entry of the library")
            continue
        if not isinstance(row.get("relevant"), bool):
            found.append(f"{name}: relevant must be true or false")
        if not str(row.get("why", "")).strip():
            found.append(f"{name}: why is empty")
        applies = row.get("applies_to")
        if not isinstance(applies, list):
            found.append(f"{name}: applies_to must be a list")
        elif row.get("relevant") is True and not applies:
            found.append(f"{name}: relevant, but applies_to is empty")
        elif row.get("relevant") is False and applies:
            found.append(f"{name}: not relevant, but applies_to is not empty")
    for name in library_ids:
        if name not in seen:
            found.append(f"{name}: missing")
    return found


def majority(classes, order=("X", "P", "F")):
    counts = collections.Counter(classes)
    top = max(counts.values())
    return min((c for c in counts if counts[c] == top), key=order.index)


def tied_entries(coverage_runs, plan):
    """{defect id: (majority class, entries cited by the runs that gave it)} for F and P."""
    calls = collections.defaultdict(list)
    for run in coverage_runs:
        for row in run:
            if row["plan"] == plan:
                calls[row["id"]].append((row["class"], row.get("entries", [])))
    tied = {}
    for defect, given in calls.items():
        winner = majority([cls for cls, _ in given])
        if winner != "X":
            tied[defect] = (winner, sorted({e for cls, entries in given if cls == winner for e in entries}))
    return tied


def measure(triage, tied):
    """What one triage kept, against the defects tied to library entries."""
    kept = {row["id"] for row in triage if row["relevant"] is True}
    result = {"entries_kept": len(kept),
              "things_to_answer_for": sum(len(row["applies_to"]) for row in triage if row["relevant"] is True)}
    for cls, label in (("F", "full"), ("P", "part")):
        defects = {d: entries for d, (c, entries) in tied.items() if c == cls}
        lost = sorted(d for d, entries in defects.items() if not kept.intersection(entries))
        result[label] = {"defects": len(defects), "kept": len(defects) - len(lost), "lost": lost}
    return result


def _load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    library_ids = [entry["id"] for entry in _load(argv[0])]
    runs_dir = argv[1]
    coverage = [_load(os.path.join(runs_dir, name, "out.json"))
                for name in sorted(os.listdir(runs_dir)) if name.startswith("run")]
    tied = tied_entries(coverage, argv[2])
    out, bad = {}, False
    kept_sets = []
    for path in argv[3:]:
        triage = _load(path)
        found = problems(library_ids, triage)
        if found:
            out[path] = {"problems": found[:20]}
            bad = True
            continue
        out[path] = measure(triage, tied)
        kept_sets.append({row["id"] for row in triage if row["relevant"] is True})
    if len(kept_sets) > 1:
        out["kept_by_every_triage"] = len(set.intersection(*kept_sets))
        out["kept_by_any_triage"] = len(set.union(*kept_sets))
    json.dump(out, sys.stdout, indent=1)
    print()
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
