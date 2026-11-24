#!/usr/bin/env python3
"""Check a kept run's quotes against the made-up services' pages: every "quote" (address) a run
wrote into an approach must be on that page, as the stand-in serves it or as the scenario started
with it saved. No model.

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


def pages_of(case_folder):
    """{address: text} for every page the scenario's made-up web serves to a site the VM allows there."""
    out = {}
    allowed = (case_folder / "state" / "web" / "allowed")
    hosts = allowed.read_text(encoding="utf-8").split() if allowed.exists() else []
    for path in sorted((case_folder / "state" / "web" / "pages").glob("*/*")):
        if path.suffix != ".down" and path.parent.name in hosts:
            address = f"https://{path.parent.name}/" + ("" if path.name == "index" else path.name)
            out[address] = page.squeeze(page.LINK.sub("", page.as_text(path.read_text(encoding="utf-8"), address)))
    return out


def count(record, case_folder):
    """(how many quotes the run's approach holds, a line for each thing wrong with one)."""
    _, files, _ = regrade.replay(record, regrade.started_with(case_folder))
    documents = {path.rsplit("/", 1)[-1]: text for path, text in files.items() if path.endswith("_approach.md")}
    return sum(len(page.PAIR.findall(text)) for text in documents.values()), page.check(documents, pages_of(case_folder))


def main(plugin, traces, name):
    for case in sorted((plugin / "evals").glob("*/case.yaml")):
        scenario, _ = regrade.graders(case)
        for run in sorted(traces.glob(f"{name}-{scenario}-*.jsonl")):
            pairs, wrong = count(run.read_text(encoding="utf-8", errors="replace"), case.parent)
            print(f"{run.stem}: {pairs} quotes, {len(wrong)} wrong")
            for line in wrong:
                print("  " + line)


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3])
