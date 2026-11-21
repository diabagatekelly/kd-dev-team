import json
import os
import tempfile
import unittest

import agreement as ag
import wording_check


class CheckRun(unittest.TestCase):
    def test_a_complete_run_is_read_as_bug_to_class(self):
        entries = [{"id": "1", "class": "N"}, {"id": "2", "class": "X"}]
        self.assertEqual(ag.check_run(entries, ["1", "2"], "f"), {"1": "N", "2": "X"})

    def test_a_missing_bug_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, r"missing \['2'\]"):
            ag.check_run([{"id": "1", "class": "N"}], ["1", "2"], "f")

    def test_a_bug_outside_the_benchmark_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, r"not in the benchmark \['9'\]"):
            ag.check_run([{"id": "1", "class": "N"}, {"id": "9", "class": "N"}], ["1"], "f")

    def test_an_unknown_class_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, "class 'Q'"):
            ag.check_run([{"id": "1", "class": "Q"}], ["1"], "f")

    def test_a_bug_scored_twice_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, "scored twice"):
            ag.check_run([{"id": "1", "class": "N"}, {"id": "1", "class": "P"}], ["1"], "f")


class Majority(unittest.TestCase):
    def test_two_of_three_wins(self):
        self.assertEqual(ag.majority(["N", "P", "N"]), "N")

    def test_a_three_way_tie_goes_to_the_least_favourable(self):
        self.assertEqual(ag.majority(["N", "P", "W"]), "W")
        self.assertEqual(ag.majority(["D", "P", "X"]), "X")


class Agreement(unittest.TestCase):
    CALLS = {
        ("a", "1"): ["N", "N", "N"],   # same class
        ("a", "2"): ["N", "D", "N"],   # same side of the line, classes differ
        ("a", "3"): ["N", "P", "N"],   # crosses the line
        ("b", "1"): ["X", "P", "W"],   # none named, classes differ
    }

    def test_named_or_not_counts_bugs_on_one_side_in_every_run(self):
        self.assertEqual(ag.agreement(self.CALLS)["same_named_or_not"], 3)

    def test_same_class_counts_only_identical_calls(self):
        self.assertEqual(ag.agreement(self.CALLS)["same_class"], 1)

    def test_named_per_plan_is_counted_run_by_run(self):
        result = ag.agreement(self.CALLS)["named_per_plan_per_run"]
        self.assertEqual(result["a"], {"bugs": 3, "named": [3, 2, 3]})
        self.assertEqual(result["b"], {"bugs": 1, "named": [0, 0, 0]})

    def test_split_lists_every_bug_the_runs_disagreed_on(self):
        self.assertEqual(ag.agreement(self.CALLS)["split"],
                         ["a:2 N/D/N", "a:3 N/P/N", "b:1 X/P/W"])


class Sample(unittest.TestCase):
    def calls(self):
        calls = {}
        for plan in ("a", "b", "c"):
            for i in range(8):
                calls[(plan, f"n{i}")] = ["N"] * 3
            calls[(plan, "p")] = ["P"] * 3
        calls[("a", "x")] = ["X"] * 3
        return calls

    def test_the_size_asked_for_is_drawn_without_repeats(self):
        picked = ag.draw_sample(self.calls(), 15, seed=1)
        self.assertEqual(len(picked), 15)
        self.assertEqual(len(set(picked)), 15)

    def test_every_class_present_is_in_the_sample(self):
        calls = self.calls()
        picked = ag.draw_sample(calls, 15, seed=1)
        self.assertEqual({ag.majority(calls[k]) for k in picked}, {"N", "P", "X"})

    def test_a_rare_class_is_not_drawn_past_what_exists(self):
        calls = self.calls()
        picked = ag.draw_sample(calls, 15, seed=1)
        self.assertEqual(sum(1 for k in picked if ag.majority(calls[k]) == "X"), 1)

    def test_every_plan_is_in_the_sample(self):
        self.assertEqual({k[0] for k in ag.draw_sample(self.calls(), 15, seed=1)}, {"a", "b", "c"})

    def test_the_same_seed_draws_the_same_sample(self):
        self.assertEqual(ag.draw_sample(self.calls(), 15, seed=7),
                         ag.draw_sample(self.calls(), 15, seed=7))

    def test_different_seeds_draw_different_samples(self):
        draws = {tuple(ag.draw_sample(self.calls(), 15, seed=seed)) for seed in range(6)}
        self.assertGreater(len(draws), 1)

    def test_a_benchmark_smaller_than_the_size_is_drawn_whole(self):
        calls = {("a", "1"): ["N"] * 3, ("a", "2"): ["X"] * 3}
        self.assertEqual(sorted(ag.draw_sample(calls, 15, seed=1)), sorted(calls))


class Owner(unittest.TestCase):
    # The first run is in the minority on a:1, so reading the first run
    # in place of the majority would give a different count.
    CALLS = {("a", "1"): ["P", "N", "N"], ("a", "2"): ["X", "X", "X"]}

    def test_the_owner_is_compared_with_the_majority_not_the_first_run(self):
        agreed, total, differ = ag.compare_owner(self.CALLS, {"a:1": "N", "a:2": "P"})
        self.assertEqual((agreed, total), (1, 2))
        self.assertEqual(differ, ["a:2: owner P, matcher X"])

    def test_an_answer_left_empty_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, "a:1"):
            ag.compare_owner(self.CALLS, {"a:1": ""})


TABLES = """# Tables

## Table 2. State by event

| id | state | event | tag | text |
|---|---|---|---|---|
| T2.1 | new | lost reply | PLAN SILENT | nothing is stored |
| `T2.2` | new | twice | DECIDED | refused |
"""


class TableRow(unittest.TestCase):
    def test_a_cell_is_given_with_its_heading_and_column_titles(self):
        self.assertEqual(ag.table_row(TABLES, "T2.1"), {
            "heading": "Table 2. State by event",
            "titles": "| id | state | event | tag | text |",
            "row": "| T2.1 | new | lost reply | PLAN SILENT | nothing is stored |"})

    def test_an_id_written_in_code_marks_is_found(self):
        self.assertIn("DECIDED", ag.table_row(TABLES, "T2.2")["row"])

    def test_an_id_that_is_only_part_of_another_is_not_found(self):
        self.assertIsNone(ag.table_row(TABLES, "T2"))


class Load(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.bench = os.path.join(self.root, "bench")
        self.runs = os.path.join(self.root, "runs")
        os.makedirs(self.bench)
        self.write(self.bench, "a.json", [{"id": "1", "title": "t", "trigger": "w", "build_behaviour": "b", "harm": "h"}])

    def write(self, folder, name, value):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, name), "w", encoding="utf-8") as handle:
            if isinstance(value, str):
                handle.write(value)
            else:
                json.dump(value, handle)

    def run_out(self, plan, run, cls="N", quote="nothing is stored"):
        folder = os.path.join(self.runs, plan, run)
        self.write(folder, "out.json", [{"id": "1", "class": cls, "cells": [{"id": "T2.1", "quote": quote}]}])
        self.write(folder, "tables.md", TABLES)

    def test_runs_are_read_with_each_cited_cell_s_whole_row(self):
        self.run_out("a", "run1")
        self.run_out("a", "run2", quote="lost reply")
        calls, cited, _ = ag.load(self.runs, self.bench)
        self.assertEqual(calls[("a", "1")], ["N", "N"])
        kept = cited[("a", "1")]["T2.1"]
        self.assertIn("PLAN SILENT", kept["row"]["row"])
        self.assertEqual(kept["quotes"], ["nothing is stored", "lost reply"])

    def test_a_plan_with_no_runs_is_refused(self):
        with self.assertRaisesRegex(ag.BadRun, "same number of runs"):
            ag.load(self.runs, self.bench)

    def test_plans_with_different_numbers_of_runs_are_refused(self):
        self.write(self.bench, "b.json", [{"id": "1", "title": "t", "trigger": "w", "build_behaviour": "b", "harm": "h"}])
        self.run_out("a", "run1")
        self.run_out("a", "run2")
        self.run_out("b", "run1")
        with self.assertRaisesRegex(ag.BadRun, "same number of runs"):
            ag.load(self.runs, self.bench)

    def test_a_scenario_id_written_twice_is_refused(self):
        scenario = {"id": "1", "title": "t", "trigger": "w", "build_behaviour": "b", "harm": "h"}
        self.write(self.bench, "a.json", [scenario, scenario])
        self.run_out("a", "run1")
        with self.assertRaisesRegex(ag.BadRun, "written twice"):
            ag.load(self.runs, self.bench)

    def test_a_plan_name_that_is_not_a_plain_name_is_refused(self):
        self.write(self.bench, "...json", [])
        with self.assertRaisesRegex(ag.BadRun, "a plan's name"):
            ag.load(self.runs, self.bench)


class Sheet(unittest.TestCase):
    def setUp(self):
        self.out = tempfile.mkdtemp()
        self.bench = {"a": {"1": {"id": "1", "title": "A title", "trigger": "w", "build_behaviour": "b", "harm": "h"}}}
        self.cited = {("a", "1"): {"T2.1": {"quotes": ["nothing is stored"], "row": ag.table_row(TABLES, "T2.1")}}}

    def sheet(self):
        with open(os.path.join(self.out, "sheet.md"), encoding="utf-8") as handle:
            return handle.read()

    def test_the_title_says_how_many_calls_there_are(self):
        ag.write_sheet([("a", "1")], self.cited, self.bench, self.out)
        self.assertTrue(self.sheet().startswith("# 1 calls to judge"))

    def test_a_cited_cell_is_shown_as_its_whole_row_with_tag_and_heading(self):
        ag.write_sheet([("a", "1")], self.cited, self.bench, self.out)
        text = self.sheet()
        self.assertIn('under "Table 2. State by event"', text)
        self.assertIn("| T2.1 | new | lost reply | PLAN SILENT | nothing is stored |", text)

    def test_answers_already_given_are_not_wiped_by_a_second_sample(self):
        ag.write_sheet([("a", "1")], self.cited, self.bench, self.out)
        with open(os.path.join(self.out, "answers.json"), "w", encoding="utf-8") as handle:
            json.dump({"a:1": "N"}, handle)
        with self.assertRaisesRegex(ag.BadRun, "holds answers"):
            ag.write_sheet([("a", "1")], self.cited, self.bench, self.out)

    def test_force_replaces_them(self):
        ag.write_sheet([("a", "1")], self.cited, self.bench, self.out)
        with open(os.path.join(self.out, "answers.json"), "w", encoding="utf-8") as handle:
            json.dump({"a:1": "N"}, handle)
        ag.write_sheet([("a", "1")], self.cited, self.bench, self.out, force=True)
        with open(os.path.join(self.out, "answers.json"), encoding="utf-8") as handle:
            self.assertEqual(json.load(handle), {"a:1": ""})


class Wording(unittest.TestCase):
    def test_a_domain_term_is_found_with_its_line(self):
        self.assertEqual(wording_check.find_terms("fine\nthe Bank's API\n"),
                         [(2, "bank"), (2, "api")])

    def test_a_term_inside_another_word_is_not_a_hit(self):
        self.assertEqual(wording_check.find_terms("a rapid embankment"), [])

    def test_a_plural_of_a_listed_term_is_found(self):
        self.assertEqual(wording_check.find_terms("two payments to merchants"),
                         [(1, "payments"), (1, "merchants")])

    def test_a_clean_text_has_no_hits(self):
        self.assertEqual(wording_check.find_terms("every cell has an id"), [])


if __name__ == "__main__":
    unittest.main()
