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
    # Added with the security pass: kad's documents named both, and the five above reach neither.
    "replies": "a reply that succeeded, to whoever asked",
    "stored": "where it is stored, and every copy made of that",
}
# The security pass (security.md, beside kept.md). Facts about the slice, each yes or no with its
# source: a fact that holds draws its questions, always the same ones. Each names the requirement of
# OWASP's verification standard 5.0.0 it rests on, or kad's security documents where the standard
# has none.
FACTS = {
    "browser": ("a person uses it in a web browser", (
        ("context", "What stops a reply meant as data, or a file someone submitted, from being shown and run as a page when its address is opened directly?", "V3.2.1"),
        ("page-policy", "From where may the page load and run code, and what does the browser do with anything else?", "V3.4.3"),
        ("framing", "May another site show this product inside a page of its own, and what prevents it?", "V3.4.6"),
        ("type-guessing", "How is the browser kept from treating a reply as a different type from the one it was sent as?", "V3.4.4"),
        ("came-from", "What does the browser tell other sites about the address a person came from, and is anything sensitive in that address?", "V3.4.5"),
        ("other-sites", "Which other sites' pages may call this product and read its replies, and how are all the rest refused?", "V3.4.2, V3.5.1"),
        ("messages", "Does the page take messages from other windows, and how does it know which to trust?", "V3.5.5"),
        ("others-code", "Which code or styles on the page come from another party, and what stops a changed copy from running with everything the page can reach?", "V3.6.1"),
        ("sent-on", "Can the product send a person on to an address that someone else supplied?", "V3.7.2"),
        ("kept-by-browser", "What does the browser keep of a page that showed sensitive data, and for how long?", "V14.3.2"),
        ("known-by", "What does the product keep in the browser to know a person by, and what else can read it or cause it to be sent?", "V3.3.2, V3.3.4"),
    )),
    "network": ("it answers requests at a network address, on one machine or many", (
        ("answers-to", "At which addresses and under which host names does the product answer, and what does it do with a request that names another?", "kad"),
        ("transport", "Is every connection to it encrypted, and what happens to one that is not?", "V12.2.1"),
        ("in-between", "Which facts about a request does it take from something in between (the sender's address, the host first asked for), and can the sender set them?", "V4.1.3, V15.3.4"),
        ("kinds-of-request", "Which kinds of request does each address accept, and what happens to the others?", "V4.1.4"),
        ("left-on", "What can be reached that nobody meant to offer: a diagnostic mode, a listing of files, the history of the source, pages of documentation or measurement, test code?", "V13.4.1 to V13.4.5, V15.2.3"),
        ("gives-away", "What does a reply reveal about what the product is built from, a refusal included?", "V13.4.6"),
    )),
    "calls-out": ("it calls another system", (
        ("where", "Which outside addresses may the product call, and what stops it calling any other?", "V13.2.4"),
        ("supplied", "Can a person give the product an address to fetch or call, and what could they reach through it?", "V13.1.1"),
        ("follows", "Does the product follow a redirect an outside system gives it, and to where?", "V15.3.2"),
        ("proves", "How does the product know that the system which answered is the one it meant to call?", "V12.3.2"),
        ("their-sign-in", "Does what a person types to sign in to the other system (a password, a code) ever pass through this product, and is any of it kept or recorded?", "kad"),
        ("first-given", "By which route does each credential for the other system first reach the product, and where else does that route leave a copy (a command line, a history, a file)?", "kad"),
    )),
    "dependency": ("it adds a component someone else wrote", (
        ("known-flaw", "When a component the product uses is found to have a known flaw, how is that learned, and how soon is the component replaced?", "V15.1.1"),
        ("inventory", "Is there a list of every component used, those they bring with them included, and of where each comes from?", "V15.1.2"),
        ("look-alike", "What makes sure each component is fetched from the place intended, and is the one intended?", "V15.2.4"),
        ("trusted-most", "Which components are trusted with the most (they see credentials, read outside data, run when installed), and what limits them?", "V15.1.4, V15.2.5"),
    )),
    "several-people": ("more than one person uses it, or one person acts for several", (
        ("fields", "Within a record a person may see or change, are there fields they may not?", "V8.2.3"),
        ("groups", "Can one group's use ever show or change what belongs to another group?", "V8.4.1"),
    )),
    "unguessable": ("it makes a value meant to be impossible to guess", (
        ("made", "Which values are meant to be impossible to guess (a link, a code, a session, an identifier), and how is each one made?", "V11.5.1"),
    )),
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


def read_security(text):
    """security.md as written by a session: the facts about the slice, and what someone who means harm would want."""
    parts = {heading.lower(): lines for heading, lines in sections(text).items()}

    def part(word):
        return next((lines for heading, lines in parts.items() if word in heading), [])

    facts = [{"fact": slug(row[0].strip("` ")), "holds": row[1].strip("` *").lower(), "source": row[2]} for row in rows(part("facts")) if len(row) >= 3]
    harm = [{"wanted": row[0].strip("` "), "through": row[1].strip("` "), "worst": row[2].strip(), "asked": row[3].strip()}
            for row in rows(part("harm")) if len(row) >= 4]
    return {"facts": facts, "harm": harm, "skipped": bool(re.search(r"(?im)^skipped at the user's word", text))}


def insecure(security, kept, names=()):
    """Why security.md cannot be drawn from: every fact once, yes or no, with its source; every class of sensitive
    values wanted by someone or said not to be; every other thing come through or said not to be; every name a known one.
    What is wanted need not be a value: a thing the slice keeps or commits to (money given back, a place taken) is wanted too,
    and `nothing` is what a thing gives that is not worth having, dismissed with the reason."""
    if security.get("skipped"):
        return []
    found, seen = [], set()
    for row in security["facts"]:
        if row["fact"] not in FACTS:
            found.append(f"{row['fact']}: not one of the facts ({', '.join(FACTS)})")
            continue
        if row["fact"] in seen:
            found.append(f"{row['fact']}: said twice")
        seen.add(row["fact"])
        if row["holds"] not in ("yes", "no"):
            found.append(f"{row['fact']}: holds is `yes` or `no`; where the documents do not say, it is `yes`")
        if not row["source"].strip():
            found.append(f"{row['fact']}: no source: the criterion or the document's line that says so")
    found += [f"{fact}: not said (a row of the facts: {FACTS[fact][0]})" for fact in FACTS if fact not in seen]
    wanted, through = classes(kept["values"]), set(kept["others"])
    members = {slug(member): name for name, names in wanted.items() for member in names}
    covered, come = set(), set()
    for row in security["harm"]:
        prize, way = slug(row["wanted"]), slug(row["through"])
        if prize in wanted or prize in members:
            covered.add(members.get(prize, prize))
        elif prize == "nothing":
            if not re.match(r"(?i)no\s*:", row["asked"]):
                found.append(f"nothing through {row['through']}: a row that wants nothing is dismissed, `no: ` and why")
        elif prize not in names and prize not in through and prize not in {slug(value["name"]) for value in kept["values"]}:
            found.append(f"{row['wanted']}: wanted, and no class of sensitive values, value, other thing of kept.md or thing the "
                         "documents name has that name (`nothing`, dismissed, where a thing gives nothing worth having)")
        if way in through or way in {slug(value["name"]) for value in kept["values"]}:
            come.add(way)
        elif way not in ("", "nothing"):
            found.append(f"{row['through']}: come through, and no other thing or value of kept.md has that name")
        if not row["worst"]:
            found.append(f"{row['wanted']} through {row['through']}: the worst from there is not said")
        if not re.match(r"(?i)(yes\b|no\s*:\s*\S)", row["asked"]):
            found.append(f"{row['wanted']} through {row['through']}: asked is `yes`, or `no: ` and why it is dismissed")
    found += [f"{name}: a class of sensitive values nobody is said to want: a row of its own, dismissed with the reason if so" for name in wanted if name not in covered]
    found += [f"{name}: another thing of the slice nothing is said to come through: a row of its own, dismissed with the reason if so" for name in sorted(through - come)]
    return found


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
    # A criterion nothing in the file names was not gone through: one added since, most often.
    flat = re.sub(r"[^a-z0-9]+", "-", bytes(kept.get("own") or kept.get("text") or b"").decode("utf-8", "replace").lower())
    for name, what in names.items():
        if what.startswith("criterion ") and kept.get("text") and not re.search(rf"(?<![a-z0-9]){re.escape(name)}(?!\d)", flat):
            found.append(f"{what[10:]}: no thing kept, value, other thing or question of kept.md names this criterion: "
                         "go through it, and change only what it brings")
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

    security = kept.get("security")
    if security is not None:
        holds = {row["fact"] for row in security["facts"] if row["holds"] != "no"} if not security.get("skipped") else set(FACTS)
        drawn = [f"- F.{fact}.{key}: {words}" for fact, (_what, asks) in FACTS.items() if fact in holds for key, words, _rests in asks]
        lines += section("By what the slice is", drawn, 0, "None of the facts holds for this slice.")
        drawn = [f"- T.{slug(row['wanted'])}.{slug(row['through'])}: someone after `{row['wanted']}` comes through `{row['through']}`: {row['worst'].rstrip('.')}. "
                 "What stops it, and how would anyone know it was tried?"
                 for row in security["harm"] if row["asked"].lower().startswith("yes")]
        lines += section("What someone who means harm would want", drawn, 0,
                         "Skipped at the user's word: a risk for the owner's list." if security.get("skipped") else "Nothing was found worth asking.")

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


def with_security(read, kept):
    """kept, with security.md beside it when there is one: its bytes join the mark, after kept.md's."""
    path = read["questions"] / "security.md" if read["questions"] else None
    if kept is None or not (path and path.is_file()):
        return kept
    return {**kept, "security": read_security(path.read_text(encoding="utf-8")), "text": kept["text"] + path.read_bytes(), "own": kept["text"]}


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
    return read, entries, with_security(read, kept)


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
    if kept.get("security") is not None and not found:
        found = insecure(kept["security"], kept, known(read))
        if found:   # the questions stage may meet these, after a change: they are the security stage's to put right
            found = ["security.md, beside kept.md, no longer fits it (the security stage's text says how each is put right):"] + found
    if found:
        print("\n".join(found), file=out)
        return 1
    text = draw(read, kept, entries)
    target = read["questions"] / "questions.md"
    if command == "draw":
        count = {mark: sum(line.startswith(f"- {mark}.") for line in text.splitlines()) for mark in "LVXSFTWC"}
        spared = sum(int(number) for number in re.findall(r"^Not drawn, (\d+) ", text, re.M))
        said = (f"{sum(count.values())} questions: {count['L']} from the library, {count['V']} of values, {count['X']} of leaks, "
                f"{count['S']} of states, "
                + (f"{count['F']} by what the slice is, {count['T']} of what someone would want, " if kept.get("security") is not None else "")
                + f"{count['W']} of every slice, {count['C']} carried from research; "
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
