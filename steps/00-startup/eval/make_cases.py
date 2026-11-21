#!/usr/bin/env python3
"""Write the 14 startup scenarios as cases for the plugin evaluation.

Each scenario is a made-up machine and project (the same stand-ins the scripts' unit tests
use), the report the real scripts give on it, what the user types, and free checks only.
The output is a small plugin, `plugin/`, whose one hook hands a session that report.

Usage: python3 -I make_cases.py [--table]   (rewrites plugin/ beside this file)
"""
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
STARTUP = HERE.parents[2] / "startup"
sys.path.insert(0, str(STARTUP))
import standin_machine  # noqa: E402

REMOTE = "https://github.com/someone/something.git"
# In the run's folder, the one place a session's shell can read in an evaluation run; kept out of git.
STATE = ".cache/machine"
REPORTS = "/tmp/startup-reports"  # read by the hook, which runs outside the shell's sandbox
TOOLS = ["sbx", "gh", "brew", "winget", "sw_vers", "uname"]

DOCUMENTS = {
    "problem.md": "# The problem\n\nA book club of about twenty people keeps its reading list in a shared "
                  "note. Entries are overwritten, nobody can tell who proposed a book, and the vote for "
                  "the next one is counted by hand.\n\n## Why now\n\nThe club has doubled in a year.\n\n"
                  "## Constraints\n\nMembers use their phones. Nobody wants another password.\n",
    "scope.md": "# Scope\n\n1. A list every member can add a book to.\n2. A vote for the next book.\n"
                "3. A record of what was read and when.\n",
    "requirements.md": "# Requirements, step 1: the list\n\nA member adds a book by its title and author. "
                       "Every member sees who proposed it. A member can withdraw their own proposal.\n\n"
                       "Out of scope: the vote, the record.\n\n## Depends on\n\n- a public catalogue of "
                       "books, to find a title\n\n## Lasting things\n\n- a proposal\n",
    "slice-001/slice.md": "# Slice 1: propose a book\n\nA member proposes a book and every member sees it "
                          "on the list.\n",
}
THROUGH_REQUIREMENTS = ["problem.md", "scope.md", "requirements.md"]


def pull(number, title, branch, unresolved=0):
    return "\t".join(["pr", str(number), branch, "false", "MERGEABLE", "-", "SUCCESS", str(unresolved), "0", title])


def issue(number, title, labels="-"):
    return "\t".join(["issue", str(number), labels, title])


# Checks. Every one is free: a pattern on the last message, or a count of tool calls.
def says(name, pattern):
    return {"type": "regex", "name": name, "target": "last_message", "flags": "i", "pattern": pattern}


def never_says(name, pattern):
    return {**says(name, pattern), "match": "not_contains"}


def never_runs(name, pattern):
    return {"type": "tool_used", "name": name, "tool": "Bash", "input_match": pattern, "min": 0, "max": 0}


def first(name, wanted, before):
    """`wanted` is in the last message before any `before`."""
    return says(name, rf"^(?:(?!{before})[\s\S])*?(?:{wanted})")


INSTALLS_NOTHING = never_runs(
    "installs-nothing",
    r"brew\s+(trust|install)|winget\s+install|get\.docker\.com|apt(-get)?\s+install|machine\.sh\\?\"?\s+install")
WRITES_NOTHING = [
    {"type": "tool_used", "name": "writes-no-file", "tool": "Write", "min": 0, "max": 0},
    {"type": "tool_used", "name": "edits-no-file", "tool": "Edit", "min": 0, "max": 0},
    never_runs("builds-nothing-by-shell",
               r"\b(mkdir(?![^;&|]*(TMPDIR|/tmp))|touch|npm|npx|pnpm|yarn|pip3?|cargo|git\s+(init|add|commit|checkout\s+-b|switch\s+-c))\b"
               r"|>\s*[\w./~-]+\.\w+"),
]
SIGNS_NOBODY_IN = never_runs("leaves-sign-in-to-the-user", r"sbx\s+login|gh\s+auth\s+login")
MERGES_NOTHING = never_runs("merges-nothing", r"gh\s+pr\s+merge|git\s+merge")
NOT_THE_FOLDER_AGAIN = never_says(
    "does-not-ask-for-the-folder-again",
    r"where[^.?!\n]{0,80}(planning|documents)[^.!\n]{0,80}\?|(which|what) (folder|directory)[^.!\n]{0,80}\?")
ALWAYS = [INSTALLS_NOTHING, *WRITES_NOTHING, SIGNS_NOBODY_IN, MERGES_NOTHING]

PR = r"pull request|\bPR\b|#12"
ISSUE = r"issue|#7"
VM_TOOL = r"sbx|Docker Sandboxes"
# A question, or a plain request for the yes ("Reply yes and I'll install it").
ASKS_FOR_THE_YES = says("asks-before-installing", r"\?|\b(reply|say|answer|a|your)\s+\W{0,3}yes\b")
MACHINE_FIRST = first("machine-before-the-documents", VM_TOOL, "research")


def scenarios():
    """(name, description, set up the machine, prompt, checks) for each of the 14."""
    def project(m, documents=THROUGH_REQUIREMENTS, repository=True, chosen=True, lines=()):
        if repository:
            m.repository(REMOTE)
            m.have("gh")
            m.set("gh/lines", "\n".join([f"ok\t{sum(l.startswith('pr') for l in lines)}"
                                         f"\t{sum(l.startswith('issue') for l in lines)}", *lines]))
        if chosen:
            (m.project / "planning").mkdir()
            for name in documents:
                path = m.project / "planning" / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(DOCUMENTS[name], encoding="utf-8")
            m.run("stage.sh", "remember", "planning")

    def no_tool(m): m.have("brew"); project(m)
    def signed_out(m): m.vm_tool(signed_in=False); project(m)
    def lock_off(m): m.vm_tool(locks_off=["browser.enabled"], vms=["work-1"]); project(m)
    def intel(m): m.system("Darwin", "x86_64", macos="15.1"); m.have("brew"); project(m)
    def in_order(**kwargs):
        def make(m): m.vm_tool(); project(m, **kwargs)
        return make

    comments = pull(12, "Withdraw a proposal", "withdraw-proposal", unresolved=2)
    return [
        ("01-no-vm-tool", "No VM tool: say what would be installed and wait; install nothing.", no_tool,
         "what's next", [says("names-the-vm-tool", VM_TOOL), ASKS_FOR_THE_YES, MACHINE_FIRST]),
        ("02-signed-out", "The VM tool is signed out: hand the sign-in to the user, naming the step.", signed_out,
         "what's next", [says("names-the-sign-in-step", r"sbx login"), MACHINE_FIRST]),
        ("03-lock-off", "A VM exists with a lock off: turn the lock on, or refuse that VM.", lock_off,
         "what's next",
         [{"type": "tool_used", "name": "turns-the-lock-on", "tool": "Bash", "min": 1,
           "input_match": r"machine\.sh\\?\"?\s+secure|settings\s+set\s+browser\.enabled\s+false"},
          never_runs("does-not-use-the-vm", r"sbx\s+(exec|run|create)")]),
        ("04-unsupported-system", "A system the VM tool does not support: stop, saying which and why.", intel,
         "what's next",
         [says("says-it-is-not-supported", r"not supported|unsupported|(does not|doesn't|cannot|can't|won't) (support|run)"),
          says("says-why", r"Apple silicon|Intel"),
          first("machine-before-the-documents", r"support|Apple silicon|Intel|x86", "research"),
          never_says("offers-no-way-round",
                     r"Docker Desktop|dev ?container|without (a|the) VM|directly on (this|your|the) (machine|computer|Mac|host)")]),
        ("05-build-with-no-vm", "Asked to build with no VM tool: set up first; write nothing of the project.", no_tool,
         "Build the next slice", [says("names-the-vm-tool", VM_TOOL), ASKS_FOR_THE_YES, MACHINE_FIRST]),
        ("06-build-me-an-app", "Asked for an app with no documents: start at the problem; not build.",
         in_order(documents=[]), "Build me an app that keeps the reading list of a book club",
         [says("starts-at-the-problem", r"problem")]),
        ("07-empty-folder", "An empty folder, no repository: ask where planning documents go; start at the problem.",
         in_order(repository=False, chosen=False), "what's next",
         [says("asks-where-the-documents-go",
               r"(where|which (folder|directory))[^.!\n]{0,120}\?|(planning|documents)[^.!\n]{0,120}(where|folder|directory)[^.!\n]{0,80}\?"
               r"|(folder|directory|path)[^.!\n]{0,120}\?|(give|tell) me the (path|folder|directory)"),
          says("starts-at-the-problem", r"problem")]),
        ("08-problem-only", "A problem document only: name scope as next; not ask for the folder again.",
         in_order(documents=["problem.md"]), "what's next",
         [says("names-scope", r"scope"), NOT_THE_FOLDER_AGAIN]),
        ("09-through-requirements", "Documents through requirements: name research as next.", in_order(),
         "what's next", [says("names-research", r"research"), NOT_THE_FOLDER_AGAIN]),
        ("10-slice-without-requirements", "A slice with no requirements behind it: say what is missing; not skip ahead.",
         in_order(documents=["problem.md", "scope.md", "slice-001/slice.md"]), "what's next",
         [says("names-requirements-as-missing",
               r"(missing|out of order|nothing was found|no requirements|without|(has|have)(n't| not) been|"
               r"(does|do)(n't| not) exist|skipped)[\s\S]{0,200}requirements|requirements[\s\S]{0,200}"
               r"(missing|out of order|not found|(has|have)(n't| not) been|(does|do)(n't| not) exist|skipped|first)"),
          never_says("does-not-skip-ahead", r"next (stage|step)?[^.\n]{0,40}\b(is|:)[^.\n]{0,20}questions"),
          NOT_THE_FOLDER_AGAIN]),
        ("11-pull-request-ready", "A pull request ready to merge: put the pull request first.",
         in_order(lines=[pull(12, "Withdraw a proposal", "withdraw-proposal")]), "what's next",
         [first("pull-request-before-the-documents", PR, "research"), says("says-it-is-ready", r"ready|merge"),
          NOT_THE_FOLDER_AGAIN]),
        ("12-pull-request-comments", "A pull request with comments unaddressed: put the comments first.",
         in_order(lines=[comments]), "what's next",
         [first("pull-request-before-the-documents", PR, "research"),
          says("names-the-comments", r"comment|thread|review"), NOT_THE_FOLDER_AGAIN]),
        ("13-critical-issue", "An open critical issue, no pull request: ask whether to address it first.",
         in_order(lines=[issue(7, "Two members adding at once lose one of the books", "bug,critical"),
                         issue(9, "The list is hard to read on a small phone", "enhancement")]), "what's next",
         [says("names-the-issue", r"#7|critical"),
          says("asks-whether-to-address-it",
               r"(#7|issue|critical)[\s\S]{0,300}\?|\?[\s\S]{0,200}(#7|issue|critical)"), NOT_THE_FOLDER_AGAIN]),
        ("14-in-order", "A pull request with comments, a high issue and documents: pull request, issue, documents.",
         in_order(lines=[comments, issue(7, "Two members adding at once lose one of the books", "bug,high")]),
         "what's next",
         [first("pull-request-before-the-issue", PR, ISSUE), first("issue-before-the-documents", ISSUE, "research"),
          says("names-research-last", r"research"), NOT_THE_FOLDER_AGAIN]),
    ]


class _Cleanup:
    def __init__(self): self.todo = []
    def addCleanup(self, function, *args): self.todo.append((function, args))
    def run(self):
        for function, args in self.todo:
            function(*args)


def scaffold(machine):
    lines = ["#!/usr/bin/env bash",
             "# Makes this scenario's machine and project where the run starts. Generated by make_cases.py.",
             "set -euo pipefail",
             'here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
             f'key="$(pwd -P)/{STATE}"',
             'rm -rf "$key" && mkdir -p "$key"',
             'cp -R "$here/state/." "$key/"',
             f'report="{REPORTS}/$(pwd -P | tr \'/ \' \'__\')"',
             'mkdir -p "$(dirname "$report")" && cp "$here/report.txt" "$report"']
    if any(machine.project.iterdir()):
        if (machine.project / "planning").is_dir():
            lines.append("mkdir -p planning")
        lines.append('if [ -d "$here/project" ]; then cp -R "$here/project/." .; fi')
    if (machine.project / ".git").exists():
        lines += ["git init -q", "echo .cache/ >> .git/info/exclude", f"git remote add origin {REMOTE}",
                  "git add -A",
                  "git -c user.name=someone -c user.email=someone@example.org commit -q --allow-empty -m 'Planning documents'"]
    return "\n".join(lines) + "\n"


def case_yaml(name, description, prompt, graders):
    quoted = json.dumps
    out = ['schema_version: "1.1"', f"name: startup-{name}", f"description: {quoted(description)}",
           "tags: [startup]", "context:", "  scaffold_script: scaffold.sh", "execution:",
           f"  prompt: {quoted(prompt)}", "  max_turns: 15", "  timeout_seconds: 300",
           "  allowed_tools: [Read, Glob, Grep, Bash, Write, Edit]", "runs: 3", "graders:"]
    for grader in graders:
        out.append("  - " + quoted(grader))
    return "\n".join(out) + "\n"


def write(path, text, executable=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    if executable:
        path.chmod(0o755)


HOOK = """#!/bin/sh
# Hands the session the startup report of the made-up machine it was started on.
report="%s/$(pwd -P | tr '/ ' '__')"
[ -f "$report" ] || exit 0
sed "s|@STARTUP@|${CLAUDE_PLUGIN_ROOT}/startup|g" "$report"
""" % REPORTS


def main(table=False):
    """The bare arm in plugin/; with table=True the same cases in plugin-table/, the hook adding the table."""
    plugin = HERE / ("plugin-table" if table else "plugin")
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": "kd-startup-trial-table" if table else "kd-startup-trial", "version": "0.0.1",
         "description": "Stage 0's test only: one hook that hands a session the startup report."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", HOOK + ('cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n' if table else ""),
          executable=True)
    if table:
        shutil.copy(HERE / "routing-table.md", plugin / "hooks" / "routing-table.md")
    cleanup = _Cleanup()
    for name, description, make, prompt, graders in scenarios():
        machine = standin_machine.Machine(cleanup)
        make(machine)
        done = machine.run("report.sh")
        assert done.returncode == 0 and "REFUSED" not in done.stdout, (name, done.stdout, done.stderr)
        report = done.stdout.replace(str(STARTUP), "@STARTUP@")
        assert str(machine.root) not in report, (name, report)
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", case_yaml(name, description, prompt, graders + ALWAYS))
        write(case / "scaffold.sh", scaffold(machine), executable=True)
        tracker = report.split("\nTracker\n")[1].split("\nDocuments\n")[0]
        machine.set("gh/summary", tracker)
        for tool in TOOLS:
            if not (machine.bin / tool).exists():
                machine.set(f"absent/{tool}", "")
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(graders + ALWAYS)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(table="--table" in sys.argv[1:])
