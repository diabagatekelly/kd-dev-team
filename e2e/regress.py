#!/usr/bin/env python3
"""Build every stage's scenarios with everything adopted loaded at once.

A stage's own test loads the texts that existed when it was run. Here each stage's adopted arm is
rebuilt and given every adopted text and the current routing table, so that a change to one
stage is seen by the scenarios of all of them.

Usage: python3 -I regress.py      (prints one line a stage: its name and the plugin to run)
"""
import pathlib
import shutil
import subprocess
import sys

import make_plugin

ROOT = pathlib.Path(__file__).resolve().parent.parent
# stage folder, the arguments that build its adopted arm, the plugin that leaves
STAGES = [("00-startup", ["--table"], "plugin-table"), ("01-problem", ["text"], "plugin-text"),
          ("02-scope-map", ["text"], "plugin-text"), ("03-requirements", ["kinds"], "plugin-kinds")]


def overlay(plugin, root=ROOT):
    """Every adopted text in the plugin, whatever it was built with."""
    for name, source in make_plugin.SKILLS.items():
        make_plugin.write(plugin / "skills" / name / "SKILL.md", (root / source).read_text(encoding="utf-8"))
    shutil.copy(root / "steps/00-startup/eval/routing-table.md", plugin / "hooks" / "routing-table.md")


def main():
    for stage, arguments, plugin in STAGES:
        folder = ROOT / "steps" / stage / "eval"
        subprocess.run([sys.executable, "-I", "make_cases.py", *arguments], cwd=folder, check=True, capture_output=True)
        overlay(folder / plugin)
        print(stage, folder / plugin)


if __name__ == "__main__":
    main()
