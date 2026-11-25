#!/usr/bin/env python3
"""Draw a slice's questions from its documents and the library (no model).

A session decides two things and writes them in `kept.md`: what the slice takes in, and which of
the library's questions matter for it, each with the things it applies to. Everything else is
drawn here, from the documents as they stand:

  - a line for each kept question and each thing it applies to;
  - each value taken in against the ways a value of its kind can be wrong;
  - each class of sensitive values against the five places it can leak to;
  - each state of each lasting thing (research's `states.md`) against each event that can reach it;
  - the questions asked of every slice, whatever it does;
  - what research left open, carried as it is.

Usage: python3 -I questions.py things SLICE     what a question may apply to, and the library's kinds
       python3 -I questions.py library KIND...  the questions of those kinds (a few kinds at a time: a shell cuts long output)
       python3 -I questions.py draw SLICE       check kept.md, then write questions.md beside it
       python3 -I questions.py check SLICE      kept.md holds, and questions.md is what draw writes
       python3 -I questions.py state SLICE      none | kept | drawn | skipped | stale: <what changed>

SLICE is the chosen slice's folder (planning/slice-001). Nothing here answers a question.

Where the user has said to skip the stage, the folder holds `skipped.md` (their words and the date)
and no kept.md: the library is not gone through, and what needs no judgement is drawn all the same.
"""
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
# The library comes first. A line of a grid is not drawn when a kept library question, applied to the
# same thing, already asks it: the library's line stands, and no question is asked twice.
SAME = {
    "empty": ("user-input-02", "user-input-07"),
    "missing": ("user-input-02",),
    "malformed": ("receive-external-data-12",),
    "edge": ("user-input-08",),
    "outside": ("user-input-08", "receive-external-data-07"),
    "long": ("user-input-01", "receive-external-data-10"),
    "twice": ("user-input-09",),
    "characters": ("user-input-03", "text-03"),
    "logs": ("secrets-03", "logging-03"),
    "again": ("user-action-01", "call-external-02", "long-operation-11"),
    "reopened": ("user-action-02", "user-action-06"),
    "restart": ("long-operation-06", "startup-read-04", "durable-write-12"),
    "second": ("concurrency-01", "concurrency-12", "user-action-07"),
    "time": ("lifecycle-04", "lifecycle-08", "long-operation-09"),
    "down": ("call-external-07", "call-external-12"),
    "slow": ("call-external-03", "call-external-04", "call-external-08"),
    "lost": ("call-external-01",),
}
# The rule for settings is asked of no one thing, so a kept question on settings stands for it wherever it applies.
SAME_SETTINGS = {"missing": ("configuration-01",), "empty": ("configuration-01",), "malformed": ("configuration-01",), "outside": ("configuration-02",)}
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


def carried(research, standing=None):
    """What research left open: [(id, what it says)] from {document name: text}. Where the things
    now committed to are given, the document of a thing no longer committed to carries nothing."""
    found = []
    for name, text in sorted(research.items()):
        stem = slug(pathlib.Path(name).stem)
        if standing is not None and stem != "states" and stem not in standing:
            continue
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
    # In the order the stage script reads them for the same mark: the slice, the approach, research by name.
    documents = [path.read_bytes() for path in [slice_doc, approach] + (sorted(research.glob("*.md"), key=lambda each: each.name) if research else [])
                 if path and path.is_file()]
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


def classes(values):
    """{class of sensitive values: its values}, in the order written. A bare `yes` is one class of its own."""
    found = {}
    for value in values:
        name = slug(value["sensitive"])
        if name and name != "no":
            found.setdefault("sensitive-values" if name == "yes" else name, []).append(value["name"])
    return found


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
    # What a criterion creates and keeps: None when the file has no such list, [] when it says nothing is kept.
    lasting = None
    if any("creates" in heading for heading in parts):
        lasting = [(match.group(1).strip(), match.group(2).strip())
                   for match in (re.match(r"\s*[-*]\s+`?([^`:]+)`?:\s*(.+)", line) for line in part("creates")) if match]
    return {"values": values, "others": others, "library": library, "lasting": lasting}


def expand(cell, entries):
    """The library entries a row's first cell names: one, several, or `kind: all`."""
    match = re.fullmatch(r"`?([a-z-]+)`?:\s*all", cell.strip(), re.I)
    if match:
        return [entry["id"] for entry in entries if entry["action"] == match.group(1).lower()] or [cell.strip()]
    return [name.strip("` ") for name in re.split(r"[,;]\s*", cell) if name.strip("` ")]


def problems(kept, names, entries, sources=()):
    """Why kept.md cannot be drawn from: every thing kept has its states, every entry once, every thing a known one,
    every value sourced."""
    found, seen = [], {}
    ids = {entry["id"] for entry in entries}
    values = {slug(value["name"]) for value in kept["values"]}
    things = set(names) | values | set(kept["others"]) | set(classes(kept["values"]))
    if kept.get("lasting") is None:
        found.append("no list of what the slice creates and keeps: one line a thing with its criterion, or `- nothing`")
    for name, source in kept.get("lasting") or []:
        if not names.get(slug(name), "").startswith("lasting thing"):
            found.append(f"{name}: created or kept ({source}), and states.md has no table for it: "
                         "add its table by the research text's rules, then draw again")
    for value in kept["values"]:
        if value["kind"] not in KINDS:
            found.append(f"{value['name']}: kind {value['kind']!r} is not one of {', '.join(KINDS)}")
        if not slug(value["sensitive"]):
            found.append(f"{value['name']}: sensitive is `no`, or the name of the class of sensitive values it belongs to")
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
    """The questions, a line a cell, each with a name that does not change. The library first."""
    lines = ["# Questions", "", STAMP % stamp(read, kept["text"]), "",
             "Drawn by script from kept.md and the slice's documents. Nothing here is answered.", ""]
    if kept.get("skipped"):
        lines[4] = ("Drawn by script from the slice's documents alone. The library was not gone through and no value was listed: "
                    "skipped at the user's word (skipped.md), a risk for the owner's list. Nothing here is answered.")
    _found, judged = problems(kept, known(read), entries)
    by_id = {entry["id"]: entry for entry in entries}
    things, _dead = states(read["research"].get("states.md", ""))
    lasting = {slug(thing): [state for state, _source, _row in table] for thing, table in things.items()}
    asked = {}
    for name, applies in judged.items():
        for thing in applies:
            asked.setdefault(slug(thing), set()).add(name)

    def already(thing, key):
        """The kept library questions that ask this of this thing."""
        return sorted(asked.get(slug(thing), set()).intersection(SAME.get(key, ())))

    def section(title, drawn, spared, empty=None):
        found = ["", f"## {title}", ""] + (drawn or ([empty] if empty else []))
        if spared:
            found.append(f"Not drawn, {spared} already asked of the same thing by a library question above.")
        return found

    drawn = []
    for name, applies in judged.items():
        for thing in applies:
            each = f" (in each of its states: {', '.join(lasting[slug(thing)])})" if slug(thing) in lasting else ""
            drawn.append(f"- L.{name}.{slug(thing)}: {thing}{each}: {by_id[name]['question']}")
    lines += section("From the library", drawn, 0, "Not gone through." if kept.get("skipped") else None)[1:]

    drawn, spared = [], 0
    for value in kept["values"]:
        for way in KINDS.get(value["kind"], KINDS["other"]):
            if already(value["name"], way):
                spared += 1
                continue
            drawn.append(f"- V.{slug(value['name'])}.{way}: `{value['name']}` ({value['from']}) {WAYS[way]}: what does the product do, and what is the person told?")
    for way in SETTINGS[1]:
        if set(judged).intersection(name for name in SAME_SETTINGS[way] if judged.get(name)):
            spared += 1
            continue
        drawn.append(f"- V.{SETTINGS[0]}.{way}: any setting the build reads {WAYS[way]}: what does the product do at start, and who is told?")
    lines += section("Each value taken in, each way it can be wrong", drawn, spared)

    drawn, spared = [], 0
    exposed = classes(kept["values"])
    for name, members in exposed.items():
        for key, words in EXITS.items():
            # Asked already when a kept library question asks it of the class, or of every value in it.
            if already(name, key) or all(already(member, key) for member in members):
                spared += 1
                continue
            drawn.append(f"- X.{name}.{key}: can any of {', '.join(f'`{member}`' for member in members)} reach {words}, on the path that works and on each that fails?")
    lines += section("Each class of sensitive values, each place it can leak to", drawn, spared, None if exposed else "No value taken in is marked sensitive.")

    drawn, spared = [], 0
    events = [(slug(name), slug(name), f"what {name} describes is done") for name in criteria(read["slice"])]
    events += [(key, key, words) for key, words in EVENTS.items()]
    events += [(f"{slug(name)}-{key}", key, words % name) for name in committed(read["approach"]) for key, words in OUTSIDE.items()]
    for thing, table in things.items():
        for state, _source, _row in table:
            for name, key, words in events:
                if already(thing, key):
                    spared += 1
                    continue
                drawn.append(f"- S.{slug(thing)}.{state}.{name}: {thing} is `{state}` and {words}: what happens to it, and what is the person shown?")
    lines += section("Each state, each event", drawn, spared, None if things else "No lasting thing has states written for this slice.")

    lines += section("Asked of every slice", [f"- W.{key}: {words}" for key, words in WHOLE.items()], 0)
    lines += section("Carried from research", [f"- {name}: {words}" for name, words in carried(read["research"], {slug(name) for name in committed(read["approach"])})],
                     0, "Nothing was left open.")
    return "\n".join(lines) + "\n"


def cksum(data):
    """The number the system's own `cksum` prints for these bytes, so that the stage script, which
    is plain shell, can tell without this script whether the questions are stale."""
    crc = 0
    size, tail = len(data), bytearray()
    while size:
        tail.append(size & 0xFF)
        size >>= 8
    for byte in bytes(data) + bytes(tail):
        top = ((crc >> 24) ^ byte) << 24
        for _bit in range(8):
            top = ((top << 1) ^ 0x04C11DB7) if top & 0x80000000 else (top << 1)
        crc = ((crc << 8) ^ top) & 0xFFFFFFFF
    return crc ^ 0xFFFFFFFF


def stamp(read, kept_bytes):
    """One mark of every document the questions were drawn from: `cat` of them, through `cksum`."""
    return str(cksum(b"".join(read["documents"]) + kept_bytes))


def load(folder, library=LIBRARY):
    read = read_slice(folder)
    entries = json.loads(pathlib.Path(library).read_text(encoding="utf-8"))
    path = read["questions"] / "kept.md" if read["questions"] else None
    kept = None
    skipped = read["questions"] / "skipped.md" if read["questions"] else None
    if path and path.is_file():
        kept = {**read_kept(path.read_text(encoding="utf-8")), "text": path.read_bytes()}
    elif skipped and skipped.is_file():
        kept = {"values": [], "others": {}, "library": [], "text": skipped.read_bytes(), "skipped": True}
    return read, entries, kept


def state(folder, library=LIBRARY):
    read, _entries, kept = load(folder, library)
    if kept is None:
        return "none"
    drawn = read["questions"] / "questions.md"
    if not drawn.is_file():
        return "kept"
    match = re.search(re.escape(STAMP).replace("%s", "([0-9]+)"), drawn.read_text(encoding="utf-8"))
    if match and match.group(1) == stamp(read, kept["text"]):
        return "skipped" if kept.get("skipped") else "drawn"
    return "stale: a document of the slice or kept.md changed after the questions were drawn"


def show(kinds, out, library=None):
    """The questions of the kinds named, a line each."""
    entries = json.loads(pathlib.Path(library or LIBRARY).read_text(encoding="utf-8"))
    code = 0
    for kind in kinds:
        found = [entry for entry in entries if entry["action"] == kind]
        if not found:
            print(f"{kind}: the library has no such kind", file=out)
            code = 1
            continue
        print(f"\n{kind}", file=out)
        for entry in found:
            print(f"  {entry['id']}: {entry['question']}", file=out)
    return code


def main(arguments, out=sys.stdout):
    if len(arguments) < 2 or arguments[0] not in ("things", "library", "draw", "check", "state"):
        print(__doc__, file=out)
        return 2
    if arguments[0] == "library":
        return show(arguments[1:], out)
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
        print("and to any value or other thing kept.md lists.\n\nThe library's kinds of action, each with how many questions it has:", file=out)
        kinds = {}
        for entry in entries:
            kinds[entry["action"]] = kinds.get(entry["action"], 0) + 1
        print("  " + ", ".join(f"{kind} ({count})" for kind, count in kinds.items()), file=out)
        print("Read every kind, four or five at a time: questions.py library KIND KIND ...", file=out)
        return 0
    if kept is None:
        print("no kept.md in the slice's questions folder: nothing to draw from", file=out)
        return 1
    found = [] if kept.get("skipped") else problems(kept, known(read), entries, criteria(read["slice"]) + list(read["research"]))[0]
    if found:
        print("\n".join(found), file=out)
        return 1
    text = draw(read, kept, entries)
    target = read["questions"] / "questions.md"
    if command == "draw":
        count = {mark: sum(line.startswith(f"- {mark}.") for line in text.splitlines()) for mark in "LVXSWC"}
        spared = sum(int(number) for number in re.findall(r"^Not drawn, (\d+) ", text, re.M))
        said = (f"{sum(count.values())} questions: {count['L']} from the library, {count['V']} of values, {count['X']} of leaks, "
                f"{count['S']} of states, {count['W']} of every slice, {count['C']} carried from research; "
                f"{spared} not drawn, already asked by the library")
        try:
            target.write_text(text, encoding="utf-8", newline="\n")
        except OSError as error:
            # A shell that may not write the project: the drawing is right, and is said not to be kept.
            print(f"drawn, and not written ({target}: {error.strerror}): {said}. Say so; do not write it by hand.", file=out)
            return 0
        print(f"drawn: {target}: {said}", file=out)
        return 0
    if not target.is_file() or target.read_text(encoding="utf-8") != text:
        print("questions.md is not what the script draws from the documents as they stand: draw it again", file=out)
        return 1
    print("ok", file=out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
