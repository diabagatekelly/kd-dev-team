"""facts.py: which known facts a research document holds, and in how many runs."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import facts  # noqa: E402

KEY = {"settles-in-three-days": r"3 working days", "refund-window": r"90 days|ninety days"}


class Facts(unittest.TestCase):
    def test_a_fact_is_held_when_its_pattern_is_found_whatever_the_case(self):
        self.assertEqual(facts.held(KEY, "- F1: Settling takes up to 3 Working Days."), ["settles-in-three-days"])

    def test_a_document_that_holds_none_holds_none(self):
        self.assertEqual(facts.held(KEY, "Payments are quick."), [])

    def test_each_fact_is_counted_over_the_runs_that_hold_it(self):
        runs = ["3 working days; ninety days", "3 working days", "nothing"]
        self.assertEqual(facts.across(KEY, runs), {"settles-in-three-days": 2, "refund-window": 1})


if __name__ == "__main__":
    unittest.main()
