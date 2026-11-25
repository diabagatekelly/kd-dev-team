"""Unit tests for outcome.py: what a drawn questions.md reaches, counted."""
import io
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import outcome  # noqa: E402

DRAWN = """# Questions

## From the library
- L.call-external-01.payment-request: payment-request: What if the reply never arrives?
- L.call-external-01.renewal-payment: A renewal payment: What if the reply never arrives?
- L.secrets-03.payright-key: payright-key: How is it kept out?

## Each value taken in, each way it can be wrong
- V.payment-status.missing: `payment-status` is missing
"""
TIED = {"A": ("F", ["call-external-01", "sync-02"]), "B": ("F", ["sync-02"]), "C": ("P", ["secrets-03"]), "D": ("P", ["text-01"]),
        "E": ("F", ["text-02"])}


class Ties(unittest.TestCase):
    def test_the_entries_kept_are_those_with_a_line_each_once(self):
        self.assertEqual(outcome.kept(DRAWN), {"call-external-01", "secrets-03"})

    def test_a_defect_is_kept_when_one_of_its_entries_has_a_line_and_lost_when_none_has(self):
        result = outcome.ties(TIED, {}, DRAWN)
        self.assertEqual(result["full"], {"defects": 3, "kept": 1, "lost": ["B", "E"]})
        self.assertEqual(result["part"], {"defects": 2, "kept": 1, "lost": ["D"]})
        self.assertEqual((result["entries_kept"], result["lines"]), (2, 4))

    def test_a_defect_marked_as_outside_the_slice_is_not_counted(self):
        result = outcome.ties(TIED, {"E": False, "D": False}, DRAWN)
        self.assertEqual(result["full"], {"defects": 2, "kept": 1, "lost": ["B"]})
        self.assertEqual(result["part"], {"defects": 1, "kept": 1, "lost": []})


class Gaps(unittest.TestCase):
    FACTS = {"held": "three working days", "slow": "2 minutes or more", "renamed": "id changes", "limit": "LIMIT_REACHED"}
    ASKS = {"held": r"^- L\.call-external-03\.", "slow": r"^- L\.call-external-01\.[a-z-]*payment", "renamed": None, "limit": r"^- L\.limits-06\."}

    def test_only_the_facts_research_lacks_are_looked_for(self):
        found = outcome.gaps(self.FACTS, self.ASKS, "A payment takes up to three working days.", DRAWN)
        self.assertEqual(found, {"slow": "asked for", "renamed": "no general question", "limit": "not asked for"})

    def test_a_fact_the_asks_do_not_name_has_no_general_question(self):
        self.assertEqual(outcome.gaps({"new": "x"}, {}, "", DRAWN), {"new": "no general question"})


class TheCommand(unittest.TestCase):
    def setUp(self):
        self.folder = pathlib.Path(tempfile.mkdtemp())
        (self.folder / "q.md").write_text(DRAWN, encoding="utf-8")

    def test_ties_are_counted_from_the_judges_runs_for_each_file_and_across_them(self):
        for number, mark in ((1, "F"), (2, "F"), (3, "X")):
            (self.folder / f"run{number}").mkdir()
            (self.folder / f"run{number}" / "out.json").write_text(json.dumps(
                [{"plan": "p", "id": "A", "class": mark, "entries": ["call-external-01"]}, {"plan": "other", "id": "Z", "class": "F", "entries": ["x"]}]))
        (self.folder / "within.json").write_text("{}")
        (self.folder / "q2.md").write_text("- L.text-01.name: n: q\n", encoding="utf-8")
        out = io.StringIO()
        self.assertEqual(outcome.main(["ties", str(self.folder), "p", str(self.folder / "within.json"), str(self.folder / "q.md"), str(self.folder / "q2.md")], out), 0)
        result = json.loads(out.getvalue())
        self.assertEqual(result[str(self.folder / "q.md")]["full"], {"defects": 1, "kept": 1, "lost": []})
        self.assertEqual(result[str(self.folder / "q2.md")]["full"]["lost"], ["A"])
        self.assertEqual((result["kept_by_every_run"], result["kept_by_any_run"]), (0, 3))

    def test_gaps_are_printed_a_line_a_fact(self):
        (self.folder / "facts.json").write_text(json.dumps(Gaps.FACTS))
        (self.folder / "asks.json").write_text(json.dumps(Gaps.ASKS))
        (self.folder / "research").mkdir()
        (self.folder / "research" / "p.md").write_text("three working days")
        out = io.StringIO()
        self.assertEqual(outcome.main(["gaps", str(self.folder / "facts.json"), str(self.folder / "asks.json"), str(self.folder / "research"), str(self.folder / "q.md")], out), 0)
        self.assertEqual(out.getvalue().splitlines(), ["asked for            slow", "no general question  renamed", "not asked for        limit"])

    def test_a_line_is_looked_for_at_the_start_of_any_line(self):
        # Found by the pilot: the key's patterns begin at a line's start, and the facts counter reads a document as one text.
        (self.folder / "key.json").write_text(json.dumps({"status": r"^- V\.payment-status\.missing:", "date": r"^- V\.[a-z-]*date"}))
        out = io.StringIO()
        self.assertEqual(outcome.main(["lines", str(self.folder / "key.json"), str(self.folder / "q.md")], out), 0)
        self.assertEqual(out.getvalue().splitlines(), ["a line     status", "no line    date", "a line for 1 of 2"])

    def test_anything_else_prints_how_it_is_used(self):
        out = io.StringIO()
        self.assertEqual(outcome.main(["count"], out), 2)
        self.assertIn("outcome.py ties", out.getvalue())


if __name__ == "__main__":
    unittest.main()
