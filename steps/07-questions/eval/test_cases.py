"""The questions cases: every arm builds, each report says what its case expects, the kept file a
case starts from is one the script draws from, and the checks pass a good file and fail a bad one."""
import contextlib
import io
import json
import os
import pathlib
import re
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_cases as cases  # noqa: E402


def checks(case, kind="regex"):
    return {check["name"]: check for check in (json.loads(line[4:]) for line in (case / "case.yaml").read_text().splitlines()
                                                 if line.startswith("  - {")) if check["type"] == kind}


def passes(check, text):
    found = re.search(check["pattern"], text, re.I) is not None
    return found != (check.get("match") == "not_contains")


@unittest.skipIf(os.name == "nt", "the cases are built and run inside the VM, which is Linux")
class Fixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            cases.main("text")
        cls.built = out.getvalue().splitlines()

    def case(self, start):
        return next((HERE / "plugin-text" / "evals").glob(start + "*"))

    def report(self, start):
        return (self.case(start) / "report.txt").read_text(encoding="utf-8")

    def test_every_arm_builds_its_cases(self):
        self.assertEqual(len(self.built), 10)
        arms = ["bare"] + (["kad"] if all(any(path.exists() for path in places) for places in cases.KAD.values()) else [])
        for arm in arms:
            with self.subTest(arm), contextlib.redirect_stdout(io.StringIO()) as out:
                cases.main(arm)
            self.assertEqual(len(out.getvalue().splitlines()), 2 if arm == "kad" else 10)

    def test_only_the_text_arm_carries_the_stage_text_and_the_bare_arm_is_told_to_do_the_stage(self):
        with contextlib.redirect_stdout(io.StringIO()):
            cases.main("bare")
        self.assertTrue((HERE / "plugin-text/skills/questions/SKILL.md").exists())
        self.assertFalse((HERE / "plugin-bare/skills/questions").exists())
        self.assertIn("The questions stage has no text of its own here", (HERE / "plugin-bare/hooks/routing-table.md").read_text())
        self.assertIn("uses-the-stage-text", (self.case("01") / "case.yaml").read_text())

    def test_every_plugin_holds_the_script_and_the_library_the_report_names(self):
        for name in ("questions/questions.py", "library/library.json", "startup/stage.sh"):
            self.assertTrue((HERE / "plugin-text" / name).exists(), name)

    def test_the_report_names_the_folder_the_commands_and_what_is_owed(self):
        report = self.report("01")
        self.assertIn("questions (its document: planning/slice-001/007_questions/, to write there: kept.md", report)
        self.assertIn('@STARTUP@/../questions/questions.py" things planning/slice-001', report)
        self.assertIn('@STARTUP@/../questions/questions.py" draw planning/slice-001', report)
        self.assertNotIn(str(cases.ROOT), report)

    def test_a_slice_with_no_approach_and_no_research_has_its_questions_next_to_the_slice(self):
        self.assertIn("questions (its document: planning/slice-001/005_questions/", self.report("03"))
        self.assertIn("mkdir -p planning/slice-001/005_questions/", (self.case("03") / "scaffold.sh").read_text())

    def test_the_two_cases_of_a_change_start_from_questions_drawn_and_now_stale(self):
        for start in ("08a", "08b"):
            with self.subTest(start):
                self.assertIn("to draw again", self.report(start))
                folder = self.case(start) / "project/planning/slice-001"
                self.assertIn("<!-- drawn from: ", (folder / "007_questions/questions.md").read_text())
                self.assertTrue(cases.questions.state(folder).startswith("stale"))
        self.assertIn("- no longer stands, its thing is not committed to in slice-001/008_approach.md: planning/slice-001/006_research/payright.md",
                      self.report("08b"))

    def test_the_kept_file_those_cases_start_from_accounts_for_the_whole_library(self):
        read, entries, kept = cases.questions.load(self.case("01") / "project/planning/slice-001")
        kept = {**cases.questions.read_kept(cases.kept_file()), "text": b""}
        found, judged = cases.questions.problems(kept, cases.questions.known(read), entries, cases.questions.criteria(read["slice"]) + list(read["research"]))
        self.assertEqual(found, [])
        self.assertEqual(len(judged), 290)

    def test_the_case_of_a_thing_with_no_states_has_none_for_it_and_the_first_case_has(self):
        self.assertNotIn("## A season ticket", (self.case("04") / "project/planning/slice-001/006_research/states.md").read_text())
        self.assertIn("## A season ticket", (self.case("01") / "project/planning/slice-001/006_research/states.md").read_text())

    def test_the_second_turn_of_skipping_carries_the_first(self):
        self.assertTrue((self.case("07b") / "history.jsonl").exists())
        self.assertFalse((self.case("07a") / "history.jsonl").exists())

    def test_a_good_kept_file_passes_the_first_cases_checks_on_it(self):
        for name, check in checks(self.case("01")).items():
            if isinstance(check["target"], dict) and check["target"]["path"].endswith("kept.md"):
                with self.subTest(name):
                    self.assertTrue(passes(check, cases.kept_file()))

    def test_a_question_dropped_with_its_whole_kind_or_by_name_is_not_kept(self):
        check = checks(self.case("01"))["keeps-call-external-01-for-the-right-thing"]
        self.assertFalse(passes(check, "| call-external: all | dropped | nothing is called |\n"))
        self.assertFalse(passes(check, "| call-external-01, call-external-02 | dropped | no |\n"))
        self.assertFalse(passes(check, "| call-external-01 | `seat-band` | no |\n"))
        self.assertTrue(passes(check, "| call-external: all | PayRight | every one arises |\n"))
        self.assertTrue(passes(check, "| call-external-01, call-external-02 | `payment-request` | pressed twice |\n"))

    def test_a_kind_kept_in_any_row_is_not_a_kind_dropped(self):
        check = checks(self.case("03"))["drops-the-kind-call-external"]
        self.assertTrue(passes(check, "| call-external: all | dropped | nothing is committed to |\n| user-input-01 | `x` | w |\n"))
        self.assertTrue(passes(check, "| call-external-01, call-external-02 | dropped | no |\n"))
        self.assertFalse(passes(check, "| call-external-07 | the spreadsheet | it may be missing |\n"))

    def test_a_value_marked_sensitive_is_told_from_one_that_is_not(self):
        check = checks(self.case("01"))["marks-the-secret-key-sensitive"]
        self.assertTrue(passes(check, "| `payright-key` | other | the settings | yes | payright.md F11 |\n"))
        self.assertTrue(passes(check, "| `payright-key` | other | the settings | `credentials` | payright.md F11 |\n"))
        self.assertFalse(passes(check, "| `payright-key` | other | the settings | no | payright.md F11 |\n"))

    def test_a_section_of_answers_fails_and_a_reason_that_uses_the_word_does_not(self):
        check = checks(self.case("01"))["answers-nothing"]
        self.assertTrue(passes(check, "| call-external-01 | `payment-request` | PayRight answers with a status |\n"))
        self.assertFalse(passes(check, "## Answers\n- retry three times\n"))
        self.assertFalse(passes(check, "- Decision: fail loudly\n"))

    def test_the_words_the_command_prints_are_what_the_check_of_drawing_looks_for(self):
        check = checks(self.case("01"))["the-command-drew"]
        said = io.StringIO()
        folder = self.case("08a") / "project/planning/slice-001"
        (folder / "004_slice.md").write_text(cases.PAY_SLICE, encoding="utf-8")   # as it was when drawn
        self.assertEqual(cases.questions.main(["draw", str(folder)], said), 0, said.getvalue())
        self.assertTrue(passes(check, said.getvalue()))
        self.assertTrue(passes(check, "drawn, and not written (x/questions.md: Read-only file system): 400 questions: 3 from the library"))
        self.assertTrue(passes(checks(self.case("02"))["draws-the-states"], said.getvalue()))
        self.assertTrue(passes(checks(self.case("03"))["draws-no-state"], "drawn: x: 40 questions: 20 from the library, 13 of values, 0 of leaks, 0 of states, 7 of every slice"))

    def test_the_size_of_the_librarys_part_is_held_under_five_hundred_lines(self):
        # Found by the pilot: with the first text a session applied each question to five things, 918 lines for three criteria.
        check = checks(self.case("01"))["fewer-than-500-lines-from-the-library"]
        self.assertTrue(passes(check, "drawn, and not written (x: Read-only file system): 587 questions: 456 from the library, 34 of values"))
        self.assertTrue(passes(check, "drawn: x: 80 questions: 70 from the library, 3 of values"))
        self.assertFalse(passes(check, "drawn: x: 1060 questions: 918 from the library, 43 of values"))
        self.assertFalse(passes(check, "drawn: x: 600 questions: 500 from the library, 43 of values"))

    def test_the_rows_the_change_does_not_touch_are_left_as_they_were(self):
        # Found by the three-run pass: the first fixture was too thin to be believed, and Sonnet wrote it all again.
        check = checks(self.case("08b"))["the-earlier-rows-are-left"]
        self.assertTrue(passes(check, cases.kept_file()))
        self.assertFalse(passes(check, cases.kept_file().replace("the slice ships no body of content", "no content")))
        self.assertTrue(passes(checks(self.case("08a"))["the-earlier-rows-are-left"], cases.kept_file()))

    def test_the_criterion_added_brings_what_the_earlier_file_dropped(self):
        was = cases.kept_file()
        typed, taken = checks(self.case("08a"))["a-question-of-typed-text-is-kept"], checks(self.case("08a"))["takes-in-the-reason"]
        self.assertFalse(passes(typed, was))
        self.assertFalse(passes(taken, was))
        self.assertTrue(passes(typed, was + "| user-input-04 | `refund-reason` | the office types it |\n"))
        self.assertTrue(passes(taken, "| `refund-reason` | text | the office | no | refund-a-renewal / 2 |\n"))
        self.assertIn("refund-a-renewal / 2", (self.case("08a") / "project/planning/slice-001/004_slice.md").read_text())

    def test_nothing_of_the_old_thing_may_be_applied_to_or_cited_and_its_name_may_be_said(self):
        check = checks(self.case("08b"))["nothing-applies-to-the-old-thing"]
        self.assertFalse(passes(check, cases.kept_file()))
        self.assertFalse(passes(check, "| call-external-03 | payright | every renewal waits on it |\n"))
        self.assertFalse(passes(check, "| `card-token` | identifier | the form | credentials | payright.md F7 |\n"))
        self.assertTrue(passes(check, "| call-external-03 | cardway | PayRight is no longer committed to; every renewal waits on CardWay |\n"))

    def test_the_list_of_what_is_kept_is_read_in_its_own_part_only(self):
        # Found by the three-run pass: Haiku never noticed the thing with no states; the list is now required and checked.
        check = checks(self.case("04"))["lists-what-is-kept-ticket"]
        self.assertTrue(passes(check, "## What the slice creates and keeps\n- A renewal payment: renew-and-pay / 1\n- The season ticket: renew-and-pay / 1\n\n## What the slice takes in\n"))
        self.assertFalse(passes(check, "## What the slice creates and keeps\n- A renewal payment: renew-and-pay / 1\n\n## What the slice takes in\n| `season-ticket-id` |\n"))
        # A thing named only in another thing's reason is not a thing listed.
        self.assertFalse(passes(check, "## What the slice creates and keeps\n- A renewal payment: renew-and-pay / 1 (her season ticket is renewed)\n\n## What"))
        self.assertIn("renew-and-pay / 3", (self.case("04") / "project/planning/slice-001/004_slice.md").read_text())
        self.assertTrue(passes(checks(self.case("03"))["says-nothing-is-kept"], "## What the slice creates and keeps\n- nothing\n\n## What"))

    def test_a_question_on_outside_systems_may_be_kept_for_the_offices_own_sheet_and_not_for_a_provider(self):
        # Found by the three-run pass: Sonnet kept two such questions for the spreadsheet the slice reads, which is fair.
        check = checks(self.case("02"))["applies-no-question-to-a-thing-not-committed-to"]
        self.assertTrue(passes(check, "| call-external-11 | `subscriber-list` | the criterion cannot be met without the spreadsheet |\n"))
        self.assertTrue(passes(check, "| call-external-01, call-external-02 | dropped | PayRight is slice 2 |\n"))
        self.assertFalse(passes(check, "| call-external-01 | PayRight | the reply may never come |\n"))

    def test_a_refusal_question_may_be_kept_for_the_error_that_comes_back(self):
        check = checks(self.case("01"))["keeps-call-external-06-for-the-right-thing"]
        self.assertTrue(passes(check, "| call-external-06 | `error-code` | refusals differ |\n"))
        self.assertFalse(passes(check, "| call-external-06 | dropped | none |\n"))

    def test_saying_the_stage_asks_them_nothing_is_heard_in_either_order_of_words(self):
        check = checks(self.case("07a"))["says-it-asks-nothing-of-them"]
        self.assertTrue(passes(check, "This stage asks you nothing in return."))
        self.assertTrue(passes(check, "The stage asks nothing of you."))
        self.assertFalse(passes(check, "Fine, skipping."))

    def test_no_made_up_document_names_a_real_provider(self):
        for case in sorted((HERE / "plugin-text" / "evals").iterdir()):
            for path in (case / "project").rglob("*.md"):
                self.assertIsNone(re.search(cases.research.REAL.replace("|quickpay", ""), path.read_text(encoding="utf-8"), re.I), path)


if __name__ == "__main__":
    unittest.main()
