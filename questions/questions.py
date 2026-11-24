#!/usr/bin/env python3
"""Draw a slice's questions from its documents and the library (no model).

A session decides two things and writes them in `kept.md`: what the slice takes in, and which of
the library's questions matter for it, each with the things it applies to. Everything else is
drawn here, from the documents as they stand:

  - a line for each kept question and each thing it applies to;
  - each value taken in against the ways a value of its kind can be wrong;
  - each sensitive value against the five places it can leak to;
  - each state of each lasting thing (research's `states.md`) against each event that can reach it;
  - the questions asked of every slice, whatever it does;
  - what research left open, carried as it is.

Usage: python3 -I questions.py things SLICE     what a question may apply to, and the library to read
       python3 -I questions.py draw SLICE       check kept.md, then write questions.md beside it
       python3 -I questions.py check SLICE      kept.md holds, and questions.md is what draw writes
       python3 -I questions.py state SLICE      none | kept | drawn | stale: <what changed>

SLICE is the chosen slice's folder (planning/slice-001). Nothing here answers a question.
"""
import hashlib
import json
import pathlib
import re
import sys

LIBRARY = pathlib.Path(__file__).resolve().parent.parent / "library" / "library.json"

# The ways a value can be wrong, and which of them a value of each kind can be. A kind the table
# does not have, and `other`, get every way: a way wrongly left out is a question lost.
WAYS = {
    "empty": "is empty",
    "missing": "is missing, or null",
    "malformed": "is of the wrong type or malformed",
    "edge": "is at the very edge of what is allowed",
    "outside": "is outside what is allowed",
    "long": "is far longer or larger than expected",
    "twice": "is the same as one already there",
    "dangling": "names something that does not exist, or no longer does",
    "characters": "holds unusual characters or another encoding",
}
KINDS = {
    "text": ("empty", "missing", "long", "twice", "characters"),
    "number": ("empty", "missing", "malformed", "edge", "outside"),
    "date": ("empty", "missing", "malformed", "edge", "outside"),
    "choice": ("missing", "outside"),
    "identifier": ("empty", "missing", "malformed", "twice", "dangling"),
    "file": ("empty", "missing", "malformed", "long", "twice", "characters"),
    "list": ("empty", "missing", "malformed", "long", "twice"),
    "other": tuple(WAYS),
}
# A build reads settings no plan names, so the rule for them is asked once, of all of them.
SETTINGS = ("every-setting", ("missing", "empty", "malformed", "outside"))

# What can reach a lasting thing whatever the slice does.
EVENTS = {
    "again": "the same action is done again at once",
    "reopened": "the page is reloaded, or the product closed and reopened, partway through",
    "restart": "the product stops and starts again",
    "second": "a second copy of the product, a second device or a second person acts on it at the same moment",
    "time": "a long time passes with nothing done",
}
# And each thing the approach committed to.
OUTSIDE = {
    "down": "%s cannot be reached",
    "slow": "%s answers very slowly",
    "lost": "%s acted, and its reply never arrived",
}
# Where a sensitive value gets out, the obvious place and the four that are missed.
EXITS = {
    "logs": "what the product logs",
    "errors-inside": "an error's own message and trace",
    "errors-shown": "an error shown or returned to whoever asked",
    "telemetry": "what is sent to monitoring or measurement",
    "samples": "test data and examples kept with the code",
}
# Asked of every slice: the answers set how much of the rest is worth doing. Answered from the
# documents where they say, and only otherwise the owner's.
WHOLE = {
    "unavailable": "What happens, and to whom, if what this slice adds cannot be used for an hour?",
    "target": "How often may it fail, and how slow is too slow, before someone would say it does not work?",
    "noticed": "Who notices when it breaks, and how?",
    "sensitive": "What does this slice touch that would harm someone if another person saw or changed it?",
    "who-sees": "Who uses it, and may any of them see or change what belongs to another?",
    "obligations": "Does a law, a contract or an outside system's terms bind how this is handled?",
    "prize": "What would someone who means harm want from what this slice adds?",
}
OPEN_SOURCES = ("not said in the documents", "to verify")
STAMP = "<!-- drawn from: %s -->"


def slug(name):
    """A thing's short name: lower case, hyphens, no leading article."""
    low = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return re.sub(r"^(a|an|the)-", "", low)


def cells_of(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def sections(text, level="##"):
    """{heading: its lines} for the headings of one level, in order."""
    found, name = {}, None
    for line in text.splitlines():
        marks = re.match(r"(#+) ", line)
        if marks and len(marks.group(1)) == len(level):
            name = line[len(level):].strip()
            found[name] = []
        elif marks and len(marks.group(1)) < len(level):
            name = None
        elif name is not None:
            found[name].append(line)
    return found


def rows(lines):
    """The rows of the first table among the lines, without its heading and rule."""
    table = [cells_of(line) for line in lines if line.strip().startswith("|")]
    return [row for row in table[1:] if not all(re.fullmatch(r":?-+:?", cell) for cell in row)]


def criteria(slice_text):
    """The slice's criteria by their names, in order: ['record-walk / 1', ...]."""
    return re.findall(r"^\s*[-*] \*\*([a-z0-9-]+ / \d+)\*\*", slice_text, re.M)


def committed(approach_text):
    """The names under the approach's "Committed to", as the stage script reads them."""
    names = []
    for heading, lines in sections(approach_text).items():
        if "committed to" not in heading.lower():
            continue
        for line in lines:
            match = re.match(r"\s*[-*]\s+(.*)", line)
            if not match:
                continue
            name = re.sub(r"[`*]", "", match.group(1)).strip().rstrip(".")
            if name.lower() in ("none", "nothing"):
                continue
            names.append(re.split(r":\s", name, maxsplit=1)[0].strip())
    return names


def states(states_text):
    """{thing: [(state, source, row)]} from research's tables, and the dead ends listed for the owner."""
    things, dead = {}, []
    for heading, lines in sections(states_text).items():
        if "owner" in heading.lower():
            dead = [line.strip()[2:].strip() for line in lines if line.strip().startswith(("- ", "* "))]
            continue
        table = rows(lines)
        if table:
            things[heading] = [(row[0].strip("` "), row[-1], row) for row in table if row and row[0].strip("` ")]
    return things, dead


def carried(research):
    """What research left open: [(id, what it says)] from {document name: text}."""
    found = []
    for name, text in sorted(research.items()):
        stem = slug(pathlib.Path(name).stem)
        if stem == "states":
            things, dead = states(text)
            for thing, table in things.items():
                for state, _source, row in table:
                    gaps = [mark for mark in OPEN_SOURCES if any(mark in cell.lower() for cell in row)]
                    if gaps:
                        found.append((f"C.states.{slug(thing)}.{state}", f"{thing}, `{state}`: {' and '.join(gaps)} ({' | '.join(row[1:])})"))
            found += [(f"C.states.dead-end.{number}", f"for the owner's list: {line}") for number, line in enumerate(dead, 1)]
            continue
        for mark, kind in re.findall(r"^\s*[-*] ((?:O|S)\d+)(?: (AGREES|CONTRADICTS|NOT COVERED))?:", text, re.M):
            if mark.startswith("O") or kind in ("CONTRADICTS", "NOT COVERED"):
                line = re.search(rf"^\s*[-*] {mark}\b.*$", text, re.M).group(0).strip()[2:]
                found.append((f"C.{stem}.{mark}", line))
    return found


def read_slice(folder):
    """The slice's documents as they stand: the latest of each by its number."""
    folder = pathlib.Path(folder)

    def latest(pattern):
        found = sorted(folder.glob(pattern))
        return found[-1] if found else None

    slice_doc, approach, research, kept = latest("[0-9]*_slice.md"), latest("[0-9]*_approach.md"), latest("[0-9]*_research"), latest("[0-9]*_questions")
    documents = {}
    for path in [slice_doc, approach] + (sorted(research.glob("*.md")) if research else []):
        if path and path.is_file():
            documents[path.relative_to(folder).as_posix()] = path.read_text(encoding="utf-8")
    return {
        "folder": folder,
        "slice": slice_doc.read_text(encoding="utf-8") if slice_doc else "",
        "approach": approach.read_text(encoding="utf-8") if approach else "",
        "research": {path.name: path.read_text(encoding="utf-8") for path in sorted(research.glob("*.md"))} if research else {},
        "documents": documents,
        "questions": kept,
    }


def known(read):
    """{short name: what it is} for everything the documents give a question to apply to."""
    names = {}
    for name in criteria(read["slice"]):
        names[slug(name)] = f"criterion {name}"
    for name in committed(read["approach"]):
        names[slug(name)] = f"committed to: {name}"
    for thing in states(read["research"].get("states.md", ""))[0]:
        names[slug(thing)] = f"lasting thing: {thing}"
    return names


def read_kept(text):
    """kept.md as written by a session: the values taken in, the other things, the library's rows."""
    parts = {heading.lower(): lines for heading, lines in sections(text).items()}

    def part(word):
        return next((lines for heading, lines in parts.items() if word in heading), [])

    values = [{"name": row[0].strip("` "), "kind": row[1].lower(), "from": row[2], "sensitive": row[3].lower(), "source": row[4]}
              for row in rows(part("takes in")) if len(row) >= 5]
    others = {}
    for line in part("other things"):
        match = re.match(r"\s*[-*]\s+`?([^`:]+)`?:\s*(.+)", line)
        if match:
            others[slug(match.group(1))] = match.group(2).strip()
    library = [{"entry": row[0], "applies": row[1], "why": row[2]} for row in rows(part("library")) if len(row) >= 3]
    return {"values": values, "others": others, "library": library}


def expand(cell, entries):
    """The library entries a row's first cell names: one, several, or `kind: all`."""
    match = re.fullmatch(r"`?([a-z-]+)`?:\s*all", cell.strip(), re.I)
    if match:
        return [entry["id"] for entry in entries if entry["action"] == match.group(1).lower()] or [cell.strip()]
    return [name.strip("` ") for name in re.split(r"[,;]\s*", cell) if name.strip("` ")]


def problems(kept, names, entries, sources=()):
    """Why kept.md cannot be drawn from: every entry once, every thing a known one, every value sourced."""
    found, seen = [], {}
    ids = {entry["id"] for entry in entries}
    values = {slug(value["name"]) for value in kept["values"]}
    things = set(names) | values | set(kept["others"])
    for value in kept["values"]:
        if value["kind"] not in KINDS:
            found.append(f"{value['name']}: kind {value['kind']!r} is not one of {', '.join(KINDS)}")
        if value["sensitive"] not in ("yes", "no"):
            found.append(f"{value['name']}: sensitive is yes or no, not {value['sensitive']!r}")
        if not value["source"].strip() or (sources and not any(mark in value["source"] for mark in sources)):
            found.append(f"{value['name']}: its source names no criterion and no research document")
    for row in kept["library"]:
        dropped = row["applies"].strip("` ").lower() == "dropped"
        applies = [] if dropped else [name.strip("` ") for name in re.split(r";\s*", row["applies"]) if name.strip("` ")]
        for name in expand(row["entry"], entries):
            if name not in ids:
                found.append(f"{name}: not an entry of the library")
                continue
            if name in seen:
                found.append(f"{name}: judged twice")
            seen[name] = applies
            if not row["why"].strip():
                found.append(f"{name}: no reason given")
            if not dropped and not applies:
                found.append(f"{name}: kept, and applies to nothing")
            for thing in applies:
                if slug(thing) not in things:
                    found.append(f"{name}: applies to {thing!r}, which is no criterion, lasting thing, thing committed to, value taken in or other thing listed")
    found += [f"{entry['id']}: neither kept nor dropped" for entry in entries if entry["id"] not in seen]
    return found, seen


def draw(read, kept, entries):
    """The questions, a line a cell, each with a name that does not change."""
    lines = ["# Questions", "", STAMP % stamp(read, kept["text"]), "",
             "Drawn by script from kept.md and the slice's documents. Nothing here is answered.", ""]
    _found, judged = problems(kept, known(read), entries)
    by_id = {entry["id"]: entry for entry in entries}
    lines += ["## From the library", ""]
    for name, applies in judged.items():
        for thing in applies:
            lines.append(f"- L.{name}.{slug(thing)}: {thing}: {by_id[name]['question']}")
    lines += ["", "## Each value taken in, each way it can be wrong", ""]
    for value in kept["values"]:
        for way in KINDS.get(value["kind"], KINDS["other"]):
            lines.append(f"- V.{slug(value['name'])}.{way}: `{value['name']}` ({value['from']}) {WAYS[way]}: what does the product do, and what is the person told?")
    for way in SETTINGS[1]:
        lines.append(f"- V.{SETTINGS[0]}.{way}: any setting the build reads {WAYS[way]}: what does the product do at start, and who is told?")
    lines += ["", "## Each sensitive value, each place it can leak to", ""]
    exposed = [value for value in kept["values"] if value["sensitive"] == "yes"]
    for value in exposed:
        for key, words in EXITS.items():
            lines.append(f"- X.{slug(value['name'])}.{key}: can `{value['name']}` reach {words}, on the path that works and on each that fails?")
    if not exposed:
        lines.append("No value taken in is marked sensitive.")
    lines += ["", "## Each state, each event", ""]
    things, _dead = states(read["research"].get("states.md", ""))
    events = [(slug(name), f"what {name} describes is done") for name in criteria(read["slice"])]
    events += list(EVENTS.items())
    events += [(f"{slug(name)}-{key}", words % name) for name in committed(read["approach"]) for key, words in OUTSIDE.items()]
    if not things:
        lines.append("No lasting thing has states written for this slice.")
    for thing, table in things.items():
        for state, _source, _row in table:
            for key, words in events:
                lines.append(f"- S.{slug(thing)}.{state}.{key}: {thing} is `{state}` and {words}: what happens to it, and what is the person shown?")
    lines += ["", "## Asked of every slice", ""]
    lines += [f"- W.{key}: {words}" for key, words in WHOLE.items()]
    lines += ["", "## Carried from research", ""]
    lines += [f"- {name}: {words}" for name, words in carried(read["research"])] or ["Nothing was left open."]
    return "\n".join(lines) + "\n"


def stamp(read, kept_text):
    """One short mark of every document the questions were drawn from."""
    digest = hashlib.sha256()
    for name, text in sorted(read["documents"].items()):
        digest.update(name.encode() + b"\0" + text.encode() + b"\0")
    digest.update(kept_text.encode())
    return digest.hexdigest()[:16]


def load(folder, library=LIBRARY):
    read = read_slice(folder)
    entries = json.loads(pathlib.Path(library).read_text(encoding="utf-8"))
    path = read["questions"] / "kept.md" if read["questions"] else None
    kept = None
    if path and path.is_file():
        text = path.read_text(encoding="utf-8")
        kept = {**read_kept(text), "text": text}
    return read, entries, kept


def state(folder, library=LIBRARY):
    read, _entries, kept = load(folder, library)
    if kept is None:
        return "none"
    drawn = read["questions"] / "questions.md"
    if not drawn.is_file():
        return "kept"
    match = re.search(re.escape(STAMP).replace("%s", "([0-9a-f]+)"), drawn.read_text(encoding="utf-8"))
    return "drawn" if match and match.group(1) == stamp(read, kept["text"]) else "stale: a document of the slice or kept.md changed after the questions were drawn"


def main(arguments, out=sys.stdout):
    if len(arguments) < 2 or arguments[0] not in ("things", "draw", "check", "state"):
        print(__doc__, file=out)
        return 2
    command, folder = arguments[0], arguments[1]
    library = arguments[2] if len(arguments) > 2 else LIBRARY
    read, entries, kept = load(folder, library)
    if command == "state":
        print(state(folder, library), file=out)
        return 0
    if command == "things":
        print("A question may apply to:", file=out)
        for name, what in known(read).items():
            print(f"  {name} ({what})", file=out)
        print("and to any value or other thing kept.md lists.\n\nThe library, by kind of action:", file=out)
        kind = None
        for entry in entries:
            if entry["action"] != kind:
                kind = entry["action"]
                print(f"\n{kind}", file=out)
            print(f"  {entry['id']}: {entry['question']}", file=out)
        return 0
    if kept is None:
        print("no kept.md in the slice's questions folder: nothing to draw from", file=out)
        return 1
    found, _judged = problems(kept, known(read), entries, criteria(read["slice"]) + list(read["research"]))
    if found:
        print("\n".join(found), file=out)
        return 1
    text = draw(read, kept, entries)
    target = read["questions"] / "questions.md"
    if command == "draw":
        target.write_text(text, encoding="utf-8")
        print(f"drawn: {target} ({sum(line.startswith('- ') for line in text.splitlines())} questions)", file=out)
        return 0
    if not target.is_file() or target.read_text(encoding="utf-8") != text:
        print("questions.md is not what the script draws from the documents as they stand: draw it again", file=out)
        return 1
    print("ok", file=out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
