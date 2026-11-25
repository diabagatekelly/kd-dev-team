#!/usr/bin/env python3
"""Write the security pass's cases for the plugin evaluation.

Every case starts where the questions stage leaves a slice of the made-up playhouse: `kept.md`
written and the questions drawn from it by the script. The security pass writes `security.md`
beside it and the questions are drawn again with it. Nothing is fetched.

An arm adds nothing for this stage (`bare`), this repository's text (`text`, from
`security-skill.md`) or kad's `security-requirements` (`kad`, on the first case: read from kad's
repository beside this one, or copied beside this file as `kad-security-requirements.md`; never
committed).

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
_spec = importlib.util.spec_from_file_location("questions_cases", ROOT / "steps/07-questions/eval/make_cases.py")
q = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(q)

startup, problem, research, questions = q.startup, q.problem, q.research, q.questions
says, never_says, write, in_file, not_in_file, trace, WROTE = q.says, q.never_says, q.write, q.in_file, q.not_in_file, q.trace, q.WROTE
KAD = [HERE / "kad-security-requirements.md", ROOT.parent / "kad-dev-team-plugin/skills/security-requirements/SKILL.md"]
EARLIER_SECURITY = (HERE / "security-earlier.md").read_text(encoding="utf-8")

PAID = dict(inventory=(q.THE_SYSTEM, q.THE_PAYMENT, q.THE_TICKET), more=q.RESEARCHED)
# A key the provider means to be seen, listed with the credentials as a session of the questions stage might list it.
PUBLIC = {"slice-001/006_research/payright.md": q.PAYRIGHT.rstrip("\n") + "\n- F12: The publishable key is public by design. \"The publishable key "
          f"identifies your account to the card form and is safe to put in a page.\" ({q.SITE}/keys)\n"}
PUBLIC_KEPT = q.kept_file().replace("| `secret-key` |", "| `publishable-key` | identifier | the playhouse's PayRight account, put in the page for the "
                                    "card form | credentials | payright.md F12 |\n| `secret-key` |", 1)
# Nobody signs in, and signing in is out: the office's refund cannot be told from anyone's.
OPEN_DOOR = "- Nobody signs in to it and nothing of the kind is planned: whoever can open the playhouse's pages can use every one of them.\n"
# The slice that keeps nothing and needs nothing from outside, with the least a kept.md can hold.
QUOTE = {name: text for name, text in {**q.playhouse(the_slice=q.QUOTE_SLICE, the_set=q.QUOTE_SET, fixed=False), "002_requirements.md": q.QUOTE_LIST}.items()
         if "approach" not in name}
QUOTE_KEPT = ("# Kept: slice 1\n\n## What the slice creates and keeps\n- nothing\n\n## What the slice takes in\n| Value | Kind | From | Sensitive | Source |\n|---|---|---|---|---|\n"
              "| `seat-band` | choice | the office | no | quote-a-price / 1 |\n| `seats` | number | the office | no | quote-a-price / 2 |\n\n"
              "## Other things the slice has\n- `price-screen`: where the office asks and is shown the price (quote-a-price / 1, quote-a-price / 2)\n\n"
              "## Library\n| Entry | Applies to | Why |\n|---|---|---|\n"
              + "".join(f"| {kind}: all | dropped | the slice does nothing of the kind: it shows a price and keeps nothing |\n"
                        for kind in dict.fromkeys(entry["action"] for entry in q.ENTRIES)))


def fact(name, holds):
    return in_file("@SEC@", f"says-{name}-{'holds' if holds == 'yes' else 'does-not-hold'}", rf"(?:^|\n)\|\s*`?{name}`?\s*\|\s*\**{holds}\b")


def row(name, wanted, through, asked):
    return in_file("@SEC@", name, rf"(?:^|\n)\|[^|\n]*(?:{wanted})[^|\n]*\|[^|\n]*(?:{through})[^|\n]*\|[^|\n]*\|\s*{asked}")


WRITTEN = {"type": "file_exists", "name": "writes-the-security-file", "path": "@SEC@"}
DRAWN = [q.DRAWN[0], trace("the-command-drew-with-it", r"drawn[^\n]{0,400}?\d+ by what the slice is, \d+ of what someone would want", never=False)]
BY_SCRIPT = trace("never-writes-the-questions-itself", WROTE + r"_questions/questions[.]md")
NOTHING_ANSWERED = [not_in_file("@SEC@", "answers-nothing", r"(?:^|\n)#+[^\n]*\b(answers?|decisions?|controls?|mitigations?|criteria)\b|"
                                                           r"(?:^|\n)\s*[-*]?\s*\**(Answer|Decision|Mitigation|Fix)\**\s*:|\bGiven\b[^\n]*\b[Ww]hen\b"),
                    q.NOTHING_ANSWERED[1]]
LEFT = [q.LIST_LEFT, q.RESEARCH_LEFT, q.LATER, q.EARLIER, BY_SCRIPT]
NOT_WRITTEN = trace("writes-no-security-file", WROTE + r"_questions/security[.]md")
SKIP = "Skip the security pass, it's a small slice. Go on to the answers."
PUSHED_BACK = ("I can skip it, and it is yours to say. What it costs: nobody will have looked at this slice as an attacker would before it "
               "is built. It asks nothing of you: I write two short tables and the questions are drawn again. Shall I do it?")

# name, what it shows, the documents, kept.md, security.md already written (or nothing), documents laid over once all is drawn (or
# nothing), the user's words, checks, what may be asked ("" or "ask"), earlier turns, whether kad's skill has something for it
SCENARIOS = [
    ("01-a-provider-a-credential-and-an-address-that-receives",
     "A slice with a provider, a credential, a subscriber's details and an address that receives events: the facts said with their sources, what is wanted and through what, drawn again by the command, nothing answered or asked.",
     q.playhouse(**PAID), q.kept_file(), None, None, q.GO_ON,
     [WRITTEN, *DRAWN, fact("browser", "yes"), fact("network", "yes"), fact("calls-out", "yes"),
      in_file("@SEC@", "every-fact-has-a-source", r"(?:(?:^|\n)\|\s*`?[a-z-]+`?\s*\|\s*\**(?:yes|no)\**\s*\|\s*[^|\s][^|\n]*\|[^\n]*){6}"),
      row("wants-the-credentials", r"credentials|secret-key|card-token", r"[a-z]", "yes"),
      row("comes-through-the-address-that-receives", r"[a-z]", r"webhook-address|payment-updated-event", "yes"),
      row("comes-through-a-screen-or-request-of-the-office", r"[a-z]", r"refund-screen|refund-request", "yes"),
      *NOTHING_ANSWERED, *LEFT], "", None, True),
    ("02-little-to-attack",
     "A slice that shows a price and keeps nothing: said to have little to attack, few rows asked, nothing padded.",
     QUOTE, QUOTE_KEPT, None, None, q.GO_ON,
     [WRITTEN, *DRAWN, fact("calls-out", "no"), fact("dependency", "no|yes"),
      not_in_file("@SEC@", "asks-of-no-more-than-three-rows", r"(?:\|\s*yes\s*\|?\s*(?:\n|$)[\s\S]*){4}"),
      row("accounts-for-the-screen", r"[a-z]|nothing", r"price-screen", r"(?:yes|no\s*:)"),
      says("says-there-is-little", r"little|few|small|not much|nothing (much|worth|sensitive)|no sensitive|low"),
      *NOTHING_ANSWERED, *LEFT], "", None, False),
    ("03-a-value-public-by-design",
     "A key the provider's own page calls public is listed with the credentials: dismissed with that reason, not asked about as a secret.",
     q.playhouse(inventory=PAID["inventory"], more={**q.RESEARCHED, **PUBLIC}), PUBLIC_KEPT, None, None, q.GO_ON,
     [WRITTEN, *DRAWN,
      in_file("@SEC@", "dismisses-the-public-key-with-the-reason",
              r"(?:^|\n)\|[^\n]*publishable-key[^\n]*\|\s*no\s*:[^|\n]*(public|by design|not (a )?secret|meant|safe)"),
      not_in_file("@SEC@", "does-not-ask-of-it-as-a-secret", r"(?:^|\n)\|[^|\n]*publishable-key[^|\n]*\|[^\n]*\|\s*yes\b"),
      row("still-wants-the-secret-key", r"credentials|secret-key", r"[a-z]", "yes"),
      *NOTHING_ANSWERED, *LEFT], "", None, False),
    ("04a-skip-the-stage", "The user says to skip the security pass: said once what it costs, the stage offered again; nothing written yet.",
     q.playhouse(**PAID), q.kept_file(), None, None, SKIP,
     [says("says-what-it-costs", r"attack|harm|nobody|no one|looked|before it is built|risk|cost|found late|gap"),
      says("says-it-asks-nothing-of-them", r"asks? (you |of you )?(nothing|no)|nothing (of|from) you|no questions? (for|to) you|without (asking|you)|do(?: not|n't) need (anything|you)"),
      says("offers-the-stage-again", q.OFFERS), NOT_WRITTEN, *LEFT], "ask", None, False),
    ("04b-the-user-insists", "The next turn: the user insists: recorded as skipped at their word, every fixed question drawn, the answers not started.",
     q.playhouse(**PAID), q.kept_file(), None, None, "No. Skip it.",
     [WRITTEN, in_file("@SEC@", "in-their-words-with-the-date", r"(?i)skipped at the user's word[\s\S]*20\d\d-\d\d-\d\d|20\d\d-\d\d-\d\d[\s\S]*skip"),
      not_in_file("@SEC@", "writes-no-table", r"\|\s*Fact\s*\|"), *DRAWN,
      says("says-it-goes-to-the-owners-list", r"owner'?s list|risk"), *LEFT], "", [("user", SKIP), ("assistant", PUSHED_BACK)], False),
    ("05-asked-what-is-needed",
     "The user offers to say how secrets should be kept: nothing is asked; said that the documents answer first and theirs comes once; the pass done.",
     q.playhouse(**PAID), q.kept_file(), None, None,
     q.GO_ON + " What do you need from me? Ask me where the key should be kept and how people sign in and I'll tell you.",
     [WRITTEN, *DRAWN,
      says("says-nothing-is-needed-now", r"nothing (is )?(needed|from you|to ask)|no(thing)? (questions?|input) (for|from) you|do(?: not|n't) need|not needed|"
                                         r"ask(?:s|ed)? (you )?nothing|none (for|from) you|later|once|one (short )?list"),
      *NOTHING_ANSWERED, *LEFT], "", None, False),
    ("06-it-cannot-be-made-safe-as-cut",
     "Nobody signs in and signing in is out, and the slice has the office give money back: nothing is written; what is missing and what it forces are said, with one recommendation, as the slice's to decide.",
     {**q.playhouse(**PAID), "000_problem.md": q.playhouse(**PAID)["000_problem.md"].rstrip("\n") + "\n" + OPEN_DOOR,
      "002_requirements.md": q.playhouse(**PAID)["002_requirements.md"].replace("## Out for now\n", "## Out for now\n- Accounts and signing in.\n", 1)},
     q.kept_file(), None, None, q.GO_ON,
     [NOT_WRITTEN,
      says("says-what-is-missing", r"sign|who (is|they are|someone is)|tell (the office|who)|know(s|ing)? who|prove|identity|account"),
      says("says-it-is-the-slices-to-decide", r"slice|scope|cut|requirement"),
      says("says-what-it-forces", r"anyone|whoever|any (person|visitor|one)|everyone"), *LEFT], "ask", None, False),
    ("07-a-criterion-added-after",
     "A criterion that takes typed text was added after the security file was written: the questions stage brings kept.md up to date, the security text is loaded and the file looked at again, its rows left, drawn again.",
     q.playhouse(**PAID), q.kept_file(), EARLIER_SECURITY,
     {"slice-001/004_slice.md": q.PAY_SLICE.replace("\n## Needs from outside", q.NOTE + "\n## Needs from outside").replace("Three criteria", "Four criteria")},
     q.GO_ON,
     [{"type": "tool_used", "name": "loads-the-security-text-too", "tool": "Skill", "min": 1, "input_match": r"security"},
      q.DRAWN[0], trace("the-command-drew-with-it", r"drawn[^\n]{0,400}?\d+ by what the slice is, \d+ of what someone would want", never=False),
      in_file("@SEC@", "the-earlier-rows-are-left",
              r"someone holding the secret key takes payments or gives refunds as the playhouse[\s\S]*a true event sent again later puts a refunded renewal back to paid"),
      in_file("@KEPT@", "the-new-value-is-taken-in", r"(?:^|\n)\|[^|\n]*(?:reason|note)[^|\n]*\|"),
      *NOTHING_ANSWERED, *LEFT], "", None, False),
]
BARE_TABLE = q.BARE_TABLE.replace("The questions stage", "The security stage")


def main(arm):
    if arm not in ("bare", "kad", "text"):
        raise SystemExit("arm: bare, kad or text")
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-security-trial-{arm}", "version": "0.0.1",
         "description": "The security pass's test only: startup and the earlier stages as adopted, and one arm's text."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n', executable=True)
    table = (ROOT / "steps/00-startup/eval/routing-table.md").read_text(encoding="utf-8")
    if arm != "text":
        last = table.rindex("- A stage with no text")
        assert "not built yet" in table[last:]
        table = table[:last] + (BARE_TABLE.replace("has no text of its own here: do it from this report and the documents",
                                                   "is done with the skill the user names") if arm == "kad" else BARE_TABLE)
    write(plugin / "hooks" / "routing-table.md", table)
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for script in ("research/page.py", "questions/questions.py", "library/library.json"):
        write(plugin / script, (ROOT / script).read_text(encoding="utf-8"))
    for name, source in q.load("make_plugin", ROOT / "e2e/make_plugin.py").SKILLS.items():
        if name != "security":   # this stage's own text is one arm's, not every arm's
            write(plugin / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    if arm == "kad":
        write(plugin / "skills" / "security-requirements" / "SKILL.md", next(path for path in KAD if path.exists()).read_text(encoding="utf-8"))
    elif arm == "text":
        write(plugin / "skills" / "security" / "SKILL.md", (HERE / "security-skill.md").read_text(encoding="utf-8"))
    else:
        used = []
    cleanup = startup._Cleanup()
    for name, description, documents, kept, security, after, prompt, graders, may, earlier, for_kad in SCENARIOS:
        if arm == "kad":
            if not for_kad:
                continue
            prompt += " Use the security-requirements skill."
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        planning = machine.project / "planning"
        planning.mkdir()
        machine.run("stage.sh", "remember", "planning")

        def lay(these):
            for relative, text in these.items():
                path = planning / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8", newline="\n")

        def draw():
            said = io.StringIO()
            assert questions.main(["draw", str(planning / "slice-001")], said) == 0, (name, said.getvalue())

        lay(documents)
        # The questions as their stage leaves them: the folder the stage script names, kept.md, drawn by the script itself.
        folder = re.search(r"next stage by the documents: questions \(its document: (\S+/)", machine.run("report.sh").stdout).group(1)
        lay({folder.split("planning/", 1)[1] + "kept.md": kept})
        draw()
        if security is not None:
            lay({folder.split("planning/", 1)[1] + "security.md": security})
            draw()
        if after is not None:
            lay(after)
        done = machine.run("report.sh")
        wanted = "questions" if after is not None else "security"
        found = re.search(rf"next stage by the documents: {wanted} \(its document: (\S+?)(?:security\.md)?, ([^\n]*)", done.stdout)
        assert done.returncode == 0 and found and found.group(1) == folder, (name, done.stdout)
        report = done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@")
        assert str(ROOT) not in report, (name, report)
        machine.set("gh/summary", done.stdout.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        machine.set("web/allowed", "api.anthropic.com")
        checks = list(graders) + ([] if may == "ask" else q.ASKS_NOTHING) + used
        checks = json.loads(json.dumps(checks).replace("@SEC@", folder + "security.md").replace("@KEPT@", folder + "kept.md").replace("@FOLDER@", folder))
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, checks, earlier)
              .replace("name: problem-", "name: security-").replace("tags: [problem]", "tags: [security]")
              .replace("max_turns: 20", "max_turns: 60").replace("timeout_seconds: 400", "timeout_seconds: 1200"))
        write(case / "scaffold.sh", startup.scaffold(machine) + f"mkdir -p {folder}\n", executable=True)
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
