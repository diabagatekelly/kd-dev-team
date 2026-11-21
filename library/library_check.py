#!/usr/bin/env python3
"""Check and merge the parts of the failure-mode library (no model).

  library_check.py merge PART.json [PART.json ...] > library.json
  library_check.py check library.json

An entry is one way a kind of action commonly goes wrong, with the
question a plan must answer and the public source it rests on. The
check refuses an entry that is malformed, repeats an id, names an
action the library does not have, or uses a word of one field of
business in its own text (a source's title may name what it names).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "judge"))
from wording_check import find_terms  # noqa: E402

ACTIONS = (
    "call-external", "receive-external-data", "sync", "limits",
    "durable-write", "startup-read", "migration", "concurrency", "lifecycle",
    "user-input", "user-action", "long-operation", "time", "text",
    "presentation", "corpus",
    "secrets", "authorization", "configuration", "logging", "accessibility",
)
FIELDS = {"id", "action", "failure", "question", "source"}
SOURCE_FIELDS = {"title", "url", "evidence"}
MIN_PER_ACTION = 8
MAX_PER_ACTION = 12
MAX_EVIDENCE_WORDS = 20
_ID = re.compile(r"^([a-z-]+)-(\d{2})$")


def problems(entries):
    """Return every reason the library cannot be used as it stands."""
    found, seen, per_action = [], set(), {}
    for position, entry in enumerate(entries):
        where = entry.get("id", f"entry {position}") if isinstance(entry, dict) else f"entry {position}"
        if not isinstance(entry, dict) or set(entry) != FIELDS:
            found.append(f"{where}: fields must be exactly {sorted(FIELDS)}")
            continue
        source = entry["source"]
        if not isinstance(source, dict) or set(source) != SOURCE_FIELDS:
            found.append(f"{where}: source fields must be exactly {sorted(SOURCE_FIELDS)}")
            continue
        texts = [entry["id"], entry["action"], entry["failure"], entry["question"],
                 source["title"], source["url"], source["evidence"]]
        if not all(isinstance(text, str) for text in texts):
            found.append(f"{where}: every field must be text")
            continue
        match = _ID.match(entry["id"])
        if entry["action"] not in ACTIONS:
            found.append(f"{where}: unknown action {entry['action']!r}")
        elif not match or match.group(1) != entry["action"]:
            found.append(f"{where}: id must be <action>-<two digits>")
        if entry["id"] in seen:
            found.append(f"{where}: id used twice")
        seen.add(entry["id"])
        per_action[entry["action"]] = per_action.get(entry["action"], 0) + 1
        for field in ("failure", "question"):
            if not entry[field].strip():
                found.append(f"{where}: {field} is empty")
            for _line, term in find_terms(entry[field]):
                found.append(f"{where}: {field} uses the word {term!r}")
        if not source["url"].startswith("https://"):
            found.append(f"{where}: source url must be https")
        if len(source["evidence"].split()) > MAX_EVIDENCE_WORDS:
            found.append(f"{where}: evidence is over {MAX_EVIDENCE_WORDS} words")
    for action, count in sorted(per_action.items()):
        if count > MAX_PER_ACTION:
            found.append(f"{action}: {count} entries, the limit is {MAX_PER_ACTION}")
        elif count < MIN_PER_ACTION and action in ACTIONS:
            found.append(f"{action}: {count} entries, at least {MIN_PER_ACTION} are asked for")
    for action in ACTIONS:
        if action not in per_action:
            found.append(f"{action}: no entries")
    return found


def main(argv):
    if len(argv) >= 2 and argv[0] == "merge":
        merged = []
        for path in argv[1:]:
            with open(path, encoding="utf-8") as handle:
                merged.extend(json.load(handle))
        merged.sort(key=lambda entry: (ACTIONS.index(entry["action"]) if entry.get("action") in ACTIONS else 99, entry.get("id", "")))
        json.dump(merged, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return 0
    if len(argv) == 2 and argv[0] == "check":
        with open(argv[1], encoding="utf-8") as handle:
            found = problems(json.load(handle))
        print("\n".join(found) if found else "ok")
        return 1 if found else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
