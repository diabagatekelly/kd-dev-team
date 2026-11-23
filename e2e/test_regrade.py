import json
import pathlib
import tempfile
import unittest

import regrade


def record(*parts):
    return json.dumps({"message": {"role": "assistant", "content": list(parts)}})


def use(name, **given):
    return {"type": "tool_use", "name": name, "input": given}


RUN = "\n".join([
    json.dumps({"message": {"role": "user", "content": "Go on."}}),
    record({"type": "text", "text": "Reading."}, use("Read", file_path="/tmp/x/planning/000_problem.md")),
    record(use("Write", file_path="/tmp/x/planning/002_requirements.md", content="- [ ] **a-b**: One.\n")),
    record(use("Edit", file_path="/tmp/x/planning/001_scope-map.md", old_string="now", new_string="next")),
    record({"type": "text", "text": "Written. Anything missing?"}),
    "not json",
    json.dumps({"type": "system", "message": "a line whose message is plain text"}),   # found by the slice stage's pilot
])
START = {"planning/001_scope-map.md": "| 1 | Borrow | now |\n| 2 | Return | now |\n"}


class Regrade(unittest.TestCase):
    def setUp(self):
        self.last, self.files, self.calls = regrade.replay(RUN, START)

    def check(self, **check):
        return regrade.passes(check, self.last, self.files, self.calls, RUN)

    def test_a_run_is_replayed_to_its_last_words_its_files_and_its_calls(self):
        self.assertEqual(self.last, "Written. Anything missing?")
        self.assertEqual(self.files["/tmp/x/planning/002_requirements.md"], "- [ ] **a-b**: One.\n")
        self.assertEqual(self.files["planning/001_scope-map.md"], "| 1 | Borrow | next |\n| 2 | Return | now |\n")
        self.assertEqual([name for name, _ in self.calls], ["Read", "Write", "Edit"])

    def test_a_file_exists_when_the_run_or_the_scenario_left_it(self):
        self.assertTrue(self.check(type="file_exists", path="planning/002_requirements.md"))
        self.assertTrue(self.check(type="file_exists", path="planning/001_scope-map.md"))
        self.assertFalse(self.check(type="file_exists", path="planning/003_research.md"))

    def test_a_pattern_is_held_to_the_last_message_a_file_or_the_transcript(self):
        self.assertTrue(self.check(type="regex", target="last_message", pattern=r"\?"))
        self.assertFalse(self.check(type="regex", target="last_message", pattern="Reading"))
        self.assertTrue(self.check(type="regex", target="trace", pattern="Reading"))
        on_file = {"source": "file", "path": "planning/002_requirements.md"}
        self.assertTrue(self.check(type="regex", target=on_file, pattern=r"\*\*a-b\*\*"))
        self.assertFalse(self.check(type="regex", target=on_file, pattern="ONE"))
        self.assertTrue(self.check(type="regex", target=on_file, pattern="ONE", flags="i"))
        self.assertTrue(self.check(type="regex", target=on_file, pattern="two", match="not_contains"))

    def test_a_check_on_a_file_never_written_fails_even_when_it_looks_for_an_absence(self):
        missing = {"source": "file", "path": "planning/009_nothing.md"}
        self.assertFalse(self.check(type="regex", target=missing, pattern="x", match="not_contains"))

    def test_a_tool_is_counted_with_or_without_what_it_was_given(self):
        self.assertTrue(self.check(type="tool_used", tool="Write", min=1))
        self.assertFalse(self.check(type="tool_used", tool="Write", min=0, max=0))
        self.assertTrue(self.check(type="tool_used", tool="Write", min=0, max=0, input_match="research"))
        self.assertFalse(self.check(type="tool_used", tool="Skill", min=1))

    def test_a_kind_of_check_it_does_not_know_is_neither_passed_nor_failed(self):
        self.assertIsNone(self.check(type="llm_judge"))

    def test_kept_runs_are_graded_by_the_checks_in_the_built_scenario(self):
        folder = pathlib.Path(tempfile.mkdtemp())
        case = folder / "plugin" / "evals" / "01-a"
        (case / "project" / "planning").mkdir(parents=True)
        (case / "project" / "planning" / "001_scope-map.md").write_text(START["planning/001_scope-map.md"])
        checks = [{"type": "regex", "name": "asks", "target": "last_message", "pattern": r"\?"},
                  {"type": "tool_used", "name": "uses-the-text", "tool": "Skill", "min": 1}]
        (case / "case.yaml").write_text("name: stage-01-a\ngraders:\n" + "".join(f"  - {json.dumps(c)}\n" for c in checks))
        (folder / "traces").mkdir()
        for number in (0, 1, 10):
            (folder / "traces" / f"pass-stage-01-a-{number}.jsonl").write_text(RUN)
        (folder / "traces" / "other-stage-01-a-0.jsonl").write_text(RUN)
        self.assertEqual(regrade.regrade(folder / "plugin", folder / "traces", "pass"),
                         {"stage-01-a": [["uses-the-text"]] * 3})


if __name__ == "__main__":
    unittest.main()
