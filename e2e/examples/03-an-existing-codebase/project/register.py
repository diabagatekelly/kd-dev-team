#!/usr/bin/env python3
"""The choir's attendance register: singers by voice part, and who came to each rehearsal."""
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).parent / "data" / "register.json"
PARTS = ("soprano", "alto", "tenor", "bass")


def load():
    return json.loads(DATA.read_text()) if DATA.exists() else {"singers": {}, "attended": {}}


def save(register):
    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps(register, indent=2) + "\n")


def add(register, name, part):
    if part not in PARTS:
        raise SystemExit(f"a voice part is one of: {', '.join(PARTS)}")
    register["singers"][name] = part


def tick(register, date, name):
    if name not in register["singers"]:
        raise SystemExit(f"no singer called {name}")
    came = register["attended"].setdefault(date, [])
    if name not in came:
        came.append(name)


def report(register, date):
    came = set(register["attended"].get(date, []))
    for part in PARTS:
        singers = sorted(name for name, theirs in register["singers"].items() if theirs == part)
        present = [name for name in singers if name in came]
        print(f"{part}: {len(present)} of {len(singers)} came")
        for name in singers:
            print(f"  {'x' if name in came else ' '} {name}")


def missed_in_a_row(register, name, dates):
    """How many of the latest rehearsals in a row this singer did not come to."""
    count = 0
    for date in sorted(dates, reverse=True):
        if name in register["attended"].get(date, []):
            break
        count += 1
    return count


if __name__ == "__main__":
    register, (command, *rest) = load(), sys.argv[1:] or ["report", ""]
    if command == "add":
        add(register, *rest)
    elif command == "tick":
        tick(register, *rest)
    elif command == "report":
        report(register, *rest)
    else:
        raise SystemExit(__doc__)
    save(register)
