#!/usr/bin/env python3
"""Run one example end to end: a planning session and a scripted user, turn by turn.

The session is the tool run headless in the example's project with the assembled plugin. The user
is a script: every word it says is written beforehand in the example's brief. A model is used for
one thing only, to say which of the brief's topics the session's message asks about; it never
writes an answer, and what it picked is kept beside each turn so a wrong pick can be seen.

What the user says, in this order:
- when a document has just appeared for the first time, the line the brief gives for that moment;
- else the brief's answers to the topics asked about, in the order asked (after the requirements
  are first shown, only as many as the brief allows), and the brief's "not known" line once for
  anything asked that no topic covers;
- else, when nothing was asked, the brief's line for going on.

A run ends after the session's first turn that began with a requirements document in the planning
folder (so the user's answers to its questions have been taken once), or at --max-turns.

Usage, inside the evaluation VM:
    python3 -I e2e/run.py e2e/examples/NAME --out FOLDER [--model M] [--sorter-model M] [--max-turns N]
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
SORTER = """You sort questions; you never answer them. You are given a message from a planning \
assistant to a person, and a list of topics, each a key and what it covers.

Reply with one line of JSON and nothing else:
{"asked": [the keys of the topics the message asks the person about, in the order it asks them], \
"uncovered": the number of separate questions in the message that no topic covers, \
"asks": true if the message asks the person anything at all or waits for their approval, else false}

A question counts only if the person is expected to answer it. A key is listed once. Use only keys \
from the list. When unsure whether a topic covers a question, count the question as uncovered.

# The topics

"""
DOCUMENTS = ("problem", "scope-map", "requirements")


def section(brief, heading):
    """The text under a second-level heading of the brief, or nothing."""
    out, inside = [], False
    for line in brief.splitlines():
        if line.startswith("## "):
            inside = line[3:].strip().lower() == heading.lower()
        elif inside:
            out.append(line)
    return "\n".join(out).strip()


def rows(text):
    """The rows of a markdown table as lists of cells, without its heading and rule."""
    found = [[cell.strip() for cell in line.strip().strip("|").split("|")]
             for line in text.splitlines() if line.strip().startswith("|")]
    return [row for row in found[2:] if any(row)]


class Brief:
    """Everything the user will ever say, read from the example's brief."""

    def __init__(self, text):
        self.opening = section(text, "Opening")
        self.folder = section(text, "Planning folder") or "planning"
        self.topics = {key: (covers, says) for key, covers, says in rows(section(text, "Answers"))}
        self.not_known = section(text, "Not known") or "I don't know yet."
        self.go_on = section(text, "Nothing asked") or "Go on."
        self.shown = {name: says for name, says in rows(section(text, "When a document is first shown"))}
        limit = section(text, "Answers to the requirements' questions")
        self.limit = int(re.search(r"\d+", limit).group()) if re.search(r"\d+", limit) else None

    def topic_list(self):
        return "\n".join(f"- {key}: {covers}" for key, (covers, _) in self.topics.items())

    def reply(self, picked, appeared, limited):
        """The user's next message: from what was picked, the documents that just appeared, and
        whether the requirements have just been shown (when only `limit` answers are given)."""
        for name in DOCUMENTS:
            if name in appeared and name in self.shown:
                return self.shown[name]
        asked = [key for key in dict.fromkeys(picked.get("asked") or []) if key in self.topics]
        skipped = 0
        if limited and self.limit is not None:
            asked, skipped = asked[:self.limit], len(asked[self.limit:])
        parts = [self.topics[key][1] for key in asked]
        if picked.get("uncovered") and not (limited and self.limit is not None and skipped):
            parts.append(self.not_known)
        return " ".join(parts) if parts else self.go_on


def path_without(absent, path, bin_folder):
    """A PATH on which the tools named in `absent` are not found.

    The evaluation VM keeps its stand-in tools in one folder with the tool under test, and a
    script asks whether a tool is installed by looking for it on the PATH. Every folder that
    holds an absent tool is left out, and what else it held is linked from `bin_folder`.
    """
    kept = []
    bin_folder.mkdir(parents=True, exist_ok=True)
    for folder in dict.fromkeys(path.split(os.pathsep)):
        here = pathlib.Path(folder)
        if not any((here / tool).exists() for tool in absent):
            kept.append(folder)
            continue
        for entry in here.iterdir():
            if entry.name not in absent and not (bin_folder / entry.name).exists():
                (bin_folder / entry.name).symlink_to(entry)
    return os.pathsep.join([str(bin_folder), *kept])


def ask(command, prompt, cwd, extra, env=None):
    """One headless call; its reply, its session and its cost."""
    done = subprocess.run([*command, "-p", prompt, "--output-format", "json", *extra], cwd=cwd, env=env,
                          capture_output=True, text=True, timeout=1500)
    try:
        answer = json.loads(done.stdout)
    except ValueError:
        raise SystemExit(f"the tool gave no answer:\n{done.stdout[-2000:]}\n{done.stderr[-2000:]}")
    return answer.get("result") or "", answer.get("session_id"), answer.get("total_cost_usd") or 0.0


def picked_from(text):
    """What the sorter said, or "one thing asked that no topic covers" when it cannot be read."""
    found = re.search(r"\{[\s\S]*\}", text or "")
    try:
        picked = json.loads(found.group()) if found else None
    except ValueError:
        picked = None
    if not isinstance(picked, dict) or not isinstance(picked.get("asked", []), list):
        return {"asked": [], "uncovered": 1, "asks": True, "unread": True}
    return picked


def present(planning):
    """Which of the three documents exist in the planning folder, by name."""
    names = [path.name for path in planning.glob("*.md")] if planning.is_dir() else []
    return {name for name in DOCUMENTS if any(name in file for file in names)}


def run(example, out, plugin, model, sorter_model, max_turns, command=("claude",)):
    brief = Brief((example / "brief.md").read_text(encoding="utf-8"))
    project, nowhere = out / "project", out / "nowhere"
    shutil.rmtree(out, ignore_errors=True)
    nowhere.mkdir(parents=True)
    if (example / "project").is_dir():
        shutil.copytree(example / "project", project)
    else:
        project.mkdir()
    # The made-up machine the stand-in tools answer as: inside a VM, a tracker with nothing open.
    machine = example / "machine" if (example / "machine").is_dir() else HERE / "machine"
    shutil.copytree(machine, project / ".cache" / "machine")
    for step in (["init", "-q"], ["remote", "add", "origin", "https://github.com/someone/something.git"],
                 ["add", "-A", "--", ".", ":!.cache"],
                 ["-c", "user.name=someone", "-c", "user.email=someone@example.org", "commit", "-q", "--allow-empty",
                  "-m", "Where the project stood"]):
        subprocess.run(["git", *step], cwd=project, check=True, capture_output=True)
    with (project / ".git" / "info" / "exclude").open("a", encoding="utf-8") as exclude:
        exclude.write(".cache/\n")
    absent = [path.name for path in (machine / "absent").iterdir()] if (machine / "absent").is_dir() else []
    env = {**os.environ, "PATH": path_without(absent, os.environ.get("PATH", ""), out / "bin")}
    session_extra = ["--model", model, "--plugin-dir", str(plugin), "--dangerously-skip-permissions"]
    sorter_extra = ["--model", sorter_model, "--system-prompt", SORTER + brief.topic_list(), "--tools", "",
                    "--no-session-persistence"]
    planning = project / brief.folder
    turns, session, said, ended, seen, cost = [], None, brief.opening, "the turns ran out", set(), 0.0
    for _ in range(max_turns):
        had_list = "requirements" in present(planning)
        reply, session, spent = ask(command, said, project, session_extra + (["--resume", session] if session else []), env)
        cost += spent
        turn = {"user": said, "session": reply}
        turns.append(turn)
        if had_list:
            ended = "the list was shown and the user's answers taken"
            break
        appeared = present(planning) - seen
        seen |= appeared
        sorted_, _, spent = ask(command, reply, nowhere, sorter_extra, env)
        cost += spent
        turn["picked"], turn["appeared"] = picked_from(sorted_), sorted(appeared)
        said = brief.reply(turn["picked"], appeared, limited="requirements" in appeared)
    (out / "transcript.md").write_text("\n\n".join(
        f"**User:** {turn['user']}\n\n**Session:** {turn['session']}" for turn in turns) + "\n", encoding="utf-8")
    (out / "turns.json").write_text(json.dumps(turns, indent=2) + "\n", encoding="utf-8")
    documents = sorted(planning.rglob("*.md")) if planning.is_dir() else []
    summary = {"example": example.name, "model": model, "ended": ended, "session": session,
               "session_turns": len(turns),
               "questions_put": sum(turn["session"].count("?") for turn in turns),
               "asked_and_not_covered": sum((turn.get("picked") or {}).get("uncovered") or 0 for turn in turns),
               "cost_usd": round(cost, 4),
               # Each document under the number and name the stage script gives it, so the next session finds it.
               "numbered_in_order": [path.name for path in documents]
               == ["000_problem.md", "001_scope-map.md", "002_requirements.md"],
               "documents": [str(path.relative_to(project)) for path in documents]}
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("example", type=pathlib.Path)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--plugin", type=pathlib.Path, default=HERE / "plugin")
    parser.add_argument("--model", default="claude-sonnet-5-5")
    parser.add_argument("--sorter-model", default="claude-haiku-5-5")
    parser.add_argument("--max-turns", type=int, default=30)
    given = parser.parse_args()
    print(json.dumps(run(given.example.resolve(), given.out.resolve(), given.plugin.resolve(), given.model,
                         given.sorter_model, given.max_turns), indent=2))
