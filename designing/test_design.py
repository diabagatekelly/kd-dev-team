"""The design's script: what has no home, what is refused, the drawing and its mark. No model."""
import io
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # found beside this file under -I
import design  # noqa: E402

SLICE = """# Slice 1: Renew a season ticket and pay for it

## Criteria
- **renew-and-pay / 1**: Given Ada Reyes holds a season ticket, when she renews it and pays by card, then she is shown that her renewal is recorded.
- **refund-a-renewal / 1**: Given a renewal that was paid for, when the office refunds it, then the subscriber is shown as refunded.

## Needs from outside
- Taking a card payment.
"""
APPROACH = """# Approach: slice 1

## Committed to
- PayRight: https://docs.payright.example/, for taking a card payment.
"""
PAYRIGHT = """# Research: PayRight

## What the slice needs from it
- F1: A payment is taken with one request. "To take a payment, send POST /v1/payments" (https://docs.payright.example/payments)
- F6: The same reference within a day takes no second payment. "Sending the same reference again within 24 hours returns the first payment" (https://docs.payright.example/payments)

## Open
- O1: What has happened when a request to take a payment gets no reply. Test: cut the connection.
"""
STATES = """# States

## A renewal payment

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `pending` | a payment is taken | wait | by itself | "x" |
| `lost` | the dispute is lost | nothing | none | "y" |
"""
KEPT = """# Kept: slice 1

## What the slice creates and keeps
- A renewal payment: renew-and-pay / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `secret-key` | other | the account | credentials | payright.md F11 |
| `payment-id` | identifier | the reply | no | payright.md F2 |
"""
QUESTIONS = """# Questions

- L.call-external-01.payment-request: what if it gets no reply?
- L.concurrency-01.renewal-payment: what if two change it at once?
- L.secrets-01.secret-key: where is it kept?
- L.text-01.screen: how is text compared?
- C.payright.O1: what has happened when a request gets no reply?
- W.target: how fast?
"""
ANSWERS = """# Answers: slice 1

## A1: A repeated request
Kind: chosen
Says: Every payment request carries a reference of the product's own, so that a repeat takes no second payment.
Rests on: payright F6: "Sending the same reference again within 24 hours returns the first payment"
Settles: L.call-external-01.payment-request
Under: renew-and-pay
Criterion: Given a renewal whose payment request was sent, when it is sent again within 24 hours, then one payment is shown.

## A2: Two changes at once
Kind: chosen
Says: Of two changes to one renewal payment the second is refused and told to look again.
Rests on: a change made on a stale reading would undo the first.
Settles: L.concurrency-01.renewal-payment

## A3: The secret key
Kind: chosen
Says: The key is read from where the product runs and is in no record.
Rests on: good practice.
Settles: L.secrets-01.secret-key

## A4: Text
Kind: not here
Says: The slice compares no text.
Settles: L.text-01.screen

## A5: No reply
Kind: test
Says: No page read says what has happened when a request gets no reply.
Test: cut the connection after sending.
Harm: high
Settles: C.payright.O1

## A6: How fast
Kind: owner
Says: How fast a renewal must be answered.
Options: no target | within 5 seconds
Recommended: no target, for a first slice.
If left: nothing is measured.
Harm: low
Decided: no target (the user, 2026-11-20: "no target for now")
Settles: W.target
"""
OPEN = """# Open facts: slice 1

## T1: No reply
Answer: A5
How: person
Either way: a renewal whose request got no reply is shown as not yet known, and asked for again by its reference.
Result: open

## The owner's list, read
"""
DESIGN = """# Design: slice 1

## Importance
1. A renewal and its payment: a defect takes money twice or loses a renewal.
2. The card payment provider's edge: a defect there is seen and can be tried again.

## C1: Renewal
Side: strategic
Does: Records a renewal and asks for its payment once; refuses the second of two changes.
Home of: renew-and-pay / 1, refund-a-renewal / 1, A1, A2, A6, T1
Holds: a renewal payment: pending
Uses: B1

## C2: Card payments
Side: tactical
Does: Sends a payment request to PayRight and turns its reply into the product's own words.
Home of: A3
Sees: credentials
Implements: B1
Isolates: PayRight
Leans on: payright F1 "To take a payment, send POST /v1/payments"; T1

## B1: Taking and giving back a payment
Owned by: C1
Crosses: an amount, a reference of the product's own, and back one of taken, refused, not yet known.
Needs: a request that can be repeated without taking money twice.
Technology: forced: the slice exists to take a card payment through the provider the problem fixes.

## D1: Changes to one renewal payment are made one at a time
Kind: chosen
Says: Each change names the state it read, and is refused when the state has moved.
Instead of: a lock held across the call to the provider, which a crash would leave held.
Because: nothing is held, so nothing is left behind.
Costs: the refused change must be asked for again.
Architectural: yes: it shapes how every later change is written.
Significant: yes: every slice that changes a payment follows it.
Non-obvious: yes: a lock is the usual answer.
Keeps apart: a refund by the office and an event that changes the same payment.
Two at once: both read pending; the first writes, the second is refused on the moved state and told to look again.
Crash: after the read and before the write nothing was changed; the next reading is true.
Stopped while waiting: nothing waits; a stop between read and write changes nothing.
Leftover: there is no marker to leave or remove.
Reused name: nothing names an owner.

## At once
D1 keeps a refund and an event apart.

## Tests
Real: the store under a temporary folder, and the renewal behind its real entry.
Faked: PayRight at its wire, and the clock.

## Kept for later slices
The provider's payment id and the state of each renewal payment: slice 2 reads them.

## No home
- renewal-payment.lost: a dispute is not in this slice; the state is shown as it arrives and nothing acts on it.
"""


class Slice(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self._reader = os.environ.get("KD_READER")
        os.environ["KD_READER"] = "kd-no-such-reader"   # no second reader on this machine: the open facts say so and are drawn
        self.addCleanup(lambda: os.environ.pop("KD_READER") if self._reader is None else os.environ.__setitem__("KD_READER", self._reader))
        self.planning = pathlib.Path(self._tmp.name).resolve() / "planning"
        self.folder = self.planning / "slice-001"
        self.lay({"003_slices.md": "# Slices\n\n| # | Slice | Items | Builds on | State |\n|---|---|---|---|---|\n| 1 | Renew | renew-and-pay | nothing | chosen |\n"
                                   "| 2 | See what is not renewed | see | 1 | open |\n",
                  "slice-001/004_slice.md": SLICE, "slice-001/005_approach.md": APPROACH, "slice-001/006_research/payright.md": PAYRIGHT,
                  "slice-001/006_research/states.md": STATES, "slice-001/007_questions/kept.md": KEPT, "slice-001/007_questions/questions.md": QUESTIONS,
                  "slice-001/008_answers.md": ANSWERS, "slice-001/009_open-facts.md": OPEN})
        said = io.StringIO()
        assert design.openfacts.main(["draw", str(self.folder)], said) == 0, said.getvalue()

    def lay(self, files):
        for name, text in files.items():
            path = self.planning / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")

    def run_(self, command, text=DESIGN):
        if text is not None:
            self.lay({"slice-001/010_design.md": text})
        said = io.StringIO()
        code = design.main([command, str(self.folder)], said)
        return code, said.getvalue()


class Next(Slice):
    def test_before_anything_is_written_everything_settled_is_listed(self):
        code, said = self.run_("next", None)
        self.assertEqual(code, 0)
        self.assertIn("0 of 9 things settled before have their home; 9 are left", said)
        for each in ("- renew-and-pay / 1: a criterion of the slice", "- A1: chosen: Every payment request", "- A6: decided by the owner: no target",
                     "- T1: an open fact (high): No page read says", "Either way: a renewal whose request got no reply", "- renewal-payment.lost: a state of A renewal payment",
                     "credentials (secret-key)", "Committed to, each isolated by one tactical part: PayRight",
                     "Answers that settle questions about two things at once: A2", "Slices that build on this one: 2: See what is not renewed"):
            self.assertIn(each, said)
        self.assertNotIn("- A4", said)   # dismissed: it needs no home
        self.assertNotIn("- A5", said)   # the test is named by its block

    def test_a_test_with_no_block_is_named_by_its_answer(self):
        (self.folder / "009_open-facts.md").unlink()
        (self.folder / "009_tested.md").unlink()
        self.assertIn("- A5: an open fact (high)", self.run_("next", None)[1])

    def test_what_is_left_is_given_so_many_at_a_time(self):
        said = io.StringIO()
        design.main(["next", str(self.folder), "2"], said)
        self.assertIn("and 7 more: give these their homes, then ask again.", said.getvalue())


class Draw(Slice):
    def test_a_design_that_holds_is_drawn(self):
        code, said = self.run_("draw")
        self.assertEqual(code, 0, said)
        self.assertIn("2 parts (1 strategic, 1 tactical), 1 boundaries; 8 things settled before have their home, 1 have none in this slice; "
                      "1 decisions, 1 earn a record; 0 things leaned on and not known; 0 decisions wait for the owner; 0 go back", said)
        drawn = (self.folder / "010_designed.md").read_text(encoding="utf-8")
        for each in ("## Strategic", "### C1: Renewal", "- **renew-and-pay / 1**: Given Ada Reyes", "- **A1**: Given a renewal whose payment request was sent",
                     "- A2, chosen: Of two changes", "- T1, an open fact (high)", "## Decisions that earn a record", "### D1: Changes to one renewal payment",
                     "- Two at once: both read pending", "- renewal-payment.lost: a dispute is not in this slice", "## Kept for later slices"):
            self.assertIn(each, drawn)
        self.assertEqual(design.state(self.folder), "drawn, 0 waiting, 0 back")

    def test_its_mark_is_the_one_the_systems_cksum_gives(self):
        self.run_("draw")
        together = b"".join((self.folder / name).read_bytes() for name in ("008_answered.md", "009_tested.md", "010_design.md"))
        try:
            printed = subprocess.run(["cksum"], input=together, capture_output=True, check=True).stdout.split()[0].decode()
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("no cksum on this machine")
        self.assertIn(f"drawn from: {printed};", (self.folder / "010_designed.md").read_text(encoding="utf-8"))

    def test_a_change_to_the_answers_makes_it_stale(self):
        self.run_("draw")
        self.lay({"slice-001/008_answers.md": ANSWERS.replace("no target for now", "no target yet")})
        design.openfacts.main(["draw", str(self.folder)], io.StringIO())
        self.assertTrue(design.state(self.folder).startswith("stale"))

    def test_skipped_at_the_users_word(self):
        code, said = self.run_("draw", 'Skipped at the user\'s word, 2026-11-28: "just build it"\n')
        self.assertEqual(code, 0)
        self.assertIn("skipped at the user's word: none of the 9 things settled before has a home", said)
        self.assertEqual(design.state(self.folder), "drawn, 0 waiting, 0 back")

    def test_a_folder_that_cannot_be_written_is_said(self):
        self.lay({"slice-001/010_design.md": DESIGN})
        (self.folder / "010_designed.md").mkdir()
        said = io.StringIO()
        self.assertEqual(design.main(["draw", str(self.folder)], said), 0)
        self.assertIn("drawn, and not written", said.getvalue())


class Refused(Slice):
    def refused(self, text, *words):
        code, said = self.run_("draw", text)
        self.assertEqual(code, 1, said)
        for each in words:
            self.assertIn(each, said)
        self.assertFalse((self.folder / "010_designed.md").exists())

    def test_something_settled_with_no_home(self):
        self.refused(DESIGN.replace(", A6, T1", ""), "2 things settled before have no home (T1, A6)")

    def test_a_state_with_no_home(self):
        self.refused(DESIGN.replace("Holds: a renewal payment: pending\n", ""), "1 things settled before have no home (renewal-payment.pending)")

    def test_a_home_given_to_nothing_the_slice_has(self):
        self.refused(DESIGN.replace("A1, A2", "A1, A2, A77"), "'A77' is given a home and is nothing the slice has")

    def test_no_home_without_a_reason(self):
        self.refused(DESIGN.replace("- renewal-payment.lost: a dispute is not in this slice; the state is shown as it arrives and nothing acts on it.", "- renewal-payment.lost:"),
                     "renewal-payment.lost is under `## No home` with no reason")

    def test_a_range_of_answers_is_spread_out(self):
        self.assertEqual(self.run_("draw", DESIGN.replace("A1, A2, A6", "A1-A2, A6"))[0], 0)

    def test_a_strategic_part_that_names_the_provider(self):
        self.refused(DESIGN.replace("asks for its payment once", "asks PayRight for its payment once"), "C1 (line 7): a strategic part names PayRight")

    def test_a_strategic_part_that_uses_a_tactical_one(self):
        self.refused(DESIGN.replace("Uses: B1", "Uses: C2"), "a strategic part uses C2, a tactical one")

    def test_a_boundary_owned_by_the_side_behind_it(self):
        self.refused(DESIGN.replace("Owned by: C1", "Owned by: C2"), "B1 is owned by C2, which is not strategic", "C2 both owns it and implements it")

    def test_what_crosses_names_the_provider(self):
        self.refused(DESIGN.replace("Crosses: an amount", "Crosses: a PayRight payment object, an amount"), "what crosses names PayRight")

    def test_a_part_named_for_its_technical_role(self):
        self.refused(DESIGN.replace("## C1: Renewal", "## C1: Renewal service"), "'Renewal service' is named for a technical role (service)")

    def test_wiring_may_keep_its_name(self):
        more = "\n## C3: Start-up handler\nSide: wiring\nDoes: Makes each part and hands it what it uses.\nUses: C1, C2\n"
        self.assertEqual(self.run_("draw", DESIGN.replace("\n## B1:", more + "\n## B1:"))[0], 0)

    def test_nothing_isolates_what_is_committed_to(self):
        self.refused(DESIGN.replace("Isolates: PayRight\n", ""), "PayRight is committed to and no part isolates it")

    def test_speaking_of_the_provider_with_nothing_leaned_on(self):
        self.refused(DESIGN.replace('Leans on: payright F1 "To take a payment, send POST /v1/payments"; T1\n', ""), "C2 (line 14): it speaks of PayRight: `Leans on`")

    def test_a_fact_leaned_on_with_words_its_document_does_not_have(self):
        self.refused(DESIGN.replace("To take a payment, send POST /v1/payments", "Payments are always taken at once"), '"payments are always taken at once" is not in the research document')

    def test_a_fact_its_document_does_not_have(self):
        self.refused(DESIGN.replace("payright F1 ", "payright F9 "), "payright has no F9")

    def test_an_open_point_leaned_on_as_a_fact(self):
        self.refused(DESIGN.replace('payright F1 "To take a payment, send POST /v1/payments"', 'payright O1 "What has happened when a request to take a payment gets no reply"'),
                     "payright O1 is an open point of the research")

    def test_a_test_leaned_on_that_is_not_open(self):
        self.refused(DESIGN.replace("; T1\n", "; T7\n"), "leans on T7, which is no open test of the slice")

    def test_what_is_not_known_says_what_is_done_either_way(self):
        unknown = DESIGN.replace("; T1\n", "; unknown: whether an event can arrive before the reply\n")
        self.refused(unknown, "what is leaned on and not known says `Either way:`")
        code, said = self.run_("draw", unknown.replace("Isolates: PayRight\n", "Isolates: PayRight\nEither way: an event for a payment not yet recorded is kept and applied once it is.\n"))
        self.assertEqual(code, 0, said)
        self.assertIn("1 things leaned on and not known", said)
        self.assertIn("- C2: whether an event can arrive before the reply Either way: an event for a payment", (self.folder / "010_designed.md").read_text(encoding="utf-8"))

    def test_a_chosen_decision_says_what_was_not_taken_and_what_it_costs(self):
        self.refused(DESIGN.replace("Costs: the refused change must be asked for again.\n", "").replace("Instead of: a lock held across the call to the provider, which a crash would leave held.\n", ""),
                     "a decision that is chosen says its `Instead of`", "a decision that is chosen says its `Costs`")

    def test_the_three_checks_are_yes_or_no(self):
        self.refused(DESIGN.replace("Significant: yes:", "Significant: borderline:"), "Significant is yes or no, then why")

    def test_a_decision_with_a_no_earns_no_record(self):
        code, said = self.run_("draw", DESIGN.replace("Non-obvious: yes: a lock is the usual answer.", "Non-obvious: no: nobody would expect otherwise."))
        self.assertEqual(code, 0, said)
        self.assertIn("1 decisions, 0 earn a record", said)

    def test_what_keeps_two_things_apart_is_walked_through_every_order(self):
        self.refused(DESIGN.replace("Reused name: nothing names an owner.\n", "").replace("Crash: after the read and before the write nothing was changed; the next reading is true.\n", ""),
                     "`Crash:` says what state is left and who would notice", "`Reused name:` says what state is left")

    def test_a_hole_is_closed_or_is_the_owners(self):
        hole = DESIGN.replace("Leftover: there is no marker to leave or remove.", "Leftover: a marker left by a crash keeps every refund stuck until someone removes it.")
        self.refused(hole, "`Leftover` leaves a hole")
        owners = (hole.replace("Kind: chosen", "Kind: owner").replace("Instead of:", "Options: accept it | a marker that names its holder\nRecommended: a marker that names its holder.\n"
                                                                      "If left: refunds can stop after a crash.\nHarm: high\nInstead of:"))
        code, said = self.run_("draw", owners)
        self.assertEqual(code, 0, said)
        self.assertIn("1 decisions wait for the owner", said)
        self.assertEqual(design.state(self.folder), "drawn, 1 waiting, 0 back")
        decided = owners.replace("Harm: high\n", 'Harm: high\nDecided: a marker that names its holder (the user, 2026-11-28: "take yours")\n')
        self.assertIn("0 decisions wait for the owner", self.run_("draw", decided)[1])

    def test_a_decision_marked_decided_without_the_users_words(self):
        self.refused(DESIGN.replace("Kind: chosen", "Kind: owner\nOptions: a | b\nRecommended: a\nIf left: b\nHarm: low\nDecided: a"), "Decided ends with who said it")

    def test_two_things_at_once_answered_and_nothing_kept_apart(self):
        text = DESIGN.split("## D1:")[0] + "## At once\nNothing: one person uses it.\n\n## Tests" + DESIGN.split("## Tests")[1]
        self.refused(text, "1 answers settle questions about two things at once (A2) and no decision keeps anything apart")

    def test_no_word_on_whether_anything_runs_at_once(self):
        self.refused(DESIGN.replace("## At once\nD1 keeps a refund and an event apart.\n", ""), "`## At once` says whether two things can run over the same state")

    def test_the_tests_fake_what_is_committed_to(self):
        self.refused(DESIGN.replace("Faked: PayRight at its wire, and the clock.", "Faked: the clock."), "`## Tests` does not say PayRight is faked")

    def test_nothing_said_of_later_slices(self):
        self.refused(DESIGN.replace("## Kept for later slices\nThe provider's payment id and the state of each renewal payment: slice 2 reads them.\n", ""), "`## Kept for later slices` names")

    def test_no_order_of_importance(self):
        self.refused(DESIGN.replace("2. The card payment provider's edge: a defect there is seen and can be tried again.\n", ""), "`## Importance` orders the parts")

    def test_a_class_of_sensitive_values_no_part_sees(self):
        self.refused(DESIGN.replace("Sees: credentials\n", ""), "no part `Sees: credentials` (secret-key)")

    def test_code_is_not_design(self):
        self.refused(DESIGN.replace("Does: Records a renewal", "Does: In src/renewal.ts, calls takePayment(amount) and records a renewal"), "no code, no file of the code, no signature")

    def test_code_that_is_already_there_is_named_as_it_is(self):
        self.assertEqual(self.run_("draw", DESIGN + "\n## Already there\n- app/subscribers.py keeps the season tickets: used as it is.\n")[0], 0)

    def test_what_goes_back_keeps_the_design_open(self):
        code, said = self.run_("draw", DESIGN + "\n## Goes back\n- approach: telling a subscriber by email needs a way to send one, which the approach does not have.\n")
        self.assertEqual(code, 0, said)
        self.assertIn("1 go back to an earlier stage", said)
        self.assertEqual(design.state(self.folder), "drawn, 0 waiting, 1 back")
        (self.folder / "010_designed.md").unlink()
        self.refused(DESIGN + "\n## Goes back\n- the builder: decide the store.\n", "`## Goes back` names the stage whose it is")


class Command(Slice):
    def test_run_as_a_command(self):
        self.lay({"slice-001/010_design.md": DESIGN})
        script = pathlib.Path(design.__file__)
        done = subprocess.run([sys.executable, "-I", str(script), "draw", str(self.folder)], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn("drawn: ", done.stdout)
        self.assertEqual(subprocess.run([sys.executable, "-I", str(script), "state", str(self.folder)], capture_output=True, text=True).stdout.strip(), "drawn, 0 waiting, 0 back")
        self.assertEqual(subprocess.run([sys.executable, "-I", str(script)], capture_output=True, text=True).returncode, 2)

    def test_nothing_to_design_from(self):
        (self.folder / "008_answers.md").unlink()
        said = io.StringIO()
        self.assertEqual(design.main(["next", str(self.folder)], said), 1)
        self.assertIn("nothing to design from yet", said.getvalue())


if __name__ == "__main__":
    unittest.main()
