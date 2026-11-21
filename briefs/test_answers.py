import unittest

import answers

LIBRARY = [
    {"id": "sync-01", "action": "sync", "failure": "Arrives twice.", "question": "Then what?"},
    {"id": "time-01", "action": "time", "failure": "Clock jumps.", "question": "Then what?"},
]
TRIAGE = [
    {"id": "sync-01", "relevant": True, "why": "it pulls", "applies_to": ["the first pull", "a later pull"]},
    {"id": "time-01", "relevant": False, "why": "no clock", "applies_to": []},
]


def answered(**change):
    cells = answers.make(TRIAGE, LIBRARY)
    for cell in cells:
        cell.update(kind="planner", tag="PLAN SILENT", says="Nothing is said.", source="")
    cells[0].update(change)
    return cells


class Make(unittest.TestCase):
    def test_a_kept_question_gets_a_cell_per_thing_and_a_dropped_one_none(self):
        self.assertEqual([c["cell"] for c in answers.make(TRIAGE, LIBRARY)], ["sync-01.01", "sync-01.02"])

    def test_a_cell_carries_the_question_and_the_thing_and_starts_empty(self):
        cell = answers.make(TRIAGE, LIBRARY)[1]
        self.assertEqual((cell["thing"], cell["failure"], cell["tag"], cell["kind"]),
                         ("a later pull", "Arrives twice.", "", ""))


class Split(unittest.TestCase):
    def test_a_question_is_never_cut_across_parts(self):
        parts = answers.split(answers.make(TRIAGE, LIBRARY), 2)
        self.assertEqual([len(p) for p in parts], [2])


class Problems(unittest.TestCase):
    def setUp(self):
        self.expected = answers.make(TRIAGE, LIBRARY)

    def test_cells_answered_as_handed_out_have_no_problems(self):
        self.assertEqual(answers.problems(self.expected, answered()), [])

    def test_a_dropped_cell_is_named(self):
        self.assertEqual(answers.problems(self.expected, answered()[1:]), ["sync-01.01: missing"])

    def test_a_changed_thing_is_named(self):
        self.assertEqual(answers.problems(self.expected, answered(thing="something easier")),
                         ["sync-01.01: thing was changed"])

    def test_a_kind_outside_the_three_is_named(self):
        self.assertEqual(answers.problems(self.expected, answered(kind="guess")), ["sync-01.01: kind is 'guess'"])

    def test_a_contradiction_with_no_source_is_refused(self):
        self.assertEqual(answers.problems(self.expected, answered(tag="CONTRADICTS DOCS")),
                         ["sync-01.01: leans on a dependency but gives no source"])

    def test_a_decided_fact_with_no_source_is_refused(self):
        self.assertEqual(answers.problems(self.expected, answered(kind="fact", tag="DECIDED")),
                         ["sync-01.01: leans on a dependency but gives no source"])

    def test_a_fact_marked_for_a_test_is_accepted(self):
        self.assertEqual(answers.problems(self.expected, answered(kind="fact", source="NEEDS A TEST: time a first pull")), [])

    def test_an_impossible_fact_needs_no_source(self):
        self.assertEqual(answers.problems(self.expected, answered(kind="fact", tag="IMPOSSIBLE")), [])


class Render(unittest.TestCase):
    def test_each_question_gets_a_heading_and_each_thing_a_row(self):
        text = answers.render(answered(source="F3"))
        self.assertIn("## sync-01 (sync): Arrives twice.", text)
        self.assertIn("| sync-01.01 | the first pull | PLAN SILENT | Nothing is said. | F3 |", text)


class Count(unittest.TestCase):
    def test_open_cells_are_split_by_who_must_answer(self):
        cells = answered(kind="owner")
        cells[1].update(tag="DECIDED")
        result = answers.count(cells)
        self.assertEqual((result["open"], result["open_by_kind"], result["open_questions_for_the_owner"]),
                         (1, {"owner": 1}, 1))

    def test_cells_marked_for_a_test_are_counted(self):
        self.assertEqual(answers.count(answered(kind="fact", source="NEEDS A TEST: x"))["marked_for_a_test"], 1)


if __name__ == "__main__":
    unittest.main()
