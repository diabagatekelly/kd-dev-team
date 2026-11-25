"""The answers stage's cases: where each starts, and that its checks tell a good answers file from a poor one."""
import importlib.util
import io
import pathlib
import re
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("answers_cases", HERE / "make_cases.py")
cases = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cases)

GOOD = """## A1: A repeat takes no second payment
Kind: fact
Says: The same reference within a day returns the first payment.
Rests on: payright F6
Settles: L.call-external-02.payment-reference

## A2: No reply
Kind: test
Says: What has happened when a request gets no reply is not said.
Test: cut the connection in test mode and ask by the reference.
Harm: high
Settles: C.payright.O1, L.call-external-01.payment-request

## A3: The key
Kind: chosen
Says: The key is never written to a record.
Rests on: a credential in a record is read by whoever reads the record.
Settles: L.secrets-03.secret-key
Under: renew-and-pay
Criterion: Given a call to PayRight fails, when its record is read, then nothing of the secret key appears in it.

## A4: A payment lost
Kind: owner
Says: A lost dispute has no way out.
Options: the renewal stays recorded | the renewal is taken back
Recommended: the renewal stays recorded.
If left: the office does not know which holds.
Harm: medium
Settles: C.states.dead-end.1
"""


def holds(check, text):
    found = re.search(check["pattern"], text, re.I if "i" in check.get("flags", "") else 0) is not None
    return found != (check.get("match") == "not_contains")


@unittest.skipIf(sys.platform == "win32", "the cases are built inside the VM, which is Linux")
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        said, out = io.StringIO(), sys.stdout
        sys.stdout = said
        try:
            cases.main("text")
        finally:
            sys.stdout = out
        cls.built = said.getvalue()
        cls.evals = HERE / "plugin-text" / "evals"

    def report(self, name):
        return (self.evals / name / "report.txt").read_text(encoding="utf-8")

    def test_seven_cases_are_built_and_each_has_checks(self):
        self.assertEqual(len(re.findall(r": \d+ checks", self.built)), 7)

    def test_the_small_slice_starts_with_nothing_answered_and_the_commands_given(self):
        report = self.report("01-a-small-slice-from-nothing")
        self.assertRegex(report, r"next stage by the documents: answers \(its document: planning/slice-001/\d+_answers\.md\)")
        self.assertIn('answers.py" next planning/slice-001', report)

    def test_the_providers_slice_starts_with_eight_questions_left(self):
        out = io.StringIO()
        cases.answers.main(["next", str(self.evals / "02-the-kinds-told-apart/project/planning/slice-001")], out)
        self.assertIn("8 are left", out.getvalue())
        for name in cases.LEFT:
            self.assertIn(f"- {name}:", out.getvalue())

    def test_the_decision_case_starts_drawn_with_the_decision_on_the_owners_list(self):
        folder = self.evals / "05-the-owner-decides-against-the-recommendation/project/planning/slice-001"
        self.assertIn("### A900: A refund asked for after ninety days (medium)", next(folder.glob("*_answered.md")).read_text(encoding="utf-8"))
        self.assertIn("answers drawn again", self.report("05-the-owner-decides-against-the-recommendation"))

    def test_the_changed_questions_case_starts_stale_with_one_question_left(self):
        self.assertIn("to draw again", self.report("06-the-questions-changed-after"))
        out = io.StringIO()
        cases.answers.main(["next", str(self.evals / "06-the-questions-changed-after/project/planning/slice-001")], out)
        self.assertIn("1 are left", out.getvalue())
        self.assertIn("T.her-details.refund-request", out.getvalue())

    def test_the_plugin_carries_the_script_and_this_stages_text(self):
        self.assertTrue((HERE / "plugin-text/answers/answers.py").is_file())
        self.assertTrue((HERE / "plugin-text/skills/answers/SKILL.md").is_file())


class Checks(unittest.TestCase):
    def checks(self, number):
        return {check["name"]: check for check in cases.SCENARIOS[number][7] if check.get("type") == "regex" and isinstance(check.get("target"), dict)}

    def test_the_kinds_are_told_apart_in_a_good_file(self):
        for name, check in self.checks(1).items():
            self.assertTrue(holds(check, GOOD), name)

    def test_a_criterion_on_a_guess_a_fact_on_nothing_and_an_owner_with_no_options_fail(self):
        checks = self.checks(1)
        self.assertFalse(holds(checks["no-criterion-on-the-guess"], GOOD.replace("Harm: high\n", "Harm: high\nCriterion: Given x, when y, then z.\n")))
        self.assertFalse(holds(checks["a-repeat-is-a-fact-from-the-providers-page"], GOOD.replace("payright F6", "what providers do")))
        self.assertFalse(holds(checks["a-dead-end-is-the-owners"], GOOD.replace("Options: the renewal stays recorded | the renewal is taken back\n", "")))
        self.assertFalse(holds(checks["the-key-out-of-the-records-is-chosen"], GOOD.replace("Kind: chosen", "Kind: owner")))
        self.assertFalse(holds(checks["a-criterion-of-absence"], GOOD.replace("nothing of the secret key appears in it", "the key is handled with care")))

    def test_a_decision_is_recorded_in_their_words_and_not_as_what_was_recommended(self):
        checks = self.checks(5)
        decided = cases.REFUNDS + ('Decided: no refund is offered after 90 days (the user, 2026-11-25: "no refund is offered after that")\n'
                                   "Under: refund-a-renewal\nCriterion: Given a renewal settled more than 90 days ago, when the office asks to refund it, then it is told no refund is offered.\n")
        for name, check in checks.items():
            self.assertTrue(holds(check, decided), name)
        self.assertFalse(holds(checks["records-the-decision-in-their-words"], cases.REFUNDS))
        self.assertFalse(holds(checks["does-not-keep-its-own-recommendation"], decided.replace("no refund is offered after 90 days (", "gives the money back another way (")))


if __name__ == "__main__":
    unittest.main()
