import unittest

import triage_check as tc

IDS = ["sync-01", "sync-02", "time-01"]


def row(name, relevant, applies=None):
    return {"id": name, "relevant": relevant, "why": "because",
            "applies_to": (["the pull"] if relevant else []) if applies is None else applies}


def triage(**relevant):
    return [row(name, relevant.get(name.replace("-", "_"), False)) for name in IDS]


class Problems(unittest.TestCase):
    def test_a_triage_of_every_entry_has_no_problems(self):
        self.assertEqual(tc.problems(IDS, triage(sync_01=True)), [])

    def test_a_missing_entry_is_named(self):
        self.assertEqual(tc.problems(IDS, triage()[:2]), ["time-01: missing"])

    def test_an_entry_judged_twice_is_named(self):
        self.assertIn("sync-01: judged twice", tc.problems(IDS, triage() + [row("sync-01", False)]))

    def test_an_entry_the_library_lacks_is_named(self):
        self.assertIn("text-09: not an entry of the library", tc.problems(IDS, triage() + [row("text-09", False)]))

    def test_relevant_must_be_a_boolean(self):
        rows = triage()
        rows[0]["relevant"] = "yes"
        self.assertIn("sync-01: relevant must be true or false", tc.problems(IDS, rows))

    def test_a_relevant_entry_must_say_what_it_applies_to(self):
        rows = triage()
        rows[0] = row("sync-01", True, applies=[])
        self.assertEqual(tc.problems(IDS, rows), ["sync-01: relevant, but applies_to is empty"])

    def test_a_dropped_entry_must_not_list_anything(self):
        rows = triage()
        rows[0] = row("sync-01", False, applies=["x"])
        self.assertEqual(tc.problems(IDS, rows), ["sync-01: not relevant, but applies_to is not empty"])

    def test_an_empty_reason_is_named(self):
        rows = triage()
        rows[0]["why"] = " "
        self.assertEqual(tc.problems(IDS, rows), ["sync-01: why is empty"])


class TiedEntries(unittest.TestCase):
    RUNS = [
        [{"plan": "a", "id": "b1", "class": "F", "entries": ["sync-01"]},
         {"plan": "a", "id": "b2", "class": "X", "entries": []},
         {"plan": "z", "id": "b1", "class": "F", "entries": ["time-01"]}],
        [{"plan": "a", "id": "b1", "class": "F", "entries": ["sync-02"]},
         {"plan": "a", "id": "b2", "class": "P", "entries": ["time-01"]}],
        [{"plan": "a", "id": "b1", "class": "P", "entries": ["time-01"]},
         {"plan": "a", "id": "b2", "class": "X", "entries": []}],
    ]

    def test_a_defect_gets_the_entries_of_the_runs_that_gave_its_majority_class(self):
        self.assertEqual(tc.tied_entries(self.RUNS, "a")["b1"], ("F", ["sync-01", "sync-02"]))

    def test_a_defect_whose_majority_is_none_is_left_out(self):
        self.assertNotIn("b2", tc.tied_entries(self.RUNS, "a"))

    def test_another_plan_with_the_same_defect_id_is_not_mixed_in(self):
        self.assertEqual(tc.tied_entries(self.RUNS, "z")["b1"], ("F", ["time-01"]))


class Measure(unittest.TestCase):
    TIED = {"b1": ("F", ["sync-01", "sync-02"]), "b2": ("F", ["time-01"]), "b3": ("P", ["time-01"])}

    def test_a_defect_is_kept_when_any_of_its_entries_is_kept(self):
        result = tc.measure(triage(sync_02=True), self.TIED)
        self.assertEqual(result["full"], {"defects": 2, "kept": 1, "lost": ["b2"]})

    def test_part_defects_are_counted_apart_from_full_ones(self):
        self.assertEqual(tc.measure(triage(sync_02=True), self.TIED)["part"], {"defects": 1, "kept": 0, "lost": ["b3"]})

    def test_the_size_is_the_entries_kept_and_the_things_they_apply_to(self):
        rows = triage(sync_01=True, time_01=True)
        rows[0]["applies_to"] = ["the pull", "the first pull"]
        result = tc.measure(rows, self.TIED)
        self.assertEqual((result["entries_kept"], result["things_to_answer_for"]), (2, 3))


if __name__ == "__main__":
    unittest.main()
