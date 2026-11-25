#!/usr/bin/env python3
"""Count what a drawn questions.md reaches on a plan whose defects are known (no model).

  outcome.py ties COVERAGE_RUNS_DIR PLAN WITHIN.json QUESTIONS.md [QUESTIONS.md ...]
      Of the defects the earlier judges tied to library entries, and that WITHIN.json marks as
      within the slice ({"defect id": true or false}), for how many does each questions.md hold a
      line from at least one of those entries? A defect whose entries were all dropped cannot be
      caught by anything built on these questions.

  outcome.py gaps FACTS.json ASKS.json RESEARCH_FOLDER QUESTIONS.md
      For each fact of the key that the research documents lack ({"fact": "pattern"}), whether a
      question asks for it ({"fact": "pattern over the lines of questions.md", or null where no
      general question exists}): asked for, not asked for, or no general question.

The keys come from real projects and are kept apart from this repository.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "briefs"))
import triage_check  # noqa: E402


def kept(text):
    """The library entries a questions.md has at least one line from."""
    return set(re.findall(r"^- L\.([a-z-]+-\d\d)\.", text, re.M))


def ties(tied, within, text):
    """{"full": {defects, kept, lost}, "part": ...} for the defects marked as within the slice."""
    have, result = kept(text), {"entries_kept": len(kept(text)), "lines": len(re.findall(r"^- [LVXSWC]\.", text, re.M))}
    for mark, label in (("F", "full"), ("P", "part")):
        defects = {name: entries for name, (found, entries) in tied.items() if found == mark and within.get(name, True)}
        lost = sorted(name for name, entries in defects.items() if not have.intersection(entries))
        result[label] = {"defects": len(defects), "kept": len(defects) - len(lost), "lost": lost}
    return result


def gaps(facts, asks, research, text):
    """{fact research lacks: "asked for" | "not asked for" | "no general question"}."""
    found = {}
    for name, pattern in facts.items():
        if re.search(pattern, research, re.I):
            continue
        ask = asks.get(name)
        found[name] = "no general question" if not ask else ("asked for" if re.search(ask, text, re.I | re.M) else "not asked for")
    return found


def _load(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def main(arguments, out=sys.stdout):
    if len(arguments) >= 5 and arguments[0] == "ties":
        runs = pathlib.Path(arguments[1])
        coverage = [_load(folder / "out.json") for folder in sorted(runs.iterdir()) if folder.name.startswith("run")]
        tied, within = triage_check.tied_entries(coverage, arguments[2]), _load(arguments[3])
        result = {path: ties(tied, within, pathlib.Path(path).read_text(encoding="utf-8")) for path in arguments[4:]}
        sets = [kept(pathlib.Path(path).read_text(encoding="utf-8")) for path in arguments[4:]]
        if len(sets) > 1:
            result["kept_by_every_run"], result["kept_by_any_run"] = len(set.intersection(*sets)), len(set.union(*sets))
        json.dump(result, out, indent=1)
        print(file=out)
        return 0
    if len(arguments) == 5 and arguments[0] == "gaps":
        research = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in sorted(pathlib.Path(arguments[3]).glob("*.md")))
        for name, verdict in gaps(_load(arguments[1]), _load(arguments[2]), research, pathlib.Path(arguments[4]).read_text(encoding="utf-8")).items():
            print(f"{verdict:20} {name}", file=out)
        return 0
    print(__doc__, file=out)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
