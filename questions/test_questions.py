"""Unit tests for questions.py: every branch of what is read, checked and drawn."""
import io
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # found beside this file under -I
import questions  # noqa: E402

SLICE = """# Slice 1: Renew a season ticket

## Criteria
- **renew-and-pay / 1**: Given a ticket, when she renews it and pays, then she is shown it is recorded.
- **renew-and-pay / 2**: Given her card is refused, when she pays, then she is told.

## Needs from outside
- Taking a card payment.
"""
APPROACH = """# Approach

## Taking a card payment
Decision: committed to PayRight.

## Committed to
- PayRight: https://docs.payright.example/, for taking a card payment.
"""
STATES = """# States

## A renewal payment

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `pending` | she pays | wait | by itself -> `paid` | "a payment is pending" (https://docs.payright.example/payments) |
| `lost` | a dispute is lost | nothing | none | to verify: lose a dispute in the test account |

## The season ticket

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `lapsed` | not said in the documents | renew | renews -> `renewed` | 002_requirements.md, renew-and-pay |

## For the owner's list
- `lost`: no way out. The money is the cardholder's again.
"""
PAYRIGHT = """# Research: PayRight

## What the slice needs from it
- F1: A payment returns a status. "status is one of pending, paid, refused" (https://docs.payright.example/payments)

## What our documents say about it
- S1 AGREES: the slice says "her card is refused". "refused" (https://docs.payright.example/payments)
- S2 CONTRADICTS: the problem says "straight away". "may take up to a day" (https://docs.payright.example/payments)
- S3 NOT COVERED: the approach says "refunds at any time". No page read speaks of it.

## Open
- O1: whether a payment sent twice is taken twice. Test: send the same payment twice in the test account.
"""
LIBRARY = [
    {"id": "call-external-01", "action": "call-external", "failure": "f", "question": "What if the reply never arrives?", "source": {}},
    {"id": "call-external-02", "action": "call-external", "failure": "f", "question": "What if it is slow?", "source": {}},
    {"id": "migration-01", "action": "migration", "failure": "f", "question": "What of what is already stored?", "source": {}},
    {"id": "migration-02", "action": "migration", "failure": "f", "question": "What if it stops halfway?", "source": {}},
]
KEEPS = "- A renewal payment: renew-and-pay / 1\n- `season-ticket`: renew-and-pay / 1\n"
KEPT = """# Kept

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `payment-status` | choice | PayRight | no | payright.md F1 |
| `card-holder-name` | text | the subscriber | yes | renew-and-pay / 1 |

## What the slice creates and keeps
- A renewal payment: renew-and-pay / 1
- `season-ticket`: renew-and-pay / 1

## Other things the slice has
- `payment-request`: the request that takes the payment (renew-and-pay / 1, renew-and-pay / 2)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external-01 | payment-request; A renewal payment | the payment is taken by a request |
| call-external-02 | PayRight | she waits on the same screen |
| migration: all | dropped | nothing is stored before this slice |
"""


def project(kept=KEPT, states=STATES, approach=APPROACH, research=True):
    """A slice's folder as the stages before leave it, with kept.md where one is given."""
    folder = pathlib.Path(tempfile.mkdtemp()) / "slice-001"
    (folder / "007_questions").mkdir(parents=True)
    (folder / "004_slice.md").write_text(SLICE, encoding="utf-8")
    if approach:
        (folder / "005_approach.md").write_text(approach, encoding="utf-8")
    if research:
        (folder / "006_research").mkdir()
        (folder / "006_research" / "states.md").write_text(states, encoding="utf-8")
        (folder / "006_research" / "payright.md").write_text(PAYRIGHT, encoding="utf-8")
    if kept:
        (folder / "007_questions" / "kept.md").write_text(kept, encoding="utf-8")
    library = folder.parent / "library.json"
    library.write_text(json.dumps(LIBRARY), encoding="utf-8")
    return folder, library


def run(command, folder, library):
    out = io.StringIO()
    code = questions.main([command, str(folder), str(library)], out)
    return code, out.getvalue()


class Reading(unittest.TestCase):
    def test_a_short_name_drops_the_article_and_joins_words(self):
        self.assertEqual(questions.slug("A renewal payment"), "renewal-payment")
        self.assertEqual(questions.slug("record-walk / 1"), "record-walk-1")

    def test_the_criteria_are_read_by_their_names_in_order(self):
        self.assertEqual(questions.criteria(SLICE), ["renew-and-pay / 1", "renew-and-pay / 2"])

    def test_what_is_committed_to_is_read_as_the_stage_script_reads_it(self):
        self.assertEqual(questions.committed(APPROACH), ["PayRight"])
        self.assertEqual(questions.committed("## Committed to\n- None.\n"), [])
        self.assertEqual(questions.committed("# Approach\n\nNo such heading.\n"), [])

    def test_every_state_of_every_thing_is_read_and_the_dead_ends_apart(self):
        things, dead = questions.states(STATES)
        self.assertEqual(list(things), ["A renewal payment", "The season ticket"])
        self.assertEqual([state for state, _source, _row in things["A renewal payment"]], ["pending", "lost"])
        self.assertEqual(len(dead), 1)

    def test_states_said_in_one_line_give_no_thing(self):
        self.assertEqual(questions.states("# States\n\nThe slice touches no lasting thing.\n"), ({}, []))

    def test_a_section_ends_at_a_heading_above_it_and_holds_those_below(self):
        found = questions.sections("## One\na\n### Under\nb\n# Top\nc\n## Two\nd\n")
        self.assertEqual(found, {"One": ["a", "### Under", "b"], "Two": ["d"]})


class Carried(unittest.TestCase):
    def test_open_points_contradictions_and_what_no_page_covers_are_carried_and_agreements_are_not(self):
        names = [name for name, _words in questions.carried({"payright.md": PAYRIGHT})]
        self.assertEqual(names, ["C.payright.S2", "C.payright.S3", "C.payright.O1"])

    def test_a_state_not_said_or_to_verify_is_carried_and_a_sourced_one_is_not(self):
        names = [name for name, _words in questions.carried({"states.md": STATES})]
        self.assertEqual(names, ["C.states.renewal-payment.lost", "C.states.season-ticket.lapsed", "C.states.dead-end.1"])

    def test_the_document_of_a_thing_no_longer_committed_to_carries_nothing(self):
        both = {"payright.md": PAYRIGHT, "cardway.md": PAYRIGHT.replace("O1:", "O7:"), "states.md": STATES}
        names = [name for name, _words in questions.carried(both, {"cardway"})]
        self.assertIn("C.cardway.O7", names)
        self.assertNotIn("C.payright.O1", names)
        self.assertIn("C.states.dead-end.1", names)

    def test_nothing_researched_carries_nothing(self):
        self.assertEqual(questions.carried({}), [])


class Checking(unittest.TestCase):
    def setUp(self):
        self.folder, self.library = project()
        self.read, self.entries, self.kept = questions.load(self.folder, self.library)
        self.names = questions.known(self.read)

    def found(self, **changed):
        return questions.problems({**self.kept, **changed}, self.names, self.entries, ["renew-and-pay / 1", "payright.md"])[0]

    def test_what_a_question_may_apply_to_is_the_criteria_the_commitments_and_the_lasting_things(self):
        self.assertEqual(sorted(self.names), ["payright", "renew-and-pay-1", "renew-and-pay-2", "renewal-payment", "season-ticket"])

    def test_a_kept_file_that_accounts_for_everything_has_no_problem(self):
        self.assertEqual(self.found(), [])

    def test_a_file_with_no_list_of_what_the_slice_creates_and_keeps_is_refused(self):
        self.assertEqual(self.found(lasting=None), ["no list of what the slice creates and keeps: one line a thing with its criterion, or `- nothing`"])

    def test_a_slice_that_keeps_nothing_says_so_and_is_drawn(self):
        kept = questions.read_kept(KEPT.replace(KEEPS, "- nothing\n"))
        self.assertEqual(kept["lasting"], [])
        self.assertEqual(self.found(lasting=[]), [])

    def test_a_thing_kept_that_states_has_no_table_for_is_named_with_what_to_do(self):
        self.assertEqual(self.found(lasting=self.kept["lasting"] + [("the waiting list", "join-the-list / 1")]),
                         ["the waiting list: created or kept (join-the-list / 1), and states.md has no table for it: "
                          "add its table by the research text's rules, then draw again"])

    def test_a_thing_committed_to_is_not_a_thing_with_states(self):
        self.assertIn("states.md has no table for it", " ".join(self.found(lasting=[("PayRight", "renew-and-pay / 1")])))

    def test_the_things_kept_are_read_with_or_without_marks_and_articles(self):
        self.assertEqual(self.kept["lasting"], [("A renewal payment", "renew-and-pay / 1"), ("season-ticket", "renew-and-pay / 1")])

    def test_a_criterion_the_file_names_nowhere_is_named_as_not_gone_through(self):
        # Found by the three-run pass: a criterion added after the drawing was read and not noticed, on both models.
        text = self.kept["text"].replace(b"renew-and-pay / 1", b"renew-and-pay / 2")
        self.assertEqual(self.found(text=text), ["renew-and-pay / 1: no thing kept, value, other thing or question of kept.md names this criterion: "
                                                 "go through it, and change only what it brings"])

    def test_a_criterion_is_named_by_its_name_or_its_short_name_and_not_by_a_longer_number(self):
        short = self.kept["text"].replace(b"renew-and-pay / 1", b"`renew-and-pay-1`")
        self.assertEqual(self.found(text=short), [])
        longer = self.kept["text"].replace(b"renew-and-pay / 1", b"renew-and-pay / 12")
        self.assertIn("renew-and-pay / 1: no thing kept", " ".join(self.found(text=longer)))

    def test_an_entry_left_out_is_named(self):
        self.assertEqual(self.found(library=self.kept["library"][:2]), ["migration-01: neither kept nor dropped", "migration-02: neither kept nor dropped"])

    def test_an_entry_judged_twice_is_named(self):
        self.assertIn("call-external-01: judged twice", self.found(library=self.kept["library"] + [self.kept["library"][0]]))

    def test_an_entry_the_library_does_not_have_is_named(self):
        row = {"entry": "call-external-99", "applies": "PayRight", "why": "w"}
        self.assertIn("call-external-99: not an entry of the library", self.found(library=self.kept["library"] + [row]))

    def test_a_kind_the_library_does_not_have_is_named(self):
        row = {"entry": "weather: all", "applies": "dropped", "why": "w"}
        self.assertIn("weather: all: not an entry of the library", self.found(library=self.kept["library"] + [row]))

    def test_a_kept_entry_must_apply_to_a_thing_that_is_listed(self):
        rows = [{"entry": "call-external-01", "applies": "the moon", "why": "w"}] + self.kept["library"][1:]
        self.assertIn("applies to 'the moon'", " ".join(self.found(library=rows)))
        rows = [{"entry": "call-external-01", "applies": " ", "why": "w"}] + self.kept["library"][1:]
        self.assertIn("call-external-01: kept, and applies to nothing", self.found(library=rows))

    def test_a_row_with_no_reason_is_named(self):
        rows = self.kept["library"][:2] + [{"entry": "migration: all", "applies": "dropped", "why": " "}]
        self.assertEqual(self.found(library=rows), ["migration-01: no reason given", "migration-02: no reason given"])

    def test_several_entries_may_share_a_row(self):
        rows = self.kept["library"][:2] + [{"entry": "migration-01, migration-02", "applies": "dropped", "why": "w"}]
        self.assertEqual(self.found(library=rows), [])

    def test_a_value_needs_a_kind_the_script_has_and_a_source_that_exists(self):
        values = [{"name": "x", "kind": "colour", "from": "the person", "sensitive": "no", "source": "renew-and-pay / 1"}]
        self.assertIn("kind 'colour'", " ".join(self.found(values=values)))
        values = [{"name": "x", "kind": "text", "from": "the person", "sensitive": "no", "source": "somewhere"}]
        self.assertEqual(self.found(values=values), ["x: its source names no criterion and no research document"])
        values = [{"name": "x", "kind": "text", "from": "the person", "sensitive": " ", "source": "renew-and-pay / 1"}]
        self.assertEqual(self.found(values=values), ["x: sensitive is `no`, or the name of the class of sensitive values it belongs to"])

    def test_a_question_may_apply_to_a_class_of_sensitive_values(self):
        values = [{"name": "x", "kind": "text", "from": "the person", "sensitive": "her details", "source": "renew-and-pay / 1"}]
        rows = [{"entry": "call-external-01", "applies": "her details", "why": "w"}] + self.kept["library"][1:]
        self.assertEqual(self.found(values=values, library=rows), [])


class Drawing(unittest.TestCase):
    def setUp(self):
        self.folder, self.library = project()

    def drawn(self):
        code, said = run("draw", self.folder, self.library)
        self.assertEqual(code, 0, said)
        return (self.folder / "007_questions" / "questions.md").read_text(encoding="utf-8")

    def test_a_kept_question_is_drawn_once_for_each_thing_it_applies_to_with_its_words(self):
        text = self.drawn()
        self.assertIn("- L.call-external-01.payment-request: payment-request: What if the reply never arrives?", text)
        self.assertIn("- L.call-external-01.renewal-payment:", text)
        self.assertNotIn("L.migration", text)

    def test_a_value_is_drawn_against_the_ways_of_its_kind_only(self):
        text = self.drawn()
        self.assertEqual(text.count("- V.payment-status."), 2)
        self.assertIn("- V.payment-status.outside:", text)
        self.assertEqual(text.count("- V.card-holder-name."), 5)

    def test_the_rule_for_settings_is_always_drawn(self):
        self.assertEqual(self.drawn().count("- V.every-setting."), 4)

    def test_a_sensitive_value_is_drawn_against_every_place_it_can_leak_to_and_no_other_value_is(self):
        text = self.drawn()
        self.assertEqual(text.count("- X.sensitive-values."), len(questions.EXITS))
        self.assertIn("- X.sensitive-values.logs: can any of `card-holder-name` reach what the product logs", text)
        self.assertNotIn("payment-status` reach", text)

    def test_values_of_one_class_are_drawn_together_once_for_each_place(self):
        kept = KEPT.replace("| the subscriber | yes |", "| the subscriber | her details |").replace(
            "| `payment-status` | choice | PayRight | no |", "| `payment-status` | choice | PayRight | Her details |")
        (self.folder / "007_questions" / "kept.md").write_text(kept, encoding="utf-8")
        text = self.drawn()
        self.assertEqual(text.count("- X."), len(questions.EXITS))
        self.assertIn("- X.her-details.telemetry: can any of `payment-status`, `card-holder-name` reach", text)

    def test_no_sensitive_value_is_said_in_a_line(self):
        (self.folder / "007_questions" / "kept.md").write_text(KEPT.replace("| yes |", "| no |"), encoding="utf-8")
        self.assertIn("No value taken in is marked sensitive.", self.drawn())

    def test_the_questions_asked_of_every_slice_are_always_drawn(self):
        self.assertEqual(self.drawn().count("- W."), len(questions.WHOLE))

    def test_a_kind_called_other_gets_every_way(self):
        kept = KEPT.replace("| choice |", "| other |")
        (self.folder / "007_questions" / "kept.md").write_text(kept, encoding="utf-8")
        self.assertEqual(self.drawn().count("- V.payment-status."), len(questions.WAYS))

    def test_every_state_meets_every_criterion_every_fixed_event_and_every_commitment(self):
        text = self.drawn()
        events = 2 + len(questions.EVENTS) + len(questions.OUTSIDE)
        self.assertEqual(text.count("- S."), 3 * events - 2)   # two are already asked by the library
        self.assertIn("- S.renewal-payment.pending.renew-and-pay-2:", text)
        self.assertIn("- S.season-ticket.lapsed.restart:", text)
        self.assertIn("- S.season-ticket.lapsed.payright-lost: The season ticket is `lapsed` and PayRight acted, and its reply never arrived", text)

    def test_nothing_committed_to_gives_no_event_from_outside(self):
        folder, library = project(kept=KEPT.replace("call-external-02 | PayRight", "call-external-02 | payment-request"), approach=None)
        code, said = run("draw", folder, library)
        self.assertEqual(code, 0, said)
        text = (folder / "007_questions" / "questions.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("- S."), 3 * (2 + len(questions.EVENTS)))

    def test_no_lasting_thing_is_said_in_a_line(self):
        kept = KEPT.replace("; A renewal payment", "").replace(KEEPS, "- nothing\n")
        folder, library = project(kept=kept, states="# States\n\nThe slice touches no lasting thing.\n")
        code, said = run("draw", folder, library)
        self.assertEqual(code, 0, said)
        text = (folder / "007_questions" / "questions.md").read_text(encoding="utf-8")
        self.assertIn("No lasting thing has states written for this slice.", text)
        self.assertNotIn("- S.", text)

    def test_a_thing_kept_with_no_table_is_refused_by_the_command_and_nothing_is_drawn(self):
        folder, library = project(states="# States\n\n## A renewal payment\n| State | Source |\n|---|---|\n| pending | payright.md F2 |\n")
        code, said = run("draw", folder, library)
        self.assertEqual(code, 1)
        self.assertIn("season-ticket: created or kept (renew-and-pay / 1), and states.md has no table for it", said)
        self.assertFalse((folder / "007_questions" / "questions.md").exists())

    def test_what_research_left_open_is_carried_and_nothing_is_said_where_there_is_none(self):
        self.assertIn("- C.payright.O1: O1: whether a payment sent twice", self.drawn())
        kept = KEPT.replace("; A renewal payment", "").replace(KEEPS, "- nothing\n").replace("call-external-02 | PayRight", "call-external-02 | payment-request").replace("payright.md F1", "renew-and-pay / 2")
        folder, library = project(kept=kept, research=False)
        code, said = run("draw", folder, library)
        self.assertEqual(code, 0, said)
        self.assertIn("Nothing was left open.", (folder / "007_questions" / "questions.md").read_text(encoding="utf-8"))

    def library_with(self, name, action, applies):
        """The made-up library with one more entry, kept and applied to one thing."""
        entries = LIBRARY + [{"id": name, "action": action, "failure": "f", "question": f"The question of {name}?", "source": {}}]
        self.library.write_text(json.dumps(entries), encoding="utf-8")
        (self.folder / "007_questions" / "kept.md").write_text(KEPT + f"| {name} | {applies} | it arises |\n", encoding="utf-8")

    def test_a_way_a_kept_library_question_already_asks_of_the_same_value_is_not_drawn_again(self):
        self.library_with("user-input-01", "user-input", "card-holder-name")
        text = self.drawn()
        self.assertNotIn("- V.card-holder-name.long:", text)
        self.assertEqual(text.count("- V.card-holder-name."), 4)
        self.assertIn("Not drawn, 1 already asked of the same thing by a library question above.", text)

    def test_the_same_library_question_kept_for_another_thing_spares_nothing(self):
        self.library_with("user-input-01", "user-input", "payment-request")
        text = self.drawn()
        self.assertEqual(text.count("- V.card-holder-name."), 5)
        self.assertIn("- V.card-holder-name.long:", text)

    def test_a_leak_a_kept_library_question_already_asks_of_the_same_value_is_not_drawn_again(self):
        self.library_with("secrets-03", "secrets", "card-holder-name")
        text = self.drawn()
        self.assertNotIn("- X.sensitive-values.logs:", text)
        self.assertEqual(text.count("- X.sensitive-values."), len(questions.EXITS) - 1)

    def test_a_leak_asked_of_only_some_values_of_a_class_is_still_drawn_for_the_class(self):
        self.library_with("secrets-03", "secrets", "card-holder-name")
        path = self.folder / "007_questions" / "kept.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| `payment-status` | choice | PayRight | no |", "| `payment-status` | choice | PayRight | yes |"), encoding="utf-8")
        self.assertIn("- X.sensitive-values.logs:", self.drawn())

    def test_a_kept_question_on_settings_stands_for_the_rule_wherever_it_applies(self):
        self.library_with("configuration-01", "configuration", "payment-request")
        text = self.drawn()
        self.assertEqual(text.count("- V.every-setting."), 1)
        self.assertIn("- V.every-setting.outside:", text)

    def test_a_dropped_question_on_settings_leaves_the_rule_whole(self):
        self.library_with("configuration-01", "configuration", "dropped")
        self.assertEqual(self.drawn().count("- V.every-setting."), 4)

    def test_an_event_a_kept_library_question_already_asks_of_the_same_thing_is_drawn_for_none_of_its_states(self):
        text = self.drawn()   # call-external-01, the reply lost, is kept for the renewal payment
        self.assertNotIn("- S.renewal-payment.pending.payright-lost:", text)
        self.assertNotIn("- S.renewal-payment.lost.payright-lost:", text)
        self.assertIn("- S.season-ticket.lapsed.payright-lost:", text)
        self.assertIn("Not drawn, 2 already asked", text)

    def test_the_library_line_of_a_lasting_thing_names_each_of_its_states(self):
        self.assertIn("- L.call-external-01.renewal-payment: A renewal payment (in each of its states: pending, lost): What if", self.drawn())

    def test_every_question_said_to_ask_the_same_is_an_entry_of_the_real_library(self):
        ids = {entry["id"] for entry in json.loads(questions.LIBRARY.read_text(encoding="utf-8"))}
        named = {name for group in (questions.SAME, questions.SAME_SETTINGS) for names in group.values() for name in names}
        self.assertEqual(named - ids, set())
        self.assertEqual(set(questions.SAME) - set(questions.WAYS) - set(questions.EXITS) - set(questions.EVENTS) - set(questions.OUTSIDE), set())

    def test_no_line_is_drawn_twice(self):
        names = [line.split(":")[0] for line in self.drawn().splitlines() if line.startswith("- ")]
        self.assertEqual(len(names), len(set(names)))

    def test_a_kept_file_with_a_problem_is_not_drawn_from(self):
        (self.folder / "007_questions" / "kept.md").write_text(KEPT.replace("| migration: all | dropped | nothing is stored before this slice |\n", ""), encoding="utf-8")
        code, said = run("draw", self.folder, self.library)
        self.assertEqual(code, 1)
        self.assertIn("migration-01: neither kept nor dropped", said)
        self.assertFalse((self.folder / "007_questions" / "questions.md").exists())

    def test_the_same_documents_draw_the_same_names(self):
        self.assertEqual(self.drawn(), self.drawn())


class TheMark(unittest.TestCase):
    def test_it_is_the_number_the_systems_own_command_prints(self):
        self.assertEqual(questions.cksum(b""), 4294967295)
        self.assertEqual(questions.cksum(b"123456789"), 930766865)

    def test_it_is_of_the_bytes_of_the_documents_in_order_then_the_kept_file(self):
        folder, library = project()
        read, _entries, kept = questions.load(folder, library)
        together = b"".join((folder / name).read_bytes() for name in
                            ("004_slice.md", "005_approach.md", "006_research/payright.md", "006_research/states.md", "007_questions/kept.md"))
        self.assertEqual(questions.stamp(read, kept["text"]), str(questions.cksum(together)))


class TheCommand(unittest.TestCase):
    def setUp(self):
        self.folder, self.library = project()

    def test_the_things_and_the_library_are_printed_for_the_session_to_read(self):
        code, said = run("things", self.folder, self.library)
        self.assertEqual(code, 0)
        self.assertIn("renewal-payment (lasting thing: A renewal payment)", said)
        self.assertIn("  call-external (2), migration (2)\n", said)
        self.assertNotIn("What if the reply never arrives?", said)

    def test_the_questions_of_the_kinds_named_are_printed_and_a_kind_it_does_not_have_is_said(self):
        out = io.StringIO()
        self.assertEqual(questions.show(["migration"], out, self.library), 0)
        self.assertEqual(out.getvalue(), "\nmigration\n  migration-01: What of what is already stored?\n  migration-02: What if it stops halfway?\n")
        out = io.StringIO()
        self.assertEqual(questions.show(["weather", "migration"], out, self.library), 1)
        self.assertIn("weather: the library has no such kind", out.getvalue())
        self.assertIn("migration-02", out.getvalue())

    def test_five_kinds_of_the_real_library_fit_what_a_shell_shows(self):
        out = io.StringIO()
        self.assertEqual(questions.main(["library", "call-external", "receive-external-data", "sync", "limits", "durable-write"], out), 0)
        self.assertEqual(out.getvalue().count("\n  "), 60)
        self.assertLess(len(out.getvalue()), 15000)

    def test_with_no_kept_file_nothing_is_drawn_and_the_state_is_none(self):
        folder, library = project(kept=None)
        self.assertEqual(run("draw", folder, library), (1, "no kept.md in the slice's questions folder: nothing to draw from\n"))
        self.assertEqual(run("state", folder, library), (0, "none\n"))

    def test_with_no_questions_folder_the_state_is_none(self):
        folder, library = project(kept=None)
        (folder / "007_questions").rmdir()
        self.assertEqual(run("state", folder, library), (0, "none\n"))

    def test_the_state_goes_from_kept_to_drawn(self):
        self.assertEqual(run("state", self.folder, self.library)[1], "kept\n")
        run("draw", self.folder, self.library)
        self.assertEqual(run("state", self.folder, self.library)[1], "drawn\n")
        self.assertEqual(run("check", self.folder, self.library), (0, "ok\n"))

    def test_what_research_adds_for_the_answers_or_from_a_test_leaves_the_questions_drawn(self):
        # Met building stage 9: a fact the second pass added sent a session back to the questions.
        run("draw", self.folder, self.library)
        document = sorted((self.folder).glob("[0-9]*_research/*.md"))[0]
        for heading in ("## Looked up for the answers", "## Shown by a test"):
            with document.open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(f"\n{heading}\n- F90: Found later. \"its own words here\" (https://docs.example/later)\n")
            self.assertEqual(run("state", self.folder, self.library)[1], "drawn\n", heading)
        with document.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write("\n## Open\n- O9: a heading that is not one of the two.\n")
        self.assertEqual(run("state", self.folder, self.library)[1], "drawn\n")   # still under the first of them

    def test_a_research_fact_changed_above_those_headings_makes_the_questions_stale(self):
        run("draw", self.folder, self.library)
        document = sorted((self.folder).glob("[0-9]*_research/*.md"))[0]
        document.write_text("- F0: put first.\n" + document.read_text(encoding="utf-8") + "\n## Shown by a test\n- F91: later.\n", encoding="utf-8", newline="\n")
        self.assertTrue(run("state", self.folder, self.library)[1].startswith("stale:"))

    def test_a_document_changed_after_the_drawing_makes_the_questions_stale(self):
        run("draw", self.folder, self.library)
        with (self.folder / "004_slice.md").open("a", encoding="utf-8") as handle:
            handle.write("- **renew-and-pay / 3**: Given a ticket, when she pays twice, then she is charged once.\n")
        self.assertTrue(run("state", self.folder, self.library)[1].startswith("stale:"))
        self.assertEqual(run("check", self.folder, self.library)[0], 1)

    def test_a_drawing_changed_by_hand_fails_the_check(self):
        run("draw", self.folder, self.library)
        target = self.folder / "007_questions" / "questions.md"
        target.write_text(target.read_text(encoding="utf-8").replace("- S.season-ticket.lapsed.restart:", "- S.season-ticket.lapsed.restart (answered):"), encoding="utf-8")
        code, said = run("check", self.folder, self.library)
        self.assertEqual(code, 1)
        self.assertIn("draw it again", said)

    def test_a_check_before_any_drawing_fails(self):
        self.assertEqual(run("check", self.folder, self.library)[0], 1)

    def test_the_drawing_says_how_many_questions_of_each_part_and_how_many_it_spared(self):
        code, said = run("draw", self.folder, self.library)
        self.assertEqual(code, 0)
        self.assertRegex(said, r"^drawn: .*questions\.md: \d+ questions: 3 from the library, 11 of values, 7 of leaks, 28 of states, 7 of every slice, 6 carried from research; 2 not drawn")

    def test_a_folder_that_cannot_be_written_is_said_and_nothing_is_to_be_written_by_hand(self):
        target = self.folder / "007_questions" / "questions.md"
        target.mkdir()   # a folder where the file would go: writing it fails on every system
        code, said = run("draw", self.folder, self.library)
        self.assertEqual(code, 0)
        self.assertIn("drawn, and not written", said)
        self.assertIn("do not write it by hand", said)

    def test_skipped_at_the_users_word_draws_what_needs_no_judgement_and_says_so(self):
        folder, library = project(kept=None)
        (folder / "007_questions" / "skipped.md").write_text("Skipped at the user's word, 2026-11-24: \"skip it\".\n", encoding="utf-8")
        self.assertEqual(run("state", folder, library)[1], "kept\n")
        code, said = run("draw", folder, library)
        self.assertEqual(code, 0, said)
        text = (folder / "007_questions" / "questions.md").read_text(encoding="utf-8")
        self.assertIn("skipped at the user's word", text)
        self.assertIn("Not gone through.", text)
        self.assertNotIn("- L.", text)
        self.assertEqual(text.count("- S."), 3 * (2 + len(questions.EVENTS) + len(questions.OUTSIDE)))
        self.assertEqual(text.count("- W."), len(questions.WHOLE))
        self.assertIn("- C.payright.O1:", text)
        self.assertEqual(run("state", folder, library)[1], "skipped\n")
        self.assertEqual(run("check", folder, library), (0, "ok\n"))

    def test_a_kept_file_written_after_a_skip_is_the_one_drawn_from(self):
        (self.folder / "007_questions" / "skipped.md").write_text("Skipped.\n", encoding="utf-8")
        run("draw", self.folder, self.library)
        self.assertEqual(run("state", self.folder, self.library)[1], "drawn\n")

    def test_a_command_it_does_not_have_prints_how_it_is_used(self):
        out = io.StringIO()
        self.assertEqual(questions.main(["answer", "x"], out), 2)
        self.assertIn("Usage:", out.getvalue())

    def test_the_real_library_is_read_where_none_is_named(self):
        out = io.StringIO()
        self.assertEqual(questions.main(["things", str(self.folder)], out), 0)
        self.assertIn("call-external (12)", out.getvalue())
        self.assertIn("startup-read (10)", out.getvalue())


SECURITY = """# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | renew-and-pay / 1: she is shown |
| network | yes | 000_problem.md: the playhouse's site |
| calls-out | yes | 005_approach.md: PayRight |
| dependency | no | 005_approach.md: nothing is added |
| several-people | no | 000_problem.md: one office |
| unguessable | no | no criterion makes one |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `card-holder-name` | `payment-request` | a payment is taken in her name. | yes |
| sensitive-values | payment-status | nothing | no: a status names nobody |
"""


class Security(unittest.TestCase):
    """The security pass: security.md beside kept.md, checked and drawn into the same list."""

    def setUp(self):
        self.folder, self.library = project()
        self.path = self.folder / "007_questions" / "security.md"

    def drawn(self, text=SECURITY):
        self.path.write_text(text, encoding="utf-8")
        code, said = run("draw", self.folder, self.library)
        return code, said, (self.folder / "007_questions" / "questions.md").read_text(encoding="utf-8") if code == 0 else ""

    def test_with_no_security_file_nothing_of_it_is_drawn_or_said(self):
        code, said = run("draw", self.folder, self.library)
        text = (self.folder / "007_questions" / "questions.md").read_text(encoding="utf-8")
        self.assertEqual(code, 0)
        self.assertNotIn("- F.", text)
        self.assertNotIn("- T.", text)
        self.assertNotIn("by what the slice is", said)

    def test_a_fact_that_holds_draws_its_questions_and_one_that_does_not_draws_none(self):
        code, said, text = self.drawn()
        self.assertEqual(code, 0, said)
        self.assertIn("- F.browser.framing: May another site show this product inside a page of its own", text)
        self.assertIn("- F.network.answers-to: ", text)
        self.assertIn("- F.calls-out.where: ", text)
        self.assertNotIn("- F.dependency.", text)
        self.assertNotIn("- F.several-people.", text)
        self.assertIn("23 by what the slice is, 1 of what someone would want", said)

    def test_what_is_wanted_is_asked_once_a_row_and_a_dismissed_row_is_not(self):
        _code, _said, text = self.drawn()
        self.assertIn("- T.card-holder-name.payment-request: someone after `card-holder-name` comes through `payment-request`: "
                      "a payment is taken in her name. What stops it, and how would anyone know it was tried?", text)
        self.assertEqual(text.count("- T."), 1)

    def test_the_two_exits_kad_named_are_asked_of_every_class(self):
        _code, _said, text = self.drawn()
        self.assertIn("- X.sensitive-values.replies: ", text)
        self.assertIn("- X.sensitive-values.stored: ", text)

    def refused(self, old, new):
        code, said, _text = self.drawn(SECURITY.replace(old, new))
        self.assertEqual(code, 1, said)
        return said

    def test_a_fact_left_out_said_twice_unknown_or_with_no_source_is_refused(self):
        self.assertIn("unguessable: not said", self.refused("| unguessable | no | no criterion makes one |\n", ""))
        self.assertIn("browser: said twice", self.refused("| network | yes", "| browser | yes | again |\n| network | yes"))
        self.assertIn("weather: not one of the facts", self.refused("| network | yes", "| weather | yes | x |\n| network | yes"))
        self.assertIn("dependency: no source", self.refused("| dependency | no | 005_approach.md: nothing is added |", "| dependency | no | |"))

    def test_a_fact_that_is_neither_yes_nor_no_is_refused_with_what_to_write(self):
        self.assertIn("network: holds is `yes` or `no`; where the documents do not say, it is `yes`", self.refused("| network | yes", "| network | perhaps"))

    def test_a_class_nobody_is_said_to_want_and_a_thing_nothing_comes_through_are_refused(self):
        said = self.refused("| `card-holder-name` | `payment-request` | a payment is taken in her name. | yes |\n", "")
        self.assertIn("payment-request: another thing of the slice nothing is said to come through", said)
        both = SECURITY[SECURITY.index("| `card-holder-name`"):]
        self.assertIn("sensitive-values: a class of sensitive values nobody is said to want", self.refused(both, ""))
        # A value of the class stands for the class.
        self.assertEqual(self.drawn(SECURITY.replace("| sensitive-values | payment-status | nothing | no: a status names nobody |\n", ""))[0], 0)

    def test_what_is_wanted_may_be_a_thing_the_documents_name_or_nothing_dismissed(self):
        # Met in the pilot: a slice with no sensitive value at all could write no row the script took.
        row = "| `card-holder-name` | `payment-request` | a payment is taken in her name. | yes |"
        self.assertEqual(self.drawn(SECURITY.replace(row, "| A renewal payment | `payment-request` | a payment is taken that nobody asked for | yes |"))[0], 0)
        self.assertEqual(self.drawn(SECURITY + "| nothing | `payment-request` | a made-up request is sent | no: it gives nothing worth having |\n")[0], 0)
        self.assertIn("nothing through payment-request: a row that wants nothing is dismissed",
                      self.refused("| sensitive-values | payment-status | nothing | no: a status names nobody |",
                                   "| nothing | payment-request | a made-up request is sent | yes |"))

    def test_a_slice_with_no_sensitive_value_is_drawn_with_rows_that_want_nothing(self):
        kept = KEPT.replace("| `card-holder-name` | text | the subscriber | yes |", "| `card-holder-name` | text | the subscriber | no |")
        folder, library = project(kept=kept)
        (folder / "007_questions" / "security.md").write_text(
            SECURITY[:SECURITY.index("| `card-holder-name`")] + "| nothing | `payment-request` | a made-up request is sent | no: nothing is kept or shown |\n", encoding="utf-8")
        code, said = run("draw", folder, library)
        self.assertEqual(code, 0, said)
        self.assertIn("0 of what someone would want", said)

    def test_a_name_kept_md_does_not_have_is_refused(self):
        self.assertIn("the-till: wanted, and no class", self.refused("| `card-holder-name` | `payment-request`", "| the-till | `payment-request`"))
        self.assertIn("the-door: come through, and no other thing", self.refused("| `card-holder-name` | `payment-request`", "| `card-holder-name` | the-door"))

    def test_a_row_with_no_worst_or_dismissed_without_a_reason_is_refused(self):
        self.assertIn("the worst from there is not said", self.refused("| a payment is taken in her name. |", "| |"))
        self.assertIn("asked is `yes`, or `no: ` and why", self.refused("| no: a status names nobody |", "| no |"))

    def test_skipped_at_the_users_word_every_fact_is_drawn_and_nothing_is_checked(self):
        code, said, text = self.drawn("Skipped at the user's word, 2026-11-25: \"skip the security pass\"\n")
        self.assertEqual(code, 0, said)
        self.assertEqual(text.count("- F."), sum(len(asks) for _what, asks in questions.FACTS.values()))
        self.assertIn("Skipped at the user's word: a risk for the owner's list.", text)

    def test_the_mark_changes_with_the_security_file_so_the_drawing_goes_stale(self):
        self.assertEqual(run("draw", self.folder, self.library)[0], 0)
        self.assertEqual(run("state", self.folder, self.library)[1].strip(), "drawn")
        self.path.write_text(SECURITY, encoding="utf-8")
        self.assertTrue(run("state", self.folder, self.library)[1].startswith("stale"))
        self.assertEqual(run("draw", self.folder, self.library)[0], 0)
        self.assertEqual(run("state", self.folder, self.library)[1].strip(), "drawn")

    def test_a_criterion_named_only_in_the_security_file_is_still_named_nowhere_in_kept(self):
        kept = KEPT.replace("renew-and-pay / 2", "renew-and-pay / 1")
        folder, library = project(kept=kept)
        (folder / "007_questions" / "security.md").write_text(SECURITY + "\nrenew-and-pay / 2\n", encoding="utf-8")
        code, said = run("draw", folder, library)
        self.assertEqual(code, 1)
        self.assertIn("renew-and-pay / 2: no thing kept", said)

    def test_every_fixed_question_has_a_name_of_its_own_is_a_question_and_says_what_it_rests_on(self):
        for fact, (what, asks) in questions.FACTS.items():
            self.assertTrue(what)
            self.assertEqual(len({key for key, _words, _rests in asks}), len(asks), fact)
            for key, words, rests in asks:
                self.assertTrue(words.endswith("?"), key)
                self.assertRegex(rests, r"^(kad|V\d+\.\d+\.\d+)", key)


if __name__ == "__main__":
    unittest.main()
