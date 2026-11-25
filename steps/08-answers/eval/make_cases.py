#!/usr/bin/env python3
"""Write the answers stage's cases for the plugin evaluation.

Every case starts where the security pass leaves a slice of the made-up playhouse: `kept.md` and
`security.md` written and the questions drawn with both. The answers stage writes its answers
file in the slice's folder and the script draws `answered.md` beside it. Nothing is fetched.

Two slices: the one that only quotes a price (29 questions, answered from nothing), and the one
that takes a payment through a provider (387), which starts with answers "written before" for
every question but the few a case is about: a session that had to settle 387 questions in each
run would cost what an example costs.

An arm adds nothing for this stage (`bare`) or this repository's text (`text`, from
`answers-skill.md`).

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import importlib.util
import io
import json
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s = load("security_cases", ROOT / "steps/07b-security/eval/make_cases.py")
answers = load("answers", ROOT / "answers/answers.py")
q = s.q
startup, problem, questions = q.startup, q.problem, q.questions
says, never_says, write, in_file, not_in_file, trace, WROTE = q.says, q.never_says, q.write, q.in_file, q.not_in_file, q.trace, q.WROTE

# The slice that only quotes a price, as the security pass leaves it: used in a browser, nothing else.
QUOTE_SECURITY = """# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | quote-a-price / 1: the office is shown the price; the documents do not say it is without a browser |
| network | no | 002_requirements.md: it runs on the office's one computer and answers nobody else |
| calls-out | no | slice-001/004_slice.md: needs from outside, none |
| dependency | no | slice-001/004_slice.md: needs from outside, none |
| several-people | no | 002_requirements.md: the office alone uses it |
| unguessable | no | quote-a-price / 1 and / 2 make only a price shown |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `nothing` | `price-screen` | A price is read by someone at the office's screen. | no: the prices are printed in the playhouse's own leaflet |
"""
# What a case on the provider's slice leaves to settle: one of each kind the text tells apart.
LEFT = ("L.call-external-01.payment-request", "L.call-external-02.payment-reference", "L.secrets-03.secret-key",
        "C.payright.O1", "C.payright.O2", "C.payright.S2", "C.states.dead-end.1", "W.target")
# The decision the owner takes in one case, as an earlier session left it for their list.
REFUNDS = """## A900: A refund asked for after ninety days
Kind: owner
Says: PayRight refuses a refund more than 90 days after a payment settled (payright F10), and the problem says a subscriber can be refunded at any time.
Options: the office is told it is too late and gives the money back another way | no refund is offered after 90 days and the subscriber is told so
Recommended: the office is told it is too late and gives the money back another way, because the playhouse has promised refunds at any time.
If left: a late refund fails with PayRight's own error and the office does not know what to do.
Harm: medium
Settles: C.payright.S2
"""


def before(drawn, left=(), owner=""):
    """Answers as an earlier session left them: every question but `left` settled, a group an answer."""
    ids = [name for name in answers.asked(drawn) if name not in left and not (owner and name == "C.payright.S2")]
    groups = {}
    for name in ids:
        groups.setdefault(".".join(name.split(".")[:2]), []).append(name)
    blocks = ["# Answers: slice 1\n"]
    for number, (group, names) in enumerate(groups.items(), 1):
        said = ("Kind: fact\nSays: Settled in an earlier session.\nRests on: 002_requirements.md, the limits that apply.\n"
                if group in ("W.target", "W.obligations") else   # never chosen for the owner: the script refuses it
                "Kind: chosen\nSays: Settled in an earlier session, as the design of this slice will carry it.\n"
                "Rests on: applied as good practice; nothing here is the owner's.\n")
        blocks.append(f"## A{number}: {group}\n{said}Settles: {', '.join(names)}\n")
    return "\n".join(blocks) + ("\n" + owner if owner else "")


ANS = "@ANS@"
WRITTEN = {"type": "file_exists", "name": "writes-the-answers-file", "path": ANS}
DRAWN = [{"type": "tool_used", "name": "draws-with-the-command", "tool": "Bash", "min": 1, "input_match": r"answers\.py[\s\S]*\bdraw\b"},
         trace("the-command-drew", r"drawn(?:: |, and not written)[^\n]{0,400}?\d+ answers settle \d+ questions", never=False),
         trace("does-not-write-the-drawing-by-hand", WROTE + r"_answered[.]md")]
ASKED_WHAT_IS_LEFT = {"type": "tool_used", "name": "form-asks-the-command-what-is-left", "tool": "Bash", "min": 1, "input_match": r"answers\.py[\s\S]*\bnext\b"}
LEFT_ALONE = [trace("changes-no-earlier-document", WROTE + r"(00[0-4]_(problem|scope-map|requirements|slices|slice)|_approach|_research/|_questions/)"),
              trace("writes-no-later-document", WROTE + r"_(open-facts|design|screens|stack|readiness)")]
NOT_WHOLE = trace("form-never-writes-the-answers-again-whole", r"\"name\"\s*:\s*\"Write\"[\s\S]{0,80}?file_path\\?\"\s*:\s*\\?\"[^\"]*_answers[.]md")
NOT_WRITTEN = trace("writes-no-answers-file", WROTE + r"_answers[.]md")


def block(name, kind, *also):
    """An answer of this kind whose block holds every pattern in `also` (an id it settles, a field it gives)."""
    return in_file(ANS, name, r"(?:^|\n)## A\d+(?=(?:(?!\n## )[\s\S])*?\nKind:\s*" + kind + r"\b)"
                   + "".join(r"(?=(?:(?!\n## )[\s\S])*?" + each + ")" for each in also))


def no_block(name, kind, *also):
    return {**block(name, kind, *also), "match": "not_contains"}


CRITERION = in_file(ANS, "writes-a-criterion-someone-could-check", r"(?:^|\n)Criterion:\s*Given\b[^\n]*\bwhen\b[^\n]*\bthen\b")
SKIP = "Skip the answers, it's a small slice. Go on to the design."
PUSHED_BACK = ("I can skip it, and it is yours to say. What it costs: the questions stay open and the slice gets no criteria from them, so each "
               "is settled by whoever builds it. This stage asks nothing of you. Shall I do it?")
SAYS_NOTHING_NEEDED = says("says-nothing-is-needed-now", r"nothing (is )?(needed|from you|to ask)|no(thing)? (questions?|input) (for|from) you|do(?: not|n't) need|not needed|"
                                                         r"ask(?:s|ed)? (you )?nothing|nothing is (asked|needed)|nothing now|(?:does not|doesn't) ask you|none (for|from) you|later|once|one (short )?list")

# On the provider's slice the answers written before are stock lines, and a session's offer to look at them again is a
# closing offer, not a preference asked: those cases keep only the check that nothing is asked of the product.
# name, what it shows, which slice ("quote" or "paid"), the answers already there (None, or a function of the drawing), whether they
# are drawn, a security file laid over after (or None), the user's words, checks, what may be asked ("" or "ask"), earlier turns
SCENARIOS = [
    ("01-a-small-slice-from-nothing",
     "A slice that quotes a price: every question settled, the limits of a value as facts from the criteria, what is the owner's a criterion written, drawn by the command, nothing asked.",
     "quote", None, False, None, q.GO_ON,
     [WRITTEN, ASKED_WHAT_IS_LEFT, *DRAWN, CRITERION,
      block("rests-a-fact-on-a-criterion", "fact", r"\nRests on:[^\n]*quote-a-price / \d"),
      no_block("does-not-ask-the-owner-a-technical-thing", "owner", r"V\.every-setting\.missing"),
      *LEFT_ALONE], "", None),
    ("02-the-kinds-told-apart",
     "A provider's slice with eight questions left: what the provider's pages say is a fact resting on them, what no page says is to test with no criterion on the guess, a dead end is the owner's, a secret kept out of the records is chosen with a criterion of its absence.",
     "paid", lambda drawn: before(drawn, LEFT), False, None, q.GO_ON,
     [ASKED_WHAT_IS_LEFT, *DRAWN, NOT_WHOLE,
      block("a-repeat-rests-on-the-providers-page", "(?:fact|chosen)", r"L\.call-external-02\.payment-reference", r"\bF6\b"),
      block("no-reply-is-to-test", "test", r"C\.payright\.O1", r"\nTest:", r"\nHarm:"),
      no_block("no-criterion-on-the-guess", "test", r"\nCriterion:"),
      block("a-dead-end-is-the-owners", "owner", r"C\.states\.dead-end\.1", r"\nOptions:[^\n]*\|", r"\nIf left:"),
      block("the-key-out-of-the-records-is-chosen", "(?:chosen|fact)", r"L\.secrets-03\.secret-key"),
      in_file(ANS, "a-criterion-of-absence", r"(?:^|\n)Criterion:[^\n]*\b(nothing of|no part of|does not appear|never appears|is not (written|recorded|shown)|not in|absent|without the)\b"),
      *LEFT_ALONE, q.ASKS_NOTHING[1]], "ask", None),
    ("03-asked-what-is-needed",
     "The user offers to answer and asks what is needed: nothing now, their decisions come once as one list; the stage is done all the same.",
     "paid", lambda drawn: before(drawn, LEFT), False, None,
     "Go on to the next stage. What do you need from me? I can tell you our refund rules and how fast it has to be.",
     [*DRAWN, SAYS_NOTHING_NEEDED, block("still-leaves-the-dead-end-for-the-list", "owner", r"C\.states\.dead-end\.1"), *LEFT_ALONE,
      q.ASKS_NOTHING[1], never_says("does-not-invite-their-answers", r"(tell|give|send) me (your|the) (refund|rules|speed|target)|once you (answer|tell)|what are your (refund|rules)")],
     "ask", None),
    ("04a-skip-the-stage", "The user says to skip the answers: said once what it costs and that it asks nothing of them, offered again, nothing written.",
     "quote", None, False, None, SKIP,
     [says("says-what-skipping-costs", r"criteri|open|whoever builds|builder|in the build|unsettled|unanswered"),
      says("says-it-asks-nothing-of-them", s.SCENARIOS[3][7][1]["pattern"] + r"|nothing (else )?is asked of you"), says("offers-the-stage-again", q.OFFERS), NOT_WRITTEN, *LEFT_ALONE], "ask", None),
    ("04b-the-user-insists", "The next turn: the user insists: recorded as skipped at their word, drawn by the command, the next stage not started.",
     "quote", None, False, None, "No. Skip it.",
     [WRITTEN, in_file(ANS, "in-their-words-with-the-date", r"[Ss]kipped at the user's word[\s\S]*20\d\d-\d\d-\d\d|20\d\d-\d\d-\d\d[\s\S]*[Ss]kip"),
      DRAWN[0], trace("the-command-drew-the-skip", r"skipped at the user's word: none of the \d+ questions is answered", never=False),
      says("says-it-goes-to-the-owners-list", r"owner'?s? list|risk accepted|accepted risk"), *LEFT_ALONE], "", [("user", SKIP), ("assistant", PUSHED_BACK)]),
    ("05-the-owner-decides-against-the-recommendation",
     "Everything is settled and drawn; the user decides one thing on their list, against what was recommended: recorded in their words with the date, its criterion written, drawn again, nothing else changed.",
     "paid", lambda drawn: before(drawn, (), REFUNDS), True, None,
     "On refunds after ninety days: no refund is offered after that. The subscriber is told so, and that's the end of it.",
     [block("records-the-decision-in-their-words", "owner", r"C\.payright\.S2", r"\nDecided:[^\n]*no refund[^\n]*\(the user, 20\d\d-\d\d-\d\d: \"[^\"\n]+\"\)"),
      block("writes-the-criterion-that-follows", "owner", r"C\.payright\.S2", r"\nCriterion:\s*Given\b[^\n]*\b(90|ninety)\b[^\n]*\bthen\b"),
      not_in_file(ANS, "does-not-keep-its-own-recommendation", r"\nDecided:[^\n]*another way"),
      *DRAWN[:2], NOT_WHOLE, *LEFT_ALONE, q.ASKS_NOTHING[1]], "ask", None),
    ("06-the-questions-changed-after",
     "Everything was settled and drawn, then the security file gained a row and the questions were drawn again: only the new question is answered, the answers before are left, drawn again.",
     "paid", lambda drawn: before(drawn), True,
     lambda security: security.rstrip("\n") + "\n| `her-details` | `refund-request` | someone who is not the office refunds a renewal by naming its payment. | yes |\n",
     q.GO_ON,
     [block("settles-the-new-question", "(?:fact|chosen|owner|test)", r"T\.her-details\.refund-request"), *DRAWN[:2], NOT_WHOLE,
      in_file(ANS, "leaves-the-answers-before", r"## A1: [^\n]*\nKind: chosen\nSays: Settled in an earlier session"), *LEFT_ALONE, q.ASKS_NOTHING[1]], "ask", None),
]
BARE_TABLE = q.BARE_TABLE.replace("The questions stage", "The answers stage")


def main(arm):
    if arm not in ("bare", "text"):
        raise SystemExit("arm: bare or text")
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-answers-trial-{arm}", "version": "0.0.1",
         "description": "The answers stage's test only: startup and the earlier stages as adopted, and one arm's text."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n', executable=True)
    table = (ROOT / "steps/00-startup/eval/routing-table.md").read_text(encoding="utf-8")
    if arm != "text":
        last = table.rindex("- A stage with no text")
        assert "not built yet" in table[last:]
        table = table[:last] + BARE_TABLE
    write(plugin / "hooks" / "routing-table.md", table)
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for script in ("research/page.py", "questions/questions.py", "library/library.json", "answers/answers.py"):
        write(plugin / script, (ROOT / script).read_text(encoding="utf-8"))
    for name, source in q.load("make_plugin", ROOT / "e2e/make_plugin.py").SKILLS.items():
        if name != "answers":   # this stage's own text is one arm's, not every arm's
            write(plugin / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    used = []
    if arm == "text":
        write(plugin / "skills" / "answers" / "SKILL.md", (HERE / "answers-skill.md").read_text(encoding="utf-8"))
        used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    cleanup = startup._Cleanup()
    for name, description, which, written, drawn, after, prompt, graders, may, earlier in SCENARIOS:
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        planning = machine.project / "planning"
        planning.mkdir()
        machine.run("stage.sh", "remember", "planning")
        slice_folder = planning / "slice-001"

        def lay(these):
            for relative, text in these.items():
                path = planning / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8", newline="\n")

        def draw(script=questions):
            said = io.StringIO()
            assert script.main(["draw", str(slice_folder)], said) == 0, (name, said.getvalue())

        lay(s.QUOTE if which == "quote" else q.playhouse(**s.PAID))
        folder = re.search(r"next stage by the documents: questions \(its document: (\S+/)", machine.run("report.sh").stdout).group(1)
        inside = folder.split("planning/", 1)[1]
        security = QUOTE_SECURITY if which == "quote" else s.EARLIER_SECURITY
        lay({inside + "kept.md": s.QUOTE_KEPT if which == "quote" else q.kept_file()})
        draw()
        lay({inside + "security.md": security})
        draw()
        found = re.search(r"next stage by the documents: answers \(its document: (\S+_answers\.md)\)", machine.run("report.sh").stdout)
        assert found, (name, machine.run("report.sh").stdout)
        document = found.group(1)
        if written is not None:
            lay({document.split("planning/", 1)[1]: written((planning / inside / "questions.md").read_text(encoding="utf-8"))})
            if drawn:
                draw(answers)
        if after is not None:
            lay({inside + "security.md": after(security)})
            draw()
        done = machine.run("report.sh")
        wanted = "tests of open facts" if (drawn and after is None) else "answers"
        assert done.returncode == 0 and f"next stage by the documents: {wanted} (" in done.stdout, (name, done.stdout)
        report = done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@")
        assert str(ROOT) not in report, (name, report)
        machine.set("gh/summary", done.stdout.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        machine.set("web/allowed", "api.anthropic.com")
        checks = list(graders) + ([] if may == "ask" else q.ASKS_NOTHING) + used
        checks = json.loads(json.dumps(checks).replace(ANS, document))
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, checks, earlier)
              .replace("name: problem-", "name: answers-").replace("tags: [problem]", "tags: [answers]")
              .replace("max_turns: 20", "max_turns: 80").replace("timeout_seconds: 400", "timeout_seconds: 1500"))
        write(case / "scaffold.sh", startup.scaffold(machine), executable=True)
        if earlier:
            write(case / "history.jsonl", startup.history(earlier))
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(checks)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bare")
