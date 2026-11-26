#!/usr/bin/env python3
"""Assemble everything adopted so far into one plugin, for the end-to-end runs.

The hook gives a new session the live startup report (the scripts run in the project, not a
canned report) and the routing table; the skills are the adopted stage texts. Nothing here is
the released plugin: it is rebuilt from the adopted pieces each time and not kept in git.

Usage: python3 -I make_plugin.py [FOLDER] [NAME=TEXT ...]      (default: plugin/ beside this file)
    NAME=TEXT   a stage's text that is not adopted yet, loaded as the skill NAME for a trial: with
                it the examples are run before the owner is asked whether the stage holds
"""
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
SKILLS = {"problem": "steps/01-problem/eval/problem-skill.md",
          "scope-map": "steps/02-scope-map/eval/scope-map-skill.md",
          "requirements": "steps/03-requirements/eval/requirements-skill-kinds.md",
          "slice": "steps/04-slice/eval/slice-skill.md",
          "approach": "steps/05-approach/eval/approach-skill.md",
          "research": "steps/06-research/eval/research-skill.md",
          "questions": "steps/07-questions/eval/questions-skill.md",
          "security": "steps/07b-security/eval/security-skill.md",
          "answers": "steps/08-answers/eval/answers-skill.md"}
HOOK = """#!/bin/sh
# The startup report of this machine and project, then what to do with it.
sh "${CLAUDE_PLUGIN_ROOT}/startup/report.sh"
cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"
"""


def write(path, text, executable=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    if executable:
        path.chmod(0o755)


def main(folder, trial=None):
    shutil.rmtree(folder, ignore_errors=True)
    write(folder / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": "kd-dev-team-trial", "version": "0.0.1",
         "description": "The adopted stages together, for end-to-end runs only."}, indent=2) + "\n")
    # Only a new session is given the report: a headless run resumes its session at every turn.
    write(folder / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"matcher": "startup", "hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(folder / "hooks" / "report.sh", HOOK, executable=True)
    shutil.copy(ROOT / "steps/00-startup/eval/routing-table.md", folder / "hooks" / "routing-table.md")
    (folder / "startup").mkdir()
    for script in [*(ROOT / "startup").glob("*.sh"), ROOT / "startup" / "tracker.jq"]:
        shutil.copy(script, folder / "startup" / script.name)
    # The page reader the stage script names for the approach and research.
    write(folder / "research" / "page.py", (ROOT / "research" / "page.py").read_text(encoding="utf-8"))
    # The script that draws a slice's questions, and the library it reads.
    write(folder / "questions" / "questions.py", (ROOT / "questions" / "questions.py").read_text(encoding="utf-8"))
    write(folder / "library" / "library.json", (ROOT / "library" / "library.json").read_text(encoding="utf-8"))
    # The script that says which questions no answer settles, and draws the answers.
    write(folder / "answers" / "answers.py", (ROOT / "answers" / "answers.py").read_text(encoding="utf-8"))
    for name, source in {**SKILLS, **(trial or {})}.items():
        write(folder / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    return folder


if __name__ == "__main__":
    given = [argument for argument in sys.argv[1:] if "=" not in argument]
    print(main(pathlib.Path(given[0]) if given else HERE / "plugin",
               dict(argument.split("=", 1) for argument in sys.argv[1:] if "=" in argument)))
