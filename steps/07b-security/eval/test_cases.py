"""The security cases: every arm builds, each report names the stage its case expects, the files a
case starts from are ones the script draws from, and the checks pass a good file and fail a bad one."""
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

    def test_every_arm_builds_its_cases(self):
        self.assertEqual(len(self.built), 8)
        for arm in ["bare"] + (["kad"] if any(path.exists() for path in cases.KAD) else []):
            with self.subTest(arm), contextlib.redirect_stdout(io.StringIO()) as out:
                cases.main(arm)
                self.assertEqual(len(out.getvalue().splitlines()), 1 if arm == "kad" else 8)

    def test_each_report_names_security_next_and_the_changed_case_the_questions(self):
        for path in sorted((HERE / "plugin-text" / "evals").iterdir()):
            report = (path / "report.txt").read_text(encoding="utf-8")
            with self.subTest(path.name):
                if path.name.startswith("07-"):
                    self.assertIn("- next stage by the documents: questions (its document: planning/slice-001/007_questions/, to draw again", report)
                else:
                    self.assertRegex(report, r"- next stage by the documents: security \(its document: planning/slice-001/00[57]_questions/security\.md, "
                                             r"to write there: security\.md; the questions are then drawn again with it\)")
                    self.assertRegex(report, r'questions\.py" draw planning/slice-001')

    def test_the_security_file_the_changed_case_starts_from_passes_the_first_cases_checks(self):
        found = checks(self.case("01-"))
        for name in ("says-browser-holds", "says-network-holds", "says-calls-out-holds", "every-fact-has-a-source", "wants-the-credentials",
                     "comes-through-the-address-that-receives", "comes-through-a-screen-or-request-of-the-office", "answers-nothing"):
            with self.subTest(name):
                self.assertTrue(passes(found[name], cases.EARLIER_SECURITY), name)

    def test_the_checks_fail_a_file_that_answers_leaves_a_source_out_or_wants_nothing(self):
        found = checks(self.case("01-"))
        self.assertFalse(passes(found["answers-nothing"], cases.EARLIER_SECURITY + "\n## Controls\n- sign every event\n"))
        self.assertFalse(passes(found["answers-nothing"], cases.EARLIER_SECURITY + "\nGiven an event arrives, when it is unsigned, then it is refused.\n"))
        self.assertFalse(passes(found["every-fact-has-a-source"], cases.EARLIER_SECURITY.replace("| 005_approach.md: PayRight is committed to |", "| |")))
        self.assertFalse(passes(found["wants-the-credentials"], cases.EARLIER_SECURITY.replace("credentials", "things").replace("card-token", "a thing")))
        self.assertFalse(passes(found["says-network-holds"], cases.EARLIER_SECURITY.replace("| network | yes", "| network | no")))

    def test_a_public_key_dismissed_passes_and_one_asked_of_fails(self):
        found = checks(self.case("03-"))
        good = cases.EARLIER_SECURITY + "| `publishable-key` | `renewal-screen` | nothing | no: it is public by design (payright.md F12) |\n"
        bad = cases.EARLIER_SECURITY + "| `publishable-key` | `renewal-screen` | someone reads it from the page | yes |\n"
        self.assertTrue(passes(found["dismisses-the-public-key-with-the-reason"], good))
        self.assertTrue(passes(found["does-not-ask-of-it-as-a-secret"], good))
        self.assertFalse(passes(found["dismisses-the-public-key-with-the-reason"], bad))
        self.assertFalse(passes(found["does-not-ask-of-it-as-a-secret"], bad))

    def test_little_to_attack_allows_three_rows_asked_and_not_four(self):
        found = checks(self.case("02-"))["asks-of-no-more-than-three-rows"]
        row = "| nothing | `price-screen` | a made-up number of seats is typed | yes |\n"
        self.assertTrue(passes(found, "## What someone who means harm would want\n" + row * 3))
        self.assertFalse(passes(found, "## What someone who means harm would want\n" + row * 4))

    def test_a_skip_is_recorded_in_their_words_with_the_date_and_no_table(self):
        found = checks(self.case("04b-"))
        good = "Skipped at the user's word, 2026-11-25: \"No. Skip it.\"\n"
        self.assertTrue(passes(found["in-their-words-with-the-date"], good))
        self.assertTrue(passes(found["writes-no-table"], good))
        self.assertFalse(passes(found["writes-no-table"], cases.EARLIER_SECURITY))

    def test_the_changed_case_keeps_the_earlier_rows(self):
        found = checks(self.case("07-"))["the-earlier-rows-are-left"]
        self.assertTrue(passes(found, cases.EARLIER_SECURITY))
        self.assertFalse(passes(found, cases.EARLIER_SECURITY.replace("a true event sent again later", "an old event replayed")))

    def test_the_kept_files_account_for_the_whole_library(self):
        for kept in (cases.q.kept_file(), cases.PUBLIC_KEPT, cases.QUOTE_KEPT):
            judged = cases.questions.problems(cases.questions.read_kept(kept), {}, cases.q.ENTRIES)[1]
            self.assertEqual(len(judged), len(cases.q.ENTRIES))


if __name__ == "__main__":
    unittest.main()
