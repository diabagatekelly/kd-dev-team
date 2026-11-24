"""The research cases: every arm builds, each report says what its case expects, and the documents
a case starts from quote only what the made-up pages hold."""
import contextlib
import io
import os
import pathlib
import re
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_cases as cases  # noqa: E402
import quotes  # noqa: E402


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
        self.assertEqual(len(self.built), 11)
        arms = ["bare"] + (["kad"] if any(path.exists() for path in cases.KAD) else [])
        for arm in arms:
            with self.subTest(arm), contextlib.redirect_stdout(io.StringIO()) as out:
                cases.main(arm)
            self.assertEqual(len(out.getvalue().splitlines()), 2 if arm == "kad" else 11)

    def test_only_the_text_arm_carries_the_stage_text_and_the_bare_arm_is_told_to_do_the_stage(self):
        with contextlib.redirect_stdout(io.StringIO()):
            cases.main("bare")
        self.assertTrue((HERE / "plugin-text/skills/research/SKILL.md").exists())
        self.assertFalse((HERE / "plugin-bare/skills/research").exists())
        self.assertIn("The research stage has no text of its own here", (HERE / "plugin-bare/hooks/routing-table.md").read_text())
        self.assertIn("uses-the-stage-text", (self.case("01") / "case.yaml").read_text())

    def test_the_report_lists_what_is_committed_to_and_what_is_to_be_written(self):
        report = self.report("01")
        self.assertIn("- to research, committed to in planning/slice-001/005_approach.md:\n  - PayRight, for taking a card payment", report)
        self.assertIn("to write there: payright.md, states.md)", report)
        self.assertIn("- 3 pages are already kept in planning/slice-001/pages", report)
        self.assertNotIn(str(cases.ROOT), report)

    def test_with_nothing_committed_to_only_the_states_are_to_be_written(self):
        report = self.report("05")
        self.assertIn("- nothing is committed to in planning/slice-001/005_approach.md: no outside system is researched", report)
        self.assertIn("to write there: states.md)", report)

    def test_after_a_changed_approach_the_report_names_what_is_owed_and_what_no_longer_stands(self):
        report = self.report("08")
        self.assertIn("still to write there: payright.md)", report)
        self.assertIn("- no longer stands, its thing is not committed to in slice-001/007_approach.md: "
                      "planning/slice-001/006_research/cardway.md", report)

    def test_a_case_that_follows_a_question_carries_the_turns_before_it(self):
        for start in ("06b", "09b"):
            self.assertTrue((self.case(start) / "history.jsonl").exists(), start)
        self.assertFalse((self.case("06a") / "history.jsonl").exists())

    def test_the_site_refused_is_not_on_the_list_until_the_user_allows_it(self):
        self.assertNotIn(cases.API, (self.case("06a") / "state/web/allowed").read_text())
        self.assertIn(cases.API, (self.case("06b") / "state/web/allowed").read_text())
        self.assertTrue((self.case("06a") / "state/web/pages" / cases.API / "errors").exists())

    def test_every_quote_in_the_documents_a_case_starts_from_is_on_the_page_served(self):
        for case in sorted((HERE / "plugin-text" / "evals").iterdir()):
            documents = {str(path.relative_to(case)): path.read_text(encoding="utf-8")
                         for path in (case / "project" / "planning").rglob("*.md") if "slice-001" in path.parts and "00" in path.name[:2]}
            with self.subTest(case.name):
                self.assertEqual(quotes.page.check(documents, quotes.served(case)), [])

    def test_the_pages_kept_are_the_pages_served(self):
        case = self.case("01")
        kept = sorted(path.name for path in (case / "project/planning/slice-001/pages").iterdir())
        self.assertEqual(kept, ["docs.payright.example-limits.txt", "docs.payright.example-payments.txt", "docs.payright.example.txt"])

    def test_no_made_up_document_or_page_names_a_real_provider(self):
        for case in sorted((HERE / "plugin-text" / "evals").iterdir()):
            for path in [*(case / "project").rglob("*.md"), *(case / "state" / "web").rglob("*")]:
                if path.is_file():
                    self.assertIsNone(re.search(cases.REAL.replace("|quickpay", ""), path.read_text(encoding="utf-8"), re.I), path)

    def test_a_check_for_a_fetch_reads_the_command_as_a_session_writes_it(self):
        any_page, of_the_reference = cases.fetched("x")["input_match"], cases.fetched("x", cases.API)["input_match"]
        loop = 'for u in errors statuses; do python3 "$P/page.py" fetch "https://api.payright.example/$u" --to p; done'
        for command in ('python3 "/p/startup/../research/page.py" fetch https://docs.payright.example/ --to planning/slice-001/pages', loop):
            self.assertRegex(command, any_page)
        self.assertRegex(loop, of_the_reference)
        self.assertNotRegex('python3 page.py fetch https://docs.payright.example/ --to p', of_the_reference)
        for command in ("python3 page.py kept planning/slice-001/pages", "python3 page.py check planning/slice-001/pages payright.md"):
            self.assertNotRegex(command, any_page)


if __name__ == "__main__":
    unittest.main()
