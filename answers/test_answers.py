"""Every branch of the answers script: what is left, what is refused, what is drawn."""
import io
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # found beside this file under -I
import answers  # noqa: E402

SLICE = """# Slice 1

- **renew-and-pay / 1**: Given a subscriber, when she renews, then she is shown the result.
- **refund-a-renewal / 1**: Given a renewal, when the office refunds it, then the money goes back.
"""
QUESTIONS = """# Questions

<!-- drawn from: 1 -->

- L.call-external-05.payment-request: What bounds a call that gets no reply?
- L.call-external-05.refund-request: What bounds a call that gets no reply?
- V.card-token.missing: What happens when `card-token` is missing?
- X.credentials.logs: can `secret-key` reach what the product logs?
- F.network.transport: Is every connection to it encrypted?
- W.who-sees: Who uses it, and may any of them see what belongs to another?
"""
FACT = """## A1: Calls are bounded
Kind: fact
Says: A payment request is refused after 30 seconds.
Rests on: payright F3
Settles: L.call-external-05.*
Under: renew-and-pay
Criterion: Given PayRight does not reply, when 30 seconds have passed, then she is shown that nothing was taken.
"""
REST = """
## A2: A missing token
Kind: chosen
Says: A renewal with no token is refused before anything is sent.
Rests on: nothing can be charged without it.
Settles: V.card-token.missing

## A3: Who may refund
Kind: owner
Says: The documents do not say who in the office may refund.
Options: anyone in the office | one named person
Recommended: one named person, because a refund moves money.
If left: nobody can refund.
Harm: high
Settles: W.who-sees

## A4: The key in records
Kind: test
Says: Whether PayRight's library writes the key on a failure is not said on its pages.
Test: a failed call in PayRight's test mode, and the records read after.
Harm: medium
Settles: X.credentials.logs

## A5: Transport
Kind: not here
Says: The slice answers at no address of its own; PayRight's is its own.
Settles: F.network.transport
"""


class Folder(unittest.TestCase):
    def setUp(self):
        self.top = pathlib.Path(tempfile.mkdtemp()).resolve()
        self.slice = self.top / "planning" / "slice-001"
        (self.slice / "006_research").mkdir(parents=True)
        (self.slice / "007_questions").mkdir()
        (self.slice / "004_slice.md").write_text(SLICE)
        (self.slice / "006_research" / "payright.md").write_text("# PayRight\n")
        (self.slice / "007_questions" / "questions.md").write_text(QUESTIONS)
        (self.top / "planning" / "002_requirements.md").write_text("# Requirements\n")

    def write(self, text):
        (self.slice / "008_answers.md").write_text("# Answers: slice 1\n\n" + text)

    def run_it(self, *arguments):
        out = io.StringIO()
        code = answers.main([arguments[0], str(self.slice), *arguments[1:]], out)
        return code, out.getvalue()

    def refused(self, text):
        self.write(text)
        code, said = self.run_it("draw")
        self.assertEqual(code, 1, said)
        return said


class Next(Folder):
    def test_with_no_answers_every_question_is_left_in_the_drawings_order(self):
        code, said = self.run_it("next")
        self.assertEqual(code, 0)
        self.assertIn("0 of 6 questions are settled by 0 answers; 6 are left.", said)
        self.assertLess(said.index("L.call-external-05.payment-request"), said.index("W.who-sees"))

    def test_an_answer_takes_its_questions_off_the_list_and_a_star_takes_every_thing_of_an_entry(self):
        self.write(FACT)
        _code, said = self.run_it("next")
        self.assertIn("2 of 6 questions are settled by 1 answers; 4 are left.", said)
        self.assertNotIn("- L.call-external-05", said)

    def test_only_as_many_as_asked_for_are_listed_and_the_rest_are_counted(self):
        _code, said = self.run_it("next", "2")
        self.assertIn("and 4 more", said)
        self.assertNotIn("- X.credentials.logs", said)

    def test_what_does_not_hold_so_far_is_said_with_what_is_left(self):
        self.write(FACT.replace("Kind: fact", "Kind: belief"))
        _code, said = self.run_it("next")
        self.assertIn("Not holding in the answers as written", said)
        self.assertIn("Kind is one of", said)

    def test_with_no_questions_drawn_there_is_nothing_to_answer(self):
        (self.slice / "007_questions" / "questions.md").unlink()
        code, said = self.run_it("next")
        self.assertEqual(code, 1)
        self.assertIn("nothing to answer yet", said)


class Refused(Folder):
    def test_no_answers_file(self):
        code, said = self.run_it("draw")
        self.assertEqual(code, 1)
        self.assertIn("no answers yet", said)

    def test_questions_no_answer_settles(self):
        self.assertIn("4 questions are settled by no answer (the first: V.card-token.missing", self.refused(FACT))

    def test_a_question_the_drawing_does_not_ask(self):
        self.assertIn("settles what the drawing does not ask: L.made-up.thing", self.refused(FACT.replace("L.call-external-05.*", "L.made-up.thing")))

    def test_a_star_that_matches_nothing(self):
        self.assertIn("does not ask: L.made-up.*", self.refused(FACT.replace("L.call-external-05.*", "L.made-up.*")))

    def test_an_answer_that_settles_nothing(self):
        self.assertIn("settles no question", self.refused(FACT.replace("Settles: L.call-external-05.*", "")))

    def test_a_question_settled_twice(self):
        again = FACT.replace("## A1", "## A9").replace("L.call-external-05.*", "L.call-external-05.refund-request")
        self.assertIn("L.call-external-05.refund-request is already settled by A1", self.refused(FACT + REST + again))

    def test_a_name_used_twice(self):
        self.assertIn("this name is used twice", self.refused(FACT + REST + REST))

    def test_a_kind_that_is_none_of_the_five(self):
        self.assertIn("it says 'guess'", self.refused(FACT.replace("Kind: fact", "Kind: guess")))

    def test_a_field_its_kind_needs(self):
        self.assertIn("a fact answer says its `Rests on`", self.refused(FACT.replace("Rests on: payright F3\n", "")))
        self.assertIn("a owner answer says its `If left`", self.refused(FACT + REST.replace("If left: nobody can refund.\n", "")))
        self.assertIn("a test answer says its `Test`", self.refused(FACT + REST.replace("Test: a failed call in PayRight's test mode, and the records read after.\n", "")))

    def test_a_fact_that_rests_on_no_document(self):
        self.assertIn("a fact rests on a document of the slice", self.refused(FACT.replace("payright F3", "what providers usually do")))

    def test_a_research_fact_named_with_no_document_of_the_slice(self):
        said = self.refused(FACT.replace("payright F3", "provider F3, and 004_slice.md"))
        self.assertIn("'provider' is no research document of the slice (payright)", said)

    def test_a_research_fact_may_be_named_in_several_ways(self):
        for source in ("payright.md F3", "payright F3 and F4", "PayRight, F3", "payright fact F3"):
            self.write(FACT.replace("payright F3", source) + REST)
            self.assertEqual(self.run_it("draw")[0], 0, source)

    def test_a_fact_may_rest_on_a_criterion_or_a_planning_document(self):
        for source in ("renew-and-pay / 1", "002_requirements.md, Limits", "requirements.md"):
            self.write(FACT.replace("payright F3", source) + REST)
            self.assertEqual(self.run_it("draw")[0], 0, source)

    def test_a_harm_that_is_none_of_the_three(self):
        self.assertIn("Harm is one of high, medium, low", self.refused(FACT + REST.replace("Harm: high", "Harm: serious")))

    def test_a_decision_for_the_owner_with_one_option(self):
        self.assertIn("at least two options", self.refused(FACT + REST.replace("anyone in the office | one named person", "one named person")))

    def test_a_criterion_from_a_decision_not_yet_taken(self):
        said = self.refused(FACT + REST.replace("Harm: high\n", "Harm: high\nUnder: refund-a-renewal\nCriterion: Given a refund, when anyone asks, then it is made.\n"))
        self.assertIn("from a owner answer it waits", said)

    def test_a_decision_the_owner_has_taken_carries_its_criterion_and_leaves_their_list(self):
        decided = REST.replace("Harm: high\n", "Harm: high\nDecided: one named person (the user, 2026-11-25: \"Only Ana refunds.\")\n"
                               "Under: refund-a-renewal\nCriterion: Given a refund, when anyone but the named person asks, then it is refused.\n")
        self.write(FACT + decided)
        code, said = self.run_it("draw")
        self.assertEqual(code, 0, said)
        self.assertIn("0 for the owner, 1 decided by the owner", said)
        text = (self.slice / "008_answered.md").read_text()
        self.assertIn('- A3: Who may refund: one named person (the user, 2026-11-25: "Only Ana refunds.")', text)
        self.assertNotIn("### A3", text)
        self.assertIn("- **refund-a-renewal / A3.2**", text)

    def test_decided_without_their_words_or_on_another_kind_is_refused(self):
        self.assertIn("Decided ends with who said it", self.refused(FACT + REST.replace("Harm: high\n", "Harm: high\nDecided: one named person\n")))
        self.assertIn("only a decision for the owner is `Decided:`", self.refused(FACT.replace("Kind: fact", 'Kind: fact\nDecided: yes (the user, 2026-11-25: "ok")')))

    def test_skipped_at_the_users_word_draws_that_nothing_is_answered(self):
        (self.slice / "008_answers.md").write_text('Skipped at the user\'s word, 2026-11-25: "Skip the answers."\n')
        code, said = self.run_it("draw")
        self.assertEqual(code, 0, said)
        self.assertIn("skipped at the user's word: none of the 6 questions is answered", said)
        self.assertIn("a risk accepted, for the owner's list", (self.slice / "008_answered.md").read_text())
        self.assertEqual(self.run_it("state")[1].strip(), "drawn")

    def test_a_criterion_under_no_item_or_an_item_the_slice_does_not_have(self):
        self.assertIn("says which item of the slice it is under", self.refused(FACT.replace("Under: renew-and-pay\n", "")))
        self.assertIn("Under names an item of the slice (refund-a-renewal, renew-and-pay)", self.refused(FACT.replace("Under: renew-and-pay", "Under: pay-later")))

    def test_a_criterion_may_be_under_a_new_item(self):
        self.write(FACT.replace("Under: renew-and-pay", "Under: new: bounded-calls") + REST)
        self.assertEqual(self.run_it("draw")[0], 0)

    def test_a_criterion_that_is_not_given_when_then(self):
        self.assertIn("one Given, when, then", self.refused(FACT.replace("Criterion: Given PayRight does not reply, when 30 seconds have passed, then", "Criterion: After a while")))

    def test_a_wait_with_no_number(self):
        said = self.refused(FACT.replace("when 30 seconds have passed", "when it times out"))
        self.assertIn("has its number", said)

    def test_a_wait_the_owner_left_unbounded_is_not_refused(self):
        self.write(FACT.replace("when 30 seconds have passed", "when it retries (unbounded, owner approved)") + REST)
        self.assertEqual(self.run_it("draw")[0], 0)

    def test_words_that_belong_to_no_field(self):
        self.assertIn("words that belong to no field (line 7)", self.refused(FACT.replace("Rests on: payright F3", "Rests on: payright F3\nand some more")))


class Drawn(Folder):
    def setUp(self):
        super().setUp()
        self.write(FACT + REST)

    def test_the_drawing_is_written_beside_the_answers_and_counted(self):
        code, said = self.run_it("draw")
        self.assertEqual(code, 0, said)
        self.assertIn("008_answered.md: 5 answers settle 6 questions: 1 facts, 1 chosen, 1 for the owner, 0 decided by the owner, 1 to test, 1 not here; 1 criteria", said)
        text = (self.slice / "008_answered.md").read_text()
        self.assertIn("- **renew-and-pay / A1.1**: Given PayRight does not reply", text)
        self.assertIn("### A3: Who may refund (high)", text)
        self.assertIn("- one named person", text)
        self.assertIn("Questions waiting on it: 1", text)
        self.assertIn("- A4 (medium): Whether PayRight's library", text)
        self.assertIn("- A2: A renewal with no token is refused before anything is sent. Because: nothing can be charged without it.", text)

    def test_the_owners_list_is_ranked_by_harm_whatever_the_order_written(self):
        low = ("\n## A7: Wording\nKind: owner\nSays: The wording of a refusal is not said.\nOptions: plain | formal\n"
               "Recommended: plain.\nIf left: plain is used.\nHarm: low\nSettles: L.call-external-05.refund-request\n")
        self.write(FACT.replace("L.call-external-05.*", "L.call-external-05.payment-request") + low + REST)
        code, said = self.run_it("draw")
        self.assertEqual(code, 0, said)
        text = (self.slice / "008_answered.md").read_text()
        self.assertLess(text.index("### A3"), text.index("### A7"))

    def test_a_value_may_go_on_to_an_indented_line(self):
        self.write(FACT.replace("Says: A payment request is refused after 30 seconds.", "Says: A payment request\n  is refused after 30 seconds.") + REST)
        self.assertEqual(self.run_it("draw")[0], 0)
        self.assertEqual(answers.one(answers.read((self.slice / "008_answers.md").read_text())[0], "Says"), "A payment request is refused after 30 seconds.")

    def test_where_the_drawing_cannot_be_written_it_is_said_and_not_failed(self):
        (self.slice / "008_answered.md").mkdir()
        code, said = self.run_it("draw")
        self.assertEqual(code, 0)
        self.assertIn("drawn, and not written", said)


class State(Folder):
    def state(self):
        return self.run_it("state")[1].strip()

    def test_none_then_written_with_its_count_then_drawn_then_stale(self):
        self.assertEqual(self.state(), "none")
        self.write(FACT)
        self.assertEqual(self.state(), "written 2 of 6")
        self.write(FACT + REST)
        self.assertEqual(self.state(), "written 6 of 6")
        self.run_it("draw")
        self.assertEqual(self.state(), "drawn")
        (self.slice / "007_questions" / "questions.md").write_text(QUESTIONS + "- T.credentials.refund-screen: someone after it?\n")
        self.assertTrue(self.state().startswith("stale"))

    def test_changed_answers_are_stale_too(self):
        self.write(FACT + REST)
        self.run_it("draw")
        self.write(FACT + REST.replace("Harm: high", "Harm: low"))
        self.assertTrue(self.state().startswith("stale"))

    def test_asked_with_no_folder_or_another_word_the_usage_is_printed(self):
        out = io.StringIO()
        self.assertEqual(answers.main(["draw"], out), 2)
        self.assertIn("Usage:", out.getvalue())


if __name__ == "__main__":
    unittest.main()
