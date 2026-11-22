#!/usr/bin/env python3
"""Run one example end to end: a planning session and a stand-in for its user, turn by turn.

The session is the tool run headless in the example's project with the assembled plugin; the
user is a second, tool-less session that answers from the example's brief and nothing else. The
stand-in is not a judge: what a run shows is read afterwards, in its transcript and documents.

A run ends after the session's first turn that began with a requirements document in the
planning folder (so the user's answers to its questions have been taken once), when the user
has nothing left to say, or at --max-turns.

Usage, inside the evaluation VM:
    python3 -I e2e/run.py e2e/examples/NAME --out FOLDER [--model M] [--user-model M] [--max-turns N]
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
USER = """You are playing a person who is talking to a planning assistant about something they \
want. You are not an assistant and you never offer help. Everything you know is in the brief below.

- Answer only what you were asked, in one to four plain sentences, the way this person talks.
- Volunteer nothing you were not asked for.
- Asked something the brief does not cover, or marks as not known, say you do not know or have \
not thought about it. Never make a fact up.
- Where the brief says how you behave at some point (a change of mind, an answer you skip), do \
exactly that at that point.
- If the assistant stops without asking anything, say: Go on.
- When the assistant has nothing more to ask and the brief leaves you nothing more to say, \
reply with the single word DONE.

You will be given the conversation so far. Reply with the person's next message and nothing else.

# The brief

"""


def section(brief, heading):
    """The text under a second-level heading of the brief, or nothing."""
    out, inside = [], False
    for line in brief.splitlines():
        if line.startswith("## "):
            inside = line[3:].strip().lower() == heading.lower()
        elif inside:
            out.append(line)
    return "\n".join(out).strip()


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


def written(planning):
    return planning.is_dir() and any(planning.glob("[0-9][0-9][0-9]_requirements*.md"))


def conversation(turns):
    return "\n\n".join(f"{'YOU' if who == 'user' else 'THE ASSISTANT'}: {text}" for who, text, _ in turns)


def run(example, out, plugin, model, user_model, max_turns, command=("claude",)):
    brief = (example / "brief.md").read_text(encoding="utf-8")
    opening, folder = section(brief, "Opening"), section(brief, "Planning folder") or "planning"
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
    user_extra = ["--model", user_model, "--system-prompt", USER + brief, "--tools", "", "--no-session-persistence"]
    turns, session, said, ended = [], None, opening, "the turns ran out"
    for _ in range(max_turns):
        had_list = written(project / folder)
        reply, session, cost = ask(command, said, project, session_extra + (["--resume", session] if session else []), env)
        turns += [("user", said, 0.0), ("assistant", reply, cost)]
        if had_list:
            ended = "the list was shown and the user's answers taken"
            break
        said, _, cost = ask(command, conversation(turns), nowhere, user_extra, env)
        turns[-1] = ("assistant", reply, turns[-1][2] + cost)   # the user's cost is kept with the turn it answers
        if said.strip().strip(".") == "DONE":
            ended = "the user had nothing more to say"
            break
    (out / "transcript.md").write_text("\n\n".join(
        f"**{'User' if who == 'user' else 'Session'}:** {text}" for who, text, _ in turns) + "\n", encoding="utf-8")
    summary = {"example": example.name, "model": model, "ended": ended, "session": session,
               "session_turns": sum(1 for who, _, _ in turns if who == "assistant"),
               "questions_put": sum(text.count("?") for who, text, _ in turns if who == "assistant"),
               "cost_usd": round(sum(cost for _, _, cost in turns), 4),
               # Each document under the number and name the stage script gives it, so the next session finds it.
               "numbered_in_order": [path.name for path in sorted((project / folder).glob("*.md"))]
               == ["000_problem.md", "001_scope-map.md", "002_requirements.md"] if (project / folder).is_dir() else False,
               "documents": sorted(str(path.relative_to(project)) for path in (project / folder).rglob("*.md"))
               if (project / folder).is_dir() else []}
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("example", type=pathlib.Path)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--plugin", type=pathlib.Path, default=HERE / "plugin")
    parser.add_argument("--model", default="claude-sonnet-5-5")
    parser.add_argument("--user-model", default="claude-sonnet-5-5")
    parser.add_argument("--max-turns", type=int, default=30)
    given = parser.parse_args()
    print(json.dumps(run(given.example.resolve(), given.out.resolve(), given.plugin.resolve(), given.model,
                         given.user_model, given.max_turns), indent=2))
