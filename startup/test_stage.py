import importlib.util
import io
import pathlib
import shutil
import unittest

from standin_machine import Machine

THROUGH_REQUIREMENTS = ["000_problem.md", "001_scope-map.md", "002_requirements.md"]
REMOTE = "https://github.com/someone/something.git"
LIST = """# Requirements: Borrow and return a tool

- [ ] **record-a-loan**: A volunteer can record which member took which tool.
- [ ] **record-a-return**: A volunteer can record that a tool came back.
- [ ] **see-who-has-it**: A volunteer can see who has a given tool now.

## Out for now
- Reserving a tool.
"""
THE_REST = ["approach", "research/states", "questions", "answers", "open-facts", "design", "screens", "stack", "readiness",
            "owner-list"]


def row(number, state, items, name="Do a thing", on="nothing"):
    return f"| {number} | {name} | {items} | {on} | {state} |\n"


def the_set(*rows, more=""):
    return ("# Slices: Borrow and return a tool\n\n| # | Slice | Items | Builds on | State |\n|---|---|---|---|---|\n"
            + "".join(rows) + "\n## Where to start\nSlice 1.\n" + more)


def the_slice(*criteria, number=1, needs="A way to tell the member their tool is due back."):
    return (f"# Slice {number}: Do a thing\n\n## Thin path\nA volunteer does it.\n\n## Criteria\n"
            + "".join(f"- **{name}**: Given a state, when one action, then an outcome.\n" for name in criteria)
            + f"\n## Needs from outside\n{needs}\n\n## Left for later\n- **not a criterion**: usable without it.\n")


def the_approach(*decisions, committed=()):
    """An approach: a section a need with its decision, then what is committed to."""
    return ("# Approach: slice 1\n\n"
            + "".join(f"## Need {place}\n\n| Way | What it ties us to |\n|---|---|\n| Without | nothing |\n\n"
                      f"Recommended: a way.\n{decision}\n\n" for place, decision in enumerate(decisions, 1))
            + "## Committed to\n" + ("".join(f"- {line}\n" for line in committed) or "Nothing.\n"))


def the_questions_script():
    spec = importlib.util.spec_from_file_location("questions", pathlib.Path(__file__).resolve().parent.parent / "questions/questions.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


THREE = the_set(row(1, "open", "record-a-loan"), row(2, "open", "record-a-return", on="1"),
                row(3, "open", "see-who-has-it", on="1"))


class Stage(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def chosen(self, *documents, folder="planning"):
        (self.machine.project / folder).mkdir(parents=True, exist_ok=True)
        for document in documents:
            self.machine.document(document, folder)
        done = self.machine.run("stage.sh", "remember", folder)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    def report(self):
        done = self.machine.run("stage.sh", "report")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def not_built(self, trial=""):
        """Startup's cases as built with that stage's text on trial, their documents laid in the project."""
        import importlib.util
        import os
        from unittest import mock
        spec = importlib.util.spec_from_file_location(
            "startup_cases", pathlib.Path(__file__).resolve().parent.parent / "steps/00-startup/eval/make_cases.py")
        cases = importlib.util.module_from_spec(spec)
        with mock.patch.dict(os.environ, {"KD_TRIAL": trial}):
            spec.loader.exec_module(cases)
        folder = self.machine.project / "planning"
        for name in cases.NOT_BUILT[1]:
            (folder / name).parent.mkdir(parents=True, exist_ok=True)
            # As written, on every system: the questions' mark is of the documents' bytes.
            (folder / name).write_text(cases.DOCUMENTS[name], encoding="utf-8", newline="\n")
        self.machine.run("stage.sh", "remember", "planning")
        return cases.NOT_BUILT[0]

    def test_the_startup_scenario_of_a_stage_not_built_has_the_documents_that_make_that_stage_next(self):
        # Found by the regression pass with the approach on trial: the scenario still named the
        # approach as not built, and the session, rightly, did the approach. With research adopted
        # (decision 44) the first stage not built is the questions.
        # With the questions adopted (decision 48) it was the security pass (decision 46), with that
        # adopted (decision 51) the answers, and with those adopted (decision 55) the tests of open facts.
        # ... and with those adopted (decision 58) the design.
        named = self.not_built()
        self.assertIn("- next stage by the documents: design", self.report())
        self.assertRegex("design", named)
        self.assertNotRegex("tests of open facts", named)

    def test_a_project_never_seen_has_no_planning_folder(self):
        out = self.report()
        self.assertIn("- planning folder: not chosen yet for this project", out)
        self.assertNotIn("next stage", out)

    def test_a_chosen_folder_is_remembered_for_that_project_only(self):
        self.chosen()
        self.assertIn("- planning folder: planning (chosen earlier for this project)", self.report())
        elsewhere = self.machine.root / "another"
        elsewhere.mkdir()
        self.assertIn("not chosen yet", self.machine.run("stage.sh", "report", cwd=elsewhere).stdout)

    def test_choosing_again_replaces_the_first_choice(self):
        self.chosen()
        self.chosen(folder="docs/plan")
        out = self.report()
        self.assertIn("- planning folder: docs/plan (chosen earlier", out)
        remembered = (self.machine.data / "planning-folders").read_text(encoding="utf-8")
        self.assertEqual(len(remembered.splitlines()), 1)

    def test_the_folder_is_found_from_a_folder_below_the_repository_root(self):
        self.machine.repository()
        self.chosen("000_problem.md")
        below = self.machine.project / "src"
        below.mkdir()
        self.assertIn("- found: problem (000_problem.md)", self.machine.run("stage.sh", "report", cwd=below).stdout)

    def test_an_empty_folder_starts_at_the_problem(self):
        self.chosen()
        out = self.report()
        self.assertIn("- found: no planning document", out)
        self.assertIn("- next stage by the documents: problem", out)

    def test_the_next_stage_is_named_with_the_document_it_writes(self):
        self.chosen()
        self.assertIn("- next stage by the documents: problem (its document: planning/000_problem.md)", self.report())
        self.chosen(*THROUGH_REQUIREMENTS, folder="docs/plan")
        self.assertIn("- next stage by the documents: slice (its document: docs/plan/003_slices.md, the set of "
                      "slices; once the user has chosen one, its own document: docs/plan/slice-NNN/004_slice.md, "
                      "NNN the slice's number in the set)", self.report())

    def test_a_problem_alone_makes_scope_next(self):
        self.chosen("000_problem.md")
        out = self.report()
        self.assertIn("- found: problem (000_problem.md)", out)
        self.assertIn("- next stage by the documents: scope", out)
        self.assertNotIn("out of order", out)

    # The order of the stages (decision 36): the slice follows the requirements; the approach and
    # research follow the slice.
    def test_documents_through_requirements_make_the_slice_next(self):
        self.chosen(*THROUGH_REQUIREMENTS)
        out = self.report()
        self.assertIn("- next stage by the documents: slice (its document: planning/003_slices.md", out)
        self.assertNotIn("research", out)

    def test_a_slice_with_no_requirements_behind_it_is_out_of_order(self):
        self.chosen("000_problem.md", "001_scope-map.md", "slice-001/004_slice.md")
        out = self.report()
        self.assertIn("- out of order: slice (slice-001/004_slice.md) exists but nothing was found for: "
                      "requirements, the set of slices", out)
        self.assertIn("- next stage by the documents: requirements", out)

    def planned(self, set_text, documents=(), list_text=LIST, slices=None, tracker=None):
        """A project with its list, a set of slices, each slice's own document by its number, and
        what the tracker answers."""
        if tracker is not None:
            # Before the folder is recorded: on Windows a repository's root is not written as a plain folder's is.
            self.machine.repository(REMOTE)
        self.chosen("000_problem.md", "001_scope-map.md", *documents)
        folder = self.machine.project / "planning"
        (folder / "002_requirements.md").write_text(list_text, encoding="utf-8")
        (folder / "003_slices.md").write_text(set_text, encoding="utf-8")
        for number, text in (slices or {}).items():
            (folder / f"slice-{number:03d}").mkdir(exist_ok=True)
            (folder / f"slice-{number:03d}" / "004_slice.md").write_text(text, encoding="utf-8")
        if tracker is not None:
            self.machine.have("gh")
            self.machine.set("gh/lines", "\n".join(["ok\t0\t0", *tracker]))
        return self.report()

    def test_a_set_with_no_slice_chosen_waits_for_the_users_choice(self):
        out = self.planned(THREE)
        self.assertIn("- found: problem (000_problem.md), scope map (001_scope-map.md), requirements "
                      "(002_requirements.md), the set of slices (003_slices.md)\n", out)
        self.assertIn("- next stage by the documents: slice (the user chooses where to start; the chosen slice's "
                      "own document: planning/slice-NNN/004_slice.md, NNN its number in the set)", out)

    def test_a_chosen_slice_with_no_document_gets_one_in_the_folder_of_its_number(self):
        out = self.planned(the_set(row(1, "open", "record-a-loan"), row(2, "chosen", "record-a-return, see-who-has-it")))
        self.assertIn("- next stage by the documents: slice (its document: planning/slice-002/004_slice.md, "
                      "the criteria of slice 2)", out)

    def test_the_approach_follows_the_slice_and_research_the_approach(self):
        chosen = the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it"))
        out = self.planned(chosen, slices={1: the_slice("record-a-loan / 1")})
        self.assertIn("slice (slice-001/004_slice.md)", out)
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/005_approach.md)", out)
        self.machine.document("slice-001/005_approach.md")
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, to write there: states.md)",
                      self.report())
        self.machine.document("slice-001/006_research/states.md")
        self.assertIn("- next stage by the documents: questions", self.report())

    # The approach, counted (its condition 19).
    ONE = the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it"))
    # The end of the reader's path: its start is written as the shell writes it, which on Windows is not as Python does.
    PAGE = '/startup/../research/page.py"'

    def approached(self, text, needs="A way to tell the member."):
        self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1", needs=needs)})
        (self.machine.project / "planning/slice-001/005_approach.md").write_text(text, encoding="utf-8")
        return self.report()

    def test_a_slice_that_needs_nothing_from_outside_skips_the_approach(self):
        for none in ("none", "`none`", "None.", "\n**none**"):
            with self.subTest(none):
                out = self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1", needs=none)})
                self.assertIn("- approach: not needed, slice 1 needs nothing from outside (slice-001/004_slice.md)\n", out)
                self.assertIn("- next stage by the documents: research (its document: planning/slice-001/005_research/, to write there: states.md)", out)
                self.assertNotIn("out of order", out)
                self.assertNotIn("to research, committed to", out)

    def test_a_need_that_only_begins_with_none_is_a_need(self):
        out = self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1", needs="None of the staff's own tools: a text message service.")})
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/005_approach.md)", out)
        self.assertNotIn("not needed", out)

    def test_a_slice_with_no_needs_section_still_gets_an_approach(self):
        out = self.planned(self.ONE, slices={1: "# Slice 1: Do a thing\n\n## Criteria\n- **record-a-loan / 1**: Given, when, then.\n"})
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/005_approach.md)", out)

    def test_an_approach_written_for_a_slice_that_needs_nothing_is_still_found(self):
        out = self.approached(the_approach(), needs="none")
        self.assertIn("approach (slice-001/005_approach.md)", out)
        self.assertNotIn("not needed", out)

    def test_the_page_command_is_given_while_the_approach_or_research_is_next(self):
        out = self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1")})
        self.assertRegex(out, r'\n- a page of documentation is read with: python3 "[^"\n]+' + self.PAGE + r" fetch URL --to planning/slice-001/pages\n"
                              r'  and every quote written from one is then looked for in its saved page: python3 "[^"\n]+' + self.PAGE
                              + r" check planning/slice-001/pages DOCUMENT\n")
        self.assertIn(" fetch URL --to planning/slice-001/pages", self.approached(the_approach("Decision: without")))
        self.machine.document("slice-001/006_research/states.md")
        self.assertNotIn("page.py", self.report())

    def test_the_page_command_is_not_given_before_the_slice(self):
        self.chosen(*THROUGH_REQUIREMENTS)
        self.assertNotIn("page.py", self.report())

    def test_a_need_still_waiting_keeps_the_approach_as_the_next_stage(self):
        out = self.approached(the_approach("Decision: committed: Postbox (the user, 2026-01-02: \"take it\").", "**Decision:** waiting",
                                           "Decision: waiting. No candidate is known.",
                                           committed=["Postbox: https://docs.postbox.example/, for telling the member."]))
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/005_approach.md, "
                      "corrected in place: 2 of its needs still waiting for the user's decision)", out)
        self.assertNotIn("approach (slice-001/005_approach.md)", out.split("- found:")[1].splitlines()[0])
        self.assertNotIn("to research", out)
        self.assertIn(" fetch URL --to planning/slice-001/pages", out)

    def test_a_table_cell_that_says_waiting_is_not_a_decision(self):
        out = self.approached(the_approach("Decision: without").replace("| nothing |", "| waiting on a contract |"))
        self.assertIn("- next stage by the documents: research", out)

    def test_what_is_committed_to_is_the_list_for_research_each_with_its_document(self):
        out = self.approached(the_approach(
            "Decision: committed: Postbox (the user, 2026-01-02: \"take it\"). Not taken: Lettera, over the limit.",
            "Decision: fixed by a limit: PayRight.", "Decision: without (the user, 2026-01-02: \"we keep the notebook\").",
            committed=["Postbox: https://docs.postbox.example/start, for telling the member their tool is due back.",
                       "**PayRight Cards**: <https://docs.payright.example/>, for taking a card payment"]))
        self.assertIn("- to research, committed to in planning/slice-001/005_approach.md:\n"
                      "  - Postbox, for telling the member their tool is due back (its documentation: "
                      "https://docs.postbox.example/start; its document: planning/slice-001/006_research/postbox.md)\n"
                      "  - PayRight Cards, for taking a card payment (its documentation: https://docs.payright.example/; "
                      "its document: planning/slice-001/006_research/payright-cards.md)\n", out)
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, "
                      "to write there: postbox.md, payright-cards.md, states.md)", out)
        self.assertNotIn("must agree", out)

    def test_a_thing_committed_to_with_no_address_is_listed_as_having_none(self):
        out = self.approached(the_approach("Decision: committed: Postbox", committed=["Postbox"]))
        self.assertIn("  - Postbox (its documentation: no address given; its document: planning/slice-001/006_research/postbox.md)\n", out)

    def test_nothing_committed_to_leaves_no_outside_system_to_research(self):
        for nothing in ((), ("none",), ("Nothing.",)):
            with self.subTest(nothing):
                out = self.approached(the_approach("Decision: without (the user: \"as today\")", committed=nothing))
                self.assertIn("- nothing is committed to in planning/slice-001/005_approach.md: no outside system is researched\n", out)
                self.assertNotIn("to research, committed to", out)

    def test_decisions_and_the_committed_list_that_disagree_are_said(self):
        out = self.approached(the_approach("Decision: committed: Postbox", "Decision: fixed by a limit: PayRight",
                                           committed=["Postbox: https://docs.postbox.example/, for telling the member."]))
        self.assertIn("- the decisions of slice-001/005_approach.md commit to 2 and its \"Committed to\" lists 1: "
                      "research starts from that list, so the two must agree\n", out)

    def test_a_changed_approach_is_corrected_in_place_until_research_is_written_from_it(self):
        out = self.approached(the_approach("Decision: without"))
        self.assertIn("- a changed approach is corrected in place (planning/slice-001/005_approach.md): no research is "
                      "written from it yet\n", out)
        self.machine.document("slice-001/006_research/states.md")
        out = self.report()
        self.assertIn("- a changed approach is a new document, the earlier one left as it is: "
                      "planning/slice-001/007_approach.md\n", out)
        self.assertNotIn("was written before the approach", out)

    # Research, counted (its condition 17).
    POSTBOX = dict(committed=["Postbox: https://docs.postbox.example/, for telling the member."])
    INVENTORY = "\n## Outside systems and lasting things\n%s\n"

    def researched(self, *documents, approach=None, inventory=None):
        self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1")},
                     list_text=LIST + (self.INVENTORY % inventory if inventory else ""))
        (self.machine.project / "planning/slice-001/005_approach.md").write_text(
            approach or the_approach("Decision: committed: Postbox", **self.POSTBOX), encoding="utf-8")
        for name in documents:
            self.machine.document(f"slice-001/006_research/{name}")
        return self.report()

    def test_research_is_done_when_every_thing_committed_to_has_its_document_and_the_states_are_written(self):
        out = self.researched("postbox.md", "states.md", inventory="- a loan")
        self.assertIn("research (slice-001/006_research/)", out)
        self.assertIn("- next stage by the documents: questions", out)

    def test_a_thing_committed_to_with_no_document_keeps_research_as_the_next_stage_in_the_same_folder(self):
        out = self.researched("states.md", inventory="- a loan")
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, "
                      "still to write there: postbox.md)", out)
        self.assertIn("its document: planning/slice-001/006_research/postbox.md)", out)
        self.assertNotIn("007_research", out)
        self.assertNotIn("research (slice-001/006_research/)", out.split("- found:")[1].splitlines()[0])
        self.assertNotIn("out of order", out)

    def test_the_states_not_written_keep_research_as_the_next_stage(self):
        for inventory in ("- a loan", None):   # a list that does not say is taken to have something
            with self.subTest(inventory):
                out = self.researched("postbox.md", inventory=inventory)
                self.assertIn("still to write there: states.md)", out)

    def test_an_inventory_of_none_needs_no_states(self):
        for none in ("none", "None.", "`none`"):
            with self.subTest(none):
                out = self.researched("postbox.md", inventory=none)
                self.assertIn("- next stage by the documents: questions", out)

    def test_before_any_research_what_is_to_be_written_is_said(self):
        out = self.researched(inventory="- a loan")
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, "
                      "to write there: postbox.md, states.md)", out)
        out = self.report()

    def test_nothing_committed_to_and_an_inventory_of_none_skips_research(self):
        out = self.researched(approach=the_approach("Decision: without"), inventory="none")
        self.assertIn("- research: not needed, nothing is committed to and the requirements name no lasting thing (002_requirements.md)\n", out)
        self.assertIn("- next stage by the documents: questions", out)
        self.assertNotIn("out of order", out)
        self.assertNotIn("page.py", out)

    def test_a_slice_that_needs_nothing_and_an_inventory_of_none_skips_the_approach_and_research(self):
        out = self.planned(self.ONE, slices={1: the_slice("record-a-loan / 1", needs="none")}, list_text=LIST + self.INVENTORY % "none")
        self.assertIn("- approach: not needed", out)
        self.assertIn("- research: not needed", out)
        self.assertIn("- next stage by the documents: questions (its document: planning/slice-001/005_questions/, "
                      "to write there: kept.md; questions.md is then drawn from it)", out)

    # The questions, counted (stage 7): a folder; kept.md is the session's, questions.md the script's.
    def asked(self, kept="Kept.\n", basis="kept.md", draw=True, folder="007_questions"):
        """A researched slice with its questions folder, drawn by the script's own mark where asked."""
        self.researched("postbox.md", "states.md", inventory="- a loan")
        at = self.machine.project / "planning/slice-001" / folder
        at.mkdir()
        if kept is not None:
            (at / basis).write_text(kept, encoding="utf-8")
        if draw:
            self.draw(at, basis)
        return self.report()

    def draw(self, at, basis="kept.md", security=False):
        slice_folder = at.parent
        # As the questions' own script marks them: a research document without what was added to it later.
        cut = the_questions_script().drawn_from
        together = b"".join(cut(name.rsplit("/", 1)[-1], (slice_folder / name).read_bytes()) if "_research/" in name else (slice_folder / name).read_bytes() for name in
                            ("004_slice.md", "005_approach.md", "006_research/postbox.md", "006_research/states.md", f"{at.name}/{basis}",
                             *([f"{at.name}/security.md"] if security else [])))
        (at / "questions.md").write_text(f"# Questions\n\n<!-- drawn from: {the_questions_script().cksum(together)} -->\n", encoding="utf-8")

    def test_the_questions_are_done_when_drawn_from_the_documents_as_they_stand(self):
        out = self.asked()
        self.assertIn("questions (slice-001/007_questions/)", out)
        self.assertNotIn("out of order", out)
        self.assertNotIn("library KIND", out)
        # The security pass is next (decision 46): its file beside kept.md, and the questions drawn again with it.
        self.assertIn("- next stage by the documents: security (its document: planning/slice-001/007_questions/security.md, "
                      "to write there: security.md; the questions are then drawn again with it)", out)
        self.assertRegex(out, r'questions\.py" things planning/slice-001\n')
        self.assertRegex(out, r'questions\.py" draw planning/slice-001\n')

    def secured(self, text="# Security\n", again=True, **asked):
        self.asked(**asked)
        at = self.machine.project / "planning/slice-001/007_questions"
        (at / "security.md").write_text(text, encoding="utf-8")
        if again:
            self.draw(at, asked.get("basis", "kept.md"), security=True)
        return self.report()

    def test_the_security_file_written_and_the_questions_not_yet_drawn_again_keeps_security_next(self):
        out = self.secured(again=False)
        self.assertIn("- next stage by the documents: security (its document: planning/slice-001/007_questions/security.md, "
                      "security.md is written there; the questions are still to be drawn again with it)", out)

    def test_security_is_done_once_the_questions_carry_its_mark_too(self):
        out = self.secured()
        self.assertIn("questions (slice-001/007_questions/), security (slice-001/007_questions/security.md)", out)
        self.assertIn("- next stage by the documents: answers (its document: planning/slice-001/008_answers.md)", out)
        self.assertNotIn("questions.py", out)
        self.assertNotIn("out of order", out)

    # The answers (stage 8): answers.md is the session's, answered.md the script's, with their mark.
    def answered(self, drawn=True, text="# Answers\n\n## A1: A lost reply\nKind: test\nSays: Not known.\nTest: one.\nHarm: high\nSettles: C.x.O1\n"):
        self.secured()
        folder = self.machine.project / "planning/slice-001"
        (folder / "008_answers.md").write_text(text, encoding="utf-8", newline="\n")
        if drawn:
            mark = the_questions_script().cksum((folder / "007_questions/questions.md").read_bytes() + (folder / "008_answers.md").read_bytes())
            (folder / "008_answered.md").write_text(f"# Answered\n\n<!-- drawn from: {mark} -->\n", encoding="utf-8")
        return folder

    def test_with_the_answers_next_the_report_gives_the_two_commands(self):
        out = self.secured()
        self.assertRegex(out, r"- the questions no answer settles yet, sixty at a time: python3 \".*answers\.py\" next planning/slice-001")
        self.assertRegex(out, r"checked and drawn by script once none is left: python3 \".*answers\.py\" draw planning/slice-001")
        # Decision 54: what the answers need of a thing committed to is looked up then, from the pages.
        self.assertRegex(out, r"looked up in the research, together: python3 \".*answers\.py\" lookups planning/slice-001")
        self.assertRegex(out, r"- a page of documentation is read with: python3 \".*page\.py\" fetch URL --to planning/slice-001/pages")

    def test_answers_written_in_and_not_drawn_keep_the_answers_next(self):
        self.answered(drawn=False)
        out = self.report()
        self.assertIn("- next stage by the documents: answers (its document: planning/slice-001/008_answers.md, written in, and not yet drawn: "
                      "the questions no answer settles are still to answer)", out)
        self.assertIn("answers.py", out)

    def test_the_answers_are_done_once_drawn_from_the_questions_and_answers_as_they_stand(self):
        self.answered()
        out = self.report()
        self.assertIn("answers (slice-001/008_answers.md)", out)
        self.assertIn("- next stage by the documents: tests of open facts (its document: planning/slice-001/009_open-facts.md)", out)
        # Met building the cases: a decision taken later had no command to draw it with.
        self.assertRegex(out, r"- a decision the owner takes on their list is recorded in planning/slice-001/008_answers\.md, and the answers drawn "
                              r"again: python3 \".*answers\.py\" draw planning/slice-001")
        self.assertNotIn("answers.py\" next", out)

    def test_answers_or_questions_changed_after_the_drawing_are_to_be_drawn_again(self):
        folder = self.answered()
        (folder / "008_answers.md").write_text("# Answers\n\nChanged.\n", encoding="utf-8")
        self.assertIn("answers (its document: planning/slice-001/008_answers.md, to draw again: the questions or the answers changed after "
                      "slice-001/008_answered.md was drawn; only what the change brings is answered)", self.report())

    def test_what_research_adds_for_the_answers_or_from_a_test_does_not_send_the_session_back_to_the_questions(self):
        # Met building stage 9: research's second pass added a fact and the questions were named as next again.
        folder = self.answered()
        for heading in ("## Looked up for the answers", "## Shown by a test"):
            with (folder / "006_research/postbox.md").open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(f"\n{heading}\n- F90: Found later.\n")
            self.assertIn("- next stage by the documents: tests of open facts (", self.report(), heading)
        # A document whose lines end as Windows ends them is marked by its own bytes (met in CI: awk there rewrote them).
        document = folder / "006_research/postbox.md"
        document.write_bytes(b"- F1: First.\r\n- O1: An open point.\r\n- S1 AGREES: said.\r\n\r\n## Shown by a test\r\n- F91: Later.\r\n- O9: later too.\r\n")
        self.draw(folder / "007_questions", security=True)
        self.assertIn("- next stage by the documents: answers (", self.report())   # the questions hold; the answers are to draw again from them
        # Met on the real plans (the round): facts looked up later were added among the first ones, with no heading, and the questions went stale.
        document.write_bytes(b"- F1: First.\r\n- F50: Looked up later, with no heading.\r\n- O1: An open point.\r\n- S1 AGREES: said.\r\n\r\nNot opened: nothing.\r\n\r\n\r\n## Shown by a test\r\n- F91: Later.\r\n- F92: More.\r\n")
        self.assertIn("- next stage by the documents: answers (", self.report())
        document.write_bytes(b"- F1: First.\r\n- O1: An open point, changed.\r\n- S1 AGREES: said.\r\n")
        self.assertIn("- next stage by the documents: questions (", self.report())   # an open point changed is a question changed
        document.write_bytes(b"- F1: First.\r\n- O1: An open point.\r\n- S1 AGREES: said.\r\n")
        self.assertIn("- next stage by the documents: answers (", self.report())
        with (folder / "006_research/states.md").open("a", encoding="utf-8", newline="\n") as handle:
            handle.write("\nA row changed.\n")
        self.assertIn("- next stage by the documents: questions (", self.report())

    # The tests of open facts (stage 9): open-facts.md is the session's, tested.md the script's, with the
    # mark of the answers and the open facts and how many decisions still wait for the owner.
    OWNER = "\n## A2: Who may refund\nKind: owner\nSays: Not said.\nOptions: a | b\nRecommended: a.\nIf left: a.\nHarm: high\nSettles: W.who\n"

    def tested(self, waiting=0, drawn=True, **more):
        folder = self.answered(**more)
        (folder / "009_open-facts.md").write_text("# Open facts\n", encoding="utf-8", newline="\n")
        if drawn:
            mark = the_questions_script().cksum((folder / "008_answers.md").read_bytes() + (folder / "009_open-facts.md").read_bytes())
            (folder / "009_tested.md").write_text(f"# Tested\n\n<!-- drawn from: {mark}; waiting: {waiting} -->\n", encoding="utf-8")
        return folder

    def test_with_the_tests_next_the_report_gives_their_commands(self):
        self.answered()
        out = self.report()
        self.assertRegex(out, r"- the tests the answers leave, the gravest first, and the decisions for the owner not read yet: (CLAUDE_PLUGIN_DATA=\"[^\"]+\" )?python3 \".*openfacts\.py\" next planning/slice-001")
        self.assertRegex(out, r"a test is run, and what it printed kept, only by: .*openfacts\.py\" run planning/slice-001 T1")
        self.assertRegex(out, r"typed by the user at a hidden prompt, in a terminal of this VM, never in the conversation: CLAUDE_PLUGIN_DATA=\"[^\"]+\" python3 \".*openfacts\.py\" key NAME")
        self.assertRegex(out, r"looked up as the answers' look-ups are: python3 \".*answers\.py\" lookups planning/slice-001")
        self.assertRegex(out, r"read against the words it quotes by a second reader, which costs a little: .*openfacts\.py\" read planning/slice-001")
        self.assertRegex(out, r"checked and drawn together by script: .*openfacts\.py\" draw planning/slice-001")
        self.assertRegex(out, r"- a page of documentation is read with: python3 \".*page\.py\" fetch URL --to planning/slice-001/pages")

    def test_answers_that_leave_nothing_to_test_and_nothing_to_decide_need_no_tests_stage(self):
        self.answered(text="# Answers\n\n## A1: Chosen\nKind: chosen\nSays: x.\nRests on: y.\nSettles: L.a\n" + self.OWNER
                      + 'Decided: a (the user, 2026-11-25: "a")\n')
        out = self.report()
        self.assertIn("- tests of open facts: not needed, the answers leave nothing to test and nothing for the owner to decide (slice-001/008_answers.md)", out)
        self.assertIn("- next stage by the documents: design (its document: planning/slice-001/009_design.md)", out)
        self.assertNotIn("openfacts.py\" next", out)

    def test_a_decision_that_waits_for_the_owner_alone_keeps_the_tests_stage(self):
        self.answered(text="# Answers\n" + self.OWNER)
        self.assertIn("- next stage by the documents: tests of open facts (its document: planning/slice-001/009_open-facts.md)", self.report())

    def test_open_facts_written_and_not_drawn_keep_the_stage_next(self):
        self.tested(drawn=False)
        self.assertIn("- next stage by the documents: tests of open facts (its document: planning/slice-001/009_open-facts.md, written in, and not yet "
                      "drawn: the tests with no block and the decisions not read are still to do)", self.report())

    def test_the_stage_is_done_once_drawn_with_no_decision_waiting(self):
        self.tested()
        out = self.report()
        self.assertIn("tests of open facts (slice-001/009_open-facts.md)", out)
        self.assertIn("- next stage by the documents: design (its document: planning/slice-001/010_design.md)", out)
        self.assertRegex(out, r"recorded in planning/slice-001/008_answers\.md, and the answers and the open facts drawn again: .*openfacts\.py\" draw planning/slice-001")
        self.assertNotIn("out of order", out)

    def test_drawn_with_decisions_waiting_the_list_is_brought_before_the_design(self):
        self.tested(waiting=3)
        out = self.report()
        self.assertIn("- next stage by the documents: tests of open facts (its document: planning/slice-001/009_open-facts.md, drawn; 3 decisions wait for "
                      "the owner: their list is brought to them now, once, the gravest first, and each decision they take is recorded)", out)
        # Met in the pilot: a decision left "for now" stayed waiting, since the answers' text, which records decisions, knows nothing of leaving one.
        self.assertRegex(out, r"- a decision the owner takes on their list is recorded in planning/slice-001/008_answers\.md, and one they leave is recorded there too "
                              r"\(`Decided: left: <what happens then> \(the user, DATE: \"their words\"\)`\); both are then drawn again: .*openfacts\.py\" draw")

    def test_open_facts_changed_after_the_drawing_are_to_be_drawn_again(self):
        folder = self.tested()
        (folder / "009_open-facts.md").write_text("# Open facts\n\nChanged.\n", encoding="utf-8")
        self.assertIn("tests of open facts (its document: planning/slice-001/009_open-facts.md, to draw again: the answers or the open facts changed after "
                      "slice-001/009_tested.md was drawn)", self.report())

    def test_answers_changed_under_the_open_facts_come_first_and_nothing_is_called_out_of_order(self):
        folder = self.tested()
        (folder / "008_answers.md").write_text("# Answers\n\nChanged.\n", encoding="utf-8")
        out = self.report()
        self.assertIn("- next stage by the documents: answers (its document: planning/slice-001/008_answers.md, to draw again", out)
        self.assertNotIn("out of order", out)

    def test_a_security_file_changed_after_the_drawing_has_the_questions_drawn_again(self):
        self.secured()
        (self.machine.project / "planning/slice-001/007_questions/security.md").write_text("# Security\n\nChanged.\n", encoding="utf-8")
        self.assertIn("- next stage by the documents: questions (its document: planning/slice-001/007_questions/, to draw again", self.report())

    def test_security_skipped_at_the_users_word_is_done_once_drawn_and_is_said(self):
        out = self.secured(text="Skipped at the user's word, 2026-11-25: \"no\"\n")
        self.assertIn("- security: skipped at the user's word (slice-001/007_questions/security.md); every fixed question is drawn, "
                      "and the skipping is for the owner's list\n", out)
        self.assertIn("- next stage by the documents: answers", out)

    def test_nothing_is_said_of_security_before_the_questions_are_drawn(self):
        out = self.asked(draw=False)
        self.assertIn("- next stage by the documents: questions", out)
        self.assertNotIn("security.md", out)

    def test_while_the_questions_are_next_the_commands_that_read_the_library_and_draw_are_given(self):
        out = self.researched("postbox.md", "states.md", inventory="- a loan")
        self.assertIn("- next stage by the documents: questions (its document: planning/slice-001/007_questions/, to write there: kept.md", out)
        self.assertRegex(out, r'questions\.py" things planning/slice-001\n')
        self.assertRegex(out, r'questions\.py" library KIND KIND')
        self.assertRegex(out, r'questions\.py" draw planning/slice-001\n')
        self.assertNotIn("page.py", out)

    def test_an_empty_questions_folder_is_the_one_named_and_is_not_the_questions_done(self):
        out = self.asked(kept=None, draw=False)
        self.assertIn("questions (its document: planning/slice-001/007_questions/, to write there: kept.md", out)
        self.assertNotIn("008_questions", out)

    def test_a_kept_file_not_yet_drawn_from_keeps_the_questions_next(self):
        out = self.asked(draw=False)
        self.assertIn("questions (its document: planning/slice-001/007_questions/, kept.md is written there; questions.md is still to be drawn from it)", out)

    def test_a_document_changed_after_the_drawing_makes_the_questions_next_again(self):
        for changed in ("004_slice.md", "005_approach.md", "006_research/states.md", "007_questions/kept.md"):
            with self.subTest(changed):
                self.setUp()
                self.asked()
                with (self.machine.project / "planning/slice-001" / changed).open("a", encoding="utf-8") as handle:
                    handle.write("One more line.\n")
                out = self.report()
                self.assertIn("questions (its document: planning/slice-001/007_questions/, to draw again: a document of the slice, or kept.md, changed", out)
                self.assertNotIn("questions (slice-001/007_questions/)", out)

    def test_a_drawing_with_no_mark_is_not_the_questions_done(self):
        self.asked(draw=False)
        (self.machine.project / "planning/slice-001/007_questions/questions.md").write_text("# Questions\n\nWritten by hand.\n", encoding="utf-8")
        self.assertIn("to draw again", self.report())

    def test_skipped_at_the_users_word_is_done_once_drawn_and_is_said(self):
        out = self.asked(kept="Skipped at the user's word.\n", basis="skipped.md")
        self.assertIn("- questions: skipped at the user's word (slice-001/007_questions/skipped.md); what needs no judgement is drawn, "
                      "and the skipping is for the owner's list\n", out)
        self.assertIn("- next stage by the documents: security", out)   # a skip of the questions is not a skip of security

    def test_skipped_and_not_yet_drawn_keeps_the_questions_next(self):
        out = self.asked(kept="Skipped at the user's word.\n", basis="skipped.md", draw=False)
        self.assertIn("skipped.md is written there; questions.md is still to be drawn from it", out)

    def test_what_the_script_draws_is_what_this_script_counts_as_drawn(self):
        script = the_questions_script()
        rows = "".join(f"| {kind}: all | dropped | the slice does nothing of the kind |\n" for kind in
                       sorted({entry["action"] for entry in __import__("json").loads(script.LIBRARY.read_text(encoding="utf-8"))}))
        for basis, text in (("kept.md", "# Kept\n\n## What the slice creates and keeps\n- nothing\n\n## Other things the slice has\n- `loan-form`: where a loan is typed in (record-a-loan / 1)\n\n## Library\n| Entry | Applies to | Why |\n|---|---|---|\n" + rows), ("skipped.md", "Skipped.\n")):
            with self.subTest(basis):
                self.setUp()
                self.asked(kept=text, basis=basis, draw=False)
                said = io.StringIO()
                self.assertEqual(script.main(["draw", str(self.machine.project / "planning/slice-001")], said), 0, said.getvalue())
                self.assertIn("- next stage by the documents: security", self.report())
                # ... and with the security file, drawn again by the script itself, the mark is still the one counted.
                (self.machine.project / "planning/slice-001/007_questions/security.md").write_text(
                    "Skipped at the user's word, 2026-11-25: \"no\"\n", encoding="utf-8")
                self.assertIn("still to be drawn again with it", self.report())
                self.assertEqual(script.main(["draw", str(self.machine.project / "planning/slice-001")], said), 0, said.getvalue())
                self.assertIn("- next stage by the documents: answers", self.report())

    def test_nothing_committed_to_still_has_the_states_to_write(self):
        out = self.researched(approach=the_approach("Decision: without"), inventory="- a loan")
        self.assertIn("to write there: states.md)", out)
        self.assertIn("- nothing is committed to in planning/slice-001/005_approach.md: no outside system is researched\n", out)

    def test_after_a_changed_approach_research_is_next_again_for_what_is_newly_committed_to(self):
        self.researched("postbox.md", "states.md", inventory="- a loan")
        (self.machine.project / "planning/slice-001/007_approach.md").write_text(
            the_approach("Decision: committed: Lettera", committed=["Lettera: https://lettera.example/docs, for telling the member."]),
            encoding="utf-8")
        out = self.report()
        self.assertIn("approach (slice-001/007_approach.md)", out)
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, "
                      "still to write there: lettera.md)", out)
        self.assertIn("- no longer stands, its thing is not committed to in slice-001/007_approach.md: "
                      "planning/slice-001/006_research/postbox.md (it is left as it is, but for a first line to be added that says so)\n", out)
        self.assertIn("- a changed approach is a new document, the earlier one left as it is: planning/slice-001/008_approach.md", out)
        self.machine.document("slice-001/006_research/lettera.md")
        out = self.report()
        self.assertIn("- next stage by the documents: questions", out)
        self.assertIn("- no longer stands", out)

    def test_the_pages_already_kept_are_counted_with_the_command_that_lists_them(self):
        self.researched(inventory="- a loan")
        self.assertNotIn("already kept", self.report())
        for name in ("docs.postbox.example.txt", "docs.postbox.example-pricing.txt"):
            self.machine.document(f"slice-001/pages/{name}")
        self.assertRegex(self.report(), r'\n- 2 pages are already kept in planning/slice-001/pages, read from their copies: '
                                        r'python3 "[^"\n]+' + self.PAGE + r" kept planning/slice-001/pages\n")

    def test_a_new_approach_with_a_need_waiting_is_the_one_counted(self):
        self.approached(the_approach("Decision: without"))
        (self.machine.project / "planning/slice-001/006_approach.md").write_text(the_approach("Decision: waiting"), encoding="utf-8")
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/006_approach.md, "
                      "corrected in place: 1 of its needs still waiting", self.report())

    def test_a_coming_back_due_is_said_before_anything_of_the_approach(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tRecord a loan"])
        self.assertIn("- next stage by the documents: slice, the coming-back", out)
        self.assertNotIn("page.py", out)

    def test_an_empty_research_folder_is_not_research_done(self):
        self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it")),
                     slices={1: the_slice("record-a-loan / 1")})
        self.machine.document("slice-001/005_approach.md")
        (self.machine.project / "planning" / "slice-001" / "006_research").mkdir()
        out = self.report()
        # Found by the pilot: with the folder there and empty, the report named a second one, 007_research.
        self.assertIn("- next stage by the documents: research (its document: planning/slice-001/006_research/, to write there: states.md)", out)
        self.assertNotIn("007_research", out)

    def test_the_chosen_slice_is_the_one_read_whatever_other_folders_exist(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan"), row(2, "built", "record-a-return"),
                                   row(3, "open", "see-who-has-it")),
                           documents=[f"slice-002/{5 + place:03d}_{name}.md" for place, name in enumerate(THE_REST)],
                           list_text=LIST.replace("- [ ] **record-a-return**", "- [x] **record-a-return**"),
                           slices={1: the_slice("record-a-loan / 1"), 2: the_slice("record-a-return / 1", number=2)})
        self.assertIn("slice (slice-001/004_slice.md)", out)
        self.assertIn("- next stage by the documents: approach (its document: planning/slice-001/", out)

    def test_a_slice_fully_planned_is_ready_to_build(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it")),
                           documents=[f"slice-001/{5 + place:03d}_{name}.md" for place, name in enumerate(THE_REST)],
                           slices={1: the_slice("record-a-loan / 1")})
        at = self.machine.project / "planning/slice-001/007_questions"
        at.mkdir()
        (at / "kept.md").write_text("Kept.\n", encoding="utf-8")
        (at / "security.md").write_text("# Security\n", encoding="utf-8")
        together = b"".join(path.read_bytes() for path in [at.parent / "004_slice.md", at.parent / "005_approach.md",
                                                           *sorted((at.parent / "006_research").glob("*.md")), at / "kept.md", at / "security.md"])
        (at / "questions.md").write_text(f"<!-- drawn from: {the_questions_script().cksum(together)} -->\n", encoding="utf-8")
        answers = next(at.parent.glob("*_answers.md"))
        mark = the_questions_script().cksum((at / "questions.md").read_bytes() + answers.read_bytes())
        answers.with_name(answers.name.replace("_answers", "_answered")).write_text(f"<!-- drawn from: {mark} -->\n", encoding="utf-8")
        tests = next(at.parent.glob("*_open-facts.md"))
        mark = the_questions_script().cksum(answers.read_bytes() + tests.read_bytes())
        tests.with_name(tests.name.replace("_open-facts", "_tested")).write_text(f"<!-- drawn from: {mark}; waiting: 0 -->\n", encoding="utf-8")
        out = self.report()
        self.assertIn("- every planning document of slice 1 exists", out)
        self.assertIn("- next stage by the documents: none, slice 1 is planned and ready to build", out)

    # The set of slices is counted (condition 22 of the slice stage).
    def test_the_slices_are_counted_by_their_states(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan"), row(2, "**chosen**", "`record-a-return`"),
                                   row(3, "Open", "see-who-has-it"), row(4, "open (waits for an answer)", "see-who-has-it")))
        self.assertIn("- slices (003_slices.md): 4 slices, 1 built, 1 chosen, 2 open\n", out)
        self.assertNotIn("no slice", out)
        self.assertNotIn("does not hold", out)

    def test_an_item_in_no_slice_is_said(self):
        out = self.planned(the_set(row(1, "open", "record-a-loan")))
        self.assertIn("- slices (003_slices.md): 1 slice, 0 built, 0 chosen, 1 open\n", out)
        self.assertIn("- a requirement in no slice: record-a-return, see-who-has-it\n", out)

    def test_an_item_the_requirements_do_not_hold_is_said_with_its_slice(self):
        out = self.planned(the_set(row(1, "open", "record-a-loan, record-a-return, see-who-has-it, reserve-a-tool")))
        self.assertIn("- a slice names an item the requirements do not hold: reserve-a-tool (slice 1)\n", out)

    def test_a_state_it_does_not_know_is_said(self):
        out = self.planned(the_set(row(1, "open", "record-a-loan, record-a-return"), row(2, "nearly", "see-who-has-it")))
        self.assertIn("- a slice whose state is not built, chosen or open: slice 2\n", out)

    def test_a_set_with_no_table_it_can_read_is_said(self):
        out = self.planned("# Slices\n\n1. Record a loan (record-a-loan)\n")
        self.assertIn("- the set of slices (003_slices.md) has no table this script can read: its columns are "
                      "# | Slice | Items | Builds on | State", out)
        self.assertIn("- next stage by the documents: slice (the set is to be written as that table", out)

    def test_two_slices_chosen_at_once_is_said(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return"), row(2, "chosen", "see-who-has-it")))
        self.assertIn("- more than one slice is chosen: slice 1, slice 2 (the first is read)\n", out)

    def test_the_latest_version_of_the_set_is_the_one_read(self):
        self.planned(THREE)
        (self.machine.project / "planning" / "005_slices-v002.md").write_text(
            the_set(row(1, "built", "record-a-loan"), row(4, "open", "record-a-return, see-who-has-it")), encoding="utf-8")
        out = self.report()
        self.assertIn("- slices (005_slices-v002.md): 2 slices, 1 built, 0 chosen, 1 open\n", out)

    def test_the_criteria_of_the_chosen_slice_are_counted(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it")),
                           slices={1: the_slice("record-a-loan / 1", "record-a-loan/2", "see-who-has-it / 1")})
        self.assertIn("- slice 1 (slice-001/004_slice.md): 3 criteria\n", out)
        self.assertNotIn("names no item", out)

    def test_documents_are_numbered_on_past_seven(self):
        # 008 and 009 are no numbers to a shell that reads a leading zero as base eight.
        self.chosen("000_problem.md", "001_scope-map.md", *[f"00{n}_scope-map-v00{n}.md" for n in range(2, 8)],
                    "008_requirements.md")
        self.assertIn("slice (its document: planning/009_slices.md, the set of slices; once the user has chosen "
                      "one, its own document: planning/slice-NNN/010_slice.md", self.report())

    def test_a_slice_marked_built_with_its_box_unchecked_has_the_box_due(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan"), row(2, "open", "record-a-return, see-who-has-it")),
                           tracker=[])
        self.assertIn("  - every slice of record-a-loan is built: check its box in planning/002_requirements.md", out)

    def test_a_criterion_that_names_no_item_is_said_by_its_line(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it")),
                           slices={1: the_slice("record-a-loan / 1", "lend-a-tool / 1", "a refusal")})
        self.assertIn("- slice 1 (slice-001/004_slice.md): 3 criteria\n", out)
        self.assertIn("- a criterion that names no item of the requirements: line 8, line 9\n", out)

    # A changed set (condition 20): corrected in place until a slice is built from it.
    def test_a_changed_set_is_corrected_in_place_until_a_slice_is_built_from_it(self):
        out = self.planned(THREE)
        self.assertIn("- a changed set is corrected in place (planning/003_slices.md): no slice is built from it yet\n", out)

    def test_a_changed_set_is_a_new_version_once_a_slice_is_built(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan"), row(2, "chosen", "record-a-return, see-who-has-it")),
                           slices={1: the_slice("record-a-loan / 1"), 2: the_slice("record-a-return / 1", number=2)})
        self.assertIn("- a changed set is a new document, the earlier one left as it is: planning/005_slices-v002.md\n", out)

    # The coming-back (conditions 14 and 15): due by what merged work names and by issues not placed.
    BUILDING = the_set(row(1, "chosen", "record-a-loan"), row(2, "open", "record-a-return, see-who-has-it", on="1"))

    def test_with_nothing_merged_and_no_issue_no_coming_back_is_due(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1", "record-a-loan / 2")}, tracker=[])
        self.assertNotIn("coming-back", out)
        self.assertIn("- next stage by the documents: approach", out)

    def test_merged_work_naming_every_criterion_of_a_slice_makes_a_coming_back_due(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1", "record-a-loan / 2")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1, record-a-loan/2\tRecord a loan"])
        self.assertIn("- a coming-back to the slices is due:\n"
                      "  - slice 1 is built by merged work (#12): mark it built in planning/003_slices.md\n"
                      "  - every slice of record-a-loan is built: check its box in planning/002_requirements.md\n", out)
        self.assertIn("- next stage by the documents: slice, the coming-back (before anything else is planned)", out)
        self.assertNotIn("activity is done", out)
        self.assertIn("a changed set is a new document", out)

    def test_criteria_named_without_their_slice_are_those_of_the_chosen_one(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\trecord-a-loan / 1\tRecord a loan"])
        self.assertIn("  - slice 1 is built by merged work (#12)", out)

    def test_two_merges_that_together_name_every_criterion_build_the_slice(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1", "record-a-loan / 2")},
                           tracker=["merged\t13\tslice 1: record-a-loan / 2\tThe refusal",
                                    "merged\t12\tslice 1: record-a-loan / 1\tRecord a loan"])
        self.assertIn("  - slice 1 is built by merged work (#12, #13)", out)

    def test_merged_work_naming_part_of_a_slice_is_said_and_nothing_is_due(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1", "record-a-loan / 2")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tRecord a loan"])
        # Found by the closing pass: with both criteria of one item merged and the slice half built, 2 runs of 5
        # checked that item's box on the user's word.
        self.assertIn("- merged work (#12) names 1 of the 2 criteria of slice 1: not built yet, so nothing is marked or "
                      "checked for it; still to come: record-a-loan / 2\n", out)
        self.assertNotIn("coming-back", out)

    def test_a_criterion_merged_work_names_that_the_slice_does_not_hold_is_said(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1, record-a-loan / 7\tRecord a loan"])
        self.assertIn("- merged work names what no slice's document holds: record-a-loan / 7 of slice 1 (#12)\n", out)

    def test_an_item_is_checked_only_when_every_slice_of_it_is_built(self):
        both = the_set(row(1, "chosen", "record-a-loan"), row(2, "open", "record-a-loan, record-a-return, see-who-has-it"))
        out = self.planned(both, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tRecord a loan"])
        self.assertIn("  - slice 1 is built by merged work (#12)", out)
        self.assertNotIn("check its box", out)

    def test_an_item_merged_work_names_outright_has_its_box_checked(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1", "record-a-loan / 2")},
                           tracker=["merged\t12\tsee-who-has-it\tA list of loans"])
        self.assertIn("  - merged work names see-who-has-it as complete (#12): check its box in "
                      "planning/002_requirements.md\n", out)

    def test_work_already_taken_in_makes_nothing_due(self):
        taken = the_set(row(1, "built", "record-a-loan"), row(2, "open", "record-a-return, see-who-has-it"))
        out = self.planned(taken, list_text=LIST.replace("- [ ] **record-a-loan**", "- [x] **record-a-loan**"),
                           slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tRecord a loan"])
        self.assertNotIn("coming-back", out)
        self.assertNotIn("merged work", out)
        self.assertIn("- next stage by the documents: slice (the user chooses where to start", out)

    def test_an_open_issue_the_set_has_not_placed_makes_a_coming_back_due(self):
        placed = the_set(row(1, "chosen", "record-a-loan"), row(2, "open", "record-a-return, see-who-has-it"),
                         more="\n## Issues\n- #14: slice 2, it is about returns.\n")
        out = self.planned(placed, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["issue\t14\tbug\tA return is lost", "issue\t15\t-\tLoans show twice",
                                    "issue\t140\t-\tA typo"])
        self.assertIn('- a coming-back to the slices is due:\n  - open issues not placed yet (each is placed, by its number, in '
                      'planning/003_slices.md): #15 "Loans show twice", #140 "A typo"\n', out)
        self.assertIn("- next stage by the documents: slice, the coming-back", out)

    def test_an_issue_placed_in_an_earlier_version_of_the_set_stays_placed(self):
        earlier = the_set(row(1, "built", "record-a-loan"), more="\n## Issues\n- #15: slice 1.\n")
        self.planned(earlier, tracker=["issue\t15\t-\tLoans show twice"])
        (self.machine.project / "planning" / "004_slices-v002.md").write_text(
            the_set(row(1, "built", "record-a-loan"), row(2, "open", "record-a-return, see-who-has-it")), encoding="utf-8")
        self.assertNotIn("not placed", self.report())

    def test_issues_are_not_placed_before_there_is_a_set(self):
        self.machine.repository(REMOTE)
        self.chosen(*THROUGH_REQUIREMENTS)
        self.machine.have("gh")
        self.machine.set("gh/lines", "ok\t0\t1\nissue\t15\t-\tLoans show twice")
        out = self.report()
        self.assertNotIn("coming-back", out)
        self.assertEqual([call for call in self.machine.calls() if call.startswith("gh")], [])

    def test_the_last_slice_merged_is_said_to_finish_the_activity(self):
        last = the_set(row(1, "built", "record-a-loan"), row(2, "chosen", "record-a-return, see-who-has-it"))
        out = self.planned(last, list_text=LIST.replace("- [ ] **record-a-loan**", "- [x] **record-a-loan**"),
                           slices={1: the_slice("record-a-loan / 1"),
                                   2: the_slice("record-a-return / 1", "see-who-has-it / 1", number=2)},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tRecord a loan",
                                    "merged\t16\tslice 2: record-a-return / 1, see-who-has-it / 1\tReturns"])
        self.assertIn("  - slice 2 is built by merged work (#16): mark it built", out)
        self.assertIn("  - every slice of record-a-return is built: check its box", out)
        self.assertIn("  - every slice of see-who-has-it is built: check its box", out)
        self.assertIn("  - with those, every slice is built and every requirement checked: the activity is done\n", out)

    def test_an_activity_with_everything_built_and_checked_is_done(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan, record-a-return, see-who-has-it")),
                           list_text=LIST.replace("- [ ]", "- [x]"), tracker=[])
        self.assertIn("- next stage by the documents: none: every slice of this activity is built and every "
                      "requirement checked; which row of the scope map is the next \"now\" is the user's to say", out)

    def test_a_set_the_script_fails_on_is_refused_not_passed_over(self):
        # Found while the script was written: a fault in reading the set left the report silent and wrong.
        self.planned(THREE)
        real = pathlib.Path(shutil.which("awk")).as_posix()
        (self.machine.bin / "awk").write_text(
            f'#!/bin/sh\ncase "$*" in *kind=work*) exit 2 ;; esac\nexec "{real}" "$@"\n', encoding="utf-8", newline="\n")
        (self.machine.bin / "awk").chmod(0o755)
        done = self.machine.run("stage.sh", "report")
        self.assertEqual(done.returncode, 3, done.stdout)
        self.assertIn("- REFUSED: the set of slices (planning/003_slices.md) could not be read", done.stdout)
        self.assertNotIn("next stage", done.stdout)

    # Found by an end-to-end run: a list of one item with eight questions open under it was cut into one
    # slice that did not wait for them, the slice was merged, the box checked, and the activity called done.
    OPEN = LIST + "\n## Not yet confirmed\n1. **Who sees a loan** (bears on record-a-loan). It may add an item.\n" \
                  "- Whether a loan can be put right.\n  It changes record-a-loan.\n\n## Outside systems and lasting things\n- a loan\n"

    def test_an_activity_is_not_done_while_a_question_of_the_list_is_open(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan, record-a-return, see-who-has-it")),
                           list_text=self.OPEN.replace("- [ ]", "- [x]"), tracker=[])
        self.assertNotIn("activity is done", out)
        self.assertNotIn("the next \"now\"", out)
        self.assertIn("- next stage by the documents: requirements (every slice cut so far is built, and 2 questions of "
                      "planning/002_requirements.md are not yet confirmed: their answers may add to the list, and the "
                      "activity is not done before them)", out)

    def test_the_last_slice_merged_does_not_finish_an_activity_with_a_question_open(self):
        out = self.planned(the_set(row(1, "chosen", "record-a-loan, record-a-return, see-who-has-it")),
                           list_text=self.OPEN, slices={1: the_slice("record-a-loan / 1")},
                           tracker=["merged\t12\tslice 1: record-a-loan / 1\tLoans"])
        self.assertIn("  - slice 1 is built by merged work (#12)", out)
        self.assertNotIn("the activity is done", out)
        self.assertIn("  - with those, every slice cut so far is built, and 2 questions of the list are not yet confirmed: "
                      "the activity is not done, and the requirements stage takes them next\n", out)

    def test_a_list_with_nothing_open_says_nothing_of_questions(self):
        out = self.planned(the_set(row(1, "built", "record-a-loan, record-a-return, see-who-has-it")),
                           list_text=LIST.replace("- [ ]", "- [x]") + "\n## Not yet confirmed\nNothing.\n", tracker=[])
        self.assertIn("which row of the scope map is the next \"now\"", out)

    def test_a_tracker_that_cannot_be_read_leaves_the_coming_back_unknown(self):
        out = self.planned(self.BUILDING, slices={1: the_slice("record-a-loan / 1")}, tracker=["what is this"])
        self.assertIn("- whether a coming-back to the slices is due is not known: the tracker could not be read\n", out)
        self.assertIn("- next stage by the documents: approach", out)

    def test_a_document_takes_the_next_number_in_the_folder_whatever_came_before(self):
        self.chosen("000_problem.md", "001_scope-map.md", "002_scope-map-v002.md")
        out = self.report()
        self.assertIn("scope map (002_scope-map-v002.md)", out)
        self.assertIn("- next stage by the documents: requirements (its document: planning/003_requirements.md)", out)

    def test_a_document_is_found_by_its_name_not_its_number(self):
        self.chosen("000_problem.md", "001_scope-map.md", "005_requirements.md")
        out = self.report()
        self.assertIn("requirements (005_requirements.md)", out)
        self.assertIn("- next stage by the documents: slice (its document: planning/006_slices.md, the set of "
                      "slices; once the user has chosen one, its own document: planning/slice-NNN/007_slice.md", out)

    def requirements(self, text):
        self.chosen("000_problem.md", "001_scope-map.md")
        (self.machine.project / "planning" / "002_requirements.md").write_text(text, encoding="utf-8")
        return self.report()

    def test_the_requirements_are_counted_and_the_checked_ones_too(self):
        out = self.requirements("# Requirements: borrow a tool\n\n"
                                "- [x] **record-a-loan**: A volunteer records who took which tool.\n"
                                "- [ ] **see-who-has-it**: A volunteer sees who has a tool.\n"
                                "* [X] **loans-of-a-member**: A volunteer sees what a member has out.\n\n"
                                "## Out for now\n- Reserving a tool.\n")
        self.assertIn("- requirements (002_requirements.md): 3 items, 2 checked", out)
        self.assertNotIn("no name", out)
        self.assertNotIn("twice", out)

    def test_a_requirement_with_no_name_of_its_own_is_said_by_its_line(self):
        out = self.requirements("- [ ] **record-a-loan**: A volunteer records a loan.\n"
                                "- [ ] A volunteer sees who has a tool.\n"
                                "- [ ] **Sees Loans**: A volunteer sees the loans.\n")
        self.assertIn("- requirements (002_requirements.md): 3 items, 0 checked", out)
        self.assertIn("- a requirement with no short name of its own: line 2, line 3", out)

    def test_a_name_used_twice_is_said_once(self):
        out = self.requirements("- [ ] **record-a-loan**: One.\n- [x] **record-a-loan**: Two.\n"
                                "- [ ] **record-a-loan**: Three.\n")
        self.assertIn("- a requirement's name used more than once: record-a-loan\n", out)

    def test_a_requirements_document_with_no_box_counts_none(self):
        out = self.requirements("# Requirements\n\nA member adds a book.\n- a plain bullet\n")
        self.assertIn("- requirements (002_requirements.md): 0 items, 0 checked", out)

    def test_nothing_is_counted_before_the_requirements_exist(self):
        self.chosen("000_problem.md", "001_scope-map.md")
        self.assertNotIn("items", self.report())

    # Found by the first end-to-end run: a session asked for the folder and never recorded it, so
    # every document went unnumbered and unfound; and a session that finished a stage had no way
    # to learn the next one's document.
    def test_an_unchosen_folder_comes_with_the_command_that_records_it(self):
        out = self.report()
        self.assertRegex(out, r'- to record the folder the user names \(it is made if it is not there\): '
                              r'.*sh ".*stage\.sh" remember FOLDER')
        self.assertIn("then read the documents again", out)

    def test_a_command_the_report_gives_reaches_the_same_record_as_the_report(self):
        # A session runs these commands in its own shell, which is not told where the plugin keeps its data.
        out = self.report()
        self.assertIn(f'CLAUDE_PLUGIN_DATA="{self.machine.data.as_posix()}" sh "', out)
        self.chosen("000_problem.md")
        self.assertIn(f'read the documents again: CLAUDE_PLUGIN_DATA="{self.machine.data.as_posix()}" sh "', self.report())

    def test_remembering_a_folder_that_is_not_there_makes_it(self):
        done = self.machine.run("stage.sh", "remember", "docs/planning")
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertTrue((self.machine.project / "docs" / "planning").is_dir())
        self.assertIn("- next stage by the documents: problem (its document: docs/planning/000_problem.md)",
                      self.report())

    def test_a_full_path_inside_the_project_is_recorded_as_the_folder_inside_it(self):
        # Found by the end-to-end runs: a session gave the folder by its full path and was refused.
        done = self.machine.run("stage.sh", "remember", (self.machine.project / "planning").as_posix())
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertIn("- planning folder: planning (chosen earlier for this project)", self.report())

    def test_a_folder_outside_the_project_is_refused(self):
        self.assertEqual(self.machine.run("stage.sh", "remember", "../elsewhere").returncode, 3)
        self.assertEqual(self.machine.run("stage.sh", "remember", "/tmp/elsewhere").returncode, 3)

    def test_the_report_says_how_the_documents_are_read_again(self):
        self.chosen("000_problem.md")
        self.assertRegex(self.report(), r'- after a stage is finished, read the documents again: .*sh ".*stage\.sh" report')

    def test_the_report_says_how_a_file_of_the_users_is_described(self):
        self.chosen("000_problem.md")
        out = self.report()
        self.assertIn("- a file of the user's (a sheet, an export) is never opened here", out)
        self.assertRegex(out, r"source\.sh describe FILE")

    def test_a_remembered_folder_that_is_gone_is_said(self):
        self.chosen()
        (self.machine.project / "planning").rmdir()
        out = self.report()
        self.assertIn("- planning folder: planning (chosen earlier for this project) no longer exists", out)
        # Found by an end-to-end run started twice in one place: with no command to record a folder again,
        # the session wrote every document without its number and never read the documents again.
        self.assertRegex(out, r'- to record the folder the user names \(it is made if it is not there\): .*stage\.sh" remember FOLDER')
        self.assertIn("then read the documents again", out)

    def test_remembering_no_folder_is_refused(self):
        self.assertEqual(self.machine.run("stage.sh", "remember").returncode, 3)


if __name__ == "__main__":
    unittest.main()
