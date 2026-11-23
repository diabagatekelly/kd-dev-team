#!/usr/bin/env python3
"""Check a kept run's quotes against the made-up provider's pages: every "quote" (address) a run
wrote into a research document must be on that page as the stand-in serves it. No model.

Usage: python3 -I quotes.py PLUGIN TRACES NAME     (as e2e/regrade.py: one line a run)
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


page = load("page", ROOT / "research/page.py")
regrade = load("regrade", ROOT / "e2e/regrade.py")


def served(case_folder):
    """{address: text} for every page the scenario's made-up web serves."""
    out = {}
    for path in sorted((case_folder / "state" / "web" / "pages").glob("*/*")):
        if path.suffix != ".down":
            address = f"https://{path.parent.name}/" + ("" if path.name == "index" else path.name)
            out[address] = page.squeeze(page.as_text(path.read_text(encoding="utf-8"), address))
    return out


def main(plugin, traces, name):
    for case in sorted((plugin / "evals").glob("*/case.yaml")):
        scenario, _ = regrade.graders(case)
        for run in sorted(traces.glob(f"{name}-{scenario}-*.jsonl")):
            _, files, _ = regrade.replay(run.read_text(encoding="utf-8", errors="replace"), {})
            documents = {path: text for path, text in files.items() if "_research/" in path and path.endswith(".md")}
            wrong = page.check(documents, served(case.parent))
            pairs = sum(len(page.PAIR.findall(text)) for text in documents.values())
            print(f"{run.stem}: {pairs} quotes, {len(wrong)} wrong")
            for line in wrong:
                print("  " + line.split("_research/")[-1])


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3])
