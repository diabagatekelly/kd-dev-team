#!/usr/bin/env python3
"""The design of a slice: what has no home yet, what does not hold, and the drawing once all does.

A session writes `NNN_design.md` in the slice's folder: the parts the slice is made of, what crosses
between them, and the decisions taken on the way. Everything the earlier stages settled is given a
part that is its home, by name, so that nothing is left to whoever builds it.

    ## Importance
    1. <a part of the slice>: <the harm a defect there does>         most important first, two or more

    ## C1: <named for what it is in the product, never for its technical role>
    Side: strategic | tactical | wiring          strategic: unchanged if the store, the framework or the provider were swapped
    Does: <what it is responsible for>
    Home of: renew-and-pay / 1, A12, A20-A24, T2 the slice's criteria, the answers (with their criteria), the open tests
    Holds: a renewal payment: pending, settled; a season ticket: renewed       the states it keeps
    Sees: credentials, her-details               the classes of sensitive values that pass through it
    Uses: C2, B1                                 a strategic part uses strategic parts and boundaries it owns, nothing else
    Implements: B1                               (tactical) the boundary it stands behind
    Isolates: PayRight                           (tactical) the one place that knows a thing the slice is committed to
    Leans on: payright F6 "its document's own words"; T2; unknown: <what is assumed>
    Either way: <what it does so that it is safe whichever is true>    (with `unknown:`)

    ## B1: <what is asked across it, in the product's words>
    Owned by: C1                                 the side that calls through it
    Crosses: <plain data, named>
    Needs: <what the slice needs of whatever stands behind it>
    Technology: forced: <what in this slice forces a choice now> | not forced: <why one held in memory satisfies this slice's tests>

    ## D1: <the decision, said as the decision>
    Kind: chosen | owner
    Says: <what is chosen, or what is to decide>
    Instead of: <each way not taken, with the concrete reason>          (chosen)
    Because: <why>                                                      (chosen)
    Costs: <what it makes harder, or closes off>                        (chosen)
    Architectural: yes | no: <why>     Significant: yes | no: <why>     Non-obvious: yes | no: <why>     (chosen; three yes earn a record)
    Keeps apart: <the two things that could run over the same state, and what keeps them apart>
    Two at once: ...   Crash: ... (a line a step)   Stopped while waiting: ...   Leftover: ...   Reused name: ...   (with Keeps apart)
    Options: <one> | <another>   Recommended: ...   If left: ...   Harm: high | medium | low               (owner)
    Decided: <the choice> (the user, DATE: "their words")                                                 (owner, once they have said)

    ## At once              `Nothing: <why>`, or the decisions that keep two things apart (D2)
    ## Tests                `Real: ...` and `Faked: ...`, the things committed to named among the faked, at their wire
    ## Kept for later slices    what a later slice will read of this one, or `none: <why>`
    ## Already there        (a project with code) what exists that the slice touches
    ## No home              `- A14, renewal-payment.lost: <why nothing in this slice is its home>`
    ## Goes back            `- requirements | slice | approach | research | answers: <what the design found that is theirs to change>`

Usage:
    python3 -I design.py next SLICE [HOW-MANY]   what has no home yet, and what does not hold as written
    python3 -I design.py draw SLICE              refuse what does not hold; else write NNN_designed.md beside it
    python3 -I design.py state SLICE             none | written N of M | drawn, N waiting, N back | stale

A user who says to skip the stage: the file is one line, `Skipped at the user's word, DATE: "their
words"`, and the drawing says that nothing was designed.

No model, no cost.
"""
import importlib.util
import os
import pathlib
import re
import sys

_spec = importlib.util.spec_from_file_location("openfacts", pathlib.Path(__file__).resolve().parent.parent / "openfacts" / "openfacts.py")
openfacts = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(openfacts)
answers, questions = openfacts.answers, openfacts.questions

SIDES = ("strategic", "tactical", "wiring")
KINDS = ("chosen", "owner")
CHECKS = ("Architectural", "Significant", "Non-obvious")
ORDERS = ("Two at once", "Crash", "Stopped while waiting", "Leftover", "Reused name")
FIELDS = ("Side", "Does", "Home of", "Holds", "Sees", "Uses", "Implements", "Isolates", "Leans on", "Either way",
          "Owned by", "Crosses", "Needs", "Technology",
          "Kind", "Says", "Instead of", "Because", "Costs", *CHECKS, "Keeps apart", *ORDERS,
          "Options", "Recommended", "If left", "Harm", "Decided")
FIELD = re.compile(r"(" + "|".join(sorted(FIELDS, key=len, reverse=True)) + r")\s*:\s*(.*)$")
BACK = ("requirements", "slice", "approach", "research", "answers")
STAMP = "<!-- drawn from: %s; waiting: %d; back: %d -->"
# A part named for its technical role says nothing of the product (kad's Screaming Architecture: the names that fail outright).
ROLES = ("handler", "controller", "service", "manager", "repository", "utils", "util", "helper", "helpers")
# An order of events answered so is a hole: the mechanism changes, or the owner accepts it in so many words.
HOLE = re.compile(r"\bboth (proceed|run|go on|continue|write)|\bnobody (would |will |can )?(know|notice|tell)|\bstuck until|\buntil someone|\bno one (would |will )?(know|notice)", re.I)
# The design says how the slice is made up, never how it is written: these belong to the build.
CODE = re.compile(r"^\s*```|\b[\w/-]+\.(py|ts|tsx|js|jsx|go|rb|java|cs|rs|sql|json|ya?ml|toml)\b|\b[a-z]+[A-Z]\w*\(|\b[a-z]+_[a-z_]+\(")
CONCURRENCY = "L.concurrency-"


def find(folder):
    """The slice's design and where its drawing goes, each a path or None."""
    folder = pathlib.Path(folder).resolve()
    written = sorted(folder.glob("[0-9]*_design.md"))
    if not written:
        return None, None
    return written[-1], written[-1].with_name(written[-1].name.replace("_design.md", "_designed.md"))


def read(text):
    """(the blocks as written: [{name, letter, title, line, fields}], the other sections: {heading in lower case: its lines})."""
    blocks, sections, current, last, section = [], {}, None, None, None
    for number, line in enumerate(text.splitlines(), 1):
        head = re.match(r"## ([CBD])(\d+)\s*:?\s*(.*)$", line)
        if head:
            current = {"name": head.group(1) + head.group(2), "letter": head.group(1), "title": head.group(3).strip(), "line": number, "fields": {}}
            blocks.append(current)
            last, section = None, None
            continue
        if line.startswith("## "):
            current, last, section = None, None, sections.setdefault(line[3:].strip().lower(), [])
            continue
        if line.startswith("#"):
            current, last, section = None, None, None
            continue
        if section is not None:
            if line.strip():
                section.append(line.strip())
            continue
        if current is None:
            continue
        field = FIELD.match(line)
        if field:
            last = current["fields"].setdefault(field.group(1), [])
            last.append(field.group(2).strip())
        elif line.strip() and last is not None and line[:1] in " \t":
            last[-1] = (last[-1] + " " + line.strip()).strip()
    return blocks, sections


def one(block, field):
    return " ".join(block["fields"].get(field, [])).strip()


def whole(block):
    """Every word of a block, its title too."""
    return " ".join([block["title"], *(" ".join(values) for values in block["fields"].values())])


def named(text):
    """The ids a field names, ranges spread out: criteria (`item / 2`), answers (`A12`, `A20-A24`), tests (`T2`), states (`thing.state`)."""
    found = []
    for each in filter(None, (part.strip().strip("`*. ") for part in re.split(r"[,;]", text))):
        span = re.fullmatch(r"A(\d+)\s*(?:-|to|–)\s*A?(\d+)", each)
        if span and int(span.group(1)) <= int(span.group(2)) <= int(span.group(1)) + 500:
            found += [f"A{number}" for number in range(int(span.group(1)), int(span.group(2)) + 1)]
        else:
            found.append(re.sub(r"\s*/\s*", " / ", each))
    return found


def held(text):
    """The states a `Holds:` names: `a renewal payment: pending, settled; a season ticket: renewed` as ['renewal-payment.pending', ...]."""
    found = []
    for part in text.split(";"):
        thing, colon, states = part.partition(":")
        if colon:
            found += [f"{questions.slug(thing)}.{state.strip('`*. ')}" for state in re.split(r",|\band\b", states) if state.strip("`*. ")]
    return found


def load(folder):
    folder = pathlib.Path(folder).resolve()
    document, designed = find(folder)
    facts = openfacts.load(folder)
    slice_read = questions.read_slice(folder)
    kept_file = slice_read["questions"] / "kept.md" if slice_read["questions"] else None
    kept = questions.read_kept(kept_file.read_text(encoding="utf-8")) if kept_file is not None and kept_file.is_file() else {"values": [], "lasting": None}
    blocks, sections = read(document.read_text(encoding="utf-8")) if document else ([], {})
    drawn = [path for path in (facts["answered"], facts["tested"] if facts["document"] else None, document) if path is not None and path.is_file()]
    return {"folder": folder, "document": document, "designed": designed, "facts": facts, "slice": slice_read, "kept": kept,
            "blocks": blocks, "sections": sections, "mark": str(questions.cksum(b"".join(path.read_bytes() for path in drawn)))}


CODE_FILES = {".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".kt", ".rb", ".php", ".cs", ".swift", ".c", ".cc", ".cpp", ".h", ".sh", ".sql", ".html", ".css"}
NOT_CODE = {"node_modules", "venv", "dist", "build", "target", "vendor", "__pycache__"}


def code(read, most=5):
    """Files of code the project already has beside its planning folder, the first few: a design that never read them names anew what is there."""
    planning = read["folder"].parent
    found = []
    for top, folders, files in os.walk(planning.parent):
        folders[:] = sorted(each for each in folders if not each.startswith(".") and each not in NOT_CODE and pathlib.Path(top, each) != planning)
        for each in sorted(files):
            if pathlib.Path(each).suffix.lower() in CODE_FILES:
                found.append(pathlib.Path(top, each).relative_to(planning.parent).as_posix())
                if len(found) == most:
                    return found
    return found


def wanted(read):
    """{id: what it is} for everything the earlier stages settled that a part of the design is the home of."""
    found = {name: "a criterion of the slice" for name in questions.criteria(read["slice"]["slice"])}
    tests = {openfacts.one(block, "Answer").strip("` "): block for block in read["facts"]["blocks"]}
    for answer in read["facts"]["answers"]:
        kind, name = answers.one(answer, "Kind").lower(), answer["name"]
        says = answers.one(answer, "Says")
        if kind == "chosen" or (kind == "fact" and answer["fields"].get("Criterion")):
            found[name] = f"{kind}: {says}"
        elif kind == "owner" and answers.one(answer, "Decided"):
            found[name] = f"decided by the owner: {answers.one(answer, 'Decided')}"
        elif kind == "test":
            block = tests.get(name)
            either = f" Either way: {openfacts.one(block, 'Either way')}" if block else ""
            found[block["name"] if block else name] = f"an open fact ({answers.one(answer, 'Harm') or 'harm not said'}): {says}{either}"
    for thing, table in questions.states(read["slice"]["research"].get("states.md", ""))[0].items():
        for state, _source, _row in table:
            found[f"{questions.slug(thing)}.{state}"] = f"a state of {thing}"
    return found


def homes(read):
    """({id: the parts that are its home}, {id: why it has none})."""
    given, none = {}, {}
    for block in read["blocks"]:
        if block["letter"] != "C":
            continue
        for name in [*named(one(block, "Home of")), *held(one(block, "Holds"))]:
            given.setdefault(name, []).append(block["name"])
    for line in read["sections"].get("no home", []):
        names, colon, why = line.lstrip("-* ").partition(":")
        for name in named(names) if colon else []:
            none[name] = why.strip()
    return given, none


def outside(read):
    """{short name: name} of the things the slice is committed to."""
    return {questions.slug(name): name for name in questions.committed(read["slice"]["approach"])}


def speaks_of(text, thing):
    return re.search(r"(?<![\w-])" + re.escape(thing) + r"(?![\w-])", text, re.I) is not None


def leans(read, block, say):
    """What a block leans on: checked as an answer's `Rests on` is, and the things assumed with no fact returned."""
    value, unknown = one(block, "Leans on"), []
    research = read["slice"]["research"]
    facts = {name[:-3].lower(): set(re.findall(r"^\s*[-*] ([FOS]\d+)\b", text, re.M)) for name, text in research.items()}
    words = answers.said_by(read["slice"])
    open_tests = {block_["name"] for block_ in read["facts"]["blocks"] if openfacts.one(block_, "Result").lower().startswith("open")}
    open_tests |= {answer["name"] for answer in read["facts"]["answers"] if answers.one(answer, "Kind").lower() == "test"}
    for entry in filter(None, (each.strip() for each in value.split(";"))):
        if re.match(r"unknown\b", entry, re.I):
            unknown.append(entry.partition(":")[2].strip() or entry)
            continue
        if re.fullmatch(r"`?[TA]\d+`?", entry):
            if entry.strip("`") not in open_tests:
                say(f"leans on {entry.strip('`')}, which is no open test of the slice: name the fact that settled it, with its words")
            continue
        cited = [(stem.lower().removesuffix(".md"), mark) for stem, marks in re.findall(r"([A-Za-z][\w.-]*),? (?:fact )?((?:[FOS]\d+(?:,? (?:and |or )?)?)+)", entry)
                 for mark in re.findall(r"[FOS]\d+", marks)]
        if not cited:
            say(f"`Leans on` gives a fact of a research document with its words (`payright F6 \"...\"`), an open test (`T2`) or `unknown: <what is assumed>`; it says '{entry[:60]}'")
            continue
        for stem, mark in cited:
            if stem not in facts:
                say(f"'{stem}' is no research document of the slice ({', '.join(sorted(facts)) or 'it has none'})")
            elif mark not in facts[stem]:
                say(f"{stem} has no {mark}: a research fact is named as its document has it")
            elif mark.startswith("O"):
                say(f"{stem} {mark} is an open point of the research: lean on its test (`T2`), or `unknown:` with what is done either way")
        quoted = [each.strip(" .,;") for each in re.findall(r'"([^"]*)"', answers.plain(entry)) if len(each.strip(" .,;")) >= 12]
        if not quoted:
            say(f"a fact leaned on is given with its document's own words, in quotes (twelve letters or more): '{entry[:60]}'")
        for each in quoted:
            if not any(each in words.get(stem, "") for stem, _mark in cited):
                say(f"\"{each[:50]}\" is not in the research document named or a page kept for the slice: quote its own words")
    if unknown and not one(block, "Either way"):
        say("what is leaned on and not known says `Either way:` what this does so that it is safe whichever is true")
    return unknown


def waiting(read):
    return [block for block in read["blocks"] if block["letter"] == "D" and one(block, "Kind").lower() == "owner" and not one(block, "Decided")]


def back(read):
    return [line.lstrip("-* ") for line in read["sections"].get("goes back", []) if not re.match(r"[-* ]*(none|nothing)\b", line, re.I)]


def concurrent(read):
    """The answers that settle a question about two things at once and do not dismiss it."""
    return [answer["name"] for answer in read["facts"]["answers"]
            if answers.one(answer, "Kind").lower() != "not here" and CONCURRENCY in answers.one(answer, "Settles")]


def problems(read):
    """(every reason the design cannot be drawn from, a line each; what has no home: {id: what it is}; what is leaned on and not known)."""
    found, seen, unknown = [], set(), []
    blocks = {block["name"]: block for block in read["blocks"]}
    parts = [block for block in read["blocks"] if block["letter"] == "C"]
    side = {block["name"]: one(block, "Side").lower().split(":")[0].split()[0] if one(block, "Side") else "" for block in parts}
    things = outside(read)
    existing = False
    for line in (read["document"].read_text(encoding="utf-8").splitlines() if read["document"] else []):
        if line.startswith("#"):
            existing = line[3:].strip().lower() == "already there"   # code that exists is named as it is
        if not existing and CODE.search(line):
            found.append(f"'{line.strip()[:60]}': the design says how the slice is made up, not how it is written: no code, no file of the code, no signature")
    for block in read["blocks"]:
        name = block["name"]
        say = lambda words: found.append(f"{name} (line {block['line']}): {words}")   # noqa: E731
        if name in seen:
            say("this name is used twice")
        seen.add(name)
        text = whole(block)
        if block["letter"] == "C":
            if side[name] not in SIDES:
                say(f"Side is one of {', '.join(SIDES)}; it says '{one(block, 'Side')}'")
            if not one(block, "Does"):
                say("a part says what it `Does`")
            role = [word for word in re.findall(r"[a-z]+", block["title"].lower()) if word in ROLES]
            if role and side[name] != "wiring":
                say(f"'{block['title']}' is named for a technical role ({role[0]}): name it for what it is in the product; "
                    "if no such name is there, it has no reason of its own to exist yet")
            for used in re.findall(r"\b[CB]\d+\b", one(block, "Uses") + " " + one(block, "Implements")):
                if used not in blocks:
                    say(f"it names {used}, and the design has no such block")
            if side[name] == "strategic":
                for used in re.findall(r"\bC\d+\b", one(block, "Uses")):
                    if side.get(used) in ("tactical", "wiring"):
                        say(f"a strategic part uses {used}, a {side[used]} one: it asks through a boundary it owns (`## B1`, `Owned by: {name}`), which {used} implements")
                for used in re.findall(r"\bB\d+\b", one(block, "Uses")):
                    owner = re.search(r"\bC\d+\b", one(blocks[used], "Owned by")) if used in blocks else None
                    if owner and side.get(owner.group(0)) != "strategic":
                        say(f"{used} is owned by {owner.group(0)}, which is not strategic: a boundary belongs to the side that calls through it")
                for thing in things.values():
                    if speaks_of(text, thing):
                        say(f"a strategic part names {thing}: it does not know what stands behind its boundary. Say what it needs in the product's own words; "
                            f"only the part that `Isolates: {thing}` knows it")
            if one(block, "Isolates") and side[name] != "tactical":
                say("only a tactical part isolates a thing the slice is committed to")
        elif block["letter"] == "B":
            for field in ("Owned by", "Crosses", "Needs", "Technology"):
                if not one(block, field):
                    say(f"a boundary says its `{field}`")
            owner = re.search(r"\bC\d+\b", one(block, "Owned by"))
            if one(block, "Owned by") and (not owner or owner.group(0) not in blocks):
                say(f"Owned by names a part of the design (`C1`); it says '{one(block, 'Owned by')}'")
            if owner and any(owner.group(0) == part["name"] and name in one(part, "Implements") for part in parts):
                say(f"{owner.group(0)} both owns it and implements it: the side that calls owns it, the other side implements it")
            if one(block, "Technology") and not re.match(r"(not )?forced\s*:\s*\S", one(block, "Technology"), re.I):
                say("Technology is `forced: <what in this slice forces a choice now>` or `not forced: <why one held in memory satisfies this slice's tests>`")
            for thing in things.values():
                if speaks_of(one(block, "Crosses"), thing):
                    say(f"what crosses names {thing}: only plain data crosses, in the product's own words; its shapes are translated at the edge")
        else:
            kind = one(block, "Kind").lower()
            if kind not in KINDS:
                say(f"Kind is one of {', '.join(KINDS)}; it says '{one(block, 'Kind')}'")
                continue
            for field in (("Says", "Instead of", "Because", "Costs", *CHECKS) if kind == "chosen" else ("Says", "Options", "Recommended", "If left", "Harm")):
                if not one(block, field):
                    say(f"a decision that is {kind} says its `{field}`")
            for check in CHECKS:
                if one(block, check) and not re.match(r"(yes|no)\b", one(block, check), re.I):
                    say(f"{check} is yes or no, then why: a check that feels borderline gets the answer it falls on")
            if kind == "owner" and one(block, "Options") and len([each for each in one(block, "Options").split("|") if each.strip()]) < 2:
                say("a decision for the owner has at least two options, separated by `|`: with one, it is chosen and recorded")
            if kind == "owner" and one(block, "Harm") and one(block, "Harm").lower().split()[0].strip(".,:;") not in answers.HARMS:
                say(f"Harm is one of {', '.join(answers.HARMS)}")
            if one(block, "Decided") and kind != "owner":
                say("only a decision for the owner is `Decided:`, and by them")
            if one(block, "Decided") and not openfacts.BY_THE_USER.search(one(block, "Decided")):
                say('Decided ends with who said it, when and in which words: (the user, YYYY-MM-DD: "their words")')
            if one(block, "Keeps apart"):
                for order in ORDERS:
                    if not one(block, order):
                        say(f"what keeps two things apart is walked through its bad orders before it is chosen: `{order}:` says what state is left and who would notice")
                holes = [order for order in ORDERS for line in block["fields"].get(order, []) if HOLE.search(line)]
                if holes and kind == "chosen":
                    say(f"`{holes[0]}` leaves a hole (both go on, nobody would know, or stuck until someone sees to it): change what keeps them apart until "
                        "no line reads so, or make the decision the owner's (`Kind: owner`), the hole said as what they accept")
        if block["letter"] in "CD" or one(block, "Leans on"):
            spoken = [thing for thing in things.values() if speaks_of(text, thing)]
            if (spoken or one(block, "Isolates")) and not one(block, "Leans on"):
                say(f"it speaks of {spoken[0] if spoken else one(block, 'Isolates')}: `Leans on` gives the facts of its research document it rests on, with their "
                    "words, an open test, or `unknown: <what is assumed>`")
            unknown += [(name, each, one(block, "Either way")) for each in leans(read, block, say)]
    for stem, thing in things.items():
        isolating = [block["name"] for block in parts if speaks_of(one(block, "Isolates"), thing)]
        if parts and not isolating:
            found.append(f"{thing} is committed to and no part isolates it: one tactical part is the only place that knows it (`Isolates: {thing}`)")
    # Everything settled before has its home.
    needed, (given, none) = wanted(read), homes(read)
    for name in sorted({*given, *none} - set(needed)):
        found.append(f"'{name}' is given a home and is nothing the slice has: a criterion (`item / 1`), an answer (`A12`), an open test (`T2`), a state (`thing.state`)")
    for name, why in none.items():
        if name in needed and not why:
            found.append(f"{name} is under `## No home` with no reason")
    left = {name: what for name, what in needed.items() if name not in given and name not in none}
    if left:
        found.append(f"{len(left)} things settled before have no home ({', '.join(list(left)[:8])}): `next` lists them")
    classes = questions.classes(read["kept"]["values"])
    seen_classes = {questions.slug(each) for block in parts for each in re.split(r"[,;]", one(block, "Sees")) if each.strip()}
    for name in classes:
        if parts and name not in seen_classes:
            found.append(f"no part `Sees: {name}` ({', '.join(classes[name])}): every part a class of sensitive values passes through says so")
    # The sections every design has.
    sections = read["sections"]
    if len([line for line in sections.get("importance", []) if re.match(r"(\d+[.)]|[-*])\s+\S", line)]) < 2:
        found.append("`## Importance` orders the parts of the slice by the harm a defect there does, most important first: two lines or more")
    at_once = " ".join(sections.get("at once", []))
    apart = [block["name"] for block in read["blocks"] if block["letter"] == "D" and one(block, "Keeps apart")]
    if not at_once:
        found.append("`## At once` says whether two things can run over the same state at the same time: `Nothing: <why>`, or the decisions that keep them apart")
    elif not apart and concurrent(read):
        found.append(f"{len(concurrent(read))} answers settle questions about two things at once ({', '.join(concurrent(read)[:6])}) and no decision keeps anything apart: "
                     "a decision with `Keeps apart:` and its orders, or under `## No home` why those answers need none")
    for name in re.findall(r"\bD\d+\b", at_once):
        if name not in apart:
            found.append(f"`## At once` names {name}, which has no `Keeps apart:`")
    tests = " ".join(sections.get("tests", []))
    faked = " ".join(line for line in sections.get("tests", []) if re.match(r"[-* ]*faked\b", line, re.I))
    if not re.search(r"\breal\b\s*:", tests, re.I) or not faked:
        found.append("`## Tests` says what the tests run for real (`Real:` the store, the parts behind their real entry) and what they fake (`Faked:` only what is "
                     "outside: a thing committed to at its wire, the clock, chance)")
    for thing in things.values():
        if faked and not speaks_of(faked, thing):
            found.append(f"`## Tests` does not say {thing} is faked, at its wire: no test of the slice calls the real thing")
    if not sections.get("kept for later slices"):
        found.append("`## Kept for later slices` names what a later slice will read of this one (an identifier, a position reached, where a thing came from), or `none: <why>`")
    if not sections.get("already there") and code(read):
        found.append(f"the project already has code ({', '.join(code(read))}) and the design does not say what of it the slice touches: read it, then "
                     "`## Already there` names what exists and is used under its name, or `none: <why the slice touches nothing of it>`")
    for line in back(read):
        if line.partition(":")[0].strip().lower() not in BACK or not line.partition(":")[2].strip():
            found.append(f"`## Goes back` names the stage whose it is ({', '.join(BACK)}), then what: '{line[:60]}'")
    return found, left, unknown


def later(read):
    """The slices of the set that build on this one: ['2: See which season tickets are not renewed']."""
    number = re.search(r"slice-0*(\d+)$", read["folder"].name)
    sets = sorted(read["folder"].parent.glob("[0-9]*_slices*.md"))
    if not number or not sets:
        return []
    table = [questions.cells_of(line) for line in sets[-1].read_text(encoding="utf-8").splitlines() if line.strip().startswith("|")]
    if not table or "Builds on" not in table[0]:
        return []
    at = table[0].index("Builds on")
    return [f"{row[0]}: {row[1]}" for row in table[2:] if len(row) > at and number.group(1) in re.findall(r"\d+", row[at])]


def drawing(read, unknown):
    """The text of NNN_designed.md and the line said of it."""
    needed, (given, none) = wanted(read), homes(read)
    parts = [block for block in read["blocks"] if block["letter"] == "C"]
    decisions = [block for block in read["blocks"] if block["letter"] == "D"]
    earned = [block for block in decisions if all(re.match(r"yes\b", one(block, check), re.I) for check in CHECKS)]
    criteria = {}
    for answer in read["facts"]["answers"]:
        criteria[answer["name"]] = answer["fields"].get("Criterion", [])
    own = dict(re.findall(r"^\s*[-*] \*\*([a-z0-9-]+ / \d+)\*\*:?\s*(.*)$", read["slice"]["slice"], re.M))
    lines = ["# Designed", "", STAMP % (read["mark"], len(waiting(read)), len(back(read))), "",
             "Drawn by script from the design, the answers and the open facts. Nothing here is written by hand: change the design and draw again.", ""]
    for heading, side in (("Strategic", "strategic"), ("Tactical", "tactical"), ("Wiring", "wiring")):
        these = [block for block in parts if one(block, "Side").lower().startswith(side)]
        if not these:
            continue
        lines += [f"## {heading}", ""]
        for block in these:
            lines += [f"### {block['name']}: {block['title']}", one(block, "Does"), ""]
            for name in dict.fromkeys([*named(one(block, "Home of")), *held(one(block, "Holds"))]):
                if name in own:
                    lines.append(f"- **{name}**: {own[name]}")
                elif name in criteria and criteria[name]:
                    lines += [f"- **{name}**: {criterion}" for criterion in criteria[name]]
                elif name in needed:
                    lines.append(f"- {name}, {needed[name]}")
            for field in ("Sees", "Uses", "Implements", "Isolates", "Leans on", "Either way"):
                if one(block, field):
                    lines.append(f"- {field}: {one(block, field)}")
            lines.append("")
    lines += ["## Boundaries", ""]
    for block in read["blocks"]:
        if block["letter"] == "B":
            lines.append(f"- {block['name']}: {block['title']}. Owned by {one(block, 'Owned by')}. Crosses: {one(block, 'Crosses')} Needs: {one(block, 'Needs')} "
                         f"Technology: {one(block, 'Technology')}")
    lines += ["", "## Decisions that earn a record", ""]
    for block in earned:
        lines += [f"### {block['name']}: {block['title']}", one(block, "Says"), f"Instead of: {one(block, 'Instead of')}", f"Because: {one(block, 'Because')}",
                  f"Costs: {one(block, 'Costs')}", ""]
    lines += [] if earned else ["None.", ""]
    lines += ["## Other decisions", ""]
    for block in decisions:
        if block not in earned and block not in waiting(read):
            said = one(block, "Decided") or one(block, "Says")
            lines.append(f"- {block['name']}: {block['title']}: {said}")
    lines += ["", "## Kept apart, and what each order of events leaves", ""]
    for block in decisions:
        if one(block, "Keeps apart"):
            lines += [f"### {block['name']}: {one(block, 'Keeps apart')}", *[f"- {order}: {line}" for order in ORDERS for line in block["fields"].get(order, [])], ""]
    lines += ["## For the owner, by harm", ""]
    rank = lambda block: answers.HARMS.index(one(block, "Harm").lower().split()[0].strip(".,:;")) if one(block, "Harm") else 2   # noqa: E731
    for block in sorted(waiting(read), key=rank):
        lines += [f"### {block['name']}: {block['title']} ({one(block, 'Harm')})", one(block, "Says"), "",
                  *[f"- {each.strip()}" for each in one(block, "Options").split("|") if each.strip()], "",
                  f"Recommended: {one(block, 'Recommended')}", f"If left: {one(block, 'If left')}", ""]
    lines += [] if waiting(read) else ["Nothing.", ""]
    lines += ["## Leaned on and not known", ""]
    lines += [f"- {name}: {what} Either way: {either}" for name, what, either in unknown] or ["Nothing."]
    lines += ["", "## With no home in this slice", ""]
    lines += [f"- {name}: {why}" for name, why in none.items()] or ["Nothing."]
    lines += ["", "## Goes back", ""]
    lines += [f"- {line}" for line in back(read)] or ["Nothing."]
    for heading in ("at once", "tests", "kept for later slices", "already there"):
        if read["sections"].get(heading):
            lines += ["", f"## {heading.capitalize()}", "", *read["sections"][heading]]
    sides = [one(block, "Side").lower() for block in parts]
    said = (f"{len(parts)} parts ({sum(1 for each in sides if each.startswith('strategic'))} strategic, {sum(1 for each in sides if each.startswith('tactical'))} tactical), "
            f"{sum(1 for block in read['blocks'] if block['letter'] == 'B')} boundaries; {len([name for name in needed if name in given])} things settled before have "
            f"their home, {len([name for name in needed if name in none])} have none in this slice; {len(decisions)} decisions, {len(earned)} earn a record; "
            f"{len(unknown)} things leaned on and not known; {len(waiting(read))} decisions wait for the owner; {len(back(read))} go back to an earlier stage")
    return "\n".join(lines) + "\n", said


def state(folder):
    read = load(folder)
    if read["document"] is None:
        return "none"
    text = read["designed"].read_text(encoding="utf-8") if read["designed"].is_file() else ""
    match = re.search(r"<!-- drawn from: " + read["mark"] + r"; waiting: (\d+); back: (\d+) -->", text)
    if match:
        return f"drawn, {match.group(1)} waiting, {match.group(2)} back"
    if text:
        return "stale: the answers, the open facts or the design changed after it was drawn"
    needed, (given, none) = wanted(read), homes(read)
    return f"written {len([name for name in needed if name in given or name in none])} of {len(needed)}"


def keep(read, text, said, out):
    try:
        read["designed"].write_text(text, encoding="utf-8", newline="\n")
    except OSError as error:
        print(f"drawn, and not written ({read['designed']}: {error.strerror}): {said}. Say so; do not write it by hand.", file=out)
        return 0
    print(f"drawn: {read['designed']}: {said}", file=out)
    return 0


def main(arguments, out=sys.stdout):
    if len(arguments) < 2 or arguments[0] not in ("next", "draw", "state"):
        print(__doc__, file=out)
        return 2
    command, folder = arguments[0], arguments[1]
    if command == "state":
        print(state(folder), file=out)
        return 0
    read = load(folder)
    if read["facts"]["answers_file"] is None:
        print("no answers in the slice's folder: there is nothing to design from yet", file=out)
        return 1
    found, left, unknown = problems(read) if read["document"] else ([], wanted(read), [])
    if command == "next":
        many = int(arguments[2]) if len(arguments) > 2 else 60
        needed = wanted(read)
        print(f"{len(needed) - len(left)} of {len(needed)} things settled before have their home; {len(left)} are left. Each is named in a part's "
              "`Home of:` (a state in its `Holds:`), or under `## No home` with why:", file=out)
        for name, what in list(left.items())[:many]:
            print(f"- {name}: {what}", file=out)
        if len(left) > many:
            print(f"and {len(left) - many} more: give these their homes, then ask again.", file=out)
        classes = questions.classes(read["kept"]["values"])
        if classes:
            print("\nClasses of sensitive values, each named in the `Sees:` of every part it passes through: "
                  + "; ".join(f"{name} ({', '.join(values)})" for name, values in classes.items()), file=out)
        if outside(read):
            print("Committed to, each isolated by one tactical part: " + ", ".join(outside(read).values()), file=out)
        if concurrent(read):
            print(f"Answers that settle questions about two things at once: {', '.join(concurrent(read))}", file=out)
        if code(read):
            print(f"The project already has code ({', '.join(code(read))}): read what the slice will touch before naming a part; what exists is used under "
                  "its name and said under `## Already there`", file=out)
        builds = later(read)
        print("Slices that build on this one: " + ("; ".join(builds) if builds else "none in the set as it stands"), file=out)
        if found:
            print("\nNot holding as written:\n" + "\n".join(found), file=out)
        return 0
    if read["document"] is None:
        print("no design yet: write NNN_design.md in the slice's folder, NNN the next number there", file=out)
        return 1
    text = read["document"].read_text(encoding="utf-8")
    if answers.SKIPPED.search(text) and not read["blocks"]:
        drawn = "\n".join(["# Designed", "", STAMP % (read["mark"], 0, 0), "", text.strip(), "",
                           f"None of the {len(wanted(read))} things settled before has a home: how the slice is made up is left to whoever builds it, a risk accepted.", ""])
        return keep(read, drawn, f"skipped at the user's word: none of the {len(wanted(read))} things settled before has a home", out)
    if found:
        print("\n".join(found), file=out)
        return 1
    drawn, said = drawing(read, unknown)
    return keep(read, drawn, said, out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
