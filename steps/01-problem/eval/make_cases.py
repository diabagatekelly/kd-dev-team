#!/usr/bin/env python3
"""Write the problem stage's scenarios as cases for the plugin evaluation.

Every scenario starts inside the project's VM, the planning folder chosen and empty, with
startup's report and routing table as adopted. An arm is that alone (`bare`), or that and a
skill holding a text for the stage: kad's `problem-framing-doc` as it stands (`kad`, the
mark to reach) or this repository's own (`text`, from `problem-skill.md` beside this file).
The made-up products are in different fields; the checks are free.

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import importlib.util
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location("startup_cases", ROOT / "steps/00-startup/eval/make_cases.py")
startup = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(startup)
says, never_says, write = startup.says, startup.never_says, startup.write

DOCUMENT = "planning/000_problem.md"
KAD = [HERE / "kad-skill.md", ROOT.parent / "kad-dev-team-plugin/skills/problem-framing-doc/SKILL.md"]


def in_document(name, pattern):
    return {"type": "regex", "name": name, "target": {"source": "file", "path": DOCUMENT}, "flags": "i",
            "pattern": pattern}


def not_in_document(name, pattern):
    return {**in_document(name, pattern), "match": "not_contains"}


def section(heading, holds):
    """`holds` is under a heading that has `heading` in it, before the next heading."""
    return rf"(?:^|\n)#{{1,6}}[^\n]*(?:{heading})[^\n]*\n(?:(?!\n#{{1,6}}\s)[\s\S])*?(?:{holds})"


# Words of a solution that no account below uses.
SOLUTION = (r"\b(web ?app|mobile app|native app|iOS|Android|log ?ins?|sign[- ]in|database|tech(nology)? stack|"
            r"framework|API|dashboard|notifications?|cloud|SaaS)\b")
WRITES_NOTHING = [
    {"type": "tool_used", "name": "writes-no-file", "tool": "Write", "min": 0, "max": 0},
    {"type": "tool_used", "name": "edits-no-file", "tool": "Edit", "min": 0, "max": 0},
    {"type": "tool_used", "name": "writes-nothing-by-shell", "tool": "Bash", "min": 0, "max": 0,
     "input_match": r">\s*[\w./~-]+\.\w+|\btee\b"},
]
ASKS = says("asks-the-user", r"\?")
NO_SOLUTION_ASKED = never_says("asks-nothing-of-the-solution", SOLUTION)
WRITTEN = {"type": "file_exists", "name": "writes-the-document", "path": DOCUMENT}
NO_SOLUTION_WRITTEN = not_in_document("names-no-solution", SOLUTION)
STOPS_THERE = {"type": "regex", "name": "writes-no-later-document", "target": "trace", "match": "not_contains",
               "pattern": r'file_path\\?"\s*:\s*\\?"[^"]*(scope|requirements|slice|design)[^"]*\.md'}
ALWAYS = [STOPS_THERE, startup.NO_ROW_NUMBERS]

GYM = ("At our climbing gym people book classes by messaging the front desk, and staff copy the names into a "
       "spreadsheet. A class holds 8. Most weeks one is overbooked and someone is turned away at the door, and "
       "no-shows leave places empty that we could have filled. We already take payments through Square and "
       "that stays. There are two of us who can look after whatever this becomes, in the evenings only. I "
       "guess we'd just add a booking page to the website? Capture the problem first.")

# (name, description, prompt, checks, what was said before)
SCENARIOS = [
    ("01-idea-only", "Only an idea: ask about the problem, not the solution; write nothing.",
     "I want to build something for my running club to organise our weekend runs.",
     [ASKS, NO_SOLUTION_ASKED, *WRITES_NOTHING], None),
    ("02-full-account", "A full account: write it, with the user's facts, the unknown left open, no solution.",
     "We're a bakery with two shops. Custom cake orders come in by phone and are written in a paper diary at "
     "whichever shop took the call. About once a week an order is missed or made for the wrong day because "
     "the other shop never saw it, and we refund the customer; last month that was six refunds. Why now: we "
     "open a third shop in March and the diary will not stretch to three. Limits: the staff who take orders "
     "are not at a computer, they have the shop phone and a tablet at the till; and I can spend no more than "
     "50 a month on running it. What I don't know yet is whether orders taken at our market stall need to go "
     "in too. That's everything, write up the problem.",
     [WRITTEN, in_document("holds-the-current-way", r"diary"), in_document("holds-the-cost", r"\b(six|6)\b"),
      in_document("why-now-is-the-users", section(r"why|now", r"March|third shop")),
      in_document("limits-are-the-users", section(r"constraint|limit", r"\b50\b")),
      in_document("limits-are-all-there", section(r"constraint|limit", r"tablet")),
      in_document("the-unknown-stays-open", section(r"open|question|unknown", r"market stall")),
      NO_SOLUTION_WRITTEN], None),
    ("03-solution-floated", "A solution floated and no reason given: ask what is missing; write nothing.",
     GYM, [ASKS, never_says("asks-nothing-of-the-solution", SOLUTION + r"|booking page\b[^.\n]*\?"),
           *WRITES_NOTHING], None),
    ("04-the-answer", "The second turn: the reason and an unknown given; write the document.",
     "Mostly the people turned away: two of them cancelled their memberships last month and said that was "
     "why. And the summer term starts in six weeks, with more classes. The limits are the two I gave you. One "
     "thing I don't know is whether drop-in sessions should be covered or only classes. That's all I have, "
     "write it up.",
     [WRITTEN, in_document("holds-the-current-way", r"spreadsheet"),
      in_document("why-now-is-the-users", section(r"why|now", r"membership|cancel|summer|six weeks")),
      in_document("limits-are-the-users", section(r"constraint|limit", r"Square")),
      in_document("limits-are-all-there", section(r"constraint|limit", r"evening|two (of|people)")),
      in_document("the-unknown-stays-open", section(r"open|question|unknown", r"drop-in")),
      not_in_document("the-floated-solution-is-no-limit", section(r"constraint|limit", r"booking page")),
      NO_SOLUTION_WRITTEN],
     [("user", GYM), ("assistant", "I have the problem and two limits: payments stay on Square, and two of "
                                   "you look after it in the evenings. One thing is missing before I write "
                                   "it up. What makes this worth solving now, instead of leaving it as it "
                                   "is?")]),
    ("05-not-known-yet", "The reason and the limits not known yet: write what there is, the rest left open.",
     "Our village hall is hired out for parties and classes. Bookings are taken by one volunteer, by email, "
     "and she keeps them in her own diary. When she is away nobody can say whether a date is free, and last "
     "year we double-booked the hall twice. I don't know why now, honestly: nothing is forcing it, it has "
     "annoyed the committee for years. I can't tell you the limits yet either; the committee meets on the "
     "12th and I will know the budget after that. That is all there is for now: write up what we have.",
     [WRITTEN, in_document("holds-the-current-way", r"diary"), in_document("holds-the-cost", r"double|twice"),
      in_document("the-unknown-stays-open", section(r"open|question|unknown", r"budget|limit|committee")),
      not_in_document("invents-no-figure", r"[$£€]\s?\d|\b\d+\s?(dollars|pounds|euros)\b"),
      NO_SOLUTION_WRITTEN], None),
    ("06-two-problems", "Two problems in one account: say so; not one long document.",
     "Two things at our dental practice. First, patients phone to rebook and sit on hold; the two "
     "receptionists spend most mornings on the phone and about one caller in five gives up. Second, our "
     "steriliser logs are kept on paper, and last month the inspector could not find March's sheets; we got "
     "a written warning. Why now: the warning, for the logs, and for the phones we are losing patients to "
     "the practice down the road. Limit: no patient data may leave the country. Write up the problem.",
     [says("says-there-are-two", r"two (separate |distinct |different |unrelated )?(problems|things|documents|docs)|"
                                 r"separate|distinct|unrelated|split|(its|their) own (document|doc)|second problem"),
      {"type": "tool_used", "name": "one-document-does-not-hold-both", "tool": "Write", "min": 0, "max": 0,
       "input_match": r"(steriliser[\s\S]*on hold|on hold[\s\S]*steriliser)"}], None),
    # Found by the first end-to-end run: a terse user's thin answers were written up as the whole problem.
    ("07-answer-by-answer", "An account given one short answer at a time: one last question before writing.",
     "Nothing yet that I can think of.",
     [*WRITES_NOTHING, says("asks-whether-anything-else-goes-wrong",
                            r"(anything|something|what) else[^?]{0,200}\?|else (that )?goes wrong[^?]{0,200}\?|"
                            r"is that (everything|all)[^?]{0,60}\?|(any|what) other[^?]{0,80}\?"),
      NO_SOLUTION_ASKED],
     [("user", "I want an app for our allotment society."),
      ("assistant", "What does your allotment society do today, and what goes wrong with it?"),
      ("user", "We have 84 plots and about 40 people waiting. The waiting list is a paper notebook I keep at home."),
      ("assistant", "Why does this need solving now?"),
      ("user", "The council says our lease renewal in March depends on showing plots are given out fairly."),
      ("assistant", "Is there a hard limit on what we do, such as a budget or a deadline?"),
      ("user", "We can spend 10 a month at most."),
      ("assistant", "Is there anything you don't know yet that matters here?")]),
    # Found by an end-to-end run: a full account in one message named one limit, the document was
    # written at once, and the user's other limits (a privacy rule among them) were never asked for.
    ("08-a-full-account-not-said-to-be-all", "A full account, not said to be everything: one last question; write nothing yet.",
     "I run a dog-walking business, four walkers and about sixty regular clients. Every month I type up an "
     "invoice for each client by hand from the walkers' paper sheets. It takes me two full days and I get two "
     "or three wrong every month. I'd like it sorted before the summer, when the work roughly doubles. We take "
     "card payments through the service we already use, and that stays. Can you write up the problem?",
     [*WRITES_NOTHING, says("asks-whether-anything-else-goes-wrong-or-limits-it",
                            r"(anything|something|what) else[^?]{0,200}\?|else (that )?goes wrong[^?]{0,200}\?|"
                            r"is that (everything|all)[^?]{0,60}\?|(any|what) other[^?]{0,80}\?"),
      NO_SOLUTION_ASKED], None),
]


def case_yaml(name, description, prompt, graders, earlier):
    quoted = json.dumps
    out = ['schema_version: "1.1"', f"name: problem-{name}", f"description: {quoted(description)}",
           "tags: [problem]", "context:", "  scaffold_script: scaffold.sh",
           *(["  history_file: history.jsonl"] if earlier else []), "execution:",
           f"  prompt: {quoted(prompt)}", "  max_turns: 20", "  timeout_seconds: 400",
           "  allowed_tools: [Skill, Read, Glob, Grep, Bash, Write, Edit]", "runs: 3", "graders:"]
    return "\n".join(out + ["  - " + quoted(grader) for grader in graders]) + "\n"


def main(arm):
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-problem-trial-{arm}", "version": "0.0.1",
         "description": "Stage 1's test only: startup's report and table, and one arm's text for the stage."},
        indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n',
          executable=True)
    shutil.copy(ROOT / "steps/00-startup/eval/routing-table.md", plugin / "hooks" / "routing-table.md")
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    used = []
    if arm == "kad":
        source = next(path for path in KAD if path.exists())
        write(plugin / "skills" / "problem-framing-doc" / "SKILL.md", source.read_text(encoding="utf-8"))
        used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    elif arm == "text":
        write(plugin / "skills" / "problem" / "SKILL.md", (HERE / "problem-skill.md").read_text(encoding="utf-8"))
        used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    elif arm != "bare":
        raise SystemExit("arm: bare, kad or text")
    cleanup = startup._Cleanup()
    for name, description, prompt, graders, earlier in SCENARIOS:
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        (machine.project / "planning").mkdir()
        machine.run("stage.sh", "remember", "planning")
        done = machine.run("report.sh")
        assert done.returncode == 0 and "next stage by the documents: problem" in done.stdout, done.stdout
        case = plugin / "evals" / name
        write(case / "report.txt", done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@"))
        write(case / "case.yaml", case_yaml(name, description, prompt, graders + ALWAYS + used, earlier))
        write(case / "scaffold.sh", startup.scaffold(machine), executable=True)
        if earlier:
            write(case / "history.jsonl", startup.history(earlier))
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(graders + ALWAYS + used)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bare")
