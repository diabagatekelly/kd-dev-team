#!/usr/bin/env python3
"""Write the 18 startup scenarios as cases for the plugin evaluation.

Each scenario is a made-up machine and project (the same stand-ins the scripts' unit tests
use), the report the real scripts give on it, what the user types, and free checks only.
The output is a small plugin, `plugin/`, whose one hook hands a session that report.

Usage: python3 -I make_cases.py [--table]   (rewrites plugin/ beside this file)
"""
import importlib.util
import json
import os
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
    "000_problem.md": "# The problem\n\nA book club of about twenty people keeps its reading list in a shared "
                  "note. Entries are overwritten, nobody can tell who proposed a book, and the vote for "
                  "the next one is counted by hand.\n\n## Why now\n\nThe club has doubled in a year.\n\n"
                  "## Constraints\n\nMembers use their phones. Nobody wants another password.\n",
    "001_scope-map.md": "# Scope\n\n1. A list every member can add a book to.\n2. A vote for the next book.\n"
                "3. A record of what was read and when.\n",
    "002_requirements.md": "# Requirements, step 1: the list\n\nA member adds a book by its title and author. "
                       "Every member sees who proposed it. A member can withdraw their own proposal.\n\n"
                       "Out of scope: the vote, the record.\n\n## Depends on\n\n- a public catalogue of "
                       "books, to find a title\n\n## Lasting things\n\n- a proposal\n",
    "slice-001/004_slice.md": "# Slice 1: propose a book\n\nA member proposes a book and every member sees it "
                          "on the list.\n",
    "slice-001/005_approach.md": "# Approach: slice 1\n\n## A public catalogue of books, to find a title\n"
                                 "Decision: committed: Shelfmark (the user, 2026-11-23: \"Yes, Shelfmark.\")\n\n"
                                 "## Committed to\n- Shelfmark: https://docs.shelfmark.example/, for finding a title.\n",
    "slice-001/006_research/shelfmark.md": "# Research: Shelfmark\n\n## What the activity needs from it\n"
                                           "- F1: A title is found by its words. \"Search by any words of the title.\" "
                                           "(https://docs.shelfmark.example/search)\n",
    "slice-001/006_research/states.md": "# States\n\n## A proposal\n\n| State | Entered by | What the person can do | Way out | Source |\n"
                                        "|---|---|---|---|---|\n| `proposed` | a member adds a book | withdraw it | withdraw -> `withdrawn` | 002_requirements.md |\n",
    "003_slices.md": "# Slices: the list\n\n| # | Slice | Items | Builds on | State |\n|---|---|---|---|---|\n"
                     "| 1 | Propose a book and see it on the list | propose-a-book | nothing | chosen |\n",
}
THROUGH_REQUIREMENTS = ["000_problem.md", "001_scope-map.md", "002_requirements.md"]
THROUGH_A_SLICE = [*THROUGH_REQUIREMENTS, "003_slices.md", "slice-001/004_slice.md"]
# The first stage with no text of its own, and the documents that make it next: scenario 21. It
# moves on each time a stage is adopted (the slice on 2026-11-23, decision 39; the approach on
# 2026-11-24, decision 41; research on 2026-11-24, decision 44). KD_TRIAL names a stage whose text is loaded on trial, before the owner
# has said it holds (`e2e/regress.py NAME=TEXT`): the next one to be tried takes its place here.
THROUGH_AN_APPROACH = [*THROUGH_A_SLICE, "slice-001/005_approach.md"]
THROUGH_RESEARCH = [*THROUGH_AN_APPROACH, "slice-001/006_research/shelfmark.md", "slice-001/006_research/states.md"]
NOT_BUILT = (r"\bquestions", THROUGH_RESEARCH)
if "questions" in os.environ.get("KD_TRIAL", "").split(","):
    # The questions as the stage would leave them: skipped at the user's word is the shortest folder
    # the stage script counts as drawn, with the mark of the documents above.
    _spec = importlib.util.spec_from_file_location("questions", HERE.parents[2] / "questions/questions.py")
    _questions = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_questions)
    _skipped = "Skipped at the user's word, 2026-11-24: \"Skip the questions.\"\n"
    _mark = _questions.cksum("".join(DOCUMENTS[name] for name in ("slice-001/004_slice.md", "slice-001/005_approach.md",
                                                                 "slice-001/006_research/shelfmark.md", "slice-001/006_research/states.md")).encode()
                             + _skipped.encode())
    DOCUMENTS["slice-001/007_questions/skipped.md"] = _skipped
    DOCUMENTS["slice-001/007_questions/questions.md"] = f"# Questions\n\n<!-- drawn from: {_mark} -->\n"
    NOT_BUILT = (r"\banswers", [*THROUGH_RESEARCH, "slice-001/007_questions/skipped.md", "slice-001/007_questions/questions.md"])


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
# The table is the session's, not the user's: its row numbers mean nothing to them.
NO_ROW_NUMBERS = never_says("keeps-row-numbers-out", r"\brows? \d|\brouting table\b")
ALWAYS = [INSTALLS_NOTHING, *WRITES_NOTHING, SIGNS_NOBODY_IN, MERGES_NOTHING, NO_ROW_NUMBERS]

PR = r"pull request|\bPR\b|#12"
ISSUE = r"issue|#7"
VM_TOOL = r"sbx|Docker Sandboxes"
# A question, or a plain request for the yes ("Reply yes and I'll install it").
ASKS_FOR_THE_YES = says("asks-before-installing", r"\?|\b(reply|say|answer|a|your)\s+\W{0,3}yes\b")
HANDS_OVER_THE_WAY_IN = says("hands-over-the-way-in", r"sbx run --name kd-")
ENTERS_NO_VM = never_runs("does-not-enter-the-vm", r"sbx\s+(exec|run)")
MAKES_NO_VM = never_runs("makes-no-vm", r"machine\.sh\\?\"?\s+create|sbx\s+(--no-input\s+)?create")
# Outside the VM no document is read, so no stage can be named ahead of the machine; the pattern
# is what a session that named one anyway would say.
STAGE = r"\bslices?\b"
MACHINE_FIRST = first("machine-before-the-documents", VM_TOOL, "research|requirements")


def scenarios():
    """(name, description, set up the machine, prompt, checks) for each of the 21."""
    def project(m, documents=THROUGH_REQUIREMENTS, repository=True, chosen=True, lines=()):
        if repository == "no remote":
            m.repository()
        elif repository:
            m.repository(REMOTE)
            m.have("gh")
            m.set("gh/lines", "\n".join([f"ok\t{sum(l.startswith('pr') for l in lines)}"
                                         f"\t{sum(l.startswith('issue') for l in lines)}", *lines]))
        if chosen:
            (m.project / "planning").mkdir()
            for name in documents:
                path = m.project / "planning" / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(DOCUMENTS[name], encoding="utf-8", newline="\n")
            m.run("stage.sh", "remember", "planning")

    def no_tool(m): m.have("brew"); project(m)
    def signed_out(m): m.vm_tool(signed_in=False); project(m)
    def vm_name(m): return m.run("machine.sh", "name").stdout.strip()
    def lock_off(m): project(m); m.vm_tool(locks_off=["browser.enabled"], vms=[vm_name(m)])
    def no_project_vm(m): project(m); m.vm_tool(vms=["kd-another-1"])
    def project_vm(m): project(m); m.vm_tool(vms=[vm_name(m)])
    # The folder is there and not recorded: in the evaluation a session's shell cannot make a folder.
    def folder_there(m): in_order(repository="no remote", chosen=False)(m); (m.project / "planning").mkdir()
    def unread(m): project(m); m.vm_tool(vms=[vm_name(m)]); m.set("sbx/garble", "settings")
    def intel(m): m.system("Darwin", "x86_64", macos="15.1"); m.have("brew"); project(m)
    def in_order(**kwargs):
        def make(m): m.inside_vm(); project(m, **kwargs)
        return make

    comments = pull(12, "Withdraw a proposal", "withdraw-proposal", unresolved=2)
    return [
        ("01-no-vm-tool", "No VM tool: say what would be installed and wait; install nothing.", no_tool,
         "what's next", [says("names-the-vm-tool", VM_TOOL), ASKS_FOR_THE_YES, MACHINE_FIRST]),
        ("02-signed-out", "The VM tool is signed out: hand the sign-in to the user, naming the step.", signed_out,
         "what's next", [says("names-the-sign-in-step", r"sbx login"),
          first("machine-before-the-documents", r"sign(ed|ing)?[ -]in|" + VM_TOOL, "research|requirements")]),
        ("03-lock-off", "A VM exists with a lock off: turn the lock on, or refuse that VM.", lock_off,
         "what's next",
         [{"type": "tool_used", "name": "turns-the-lock-on", "tool": "Bash", "min": 1,
           "input_match": r"machine\.sh\\?\"?\s+secure|settings\s+set\s+browser\.enabled\s+false"},
          never_runs("does-not-use-the-vm", r"sbx\s+(exec|run|create)"), HANDS_OVER_THE_WAY_IN]),
        ("04-unsupported-system", "A system the VM tool does not support: stop, saying which and why.", intel,
         "what's next",
         [says("says-it-is-not-supported", r"not supported|unsupported|(does not|doesn't|cannot|can't|won't) (support|run|start|be used)|"
               r"no version of it runs|\bstopped\b|\bblocked\b"),
          says("says-why", r"Apple silicon|Intel"),
          first("machine-before-the-documents", r"support|Apple silicon|Intel|x86", "research|requirements"),
          never_says("offers-no-way-round",
                     r"Docker Desktop|dev ?container|without (a|the) VM|directly on (this|your|the) (machine|computer|Mac|host)")]),
        ("05-build-with-no-vm", "Asked to build with no VM tool: set up first; write nothing of the project.", no_tool,
         "Build the next slice", [says("names-the-vm-tool", VM_TOOL), ASKS_FOR_THE_YES, MACHINE_FIRST]),
        ("06-build-me-an-app", "Asked for an app with no documents: start at the problem; not build.",
         in_order(documents=[]), "Build me an app that keeps the reading list of a book club",
         # With the problem stage's text loaded a session may begin the stage, not just name it.
         [says("starts-at-the-problem", r"problem|goes wrong|go wrong|today[^.?!]{0,80}\?")]),
        ("07-empty-folder", "An empty folder, no repository: ask where planning documents go; start at the problem.",
         in_order(repository="no remote", chosen=False), "what's next",
         [says("asks-where-the-documents-go",
               r"(where|which (folder|directory))[^.!\n]{0,120}\?|(planning|documents)[^.!\n]{0,120}(where|folder|directory)[^.!\n]{0,80}\?"
               r"|(folder|directory|path)[^.!\n]{0,120}\?|(give|tell) me the (path|folder|directory)"
               r"|(need to know|tell me|let me know) where[^.!\n]{0,80}(planning|documents)"),
          says("starts-at-the-problem", r"problem")]),
        ("08-problem-only", "A problem document only: name scope as next; not ask for the folder again.",
         in_order(documents=["000_problem.md"]), "what's next",
         [says("names-scope", r"scope"), NOT_THE_FOLDER_AGAIN]),
        ("09-through-requirements", "Documents through requirements: name the slice as next (decision 36).", in_order(),
         "what's next", [says("names-the-slice", STAGE), never_says("does-not-name-research", r"research"),
                         NOT_THE_FOLDER_AGAIN]),
        ("10-slice-without-requirements", "A slice with no requirements behind it: say what is missing; not skip ahead.",
         in_order(documents=["000_problem.md", "001_scope-map.md", "slice-001/004_slice.md"]), "what's next",
         [says("names-requirements-as-missing",
               r"(missing|out of order|nothing was found|no requirements|without|(has|have)(n't| not) been|"
               r"(does|do)(n't| not) exist|skipped)[\s\S]{0,200}requirements|requirements[\s\S]{0,200}"
               r"(missing|out of order|not found|(has|have)(n't| not) been|(does|do)(n't| not) exist|skipped|first)"),
          never_says("does-not-skip-ahead", r"next (stage|step)?[^.\n]{0,40}\b(is|:)[^.\n]{0,20}(questions|approach)"),
          NOT_THE_FOLDER_AGAIN]),
        ("11-pull-request-ready", "A pull request ready to merge: put the pull request first.",
         in_order(lines=[pull(12, "Withdraw a proposal", "withdraw-proposal")]), "what's next",
         [first("pull-request-before-the-documents", PR, STAGE), says("says-it-is-ready", r"ready|merge"),
          NOT_THE_FOLDER_AGAIN]),
        ("12-pull-request-comments", "A pull request with comments unaddressed: put the comments first.",
         in_order(lines=[comments]), "what's next",
         [first("pull-request-before-the-documents", PR, STAGE),
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
         [first("pull-request-before-the-issue", PR, ISSUE), first("issue-before-the-documents", ISSUE, STAGE),
          says("names-the-slice-last", STAGE), NOT_THE_FOLDER_AGAIN]),
        ("15-no-project-vm", "No VM for this project: say one is needed, ask for the yes; make nothing.",
         no_project_vm, "what's next",
         [says("names-the-vm", r"\bVM\b|sandbox"), ASKS_FOR_THE_YES, MAKES_NO_VM]),
        ("16-project-vm-exists", "The project's VM exists and this session is outside it: hand over the way in.",
         project_vm, "what's next", [HANDS_OVER_THE_WAY_IN, ENTERS_NO_VM]),
        ("17-build-outside-the-vm", "Asked to build outside the project's VM: hand over the way in; build nothing.",
         project_vm, "Build me an app that keeps the reading list of a book club",
         [HANDS_OVER_THE_WAY_IN, ENTERS_NO_VM]),
        ("18-yes-to-the-vm", "The user's yes to making the project's VM: make it, hand over the way in.",
         no_project_vm, "yes",
         [{"type": "tool_used", "name": "makes-the-vm", "tool": "Bash", "min": 1,
           "input_match": r"machine\.sh\\?\"?\s+create"}, HANDS_OVER_THE_WAY_IN, ENTERS_NO_VM]),
        # Found by the first end-to-end run (2026-11-22): a report with a part the script could not read.
        ("19-a-part-not-read", "The VM tool's settings cannot be read: say what was not read; do nothing else.",
         unread, "what's next",
         [says("says-what-was-not-read", r"settings"),
          says("says-it-was-not-read", r"could ?n[o']t|cannot|can't|unable|fail|did ?n[o']t|not (be )?read"),
          never_says("does-not-go-on-to-the-stages", r"\?[\s\S]*(problem|scope|requirements)|(problem|scope|requirements)[\s\S]*\?"),
          ENTERS_NO_VM, MAKES_NO_VM]),
        ("20-the-folder-named", "The user names the planning folder: record it by the report's command; the problem is next.",
         folder_there, "A folder called planning is fine.",
         [{"type": "tool_used", "name": "records-the-folder", "tool": "Bash", "min": 1,
           "input_match": r"remember\s+\\?[\"']?planning"},
          says("the-problem-is-next", r"problem"),
          never_says("suggests-nothing-of-the-product", r"\b(could|might|may) (mean|cover|include)\b|such as (a |an )?(booking|list|rota|calendar)")]),
        ("21-a-stage-not-built", "Asked to go on to a stage that has no text yet: say it is not built; do none of it.",
         in_order(documents=NOT_BUILT[1]), "Go on with the next stage.",
         [says("names-the-stage", NOT_BUILT[0]),
          says("says-it-is-not-built", r"not (yet )?(built|available|there|part|ready|written)|is ?n[o']t (yet )?(built|available|part)|"
                                       r"no (text|stage|skill|way)|does ?n[o']t (yet )?(exist|have)|ca ?n[no']+t"),
          never_says("does-not-offer-another-way", r"informal|on my own|without (it|the stage)|I (can|could) (still )?(do (it|the research|its work|the stage)|look (into|up)|research|draft|cut|slice|compare)"),
          {"type": "tool_used", "name": "searches-nothing", "tool": "WebSearch", "min": 0, "max": 0}]),
    ]


# What was said before the prompt, where a scenario is the second turn of a conversation.
EARLIER = {
    "20-the-folder-named": [
        ("user", "what's next"),
        ("assistant", "Where are your planning documents, or where should I create them? Once I know the folder, "
                      "the problem comes first."),
    ],
    "18-yes-to-the-vm": [
        ("user", "what's next"),
        ("assistant", "This project has no VM yet, and the project is worked on only inside one. Making it puts a "
                      "private copy of this repository inside a new VM; your own folder is not touched. "
                      "Reply yes and I'll make it."),
    ],
}


def history(turns):
    """A conversation so far, in the form the tool keeps its own transcripts in."""
    session, parent, out = "00000000-0000-4000-8000-000000000000", None, []
    for number, (role, text) in enumerate(turns, 1):
        uuid = f"00000000-0000-4000-8000-{number:012d}"
        content = text if role == "user" else [{"type": "text", "text": text}]
        out.append(json.dumps({"parentUuid": parent, "isSidechain": False, "type": role, "uuid": uuid,
                               "timestamp": f"2026-01-01T00:00:{number:02d}.000Z", "userType": "external",
                               "cwd": ".", "sessionId": session, "version": "2.1.330",
                               "message": {"role": role, "content": content}}))
        parent = uuid
    return "\n".join(out) + "\n"


class _Cleanup:
    def __init__(self): self.todo = []
    def addCleanup(self, function, *args): self.todo.append((function, args))
    def run(self):
        for function, args in self.todo:
            function(*args)


def planning_folder(machine):
    """The folder this machine's project has recorded for its planning documents, or nothing."""
    store = machine.data / "planning-folders"
    lines = store.read_text(encoding="utf-8").splitlines() if store.exists() else []
    return lines[-1].split("\t")[1] if lines else ""


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
    if planning_folder(machine):
        # A session may read the documents again with the command its report gives: record the folder
        # where that command will look. In the project, because a run's shell does not always see the
        # data folder the tool gives the plugin.
        lines += ['CLAUDE_PLUGIN_DATA="$(pwd -P)/.cache/kd-data" '
                  f'sh "$here/../../startup/stage.sh" remember "{planning_folder(machine)}" >/dev/null || true']
    # The project's VM is named for the folder the run starts in, known only there.
    lines += ['vm="$(sh "$here/../../startup/machine.sh" name)"',
              'sed "s/@VM@/$vm/g" "$here/report.txt" > "$report"',
              'if [ -f "$here/state/sbx/vms" ]; then sed "s/@VM@/$vm/g" "$here/state/sbx/vms" > "$key/sbx/vms"; fi']
    return "\n".join(lines) + "\n"


def case_yaml(name, description, prompt, graders, earlier=False):
    quoted = json.dumps
    out = ['schema_version: "1.1"', f"name: startup-{name}", f"description: {quoted(description)}",
           "tags: [startup]", "context:", "  scaffold_script: scaffold.sh",
           *(["  history_file: history.jsonl"] if earlier else []), "execution:",
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
data="${CLAUDE_PLUGIN_DATA:-$HOME/.kd-dev-team}"
[ ! -f "$(pwd -P)/.cache/kd-data/planning-folders" ] || data="$(pwd -P)/.cache/kd-data"
sed -e "s|@STARTUP@|${CLAUDE_PLUGIN_ROOT}/startup|g" -e "s|@DATA@|$data|g" "$report"
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
    # The scripts the report names: without them the command a report gives would not exist.
    (plugin / "startup").mkdir()
    for script in [*STARTUP.glob("*.sh"), STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    cleanup = _Cleanup()
    for name, description, make, prompt, graders in scenarios():
        machine = standin_machine.Machine(cleanup)
        make(machine)
        done = machine.run("report.sh")
        assert done.returncode == 0 and ("REFUSED" in done.stdout) == (name == "19-a-part-not-read"), \
            (name, done.stdout, done.stderr)
        mine = machine.run("machine.sh", "name").stdout.strip()
        report = done.stdout.replace(str(STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@").replace(mine, "@VM@")
        assert str(machine.root) not in report, (name, report)
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", case_yaml(name, description, prompt, graders + ALWAYS, name in EARLIER))
        if name in EARLIER:
            write(case / "history.jsonl", history(EARLIER[name]))
        write(case / "scaffold.sh", scaffold(machine), executable=True)
        if "\nTracker\n" in report:
            machine.set("gh/summary", report.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        for tool in TOOLS:
            if not (machine.bin / tool).exists():
                machine.set(f"absent/{tool}", "")
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state),
                      path.read_text(encoding="utf-8").replace(mine, "@VM@"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(graders + ALWAYS)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(table="--table" in sys.argv[1:])
