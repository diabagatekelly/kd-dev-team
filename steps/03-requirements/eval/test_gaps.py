import unittest

import gaps

LIST = """# Requirements: Register a child

- [ ] **register-child**: A parent can register their child.

## Not yet confirmed
- By when must the coach have the list? It changes coach-sees-list.
- Who places a child in a team: the parent or the league?

## Outside systems and lasting things
- the secretary's ledger
"""


class Gaps(unittest.TestCase):
    def test_only_the_questions_are_read(self):
        self.assertEqual(gaps.questions(LIST).count("\n- ") + 1, 2)
        self.assertNotIn("ledger", gaps.questions(LIST))

    def test_a_gap_is_raised_when_a_question_speaks_to_it(self):
        self.assertEqual(gaps.raised("03", LIST), ["what-in-time-means", "who-places-a-child-in-a-team"])

    def test_a_word_outside_the_questions_raises_nothing(self):
        self.assertNotIn("the-secretary-sees", gaps.raised("03", LIST))

    def test_no_document_raises_nothing(self):
        self.assertEqual(gaps.raised("03", None), [])
        self.assertEqual(gaps.raised("09", LIST), [])

    def test_the_questions_are_counted(self):
        self.assertEqual(gaps.count(gaps.questions(LIST)), 2)
        self.assertEqual(gaps.count("Nothing."), 0)


if __name__ == "__main__":
    unittest.main()
