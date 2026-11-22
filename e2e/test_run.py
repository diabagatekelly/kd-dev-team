import json
import pathlib
import sys
import tempfile
import textwrap
import unittest

import run

BRIEF = "# A brief\n\n## Opening\nI want a thing.\n\n## What you know\n- It is for the club.\n\n## Planning folder\nplans\n"
# A stand-in for the tool: as the session it writes the list on its second turn; as the user it
# says "Yes." once and then DONE if asked again.
FAKE = textwrap.dedent('''
    import json, pathlib, sys
    args = sys.argv[1:]
    prompt = args[args.index("-p") + 1]
    log = pathlib.Path(__file__).with_name("calls.jsonl")
    with log.open("a") as out: out.write(json.dumps(args) + "\\n")
    if "--system-prompt" in args:
        reply = "DONE" if prompt.count("YOU:") >= @LIMIT@ else "Yes."
    else:
        count = pathlib.Path("count"); n = int(count.read_text()) + 1 if count.exists() else 1
        count.write_text(str(n))
        if n == 2:
            pathlib.Path("plans").mkdir(exist_ok=True); pathlib.Path("plans/002_requirements.md").write_text("- [ ] **a**: b")
        reply = f"Turn {n}. Is that right?"
    print(json.dumps({"result": reply, "session_id": "s-1", "total_cost_usd": 0.01}))
''')


class Run(unittest.TestCase):
    def setUp(self):
        self.folder = pathlib.Path(tempfile.mkdtemp())
        self.example = self.folder / "example"
        (self.example / "project").mkdir(parents=True)
        (self.example / "project" / "README.md").write_text("An app.\n")
        (self.example / "brief.md").write_text(BRIEF)

    def go(self, limit=99, turns=10):
        fake = self.folder / "fake.py"
        fake.write_text(FAKE.replace("@LIMIT@", str(limit)))
        summary = run.run(self.example, self.folder / "out", self.folder / "plugin", "m", "u", turns,
                          command=(sys.executable, str(fake)))
        calls = [json.loads(line) for line in (self.folder / "calls.jsonl").read_text().splitlines()]
        return summary, calls

    def test_a_section_of_the_brief_is_read_by_its_heading(self):
        self.assertEqual(run.section(BRIEF, "opening"), "I want a thing.")
        self.assertEqual(run.section(BRIEF, "not there"), "")

    def test_it_ends_after_the_turn_that_took_the_answers_to_the_list(self):
        summary, calls = self.go()
        self.assertEqual(summary["ended"], "the list was shown and the user's answers taken")
        self.assertEqual(summary["session_turns"], 3)
        self.assertEqual(summary["documents"], ["plans/002_requirements.md"])
        self.assertEqual(summary["questions_put"], 3)
        self.assertAlmostEqual(summary["cost_usd"], 0.05)

    def test_the_session_opens_with_the_brief_and_is_resumed_after(self):
        _, calls = self.go()
        sessions = [call for call in calls if "--system-prompt" not in call]
        self.assertEqual(sessions[0][sessions[0].index("-p") + 1], "I want a thing.")
        self.assertNotIn("--resume", sessions[0])
        self.assertEqual(sessions[1][sessions[1].index("--resume") + 1], "s-1")
        self.assertEqual(sessions[1][sessions[1].index("-p") + 1], "Yes.")

    def test_the_user_has_the_brief_no_tools_and_the_conversation_so_far(self):
        _, calls = self.go()
        user = [call for call in calls if "--system-prompt" in call][0]
        self.assertIn("It is for the club.", user[user.index("--system-prompt") + 1])
        self.assertEqual(user[user.index("--tools") + 1], "")
        self.assertIn("THE ASSISTANT: Turn 1. Is that right?", user[user.index("-p") + 1])

    def test_it_ends_when_the_user_has_nothing_more_to_say(self):
        summary, _ = self.go(limit=1)
        self.assertEqual(summary["ended"], "the user had nothing more to say")
        self.assertEqual(summary["session_turns"], 1)

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
