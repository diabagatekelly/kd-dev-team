import unittest

import library_check as lc


def entry(action="sync", number="01", **changes):
    made = {
        "id": f"{action}-{number}", "action": action,
        "failure": "The same change arrives twice.",
        "question": "What does the product do with a change it has already applied?",
        "source": {"title": "A page", "url": "https://example.org/a", "evidence": "duplicates are delivered"},
    }
    made.update(changes)
    return made


def full_library():
    """Every action at the fewest entries allowed, numbered from 50 so tests can add low numbers."""
    return [entry(action=a, number=f"{n}") for a in lc.ACTIONS for n in range(50, 50 + lc.MIN_PER_ACTION)]


class Problems(unittest.TestCase):
    def test_a_library_with_every_action_has_no_problems(self):
        self.assertEqual(lc.problems(full_library()), [])

    def test_an_action_with_no_entries_is_named(self):
        library = [e for e in full_library() if e["action"] != "time"]
        self.assertEqual(lc.problems(library), ["time: no entries"])

    def test_an_action_with_too_few_entries_is_named(self):
        library = [e for e in full_library() if not (e["action"] == "time" and e["id"] > "time-52")]
        self.assertEqual(lc.problems(library), ["time: 3 entries, at least 8 are asked for"])

    def test_a_field_that_is_not_text_is_named_and_does_not_crash(self):
        self.assertIn("sync-02: every field must be text",
                      lc.problems(full_library() + [entry(number="02", failure=7)]))

    def test_a_missing_field_is_refused(self):
        broken = entry()
        del broken["question"]
        self.assertIn("sync-01: fields must be exactly", "\n".join(lc.problems(full_library() + [broken])))

    def test_an_unknown_action_is_refused(self):
        self.assertIn("payments-01: unknown action 'payments'",
                      lc.problems(full_library() + [entry(action="payments")]))

    def test_an_id_that_does_not_match_its_action_is_refused(self):
        self.assertIn("text-01: id must be <action>-<two digits>",
                      lc.problems(full_library() + [entry(id="text-01", action="sync")]))

    def test_an_id_used_twice_is_refused(self):
        self.assertIn("sync-50: id used twice", lc.problems(full_library() + [entry(number="50")]))

    def test_a_word_of_one_field_of_business_is_refused_in_the_entry_text(self):
        found = lc.problems(full_library() + [entry(number="02", failure="The bank sends it twice.")])
        self.assertEqual(found, ["sync-02: failure uses the word 'bank'"])

    def test_the_same_word_in_a_source_title_is_allowed(self):
        source = {"title": "SQLite and HTTP notes", "url": "https://example.org/b", "evidence": "x"}
        self.assertEqual(lc.problems(full_library() + [entry(number="02", source=source)]), [])

    def test_a_source_that_is_not_https_is_refused(self):
        source = {"title": "A", "url": "http://example.org", "evidence": "x"}
        self.assertEqual(lc.problems(full_library() + [entry(number="02", source=source)]),
                         ["sync-02: source url must be https"])

    def test_evidence_over_the_word_limit_is_refused(self):
        source = {"title": "A", "url": "https://example.org", "evidence": " ".join(["w"] * 21)}
        self.assertEqual(lc.problems(full_library() + [entry(number="02", source=source)]),
                         ["sync-02: evidence is over 20 words"])

    def test_more_than_the_limit_for_one_action_is_refused(self):
        extra = [entry(number=f"{n:02d}") for n in range(2, 7)]
        self.assertEqual(lc.problems(full_library() + extra), ["sync: 13 entries, the limit is 12"])


if __name__ == "__main__":
    unittest.main()
