import unittest

import tally


def run(*failed, error=None):
    names = ["writes-the-set", "form-the-table", "asks-the-user"]
    return {"error": error, "graders": [{"name": name, "passed": name not in failed} for name in names]}


class Tally(unittest.TestCase):
    def test_runs_are_counted_with_and_without_the_checks_of_form(self):
        result = {"costUsd": 1.2345, "cases": [
            {"name": "slice-01", "arms": {"with": [run(), run("form-the-table"), run("form-the-table", "asks-the-user")]}},
            {"name": "slice-02", "arms": {"with": [run("writes-the-set")]}}]}
        runs, passed, held, cost, failures = tally.tally(result)
        self.assertEqual((runs, passed, held, cost), (4, 1, 2, 1.23))
        self.assertEqual(failures, [("slice-01", 1, ["form-the-table"]), ("slice-01", 2, ["form-the-table", "asks-the-user"]),
                                    ("slice-02", 0, ["writes-the-set"])])

    def test_a_run_that_did_not_finish_is_a_failure_though_no_check_failed(self):
        runs, passed, held, _, failures = tally.tally({"cases": [{"name": "a", "arms": {"with": [{"error": "timed out", "graders": []}]}}]})
        self.assertEqual((runs, passed, held), (1, 0, 0))
        self.assertEqual(failures, [("a", 0, ["the run itself: timed out"])])

    def test_a_result_with_no_case_counts_nothing(self):
        self.assertEqual(tally.tally({})[:3], (0, 0, 0))


if __name__ == "__main__":
    unittest.main()
