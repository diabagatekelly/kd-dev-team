#!/usr/bin/env python3
"""Write the requirements stage's scenarios as cases for the plugin evaluation.

Every scenario starts inside the project's VM with a problem document and a scope map in the
planning folder, startup's report and table and the two earlier stages' texts as adopted. An arm
adds nothing for this stage (`bare`), kad's `requirements-refinement` as it stands (`kad`) or
this repository's own text: `free` (the planner's questions as they come), `kinds` (every item
walked against eight kinds of gap) or `grid` (the walk written down as a table), each from
`requirements-skill-ARM.md`.

kad's skill asks before it writes, so its arm's prompt carries the user's answer to its
questions, "go by the documents", and names the skill, as kad's orchestrator does: left to its
description, the pilot's sessions on Haiku never invoked it.

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
says, never_says, write, section = startup.says, startup.never_says, startup.write, problem.section

LIST = "planning/002_requirements.md"
KAD = [HERE / "kad-skill.md", ROOT.parent / "kad-dev-team-plugin/skills/requirements-refinement/SKILL.md"]

# An item is a line that starts with a box. FORM checks are the box and the name, which nothing
# tells the bare model or kad's skill to write: the result is reported with and without them.
BOX = r"(?:^|\n)[ \t]*[-*] \[[ xX]\]"
SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"


def in_list(name, pattern, flags="i"):
    return {"type": "regex", "name": name, "target": {"source": "file", "path": LIST}, "flags": flags,
            "pattern": pattern}


def not_in_list(name, pattern, flags="i"):
    return {**in_list(name, pattern, flags), "match": "not_contains"}


def items(times):
    return rf"(?:{BOX}[\s\S]*?){{{times}}}"


def item_with(words):
    return rf"{BOX}[^\n]*(?:{words})"


def between(low, high):
    return [in_list(f"form-at-least-{low}-items", items(low)), not_in_list(f"form-at-most-{high}-items", items(high + 1))]


WRITTEN = {"type": "file_exists", "name": "writes-the-list", "path": LIST}
FORM = [not_in_list("form-every-item-has-a-name", BOX + rf"(?! \*\*{SLUG}\*\*)", flags=""),
        not_in_list("form-no-name-twice", rf"\[[ xX]\] \*\*({SLUG})\*\*[\s\S]*\[[ xX]\] \*\*\1\*\*", flags=""),
        not_in_list("form-no-box-is-checked", r"(?:^|\n)[ \t]*[-*] \[[xX]\]"),
        not_in_list("form-no-item-is-a-question", BOX + r"[^\n]*\?"),
        # Found by the first end-to-end run: items written as "I can ...", taken from the problem document's voice.
        not_in_list("form-who-is-named-by-role", BOX + r" \*\*[^*\n]*\*\*:?[^\n]*\b(I|me|my|you|your)\b", flags="")]
PLAIN = not_in_list("nothing-of-the-build",
                    problem.SOLUTION + r"|\b\d+\s*(days?|weeks?|sprints?|hours?|story points?)\b|acceptance criteri|"
                                       r"given[^\n]*when[^\n]*then|thin path")
INVENTORY = r"outside systems|lasting things"
ASKS = says("asks-the-user", r"\?")
# The owner is willing to answer questions (2026-11-22): this catches only a list that sprawls.
FEW = not_in_list("at-most-ten-questions", section(r"not yet confirmed", r"(?:(?:[-*]|\d+\.) [^\n]*\n+){11}"))
WROTE = r'"name"\s*:\s*"(?:Write|Edit)"[\s\S]{0,80}?file_path\\?"\s*:\s*\\?"[^"]*'
STOPS_THERE = {"type": "regex", "name": "writes-no-later-document", "target": "trace", "match": "not_contains",
               "pattern": WROTE + r"_(research|slice|questions|answers|design)"}
MAP_UNTOUCHED = {"type": "regex", "name": "leaves-the-map-alone", "target": "trace", "match": "not_contains",
                 "pattern": WROTE + r"scope-map"}
CHANGES_THE_LIST = {"type": "regex", "name": "changes-the-list", "target": "trace",
                    "pattern": r'"name"\s*:\s*"(Write|Edit)"[\s\S]{0,400}?002_requirements'}
ALWAYS = [STOPS_THERE, MAP_UNTOUCHED, never_says("keeps-the-routing-table-out", r"\brouting table\b")]
GO_ON = "Go on to the next stage."

TOOLS_PROBLEM = load("scope_cases", ROOT / "steps/02-scope-map/eval/make_cases.py").TOOLS_PROBLEM
TOOLS_MAP = """# Scope map: Lending at the tool library

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Join and pay the yearly fee | A person becomes a member and their fee is recorded | later |
| 2 | Reserve a tool | A member holds a tool for a day, with no clash | next |
| 3 | Borrow and return a tool | A volunteer records who took which tool, and that it came back | now |
| 4 | Report and track a repair | A broken tool is flagged and followed until it is fixed | later |

## Holds for every activity
- The volunteers at the desk have only their own phones.
- Nothing may cost more than 20 a month to run.

## Open
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
ROTA_MAP = """# Scope map: The weekly rota email

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Send next week's rota to the staff | The manager gets the week's shifts to every member of staff, each shift right | now |

## Holds for every activity
- The staff read email and nothing else.

## Open
- None.
"""
LEAGUE = """# Problem: Running the youth league on paper

## The problem
- Parents register their children on paper forms at the start of the season; coaches get their lists weeks late.
- Fixture changes are phoned round, and some parents do not hear and travel to the wrong ground.
- Match results are phoned in to the secretary, who retypes them into the league table.

## Why now
- The league grew from 12 teams to 20 this season and the secretary cannot keep up.

## Constraints
- A child's details may be seen only by that child's own coach and the league secretary.

## Open questions
- %s
"""
LEAGUE_MAP = """# Scope map: Running the youth league on paper

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Register a child for the season | A parent registers their child and the coach has the list in time | now |
| 2 | Hear of a fixture change | Every parent of a team learns of a change before they travel | next |
| 3 | Report a match result | A result reaches the league table without being retyped | later |

## Holds for every activity
- A child's details may be seen only by that child's own coach and the league secretary.

## Open
- %s
"""
FEE = "Whether a parent pays the season's fee when registering, or paying stays with the treasurer."
REFEREES = "Whether paying the referees is part of this or stays with the treasurer."
THEATRE_PROBLEM = """# Problem: Season tickets at the playhouse

## The problem
- A subscriber pays for a season ticket once a year, by card, through our account with PayRight.
- The office renews each season ticket by hand from a spreadsheet, and about one in six lapses without anyone noticing.
- A subscriber whose ticket has lapsed finds out at the door, on the night.
- Single tickets are sold at the door and by phone, and the two lists of seats do not always agree.

## Why now
- Renewals for next season open in eight weeks.

## Constraints
- Card payments stay with PayRight: the contract runs two more years.

## Open questions
- None.
"""
THEATRE_MAP = """# Scope map: Season tickets at the playhouse

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Renew a season ticket | A subscriber's season ticket is renewed and paid for before it lapses | now |
| 2 | Buy a single ticket | A person buys a seat for one night, and the seat is sold once | next |

## Holds for every activity
- Card payments stay with PayRight: the contract runs two more years.

## Open
- None.
"""
TOOLS_LIST = """# Requirements: Borrow and return a tool

- [ ] **record-a-loan**: A volunteer can record which member took which tool.
- [ ] **record-a-return**: A volunteer can record that a tool came back.
- [ ] **see-who-has-it**: A volunteer can see who has a given tool now.
- [ ] **list-overdue-tools**: A volunteer can see every tool that has not come back.

## Out for now
- Reserving a tool, joining and the yearly fee, and repairs: other rows of the scope map.

## Limits that apply
- The volunteers have only their own phones: every item must be doable on a phone at the desk.
- Nothing may cost more than 20 a month to run: applies to how it is run, not to what a volunteer can do.

## Not yet confirmed
Nothing.

## Outside systems and lasting things
- a loan
- a tool
- a member
"""
SHOWN = ("I've written the requirements for borrowing and returning a tool. Four items: a volunteer can record "
         "which member took which tool (record-a-loan); record that a tool came back (record-a-return); see who "
         "has a given tool now (see-who-has-it); and see every tool that has not come back "
         "(list-overdue-tools). Is anything missing, unwanted or not for now?")
# kad's skill asks before it writes: the user's answer to its five questions, given with the request.
KAD_ANSWER = (" To save you asking: who benefits and what they need are as the problem document and the scope "
              "map say. No priority beyond what is written there. The simplest version is whatever covers this "
              "activity. No other approach was considered. Write it up.")

LEAGUE_LIST = """# Requirements: Register a child for the season

- [ ] **register-child**: A parent can register their child for the season.
- [ ] **coach-sees-list**: A coach can see the list of children registered to their team.

## Out for now
- Hearing of a fixture change and reporting a match result: other rows of the scope map.

## Limits that apply
- A child's details may be seen only by that child's own coach and the league secretary: a coach's list holds only the children of their own team, and no one else sees a child's details.

## Not yet confirmed
- Whether a parent pays the season's fee when registering, or paying stays with the treasurer. If paying is part of registering, an item for paying is added.
- By when a coach needs the list: by a date before the season, or as each child registers. It changes what "in time" means in coach-sees-list.

## Outside systems and lasting things
- a child's registration for the season
"""
LEAGUE_SHOWN = ("I've written the requirements for registering a child. Two items: a parent can register their child "
                "for the season (register-child), and a coach can see the list of children registered to their team "
                "(coach-sees-list). Two things are not yet confirmed. Does a parent pay the season's fee when "
                "registering, or does paying stay with the treasurer? And by when does a coach need the list: by a "
                "date before the season, or as each child registers? Is anything missing, unwanted or not for now?")
NOT_CONFIRMED = r"confirmed|open|question"
OTHER_ROWS = r"reserv|repair|yearly fee|\bjoin"
# (name, description, documents when the session started, documents added since, prompt, checks, said before)
SCENARIOS = [
    ("01-the-now-row-of-a-large-problem", "The now row of four: a list for it, nothing from the other rows.",
     {"000_problem.md": TOOLS_PROBLEM, "001_scope-map.md": TOOLS_MAP}, {}, GO_ON,
     [WRITTEN, *between(2, 8), *FORM, PLAIN, FEW, ASKS,
      not_in_list("no-item-from-another-row", item_with(OTHER_ROWS)),
      in_list("the-limit-is-kept", r"phones?"), not_in_list("the-limit-is-no-item", item_with(r"20 a month|\bcosts?\b")),
      in_list("has-the-inventory", INVENTORY)], None),
    ("02-a-one-row-problem", "A problem of one activity: a short list.",
     {"000_problem.md": ROTA_PROBLEM, "001_scope-map.md": ROTA_MAP}, {}, GO_ON,
     # "Email and nothing else" forces "nothing to sign in to": said of this limit, the word is no solution.
     [WRITTEN, *between(1, 5), *FORM, {**PLAIN, "pattern": PLAIN["pattern"].replace("log ?ins?|sign[- ]in|", "")}, FEW, ASKS,
      in_list("the-outside-system-is-listed", section(INVENTORY, r"e-?mail"))], None),
    ("03-a-limit-and-an-open-question-it-leans-on", "The limit said as what it forces; the question still open, and asked.",
     {"000_problem.md": LEAGUE % FEE, "001_scope-map.md": LEAGUE_MAP % FEE}, {}, GO_ON,
     [WRITTEN, *between(2, 8), *FORM, PLAIN, FEW,
      in_list("the-limit-is-kept", r"coach[\s\S]*secretary|secretary[\s\S]*coach"),
      not_in_list("the-open-question-is-no-item", item_with(r"\bfees?\b|\bpay")),
      in_list("the-open-question-is-kept-open", section(r"confirmed|open|question", r"\bfees?\b|\bpay")),
      says("asks-the-open-question", r"(\bfees?\b|\bpay)[\s\S]*\?|\?[\s\S]*(\bfees?\b|\bpay)"),
      not_in_list("no-item-from-another-row", item_with(r"fixture|result"))], None),
    ("04-a-technology-floated-and-a-question-it-does-not-touch", "Neither the technology nor the far question in the list.",
     {"000_problem.md": LEAGUE % REFEREES, "001_scope-map.md": LEAGUE_MAP % REFEREES}, {},
     GO_ON + " We could just use Google Forms for this, by the way.",
     [WRITTEN, *between(2, 8), *FORM, PLAIN, FEW, ASKS,
      not_in_list("the-floated-technology-is-left-out", r"google"),
      not_in_list("the-far-question-is-no-item", item_with(r"referee"))], None),
    ("05-an-outside-system-and-a-lasting-thing", "A payment provider and a season ticket: both in the inventory.",
     {"000_problem.md": THEATRE_PROBLEM, "001_scope-map.md": THEATRE_MAP}, {}, GO_ON,
     [WRITTEN, *between(2, 8), *FORM, PLAIN, FEW, ASKS,
      in_list("the-outside-system-is-listed", section(INVENTORY, r"payright")),
      in_list("the-lasting-thing-is-listed", section(INVENTORY, r"season ticket|subscription")),
      not_in_list("no-item-from-another-row", item_with(r"single ticket|one night|\bseats?\b"))], None),
    ("06-the-users-correction", "The second turn: one item dropped, one added, the other names unchanged.",
     {"000_problem.md": TOOLS_PROBLEM, "001_scope-map.md": TOOLS_MAP}, {"002_requirements.md": TOOLS_LIST},
     "Drop the overdue list, that can wait. And add one: a volunteer has to be able to put right a loan that "
     "was recorded against the wrong member.",
     [CHANGES_THE_LIST, *FORM,
      in_list("the-other-names-are-unchanged",
              r"\*\*record-a-loan\*\*[\s\S]*\*\*record-a-return\*\*[\s\S]*\*\*see-who-has-it\*\*"),
      not_in_list("the-dropped-item-is-gone", item_with(r"overdue|not come back")),
      in_list("the-new-item-is-there", item_with(r"wrong member|correct|put right|fix|amend|chang"))],
     [("user", GO_ON), ("assistant", SHOWN)]),
    ("07-an-answer-to-one-question-of-two", "The second turn: one question answered, the other passed over and asked again.",
     {"000_problem.md": LEAGUE % FEE, "001_scope-map.md": LEAGUE_MAP % FEE}, {"002_requirements.md": LEAGUE_LIST},
     "Paying stays with the treasurer. Nothing else to add or take out.",
     [CHANGES_THE_LIST, *FORM,
      in_list("the-names-are-unchanged", r"\*\*register-child\*\*[\s\S]*\*\*coach-sees-list\*\*"),
      not_in_list("the-answered-question-is-closed", section(NOT_CONFIRMED, r"whether a parent pays")),
      not_in_list("the-answer-adds-no-item", item_with(r"\bfees?\b|\bpay")),
      in_list("the-other-question-stays", section(NOT_CONFIRMED, r"by when|in time|date|as each")),
      says("asks-the-other-question-again", r"(by when|in time|date|as each)[\s\S]*\?|\?[\s\S]*(by when|in time|date|as each)")],
     [("user", GO_ON), ("assistant", LEAGUE_SHOWN)]),
]
TEXTS = {"problem": ROOT / "steps/01-problem/eval/problem-skill.md",
         "scope-map": ROOT / "steps/02-scope-map/eval/scope-map-skill.md"}


def main(arm):
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-requirements-trial-{arm}", "version": "0.0.1",
         "description": "Stage 3's test only: startup and the two earlier stages as adopted, and one arm's text."},
        indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n',
          executable=True)
    shutil.copy(ROOT / "steps/00-startup/eval/routing-table.md", plugin / "hooks" / "routing-table.md")
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for name, source in TEXTS.items():
        write(plugin / "skills" / name / "SKILL.md", source.read_text(encoding="utf-8"))
    used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    if arm == "kad":
        source = next(path for path in KAD if path.exists())
        write(plugin / "skills" / "requirements-refinement" / "SKILL.md", source.read_text(encoding="utf-8"))
    elif arm in ("free", "kinds", "grid"):
        write(plugin / "skills" / "requirements" / "SKILL.md",
              (HERE / f"requirements-skill-{arm}.md").read_text(encoding="utf-8"))
    elif arm == "bare":
        used = []
    else:
        raise SystemExit("arm: bare, kad, free, kinds or grid")
    cleanup = startup._Cleanup()
    for name, description, before, added, prompt, graders, earlier in SCENARIOS:
        if arm == "kad":   # named, as kad's orchestrator names it; its questions answered beforehand
            prompt += " Use the requirements-refinement skill." + ("" if earlier else KAD_ANSWER)
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
        assert done.returncode == 0 and "next stage by the documents: requirements" in done.stdout, done.stdout
        put(added)
        case = plugin / "evals" / name
        write(case / "report.txt", done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@"))
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, graders + ALWAYS + used, earlier)
              .replace("name: problem-", "name: requirements-").replace("tags: [problem]", "tags: [requirements]"))
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
