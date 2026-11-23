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

Where the brief says so, the user closes the session once a document has been written and comes
back in a new one, which is given a fresh startup report and none of the conversation.

A run goes on through the slice stage: once a slice's own document has been written, its merge is
made up (the tracker's stand-in is given a merged pull request that names that document's
criteria), the user comes back in a new session and says the slice is built and merged, and the
run ends after that session's first turn: the coming-back to the set. With `--through
requirements` it ends as it did before the slice stage existed, after the session's first turn
that began with a requirements document in the planning folder. It also ends when the user would
say the same thing a third time running, or at --max-turns.

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

A question counts only if the message puts it to the person and waits for the answer, with or \
without a question mark ("I need the folder from you" asks for the folder): something \
the assistant states, proposes or says it will do is not a question, and neither is a topic it \
merely mentions. A key is listed once. Use only keys from the list. When unsure whether a topic \
covers a question, count the question as uncovered.

# The topics

"""
DOCUMENTS = ("problem", "scope-map", "requirements", "slices", "slice")
MERGED = 7   # the number of the made-up pull request


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
        # Asked whether to begin or go on, any user says yes unless their brief says otherwise.
        self.topics.setdefault("proceed", ("whether to go on, begin or continue with the next stage or step", "Yes, go on."))
        # Asked where to start, any user takes the slice recommended unless their brief says otherwise.
        self.topics.setdefault("start", ("where to start, which slice to begin with or build first", "Start with the one you recommend."))
        self.merged = section(text, "After the merge") or "That slice is built and merged. What's next?"
        self.not_known = section(text, "Not known") or "I don't know yet."
        self.go_on = section(text, "Nothing asked") or "Go on."
        self.shown = {name: says for name, says in rows(section(text, "When a document is first shown"))}
        # After which documents the user closes the session and comes back in a new one, and what they say then.
        self.away_after = {name for name in DOCUMENTS if name in section(text, "A new session after").lower()}
        self.back = section(text, "On coming back") or "Let's carry on where we left off."
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
                try:
                    (bin_folder / entry.name).symlink_to(entry)
                except OSError:   # a system that keeps links for administrators: a copy serves
                    shutil.copy2(entry, bin_folder / entry.name)
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


def tool_calls(record):
    """What a session did, from the tool's own record of it: each tool call as its name and the
    file, text or command it was given, shortened."""
    calls = []
    for line in record.splitlines():
        try:
            message = json.loads(line).get("message") or {}
        except ValueError:
            continue
        if message.get("role") != "assistant" or not isinstance(message.get("content"), list):
            continue
        for part in message["content"]:
            if part.get("type") == "tool_use":
                given = part.get("input") or {}
                what = given.get("file_path") or given.get("skill") or given.get("pattern") or given.get("command") or ""
                calls.append(f"{part.get('name')}: {str(what).splitlines()[0][:160] if what else ''}".rstrip())
    return calls


def record_of(session, home):
    """The tool's record of a session, wherever under its projects folder it was kept, or nothing."""
    found = sorted(pathlib.Path(home, ".claude", "projects").glob(f"*/{session}.jsonl")) if session else []
    return found[0].read_text(encoding="utf-8", errors="replace") if found else ""


def written_down(files, project, script):
    """Each place in the project where a value of one of the user's own files is written, as the
    plugin's scan reports it (where, never what); and whether every file could be scanned."""
    places, scanned = [], True
    for path in sorted(files.iterdir()) if files.is_dir() else []:
        done = subprocess.run(["sh", str(script), "scan", str(path), str(project)], capture_output=True, text=True)
        scanned = scanned and done.returncode in (0, 1)
        places += [line[2:] for line in done.stdout.splitlines() if " line " in line and ": a value of column " in line]
    return places, scanned


def present(planning):
    """Which of the documents exist in the planning folder, by name: the first three, the set of
    slices, and a slice's own document in its folder."""
    names = [path.name for path in planning.glob("*.md")] if planning.is_dir() else []
    found = {name for name in DOCUMENTS[:3] if any(name in file for file in names)}
    if any(re.match(r"\d+_slices", file) for file in names):
        found.add("slices")
    if planning.is_dir() and any(planning.glob("slice-*/*_slice.md")):
        found.add("slice")
    return found


def in_order(names):
    """Whether documents, by their file names, are numbered from 000 with no gap, in the order the
    stages write them."""
    stages = ["problem", "scope-map", "requirements", "slices", "slice"]
    numbered = sorted(name for name in names if re.match(r"\d{3}_", name))
    return (len(numbered) == len(names) and len(names) >= 3 and [int(name[:3]) for name in numbered] == list(range(len(names)))
            and all(re.match(rf"\d{{3}}_{stage}(?:-v\d+)?\.md$", name) for name, stage in zip(numbered, stages)))


def criteria(text):
    """The names of a slice's criteria, as its document writes them under "Criteria"."""
    names, inside = [], False
    for line in text.splitlines():
        if line.startswith("#"):
            inside = "criteri" in line.lower()
        elif inside:
            found = re.match(r"\s*[-*] (?:\[[ xX]\] )?\*\*([^*]+)\*\*", line)
            if found:
                names.append(re.sub(r"\s*/\s*", " / ", found.group(1).strip().rstrip(":")))
    return names


def merge(project, planning):
    """Make up the merge of the slice whose document was written last: the tracker's stand-in is
    given one merged pull request that names every criterion of that document. Returns what it names."""
    written = sorted(planning.glob("slice-*/*_slice.md"), key=lambda path: path.name)[-1]
    text = written.read_text(encoding="utf-8", errors="replace")
    number = int(re.sub(r"\D", "", written.parent.name) or 0)
    names = criteria(text)
    title = (text.splitlines() or ["A slice"])[0].lstrip("# ").strip() or "A slice"
    named = f"slice {number}: " + ", ".join(names) if names else "nothing: no criterion was found in the slice's document"
    lines = ["ok\t0\t0"] + ([f"merged\t{MERGED}\t{named}\t{title}"] if names else [])
    (project / ".cache" / "machine" / "gh" / "lines").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return named


def marks(planning):
    """What the latest set of slices says of each slice, and whether each box of the list is checked."""
    slices, boxes = {}, {}
    sets = sorted(planning.glob("[0-9][0-9][0-9]_slices*.md")) if planning.is_dir() else []
    for line in (sets[-1].read_text(encoding="utf-8", errors="replace").splitlines() if sets else []):
        cells = [cell.strip().strip("*`").strip() for cell in line.strip().strip("|").split("|")]
        if line.strip().startswith("|") and cells and cells[0].isdigit():
            slices[cells[0]] = cells[-1].lower()
    lists = sorted(planning.glob("[0-9][0-9][0-9]_requirements*.md")) if planning.is_dir() else []
    for line in (lists[-1].read_text(encoding="utf-8", errors="replace").splitlines() if lists else []):
        found = re.match(r"\s*[-*] \[([ xX])\] \*\*([^*]+)\*\*", line)
        if found:
            boxes[found.group(2)] = found.group(1) != " "
    return slices, boxes


def run(example, out, plugin, model, sorter_model, max_turns, command=("claude",), through="requirements"):
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
    turns, session, said, ended, seen, cost, same = [], None, brief.opening, "the turns ran out", set(), 0.0, 0
    sessions, merged, back = [], "", False
    for _ in range(max_turns):
        had_list = through == "requirements" and "requirements" in present(planning)
        reply, session, spent = ask(command, said, project, session_extra + (["--resume", session] if session else []), env)
        cost += spent
        if session not in sessions:
            sessions.append(session)
        turn = {"user": said, "session": reply}
        turns.append(turn)
        if had_list:
            ended = "the list was shown and the user's answers taken"
            break
        if back:
            ended = "the slice was merged and the session came back to the set"
            break
        appeared = present(planning) - seen
        seen |= appeared
        sorted_, _, spent = ask(command, reply, nowhere, sorter_extra, env)
        cost += spent
        turn["picked"] = picked_from(sorted_)
        turn["appeared"] = sorted(appeared)
        said = brief.reply(turn["picked"], appeared, limited="requirements" in appeared)
        if appeared & brief.away_after:   # the user comes back another day: nothing carries over but the files
            session, said, turn["new_session_next"] = None, brief.back, True
        if through == "merge" and "slice" in appeared:   # the slice is built and merged while the user is away
            merged, back = merge(project, planning), True
            session, said, turn["new_session_next"], turn["merged"] = None, brief.merged, True, merged
        same = same + 1 if said == turn["user"] else 0
        if same == 2:   # said twice running, and this would be the third time
            ended = "stuck: the user had only the same thing to say"
            break
    (out / "transcript.md").write_text("\n\n".join(
        f"**User:** {turn['user']}\n\n**Session:** {turn['session']}" for turn in turns) + "\n", encoding="utf-8")
    (out / "turns.json").write_text(json.dumps(turns, indent=2) + "\n", encoding="utf-8")
    calls = [call for one in sessions for call in tool_calls(record_of(one, os.environ.get("HOME", "")))]
    (out / "tools.txt").write_text("\n".join(calls) + "\n", encoding="utf-8")
    # The user's own files stay outside the project; no value of one may be written in it.
    places, scanned = written_down(example / "files", project, plugin / "startup" / "source.sh")
    documents = sorted(planning.rglob("*.md")) if planning.is_dir() else []
    summary = {"example": example.name, "model": model, "ended": ended, "session": session,
               "session_turns": len(turns),
               "sessions": 1 + sum(1 for turn in turns if turn.get("new_session_next")),
               "questions_put": sum(turn["session"].count("?") for turn in turns),
               "asked_and_not_covered": sum((turn.get("picked") or {}).get("uncovered") or 0 for turn in turns),
               "cost_usd": round(cost, 4),
               "tool_calls": len(calls),
               "values_of_the_users_files_written_down": places if scanned else "the scan could not run",
               "the_users_files_opened": [call for call in calls
                                          if any(path.name in call for path in (example / "files").glob("*"))]
               if (example / "files").is_dir() else [],
               # Each document under the number and name the stage script gives it, so the next session finds it.
               "numbered_in_order": in_order([path.name for path in documents if path.name != "sources.md"]),
               "merged": merged, "slices": marks(planning)[0], "boxes": marks(planning)[1],
               "documents": [path.relative_to(project).as_posix() for path in documents]}
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
    parser.add_argument("--through", choices=("merge", "requirements"), default="merge")
    given = parser.parse_args()
    print(json.dumps(run(given.example.resolve(), given.out.resolve(), given.plugin.resolve(), given.model,
                         given.sorter_model, given.max_turns, through=given.through), indent=2))
