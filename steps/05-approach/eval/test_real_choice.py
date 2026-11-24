"""The count of an approach against a key, on a made-up key and made-up approaches."""
import unittest

import real_choice

KEY = {"sites": {"Postbox": "postbox.example", "Lettera": "lettera.example"},
       "statements": {"postbox-price": {"candidate": "Postbox", "pattern": r"£\d+ a month"},
                      "postbox-where": {"candidate": "Postbox", "pattern": r"London|data centres?"},
                      "lettera-price": {"candidate": "Lettera", "pattern": r"£\d+ a month"}}}
TABLE = """| Way | Cost | Where | Ties |
|---|---|---|---|
| Without: by hand | £0 a month | here | nothing |
| Postbox (https://docs.postbox.example/) | "The Starter plan is £12 a month" (https://docs.postbox.example/pricing) | %s | not said on the pages read |
| **Lettera** | %s | not said on the pages read | Not said on the pages read |

Recommended: Postbox, at £12 a month, kept in London.
"""


class Count(unittest.TestCase):
    def count(self, where='"stored in London" (https://docs.postbox.example/data)', lettera="about £35 a month"):
        return real_choice.count(TABLE % (where, lettera), KEY)

    def test_a_statement_quoted_from_the_candidates_own_site_is_quoted(self):
        found, _ = self.count()
        self.assertEqual((found["postbox-price"], found["postbox-where"]), ("quoted", "quoted"))

    def test_a_statement_with_no_quote_is_unquoted(self):
        self.assertEqual(self.count()[0]["lettera-price"], "unquoted")

    def test_a_quote_from_another_site_is_not_the_candidates_own(self):
        found, _ = self.count(lettera='"Lettera is £35 a month" (https://reviews.example/lettera)')
        self.assertEqual(found["lettera-price"], "unquoted")

    def test_a_statement_made_only_outside_the_table_is_absent(self):
        self.assertEqual(self.count(where="not said on the pages read")[0]["postbox-where"], "absent")

    def test_another_candidates_row_does_not_count_for_this_one(self):
        self.assertEqual(self.count(lettera="not said on the pages read")[0]["lettera-price"], "absent")

    def test_the_cells_that_say_the_pages_do_not_say_are_counted_by_candidate(self):
        self.assertEqual(self.count()[1], {"Postbox": 1, "Lettera": 2})

    def test_a_quoted_cell_wins_over_an_unquoted_one_for_the_same_statement(self):
        found, _ = real_choice.count(TABLE.replace("| %s | not said on the pages read |\n", '| %s | from £10 a month |\n') %
                                     ("stored in London", "x"), KEY)
        self.assertEqual(found["postbox-price"], "quoted")
        self.assertEqual(found["postbox-where"], "unquoted")


if __name__ == "__main__":
    unittest.main()
