#!/usr/bin/env python3
"""The answers to a slice's questions: what is still to settle, and the drawing once all are.

A session writes `NNN_answers.md` in the slice's folder: one block an answer, and an answer
settles as many of the drawn questions as it truly answers.

    ## A1: <a short title>
    Kind: fact | chosen | owner | test | not here
    Says: <what holds, what is chosen, what is to decide, what is not known, or why it does not arise>
    Rests on: <fact: the document and its line, fact or criterion; chosen: the reason>
    Settles: <ids of questions.md, separated by commas; `L.entry.*` is every thing of that entry>
    Under: <the slice's item a criterion belongs to, or `new: a-name`>
    Criterion: Given ..., when ..., then ...          (none, one or several)
    Options: <one> | <another>                        (owner)
    Recommended: <one of them, and why>               (owner)
    If left: <what happens while it is not decided>   (owner)
    Harm: high | medium | low                         (owner, test)
    Decided: <the choice> (the user, DATE: "their words")   (owner, once they have said)
    Test: <what would be run, against what>           (test)

Usage:
    python3 -I answers.py next SLICE [HOW-MANY]   the questions no answer settles yet, in the drawing's order
    python3 -I answers.py draw SLICE              refuse what does not hold; else write NNN_answered.md beside it
    python3 -I answers.py state SLICE             none | written N of M | drawn | stale

A user who says to skip the stage: the file is one line, `Skipped at the user's word, DATE: "their
words"`, and the drawing says that nothing is answered.

No model, no cost.
"""
import importlib.util
import pathlib
import re
import sys

_spec = importlib.util.spec_from_file_location("questions", pathlib.Path(__file__).resolve().parent.parent / "questions" / "questions.py")
questions = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(questions)

KINDS = ("fact", "chosen", "owner", "test", "not here")
HARMS = ("high", "medium", "low")
NEEDS = {"fact": ("Says", "Rests on"), "chosen": ("Says", "Rests on"), "owner": ("Says", "Options", "Recommended", "If left", "Harm"),
         "test": ("Says", "Test", "Harm"), "not here": ("Says",)}
FIELDS = ("Kind", "Says", "Rests on", "Settles", "Under", "Criterion", "Options", "Recommended", "If left", "Harm", "Test", "Decided")
SKIPPED = re.compile(r"^skipped at the user's word", re.I | re.M)
STAMP = "<!-- drawn from: %s -->"
# A wait, a retry or a giving up with no number is a criterion nobody can check (kad's `numbers-on-waits`).
WAITS = re.compile(r"\b(retr(y|ies|ied)|waits?|waiting|times? out|timeout|polls?|gives? up|tries again|again after|too long|eventually|soon|promptly|quickly)\b", re.I)
UNBOUNDED = "unbounded, owner approved"


def find(folder):
    """The slice's drawn questions, its answers and where the drawing goes, each a path or None."""
    folder = pathlib.Path(folder)
    drawn = sorted(folder.glob("[0-9]*_questions/questions.md"))
    answers = sorted(folder.glob("[0-9]*_answers.md"))
    answered = answers[-1].with_name(answers[-1].name.replace("_answers.md", "_answered.md")) if answers else None
    return (drawn[-1] if drawn else None), (answers[-1] if answers else None), answered


def asked(text):
    """{id: the question's words} for every line of a drawing, in its order."""
    return dict(re.findall(r"^- ([A-Z]\.[^\s:]+): (.*)$", text, re.M))


def read(text):
    """The answers as written: [{name, title, line, fields {name: [values]}, stray [lines]}]."""
    found, current, last = [], None, None
    for number, line in enumerate(text.splitlines(), 1):
        head = re.match(r"## (A\d+)\s*:?\s*(.*)$", line)
        if head:
            current = {"name": head.group(1), "title": head.group(2).strip(), "line": number, "fields": {}, "stray": []}
            found.append(current)
            last = None
            continue
        if current is None or line.startswith("#"):
            current = None if line.startswith("#") else current
            continue
        field = re.match(r"(" + "|".join(FIELDS) + r")\s*:\s*(.*)$", line)
        if field:
            last = current["fields"].setdefault(field.group(1), [])
            last.append(field.group(2).strip())
        elif line.strip() and last is not None and line[:1] in " \t":
            last[-1] = (last[-1] + " " + line.strip()).strip()   # a value carried on to the next line
        elif line.strip():
            current["stray"].append(f"line {number}")
    return found


def one(answer, field):
    return " ".join(answer["fields"].get(field, [])).strip()


def settles(answer, ids):
    """(the ids an answer settles, the ones it names that the drawing does not have)."""
    took, unknown = [], []
    for name in filter(None, (each.strip().strip("`") for each in re.split(r"[,;]", one(answer, "Settles")))):
        if name.endswith(".*"):
            under = [each for each in ids if each.startswith(name[:-1])]
            took += under
            if not under:
                unknown.append(name)
        elif name in ids:
            took.append(name)
        else:
            unknown.append(name)
    return took, unknown


def sources(slice_read):
    """What a fact may rest on: a criterion, a research document, a document of the planning folder."""
    names = set(questions.criteria(slice_read["slice"])) | {name[:-3] for name in slice_read["research"]}
    names |= {name for name in slice_read["research"]}
    folder = slice_read["folder"]
    for path in [*folder.glob("*.md"), *folder.parent.glob("*.md"), *folder.glob("[0-9]*_questions/*.md")]:
        names |= {path.name, re.sub(r"^\d+_", "", path.name)}
    return names


def problems(answers, ids, slice_read):
    """Every reason the answers cannot be drawn from, a line each; none when they hold."""
    found, seen, taken = [], set(), {}
    items = {name.split(" / ")[0] for name in questions.criteria(slice_read["slice"])}
    known = sources(slice_read)
    # What the slice is committed to and has a research document for: an answer that speaks of one
    # rests on a fact that document holds (met on the real plans: one answer in five did not).
    facts = {name[:-3].lower(): set(re.findall(r"^- ([FOS]\d+)\b", text, re.M)) for name, text in slice_read["research"].items()}
    outside = {questions.slug(name): name for name in questions.committed(slice_read["approach"]) if questions.slug(name) in facts}
    for answer in answers:
        name, kind = answer["name"], one(answer, "Kind").lower()
        say = lambda words: found.append(f"{name} (line {answer['line']}): {words}")   # noqa: E731
        if name in seen:
            say("this name is used twice")
        seen.add(name)
        if answer["stray"]:
            say(f"words that belong to no field ({', '.join(answer['stray'])}): a value goes on after its field's name, or indented under it")
        if kind not in KINDS:
            say(f"Kind is one of {', '.join(KINDS)}; it says '{one(answer, 'Kind')}'")
            continue
        for field in NEEDS[kind]:
            if not one(answer, field):
                say(f"a {kind} answer says its `{field}`")
        took, unknown = settles(answer, ids)
        if unknown:
            say(f"settles what the drawing does not ask: {', '.join(unknown)}")
        if not took:
            say("settles no question: every answer names the questions it settles")
        for each in took:
            if each in taken and taken[each] != name:
                say(f"{each} is already settled by {taken[each]}: one answer a question")
            taken.setdefault(each, name)
        if kind == "fact" and one(answer, "Rests on") and not any(source.lower() in one(answer, "Rests on").lower() for source in known):
            say("a fact rests on a document of the slice, by its name: a criterion (`item / n`), a research document, a planning document")
        # A research fact is named with its document: "provider F6" names none (met in the three runs).
        stems = {name[:-3].lower() for name in slice_read["research"]}
        for word in re.findall(r"([A-Za-z][\w.-]*),? (?:fact )?[FOS]\d+\b", one(answer, "Rests on")) if kind == "fact" and stems else []:
            if re.sub(r"\.md$", "", word).lower() not in stems | {"and", "or", "to", "through", "with", "also", "see", "fact", "facts"}:
                say(f"'{word}' is no research document of the slice ({', '.join(sorted(stems))}): a research fact is named with its document")
        if kind in ("fact", "chosen"):
            rests, speaks = one(answer, "Rests on"), " ".join([one(answer, "Says"), *answer["fields"].get("Criterion", [])])
            cited = {(stem.lower().removesuffix(".md"), mark) for stem, marks in re.findall(r"([A-Za-z][\w.-]*),? (?:fact )?((?:[FOS]\d+(?:,? (?:and |or )?)?)+)", rests)
                     for mark in re.findall(r"[FOS]\d+", marks)}
            for stem, mark in sorted(cited):
                if stem in facts and mark not in facts[stem]:
                    say(f"{stem} has no {mark}: a research fact is named as its document has it")
                elif stem in facts and mark.startswith("O"):
                    say(f"{stem} {mark} is an open point of the research: what rests on it is a `test`, or is chosen so as to hold either way")
            for stem, thing in outside.items():
                if re.search(r"\b" + re.escape(thing) + r"\b", speaks, re.I) and not any(doc == stem and mark[0] in "FS" for doc, mark in cited):
                    say(f"it speaks of {thing} and rests on no fact of {stem}.md (`{stem} F1`): name the fact, or leave how {thing} behaves to a `test`")
        owed = [each for each in took if each in ("W.target", "W.obligations")]
        if owed and kind not in ("fact", "owner"):
            say(f"{', '.join(owed)}: a target and an obligation are what the documents say (`fact`) or the owner's (`owner`), never chosen for them")
        if kind in ("owner", "test") and one(answer, "Harm") and one(answer, "Harm").lower().split()[0].strip(".,:;") not in HARMS:
            say(f"Harm is one of {', '.join(HARMS)}")
        if kind == "owner" and one(answer, "Options") and len([each for each in one(answer, "Options").split("|") if each.strip()]) < 2:
            say("a decision for the owner has at least two options, separated by `|`: with one, it is chosen and recorded")
        written = answer["fields"].get("Criterion", [])
        if written and kind not in ("fact", "chosen") and not (kind == "owner" and one(answer, "Decided")):
            say(f"a criterion is written from a fact, a choice or a decision the owner has taken (`Decided:`); from a {kind} answer it waits")
        if one(answer, "Decided") and kind != "owner":
            say("only a decision for the owner is `Decided:`, and by them")
        if one(answer, "Decided") and not re.search(r"\(the user, \d{4}-\d\d-\d\d: \".+\"\)", one(answer, "Decided")):
            say('Decided ends with who said it, when and in which words: (the user, YYYY-MM-DD: "their words")')
        if written and not one(answer, "Under"):
            say("a criterion says which item of the slice it is under (`Under:`), or `new: a-name`")
        under = one(answer, "Under")
        if under and not under.startswith("new:") and under.strip("`* ") not in items:
            say(f"Under names an item of the slice ({', '.join(sorted(items)) or 'it has none yet'}) or `new: a-name`; it says '{under}'")
        for criterion in written:
            if not re.search(r"\bgiven\b.*\bwhen\b.*\bthen\b", criterion, re.I):
                say(f"a criterion is one Given, when, then: '{criterion[:60]}'")
            elif WAITS.search(criterion) and not re.search(r"\d", criterion) and UNBOUNDED not in criterion.lower():
                say(f"a wait, a retry or a giving up has its number, or says `{UNBOUNDED}`: '{criterion[:60]}'")
    return found, taken


def drawing(answers, ids, taken, mark):
    """The text of NNN_answered.md: the criteria, the owner's list, what to test, what was chosen."""
    by_kind = {kind: [answer for answer in answers if one(answer, "Kind").lower() == kind] for kind in KINDS}
    rank = lambda answer: HARMS.index(one(answer, "Harm").lower().split()[0].strip(".,:;"))   # noqa: E731
    count = lambda answer: sum(1 for owner in taken.values() if owner == answer["name"])   # noqa: E731
    lines = ["# Answered", "", STAMP % mark, "",
             "Drawn by script from the answers. Nothing here is written by hand: change the answers and draw again.", ""]
    lines += ["## Criteria", ""]
    number = 0
    for answer in answers:
        for criterion in answer["fields"].get("Criterion", []):
            number += 1
            lines.append(f"- **{one(answer, 'Under')} / {answer['name']}.{number}**: {criterion}")
    lines += [""] if number else ["None.", ""]
    lines += ["## For the owner, by harm", ""]
    waiting = [answer for answer in by_kind["owner"] if not one(answer, "Decided")]
    for answer in sorted(waiting, key=rank):
        lines += [f"### {answer['name']}: {answer['title']} ({one(answer, 'Harm')})", one(answer, "Says"), "",
                  *[f"- {each.strip()}" for each in one(answer, "Options").split("|") if each.strip()], "",
                  f"Recommended: {one(answer, 'Recommended')}", f"If left: {one(answer, 'If left')}",
                  f"Questions waiting on it: {count(answer)}", ""]
    lines += [] if waiting else ["Nothing.", ""]
    lines += ["## Decided by the owner", ""]
    for answer in by_kind["owner"]:
        if one(answer, "Decided"):
            lines.append(f"- {answer['name']}: {answer['title']}: {one(answer, 'Decided')}")
    lines += [""] if len(waiting) < len(by_kind["owner"]) else ["Nothing.", ""]
    lines += ["## To test, by harm", ""]
    for answer in sorted(by_kind["test"], key=rank):
        lines.append(f"- {answer['name']} ({one(answer, 'Harm')}): {one(answer, 'Says')} Test: {one(answer, 'Test')}")
    lines += [""] if by_kind["test"] else ["Nothing.", ""]
    lines += ["## Chosen without asking; the owner can overturn any of these", ""]
    for answer in by_kind["chosen"]:
        lines.append(f"- {answer['name']}: {one(answer, 'Says')} Because: {one(answer, 'Rests on')}")
    lines += [""] if by_kind["chosen"] else ["Nothing.", ""]
    said = (f"{len(answers)} answers settle {len(ids)} questions: {len(by_kind['fact'])} facts, {len(by_kind['chosen'])} chosen, "
            f"{len(waiting)} for the owner, {len(by_kind['owner']) - len(waiting)} decided by the owner, {len(by_kind['test'])} to test, {len(by_kind['not here'])} not here; {number} criteria")
    return "\n".join(lines), said


def keep(answered, text, said, out):
    try:
        answered.write_text(text, encoding="utf-8", newline="\n")
    except OSError as error:
        # A shell that may not write the project: the drawing is right, and is said not to be kept.
        print(f"drawn, and not written ({answered}: {error.strerror}): {said}. Say so; do not write it by hand.", file=out)
        return 0
    print(f"drawn: {answered}: {said}", file=out)
    return 0


def load(folder):
    drawn, written, answered = find(folder)
    ids = asked(drawn.read_text(encoding="utf-8")) if drawn else {}
    answers = read(written.read_text(encoding="utf-8")) if written else []
    mark = str(questions.cksum((drawn.read_bytes() if drawn else b"") + (written.read_bytes() if written else b"")))
    return drawn, written, answered, ids, answers, mark


def state(folder):
    drawn, written, answered, ids, answers, mark = load(folder)
    if written is None:
        return "none"
    if answered.is_file() and (STAMP % mark) in answered.read_text(encoding="utf-8"):
        return "drawn"
    settled = set()
    for answer in answers:
        settled |= set(settles(answer, ids)[0])
    if answered.is_file():
        return "stale: the questions or the answers changed after the answers were drawn"
    return f"written {len(settled)} of {len(ids)}"


def main(arguments, out=sys.stdout):
    if len(arguments) < 2 or arguments[0] not in ("next", "draw", "state"):
        print(__doc__, file=out)
        return 2
    command, folder = arguments[0], arguments[1]
    if command == "state":
        print(state(folder), file=out)
        return 0
    drawn, written, answered, ids, answers, mark = load(folder)
    if drawn is None:
        print("no questions.md in the slice's questions folder: there is nothing to answer yet", file=out)
        return 1
    found, taken = problems(answers, ids, questions.read_slice(folder)) if answers else ([], {})
    left = [name for name in ids if name not in taken]
    if command == "next":
        many = int(arguments[2]) if len(arguments) > 2 else 60
        print(f"{len(ids) - len(left)} of {len(ids)} questions are settled by {len(answers)} answers; {len(left)} are left.", file=out)
        for name in left[:many]:
            print(f"- {name}: {ids[name]}", file=out)
        if len(left) > many:
            print(f"and {len(left) - many} more: answer these, then ask again.", file=out)
        if found:
            print("\nNot holding in the answers as written:\n" + "\n".join(found), file=out)
        return 0
    if written is None:
        print("no answers yet: write NNN_answers.md in the slice's folder, NNN the next number there", file=out)
        return 1
    skipped = SKIPPED.search(written.read_text(encoding="utf-8"))
    if skipped and not answers:
        text = "\n".join(["# Answered", "", STAMP % mark, "", written.read_text(encoding="utf-8").strip(), "",
                          f"None of the {len(ids)} questions is answered, and the slice has no criteria from them: a risk accepted, for the owner's list.", ""])
        said = f"skipped at the user's word: none of the {len(ids)} questions is answered"
        return keep(answered, text, said, out)
    if left:
        found.append(f"{len(left)} questions are settled by no answer (the first: {', '.join(left[:5])}): `next` lists them")
    if found:
        print("\n".join(found), file=out)
        return 1
    text, said = drawing(answers, ids, taken, mark)
    return keep(answered, text, said, out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
