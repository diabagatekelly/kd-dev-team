import json
import pathlib
import sys
import tempfile
import textwrap
import unittest

import run

BRIEF = """# A brief

## Opening
I want a thing.

## Planning folder
plans

## Answers
| Key | When the assistant asks about | The user says |
|---|---|---|
| today | how it is done today | On paper. |
| limits | a budget, a deadline | Ten a month. |
| who | who it is for | The club. |

## Not known
I don't know that yet.

## Nothing asked
Carry on.

## When a document is first shown
| Document | The user says |
|---|---|
| scope-map | Put the second one first. |

## Answers to the requirements' questions
At most 1.
"""
# A stand-in for the tool. As the session it writes the map on its second turn and the list on its
# third; as the sorter it answers with whatever the test put in sorter.json.
FAKE = textwrap.dedent('''
    import json, pathlib, sys
    args = sys.argv[1:]
    here = pathlib.Path(__file__).parent
    with (here / "calls.jsonl").open("a") as out: out.write(json.dumps(args) + "\\n")
    if "--system-prompt" in args:
        reply = (here / "sorter.json").read_text()
    else:
        count = pathlib.Path("count"); n = int(count.read_text()) + 1 if count.exists() else 1
        count.write_text(str(n))
        pathlib.Path("plans").mkdir(exist_ok=True)
        if n == 2: pathlib.Path("plans/001_scope-map.md").write_text("a map")
        if n == 3: pathlib.Path("plans/002_requirements.md").write_text("- [ ] **a**: b")
        reply = f"Turn {n}. Is that right?"
    print(json.dumps({"result": reply, "session_id": "s-1", "total_cost_usd": 0.01}))
''')


class TheBrief(unittest.TestCase):
    def setUp(self):
        self.brief = run.Brief(BRIEF)

    def test_a_section_of_the_brief_is_read_by_its_heading(self):
        self.assertEqual(run.section(BRIEF, "opening"), "I want a thing.")
        self.assertEqual(run.section(BRIEF, "not there"), "")

    def test_the_brief_is_read_whole(self):
        self.assertEqual(self.brief.folder, "plans")
        self.assertEqual(self.brief.topics["limits"], ("a budget, a deadline", "Ten a month."))
        self.assertEqual(self.brief.limit, 1)
        self.assertEqual(self.brief.topic_list().splitlines()[0], "- today: how it is done today")

    def test_the_answers_come_word_for_word_in_the_order_asked(self):
        self.assertEqual(self.brief.reply({"asked": ["who", "today"], "uncovered": 0}, set(), False),
                         "The club. On paper.")

    def test_a_topic_asked_twice_is_answered_once_and_an_unknown_key_is_dropped(self):
        self.assertEqual(self.brief.reply({"asked": ["who", "who", "made-up"], "uncovered": 0}, set(), False), "The club.")

    def test_what_no_topic_covers_gets_the_not_known_line_once(self):
        self.assertEqual(self.brief.reply({"asked": ["today"], "uncovered": 3}, set(), False),
                         "On paper. I don't know that yet.")
        self.assertEqual(self.brief.reply({"asked": [], "uncovered": 2}, set(), False), "I don't know that yet.")

    def test_nothing_asked_gets_the_line_for_going_on(self):
        self.assertEqual(self.brief.reply({"asked": [], "uncovered": 0, "asks": False}, set(), False), "Carry on.")

    def test_a_document_first_shown_gets_its_own_line_whatever_was_asked(self):
        self.assertEqual(self.brief.reply({"asked": ["who"], "uncovered": 1}, {"scope-map"}, False),
                         "Put the second one first.")
        self.assertEqual(self.brief.reply({"asked": ["who"], "uncovered": 0}, {"problem"}, False), "The club.")

    def test_the_requirements_questions_are_answered_only_as_far_as_the_brief_allows(self):
        self.assertEqual(self.brief.reply({"asked": ["who", "today", "limits"], "uncovered": 2}, {"requirements"}, True),
                         "The club.")
        self.assertEqual(self.brief.reply({"asked": ["who"], "uncovered": 2}, {"requirements"}, True),
                         "The club. I don't know that yet.")

    def test_asked_whether_to_go_on_the_user_says_yes_unless_the_brief_says_otherwise(self):
        # Found by an end-to-end run: "Say the word and I'll start" was met with "I don't know." five times.
        self.assertEqual(self.brief.reply({"asked": ["proceed"], "uncovered": 0}, set(), False), "Yes, go on.")
        other = run.Brief(BRIEF.replace("| who | who it is for | The club. |", "| proceed | whether to go on | Not yet. |"))
        self.assertEqual(other.reply({"asked": ["proceed"], "uncovered": 0}, set(), False), "Not yet.")

    def test_a_brief_without_the_optional_parts_has_plain_defaults(self):
        brief = run.Brief("## Opening\nHello.\n")
        self.assertEqual((brief.folder, brief.not_known, brief.go_on, brief.limit), ("planning", "I don't know yet.", "Go on.", None))

    def test_what_the_sorter_said_is_read_or_counted_as_one_thing_uncovered(self):
        self.assertEqual(run.picked_from('Here: {"asked": ["who"], "uncovered": 0, "asks": true}')["asked"], ["who"])
        self.assertEqual(run.picked_from("no idea"), {"asked": [], "uncovered": 1, "asks": True, "unread": True})
        self.assertTrue(run.picked_from('{"asked": "who"}')["unread"])


class TheExamples(unittest.TestCase):
    def test_every_example_has_a_brief_the_script_can_speak_from(self):
        examples = sorted((pathlib.Path(run.__file__).parent / "examples").glob("*/brief.md"))
        self.assertGreaterEqual(len(examples), 4)
        for path in examples:
            text = path.read_text(encoding="utf-8")
            brief = run.Brief(text)
            with self.subTest(path.parent.name):
                self.assertTrue(brief.opening)
                self.assertTrue({"folder", "confirm"} <= set(brief.topics))
                self.assertTrue(all(len(row) == 3 and all(row) for row in run.rows(run.section(text, "Answers"))))
                self.assertTrue(set(brief.shown) <= set(run.DOCUMENTS))


class WhatASessionDid(unittest.TestCase):
    RECORD = "\n".join(json.dumps(line) for line in [
        {"message": {"role": "user", "content": "hello"}},
        {"message": {"role": "assistant", "content": [
            {"type": "text", "text": "Reading."},
            {"type": "tool_use", "name": "Read", "input": {"file_path": "/p/register.py"}},
            {"type": "tool_use", "name": "Bash", "input": {"command": "cat > a.md <<'EOF'\nmany lines\nEOF"}}]}},
        {"message": {"role": "assistant", "content": [{"type": "tool_use", "name": "Skill", "input": {"skill": "x:problem"}}]}},
    ]) + "\nnot json\n"

    def test_each_tool_call_is_listed_with_what_it_was_given(self):
        self.assertEqual(run.tool_calls(self.RECORD), ["Read: /p/register.py", "Bash: cat > a.md <<'EOF'", "Skill: x:problem"])

    def test_a_line_of_the_record_whose_message_is_plain_text_is_passed_over(self):
        # Found by the slice stage's pilot: one transcript held such a line and grading it again stopped there.
        self.assertEqual(run.tool_calls(json.dumps({"type": "system", "message": "compacted"}) + "\n"), [])

    def test_no_record_lists_nothing(self):
        self.assertEqual(run.tool_calls(""), [])
        self.assertEqual(run.record_of("s-1", tempfile.mkdtemp()), "")
        self.assertEqual(run.record_of(None, tempfile.mkdtemp()), "")

    def test_a_record_is_found_under_the_projects_folder(self):
        home = pathlib.Path(tempfile.mkdtemp())
        (home / ".claude" / "projects" / "-tmp-x").mkdir(parents=True)
        (home / ".claude" / "projects" / "-tmp-x" / "s-1.jsonl").write_text(self.RECORD)
        self.assertEqual(run.record_of("s-1", home), self.RECORD)


class TheUsersOwnFiles(unittest.TestCase):
    SCRIPT = pathlib.Path(run.__file__).parent.parent / "startup" / "source.sh"

    def setUp(self):
        self.folder = pathlib.Path(tempfile.mkdtemp())
        (self.folder / "files").mkdir()
        (self.folder / "files" / "prices.csv").write_text("Client,Price\nOkafor,14.50\n")
        (self.folder / "project" / "planning").mkdir(parents=True)

    def test_a_value_written_in_the_project_is_reported_by_its_place(self):
        (self.folder / "project" / "planning" / "002_requirements.md").write_text("- Mrs Okafor pays.\n")
        places, scanned = run.written_down(self.folder / "files", self.folder / "project", self.SCRIPT)
        self.assertTrue(scanned)
        self.assertEqual(places, ['planning/002_requirements.md line 1: a value of column "Client"'])

    def test_nothing_written_and_no_files_at_all_report_nothing(self):
        self.assertEqual(run.written_down(self.folder / "files", self.folder / "project", self.SCRIPT), ([], True))
        self.assertEqual(run.written_down(self.folder / "none", self.folder / "project", self.SCRIPT), ([], True))

    def test_a_scan_that_cannot_run_is_not_a_clean_result(self):
        (self.folder / "files" / "book.xlsx").write_bytes(b"PK")
        self.assertFalse(run.written_down(self.folder / "files", self.folder / "project", self.SCRIPT)[1])


class Run(unittest.TestCase):
    def setUp(self):
        self.folder = pathlib.Path(tempfile.mkdtemp())
        self.example = self.folder / "example"
        (self.example / "project").mkdir(parents=True)
        (self.example / "project" / "README.md").write_text("An app.\n")
        (self.example / "brief.md").write_text(BRIEF)

    def go(self, sorter='{"asked": ["today"], "uncovered": 0, "asks": true}', turns=10):
        fake = self.folder / "fake.py"
        fake.write_text(FAKE)
        (self.folder / "sorter.json").write_text(sorter)
        summary = run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", turns,
                          command=(sys.executable, str(fake)))
        calls = [json.loads(line) for line in (self.folder / "calls.jsonl").read_text().splitlines()]
        return summary, calls

    def test_it_ends_after_the_turn_that_took_the_answers_to_the_list(self):
        summary, _ = self.go()
        self.assertEqual(summary["ended"], "the list was shown and the user's answers taken")
        self.assertEqual(summary["session_turns"], 4)
        self.assertEqual(summary["documents"], ["plans/001_scope-map.md", "plans/002_requirements.md"])
        self.assertFalse(summary["numbered_in_order"])
        self.assertEqual(summary["questions_put"], 4)
        self.assertAlmostEqual(summary["cost_usd"], 0.07)

    def test_the_user_says_only_what_the_brief_holds(self):
        _, calls = self.go()
        said = [call[call.index("-p") + 1] for call in calls if "--system-prompt" not in call]
        self.assertEqual(said, ["I want a thing.", "On paper.", "Put the second one first.", "On paper."])

    def test_the_session_is_resumed_and_the_sorter_sees_the_topics_and_no_tools(self):
        _, calls = self.go()
        sessions = [call for call in calls if "--system-prompt" not in call]
        self.assertNotIn("--resume", sessions[0])
        self.assertEqual(sessions[1][sessions[1].index("--resume") + 1], "s-1")
        sorter = [call for call in calls if "--system-prompt" in call][0]
        self.assertIn("- limits: a budget, a deadline", sorter[sorter.index("--system-prompt") + 1])
        self.assertNotIn("Ten a month.", sorter[sorter.index("--system-prompt") + 1])
        self.assertEqual(sorter[sorter.index("--tools") + 1], "")
        self.assertEqual(sorter[sorter.index("-p") + 1], "Turn 1. Is that right?")

    def test_what_was_picked_is_kept_beside_each_turn(self):
        summary, _ = self.go(sorter='{"asked": [], "uncovered": 2, "asks": true}')
        turns = json.loads((self.folder / "out" / "turns.json").read_text())
        self.assertEqual(turns[0]["picked"]["uncovered"], 2)
        self.assertEqual(turns[1]["appeared"], ["scope-map"])
        self.assertEqual(turns[1]["user"], "I don't know that yet.")
        self.assertEqual(summary["asked_and_not_covered"], 6)

    def test_an_absent_tool_is_off_the_path_and_its_neighbours_stay(self):
        tools, other = self.folder / "tools", self.folder / "other"
        for folder, names in ((tools, ("sbx", "gh", "claude")), (other, ("ls",))):
            folder.mkdir()
            for name in names:
                (folder / name).write_text("#!/bin/sh\n")
        path = run.path_without(["sbx"], f"{tools}{run.os.pathsep}{other}", self.folder / "bin").split(run.os.pathsep)
        self.assertEqual(path, [str(self.folder / "bin"), str(other)])
        self.assertEqual(sorted(entry.name for entry in (self.folder / "bin").iterdir()), ["claude", "gh"])

    def test_it_ends_when_the_user_has_only_the_same_thing_to_say(self):
        (self.example / "brief.md").write_text(BRIEF.replace("| scope-map | Put the second one first. |", "")
                                               .replace("At most 1.", ""))
        fake = self.folder / "fake.py"
        fake.write_text(FAKE.replace("if n == 3:", "if n == 99:"))
        (self.folder / "sorter.json").write_text('{"asked": ["today"], "uncovered": 0, "asks": true}')
        summary = run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 20,
                          command=(sys.executable, str(fake)))
        self.assertEqual(summary["ended"], "stuck: the user had only the same thing to say")
        self.assertEqual(summary["session_turns"], 3)   # said twice, and about to be said a third time

    def test_a_request_with_no_question_mark_still_reaches_the_sorter(self):
        # Found by an end-to-end run: "give me the path" was taken for nothing asked, and the user said "Go on."
        fake = self.folder / "fake.py"
        fake.write_text(FAKE.replace('reply = f"Turn {n}. Is that right?"', 'reply = f"Turn {n}. Give me the path."'))
        (self.folder / "sorter.json").write_text('{"asked": ["today"], "uncovered": 0, "asks": true}')
        run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 2, command=(sys.executable, str(fake)))
        calls = [json.loads(line) for line in (self.folder / "calls.jsonl").read_text().splitlines()]
        self.assertEqual(len([call for call in calls if "--system-prompt" in call]), 2)
        self.assertEqual(json.loads((self.folder / "out" / "turns.json").read_text())[0]["picked"]["asked"], ["today"])

    def test_the_user_comes_back_in_a_new_session_where_the_brief_says_so(self):
        (self.example / "brief.md").write_text(BRIEF + "\n## A new session after\nscope-map\n\n## On coming back\nI'm back.\n")
        summary, calls = self.go()
        sessions = [call for call in calls if "--system-prompt" not in call]
        said = [call[call.index("-p") + 1] for call in sessions]
        self.assertEqual(said[2], "I'm back.")           # after the turn that wrote the map
        self.assertNotIn("--resume", sessions[2])        # a new session, not the old one resumed
        self.assertIn("--resume", sessions[1])
        self.assertIn("--resume", sessions[3])
        self.assertEqual(summary["sessions"], 2)

    def test_a_brief_that_says_nothing_of_it_stays_in_one_session(self):
        summary, _ = self.go()
        self.assertEqual(summary["sessions"], 1)
        self.assertEqual(run.Brief(BRIEF).away_after, set())

    def test_the_list_of_the_users_files_is_no_break_in_the_numbering(self):
        fake = self.folder / "fake.py"
        fake.write_text(FAKE.replace('if n == 2: pathlib.Path("plans/001_scope-map.md").write_text("a map")',
                                     'if n == 2: pathlib.Path("plans/001_scope-map.md").write_text("a map"); '
                                     'pathlib.Path("plans/000_problem.md").write_text("p"); pathlib.Path("plans/sources.md").write_text("s")'))
        (self.folder / "sorter.json").write_text('{"asked": ["today"], "uncovered": 0, "asks": true}')
        summary = run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 10,
                          command=(sys.executable, str(fake)))
        self.assertTrue(summary["numbered_in_order"])

    # Carried on through the slice stage: a set, a chosen slice, one merge and the coming-back.
    THROUGH = FAKE.replace(
        'if n == 3: pathlib.Path("plans/002_requirements.md").write_text("- [ ] **a**: b")',
        'if n == 3: pathlib.Path("plans/002_requirements.md").write_text("- [ ] **a**: b")\n'
        '    if n == 4: pathlib.Path("plans/003_slices.md").write_text("| # | Slice | Items | Builds on | State |\\n|---|---|---|---|---|\\n| 2 | Do b | a | nothing | open |\\n")\n'
        '    if n == 5:\n'
        '        pathlib.Path("plans/slice-002").mkdir(exist_ok=True)\n'
        '        pathlib.Path("plans/slice-002/004_slice.md").write_text("# Slice 2: Do b\\n\\n## Criteria\\n- **a / 1**: Given x, when y, then z.\\n- **a/2**: Given p, when q, then r.\\n\\n## Left for later\\n- **not one**: later.\\n")\n'
        '    if n == 6:\n'
        '        pathlib.Path("plans/003_slices.md").write_text("| # | Slice | Items | Builds on | State |\\n|---|---|---|---|---|\\n| 2 | Do b | a | nothing | built |\\n")\n'
        '        pathlib.Path("plans/002_requirements.md").write_text("- [x] **a**: b")')

    def through(self, fake=None, brief=BRIEF, turns=20, through="merge", out="out"):
        # A second run in one test takes a folder of its own: on Windows a run's repository cannot be swept away.
        (self.example / "brief.md").write_text(brief)
        script = self.folder / "fake.py"
        script.write_text(fake or self.THROUGH)
        (self.folder / "sorter.json").write_text('{"asked": ["today"], "uncovered": 0, "asks": true}')
        summary = run.run(self.example, self.folder / out, self.folder / "plugin", "m", "s", turns,
                          command=(sys.executable, str(script)), through=through)
        calls = [json.loads(line) for line in (self.folder / "calls.jsonl").read_text().splitlines()]
        return summary, [call for call in calls if "--system-prompt" not in call]

    def test_carried_through_a_merge_it_ends_after_the_session_has_come_back_to_the_set(self):
        summary, sessions = self.through()
        self.assertEqual(summary["ended"], "the slice was merged and the session came back to the set")
        self.assertEqual(summary["session_turns"], 6)
        self.assertEqual(summary["documents"], ["plans/001_scope-map.md", "plans/002_requirements.md", "plans/003_slices.md",
                                                "plans/slice-002/004_slice.md"])

    def test_it_can_end_once_the_chosen_slice_is_written(self):
        summary, _ = self.through(through="slice")
        self.assertEqual((summary["ended"], summary["session_turns"], summary["merged"]), ("the chosen slice was written", 5, ""))

    def test_once_a_slice_is_written_its_merge_is_made_up_from_its_own_criteria(self):
        summary, _ = self.through()
        lines = (self.folder / "out" / "project" / ".cache" / "machine" / "gh" / "lines").read_text().splitlines()
        self.assertEqual(lines, ["ok\t0\t0", "merged\t7\tslice 2: a / 1, a / 2\tSlice 2: Do b"])
        self.assertEqual(summary["merged"], "slice 2: a / 1, a / 2")

    def test_after_the_merge_the_user_comes_back_in_a_new_session_and_says_so(self):
        _, sessions = self.through()
        said = [call[call.index("-p") + 1] for call in sessions]
        self.assertEqual(said[5], "That slice is built and merged. What's next?")
        self.assertNotIn("--resume", sessions[5])
        self.assertIn("--resume", sessions[4])
        _, sessions = self.through(brief=BRIEF + "\n## After the merge\nIt's in. Now what?\n", out="again")
        self.assertEqual(sessions[-1][sessions[-1].index("-p") + 1], "It's in. Now what?")

    def test_what_the_set_and_the_list_say_at_the_end_is_kept(self):
        summary, _ = self.through()
        self.assertEqual(summary["slices"], {"2": "built"})
        self.assertEqual(summary["boxes"], {"a": True})
        early, _ = self.through(turns=5, out="early")
        self.assertEqual((early["ended"], early["slices"], early["boxes"]), ("the turns ran out", {"2": "open"}, {"a": False}))

    def test_a_session_that_never_marks_the_merged_slice_is_given_four_turns(self):
        # Found by the pilot: asked what is next after a merge, a session names the coming-back and waits for the word.
        summary, sessions = self.through(fake=self.THROUGH.replace("if n == 6:", "if n == 7:"))
        self.assertEqual((summary["ended"], summary["session_turns"]), ("the slice was merged and the session came back to the set", 7))

    def test_asked_where_to_start_the_user_takes_the_recommended_slice_unless_the_brief_says_otherwise(self):
        self.assertEqual(run.Brief(BRIEF).reply({"asked": ["start"], "uncovered": 0}, set(), False),
                         "Start with the one you recommend.")
        other = run.Brief(BRIEF.replace("| who | who it is for | The club. |", "| start | where to start | The last one. |"))
        self.assertEqual(other.reply({"asked": ["start"], "uncovered": 0}, set(), False), "The last one.")

    def test_documents_numbered_on_through_the_slice_are_in_order(self):
        self.assertTrue(run.in_order(["000_problem.md", "001_scope-map.md", "002_requirements.md", "003_slices.md", "004_slice.md"]))
        self.assertTrue(run.in_order(["000_problem.md", "001_scope-map.md", "002_requirements.md"]))
        self.assertFalse(run.in_order(["000_problem.md", "001_scope-map.md", "002_requirements.md", "004_slices.md"]))
        self.assertFalse(run.in_order(["000_problem.md", "001_scope-map.md", "002_requirements.md", "slices.md"]))
        self.assertFalse(run.in_order(["001_scope-map.md", "002_requirements.md"]))

    def test_a_slice_with_no_criterion_it_can_read_is_merged_as_naming_nothing(self):
        fake = self.THROUGH.replace("- **a / 1**: Given x, when y, then z.\\n- **a/2**: Given p, when q, then r.", "1. Given x, when y, then z.")
        summary, _ = self.through(fake=fake)
        self.assertEqual(summary["merged"], "nothing: no criterion was found in the slice's document")

    # An example is started from its documents as its last good run left them (decision 38).
    def kept(self):
        plugin = self.folder / "plugin"
        (plugin / "skills" / "problem").mkdir(parents=True, exist_ok=True)
        (plugin / "skills" / "problem" / "SKILL.md").write_text("the problem text")
        (plugin / "hooks").mkdir(exist_ok=True)
        (plugin / "hooks" / "routing-table.md").write_text("the table")
        planning = self.folder / "done" / "project" / "plans"
        (planning / "slice-002").mkdir(parents=True)
        for name in ("000_problem.md", "001_scope-map.md", "002_requirements.md", "sources.md", "003_slices.md", "slice-002/004_slice.md"):
            (planning / name).write_text("kept " + name)
        return run.keep(self.folder / "done", self.example, "requirements", plugin)

    def test_the_documents_of_a_good_run_are_kept_up_to_a_stage(self):
        kept = self.kept()
        self.assertEqual(kept, self.example / "after" / "requirements")
        self.assertEqual(sorted(path.name for path in kept.iterdir()),
                         ["000_problem.md", "001_scope-map.md", "002_requirements.md", "made-with.json", "sources.md"])

    def test_a_run_started_from_kept_documents_begins_with_them_and_the_users_coming_back(self):
        self.kept()
        script = self.folder / "fake.py"
        script.write_text(self.THROUGH)
        (self.folder / "sorter.json").write_text('{"asked": ["today"], "uncovered": 0, "asks": true}')
        summary = run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 1,
                          command=(sys.executable, str(script)), through="merge", start="requirements")
        self.assertEqual((self.folder / "out" / "project" / "plans" / "002_requirements.md").read_text(), "kept 002_requirements.md")
        self.assertFalse((self.folder / "out" / "project" / "plans" / "made-with.json").exists())
        calls = [json.loads(line) for line in (self.folder / "calls.jsonl").read_text().splitlines()]
        self.assertEqual(calls[0][calls[0].index("-p") + 1], "Let's carry on where we left off.")
        self.assertEqual(summary["started_from"], "requirements")

    def test_kept_documents_are_refused_once_a_text_they_were_made_with_has_changed(self):
        self.kept()
        (self.folder / "plugin" / "skills" / "problem" / "SKILL.md").write_text("the problem text, changed")
        with self.assertRaises(SystemExit) as refused:
            run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 1, command=("true",), start="requirements")
        self.assertIn("problem", str(refused.exception))

    def test_a_text_added_since_does_not_stale_what_was_kept(self):
        self.kept()
        (self.folder / "plugin" / "skills" / "slice").mkdir()
        (self.folder / "plugin" / "skills" / "slice" / "SKILL.md").write_text("a later stage")
        self.assertEqual(run.stale(self.example / "after" / "requirements", self.folder / "plugin"), [])

    def test_starting_from_documents_that_were_never_kept_is_refused(self):
        with self.assertRaises(SystemExit):
            run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "s", 1, command=("true",), start="requirements")

    def test_it_ends_when_the_turns_run_out(self):
        summary, _ = self.go(turns=1)
        self.assertEqual(summary["ended"], "the turns ran out")

    def test_the_transcript_and_the_project_are_kept(self):
        self.go()
        out = self.folder / "out"
        self.assertIn("**User:** I want a thing.", (out / "transcript.md").read_text())
        self.assertTrue((out / "project" / "README.md").exists())


if __name__ == "__main__":
    unittest.main()
