#!/usr/bin/env python3
"""Build every stage's scenarios with everything adopted loaded at once.

A stage's own test loads the texts that existed when it was run. Here each stage's adopted arm is
rebuilt and given every adopted text and the current routing table, so that a change to one
stage is seen by the scenarios of all of them.

Usage: python3 -I regress.py [NAME=TEXT ...]      (prints one line a stage: its name and the plugin to run)
    NAME=TEXT   a stage's text on trial, loaded as the skill NAME in every plugin before the owner
                has said it holds; startup's scenario of a stage that is not built moves past it
"""
import os
import pathlib
import shutil
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # found beside this file under -I
import make_plugin  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
# stage folder, the arguments that build its adopted arm, the plugin that leaves
STAGES = [("00-startup", ["--table"], "plugin-table"), ("01-problem", ["text"], "plugin-text"),
          ("02-scope-map", ["text"], "plugin-text"), ("03-requirements", ["kinds"], "plugin-kinds"), ("04-slice", ["text"], "plugin-text"),
          ("05-approach", ["text"], "plugin-text"), ("06-research", ["text"], "plugin-text"),
          ("07-questions", ["text"], "plugin-text")]


def overlay(plugin, root=ROOT, trial=None):
    """Every adopted text in the plugin, whatever it was built with, and any text on trial."""
    for name, source in {**make_plugin.SKILLS, **(trial or {})}.items():
        make_plugin.write(plugin / "skills" / name / "SKILL.md", (root / source).read_text(encoding="utf-8"))
    shutil.copy(root / "steps/00-startup/eval/routing-table.md", plugin / "hooks" / "routing-table.md")
    # The script the stage script names once the questions are next, and the library it reads.
    for script in ("questions/questions.py", "library/library.json"):
        make_plugin.write(plugin / script, (root / script).read_text(encoding="utf-8"))


def main(trial=None):
    for stage, arguments, plugin in STAGES:
        folder = ROOT / "steps" / stage / "eval"
        subprocess.run([sys.executable, "-I", "make_cases.py", *arguments], cwd=folder, check=True, capture_output=True,
                       env={**os.environ, "KD_TRIAL": ",".join(trial or {})})
        overlay(folder / plugin, trial=trial)
        print(stage, folder / plugin)


if __name__ == "__main__":
    main(dict(argument.split("=", 1) for argument in sys.argv[1:] if "=" in argument))
