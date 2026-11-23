#!/usr/bin/env python3
"""Write the scope-map stage's scenarios as cases for the plugin evaluation.

Every scenario starts inside the project's VM with a problem document in the planning folder
(and, for a re-read, a map and a planned slice), startup's report and table and the problem
stage's text as adopted. An arm adds nothing for this stage (`bare`), kad's `scope-map` as it
stands (`kad`) or this repository's own text (`text`, from `scope-map-skill.md`).

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import importlib.util
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


startup = load("startup_cases", ROOT / "steps/00-startup/eval/make_cases.py")
problem = load("problem_cases", ROOT / "steps/01-problem/eval/make_cases.py")
says, never_says, write = startup.says, startup.never_says, startup.write

MAP = "planning/001_scope-map.md"
KAD = [HERE / "kad-skill.md", ROOT.parent / "kad-dev-team-plugin/skills/scope-map/SKILL.md"]


def in_map(name, pattern, path=MAP):
    return {"type": "regex", "name": name, "target": {"source": "file", "path": path}, "flags": "i", "pattern": pattern}


def not_in_map(name, pattern, path=MAP):
    return {**in_map(name, pattern, path), "match": "not_contains"}


# An activity is a line that carries one of the three marks, set off as a cell, in brackets or in bold.
def mark(word):
    return rf"[(|*]\s*(?:{word})\s*[)|*]"


def marked(times, word="now|next|later"):
    return rf"(?:[\s\S]*?{mark(word)}){{{times}}}"


def activity_with(words):
    return rf"(?:^|\n)[^\n]*(?:{words})[^\n]*{mark('now|next|later')}|(?:^|\n)[^\n]*{mark('now|next|later')}[^\n]*(?:{words})"


WRITTEN = {"type": "file_exists", "name": "writes-the-map", "path": MAP}
MARKS = [in_map("marks-the-activities", marked(1)), in_map("one-is-now", mark("now")),
         not_in_map("only-one-is-now", marked(2, "now"))]
SEVERAL = [in_map("at-least-three-activities", marked(3)), not_in_map("at-most-eight-activities", marked(9))]
PLAIN = not_in_map("nothing-of-the-build",
                   problem.SOLUTION + r"|\b\d+\s*(days?|weeks?|sprints?|hours?|points?)\b|acceptance criteri|given[^\n]*when[^\n]*then")
ASKS = says("asks-the-user", r"\?")
STOPS_THERE = {"type": "regex", "name": "writes-no-later-document", "target": "trace", "match": "not_contains",
               "pattern": r'"name"\s*:\s*"(?:Write|Edit)"[\s\S]{0,80}?file_path\\?"\s*:\s*\\?"[^"]*'
                          r'_(requirements|research|slice|questions|answers|design)'}
CHANGES_THE_MAP = {"type": "regex", "name": "changes-the-map", "target": "trace",
                   "pattern": r'"name"\s*:\s*"(Write|Edit)"[\s\S]{0,400}?001_scope-map'}
# A map has rows of its own, so only the table is kept from the user here, not the word "row".
ALWAYS = [STOPS_THERE, never_says("keeps-the-routing-table-out", r"\brouting table\b")]
GO_ON = "Go on to the next stage."

TOOLS_PROBLEM = """# Problem: Lending at the tool library

## The problem
- Members borrow tools; each loan is a line in a paper ledger at the desk.
- Nobody can say who has which tool, and about one tool in ten is never returned.
- Reservations are taken by phone and clash: two people turn up for the same tool most Saturdays.
- Tools that come back broken wait weeks, because nobody tracks what needs repair.
- People join at the desk and pay the yearly fee in cash; the cash and the list of members do not agree.

## Why now
- We move to a bigger space in spring and expect twice the members.

## Constraints
- The volunteers at the desk have only their own phones.
- Nothing may cost more than 20 a month to run.

## Open questions
- None.
"""
ROTA_PROBLEM = """# Problem: The weekly rota email

## The problem
- Every Sunday the manager copies next week's rota from the wall chart into an email to the staff.
- It takes about an hour, and most weeks one shift is typed wrong and someone turns up at the wrong time.

## Why now
- Two new staff start next month, which makes the chart and the email longer.

## Constraints
- The staff read email and nothing else.

## Open questions
- None.
"""
LEAGUE_PROBLEM = """# Problem: Running the youth league on paper

## The problem
- Parents register their children on paper forms at the start of the season; coaches get their lists weeks late.
- Fixture changes are phoned round, and some parents do not hear and travel to the wrong ground.
- Match results are phoned in to the secretary, who retypes them into the league table.

## Why now
- The league grew from 12 teams to 20 this season and the secretary cannot keep up.

## Constraints
- A child's details may be seen only by that child's own coach and the league secretary.

## Open questions
- Whether paying the referees is part of this or stays with the treasurer.
"""
TOOLS_MAP = """# Scope map: Lending at the tool library

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Join and pay the yearly fee | A person becomes a member and their fee is recorded | later |
| 2 | Reserve a tool | A member holds a tool for a day, with no clash | next |
| 3 | Borrow a tool | A volunteer records who took which tool | now |
| 4 | Return a tool | A volunteer records that the tool is back | next |
| 5 | Report and track a repair | A broken tool is flagged and followed until it is fixed | later |

## Holds for every activity
- The volunteers at the desk have only their own phones.
- Nothing may cost more than 20 a month to run.

## Open
- None.
"""
SHOWN = ("I've drawn the scope map from the problem document. Five things a user does: join and pay the yearly "
         "fee (later); reserve a tool (next); borrow a tool (now); return a tool (next); report and track a "
         "repair (later). Two limits hold for all of them: the volunteers have only their own phones, and "
         "nothing may cost more than 20 a month. I put borrowing first because nobody can say who has which "
         "tool. Is anything missing, unwanted or in the wrong order?")

# (name, description, documents when the session started, documents added since, prompt, checks, said before)
SCENARIOS = [
    ("01-a-large-problem", "A problem of several activities: a map of them, marked, one now; ask once.",
     {"000_problem.md": TOOLS_PROBLEM}, {}, GO_ON,
     [WRITTEN, *SEVERAL, *MARKS, PLAIN, ASKS,
      not_in_map("the-limit-is-no-activity", activity_with(r"20 a month|\bcost|budget|own phones")),
      # Why it is done now is a reason, not a limit: it is no bullet under the limits.
      not_in_map("the-reason-for-now-is-no-limit", r"(?:^|\n)\s*[-*][^\n]*(?:spring|twice)")], None),
    ("02-a-small-problem", "A problem that is one activity: one row, said to be one.",
     {"000_problem.md": ROTA_PROBLEM}, {}, GO_ON,
     [WRITTEN, in_map("marks-the-activities", marked(1)), not_in_map("one-row-only", marked(2)), PLAIN,
      says("says-it-is-one", r"\bone\b|single|small|only")], None),
    ("03-a-limit-and-an-open-question", "A limit on everything and an open question: neither becomes an activity.",
     {"000_problem.md": LEAGUE_PROBLEM}, {}, GO_ON,
     [WRITTEN, *MARKS, PLAIN,
      not_in_map("the-limit-is-no-activity", activity_with(r"details may be seen|only by|privacy|who (can|may) see")),
      in_map("the-limit-is-kept", r"own coach|secretary"),
      not_in_map("the-open-question-is-no-activity", activity_with(r"referee")),
      in_map("the-open-question-is-kept", r"referee")], None),
    ("04-a-technology-floated", "A technology named in passing: not in the map.",
     {"000_problem.md": TOOLS_PROBLEM}, {}, GO_ON + " I was thinking Airtable for this, by the way.",
     [WRITTEN, *SEVERAL, *MARKS, PLAIN, not_in_map("the-floated-technology-is-left-out", r"airtable")], None),
    ("05-the-users-correction", "The second turn: the user drops one activity and puts another first.",
     {"000_problem.md": TOOLS_PROBLEM}, {"001_scope-map.md": TOOLS_MAP},
     "Repairs aren't part of this, a different group handles them. And returns matter most: start there.",
     [CHANGES_THE_MAP, *MARKS, in_map("returns-are-now", activity_with(r"return").replace("now|next|later", "now")),
      not_in_map("repairs-are-no-activity", activity_with(r"repair")),
      # Set beside kad's skill (decision 26): what the user takes out is said, so its absence is not read as a gap.
      in_map("what-was-taken-out-is-said", problem.section(r"\bout\b", r"repair"))],
     [("user", GO_ON), ("assistant", SHOWN)]),
    # Set beside kad's skill (decision 26): a limit named for one activity may be about the whole product.
    ("06-a-limit-worded-for-one-activity", "A limit that names one activity: under the limits as worded, and asked about.",
     {"000_problem.md": TOOLS_PROBLEM.replace("- Nothing may cost more than 20 a month to run.",
                                              "- Texting a member about a reservation must cost us nothing.")}, {}, GO_ON,
     [WRITTEN, *SEVERAL, *MARKS, PLAIN,
      in_map("the-limit-is-under-the-limits", problem.section(r"holds", r"cost|nothing|free")),
      not_in_map("the-limit-is-no-activity", activity_with(r"cost us nothing|\bcosts? nothing|free of charge")),
      says("asks-which-was-meant", r"(cost|texting|texts?)[\s\S]{0,400}\?|\?[\s\S]{0,400}(cost|texting)")], None),
]


def main(arm):
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-scope-trial-{arm}", "version": "0.0.1",
         "description": "Stage 2's test only: startup and the problem stage as adopted, and one arm's text."},
        indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n',
          executable=True)
    shutil.copy(ROOT / "steps/00-startup/eval/routing-table.md", plugin / "hooks" / "routing-table.md")
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    write(plugin / "skills" / "problem" / "SKILL.md",
          (ROOT / "steps/01-problem/eval/problem-skill.md").read_text(encoding="utf-8"))
    used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    if arm == "kad":
        source = next(path for path in KAD if path.exists())
        write(plugin / "skills" / "scope-map" / "SKILL.md", source.read_text(encoding="utf-8"))
    elif arm == "text":
        write(plugin / "skills" / "scope-map" / "SKILL.md", (HERE / "scope-map-skill.md").read_text(encoding="utf-8"))
    elif arm == "bare":
        used = []
    else:
        raise SystemExit("arm: bare, kad or text")
    cleanup = startup._Cleanup()
    for name, description, before, added, prompt, graders, earlier in SCENARIOS:
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        (machine.project / "planning").mkdir()
        machine.run("stage.sh", "remember", "planning")

        def put(documents):
            for relative, text in documents.items():
                path = machine.project / "planning" / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
        put(before)
        done = machine.run("report.sh")   # what the session was given when it started
        assert done.returncode == 0 and "next stage by the documents: scope map" in done.stdout, done.stdout
        put(added)
        case = plugin / "evals" / name
        write(case / "report.txt", done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@"))
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, graders + ALWAYS + used, earlier)
              .replace("name: problem-", "name: scope-").replace("tags: [problem]", "tags: [scope]"))
        write(case / "scaffold.sh", startup.scaffold(machine), executable=True)
        if earlier:
            write(case / "history.jsonl", startup.history(earlier))
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(graders + ALWAYS + used)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bare")
