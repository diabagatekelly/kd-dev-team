"""The slice stage's checks, graded for nothing on documents written by hand: a check must pass
the document this stage's text describes and fail the fault it is there for, before any run."""
import contextlib
import importlib.util
import io
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


cases = load("slice_cases", HERE / "make_cases.py")
regrade = load("regrade", ROOT / "e2e/regrade.py")
CHECKS = {name: checks for name, _, _, _, _, _, _, checks, _, _, _ in cases.SCENARIOS}
SLICE_1 = "planning/slice-001/004_slice.md"
ROTA_SLICE = """# Slice 1: Enter one person's shifts for the week and email them to that person

## Thin path
The manager enters one member of staff's shifts for next week and sends them; that person gets an email of their shifts.

## Criteria
- **enter-the-week / 1**: Given no shifts are entered for next week, when the manager enters Monday 9 to 5 for Dana, then Dana's week shows Monday 9 to 5.
- **enter-the-week / 2**: Given Dana has Monday 9 to 5, when the manager enters a shift for Dana that ends before it starts, then the shift is refused and the manager is told why.
- **send-the-rota / 1**: Given Dana has Monday 9 to 5 entered, when the manager sends Dana her shifts, then Dana receives an email that lists Monday 9 to 5.

## Needs from outside
- Sending an email to a member of staff.

## Left for later
- The whole week for everyone: slice 2. Usable without it: the manager sends one person at a time.

## Size
Criteria: 3.
"""
RACE_SLICE = """# Slice 1: Register a runner and see them on the start list

## Thin path
A volunteer registers a runner on the day and sees them on the start list.

## Criteria
- **register-a-runner / 1**: Given the start list is empty, when a volunteer registers Sam Doe, then Sam Doe is on the start list.
%s
## Needs from outside
none

## Left for later
%s
## Size
Criteria: 1.
"""


def failed(scenario, files, last="", calls=(), record=""):
    """The names of a scenario's checks that fail on these files, this last message and these tool calls."""
    return [check["name"] for check in CHECKS[scenario]
            if regrade.passes(check, last, files, list(calls), record) is False]


class Checks(unittest.TestCase):
    def test_a_set_as_the_text_describes_it_passes_every_check_of_the_first_scenario(self):
        files = {cases.SET: cases.ROTA_SET, cases.LIST: cases.ROTA_LIST}
        self.assertEqual(failed("01-a-list-of-four-items", files, cases.ROTA_SHOWN), [])

    def test_a_set_that_leaves_an_item_out_or_writes_criteria_fails(self):
        files = {cases.SET: cases.ROTA_SET.replace("start-from-last-week", "") + "\nGiven a week, when it is sent, then it arrives.\n"}
        self.assertEqual(failed("01-a-list-of-four-items", files, cases.ROTA_SHOWN),
                         ["every-item-is-in-the-set", "no-criteria-in-the-set"])

    def test_a_set_with_no_table_fails_only_its_form(self):
        prose = "# Slices\n\n1. Enter and send one person's shifts (enter-the-week, send-the-rota).\n2. Change a shift (change-a-shift).\n" \
                "3. Copy a week (start-from-last-week).\n"
        self.assertTrue(all(name.startswith("form-") for name in failed("01-a-list-of-four-items", {cases.SET: prose}, cases.ROTA_SHOWN)))

    def test_a_reply_that_neither_recommends_nor_asks_fails(self):
        self.assertEqual(failed("01-a-list-of-four-items", {cases.SET: cases.ROTA_SET}, "Here are four slices."),
                         ["recommends-a-start", "asks-the-user"])

    def test_a_slice_as_the_text_describes_it_passes(self):
        files = {cases.SET: cases.ROTA_SET.replace("| nothing | open |", "| nothing | chosen |"), SLICE_1: ROTA_SLICE}
        self.assertEqual(failed("02-the-user-chooses", files), [])

    def test_a_slice_with_a_provider_a_layout_or_a_later_stages_criterion_fails(self):
        chosen = cases.ROTA_SET.replace("| nothing | open |", "| nothing | chosen |")
        for fault, check in (("then Dana receives an email", "then SendGrid delivers an email"), "nothing-of-how"), \
                            (("when the manager sends Dana her shifts", "when the manager clicks the Send button"), "nothing-of-how"), \
                            (("then the shift is refused and the manager is told why", "then, if the email service is down, the manager is told"),
                             "none-of-the-later-stages-criteria"), \
                            (("- **send-the-rota / 1**", "- **the email**"), "form-no-criterion-without-its-item"), \
                            (("- Sending an email to a member of staff.", "none"), "says-what-it-needs-from-outside"):
            self.assertEqual(failed("02-the-user-chooses", {cases.SET: chosen, SLICE_1: ROTA_SLICE.replace(*fault)}), [check], fault)

    def test_one_slice_passes_and_a_made_up_set_fails(self):
        one = "# Slices: See whether the hall is free on a date\n\n| # | Slice | Items | Builds on | State |\n|---|---|---|---|---|\n" \
              "| 1 | See whether the hall is free on a date | see-a-date | nothing | chosen |\n\n## Where to start\nSlice 1.\n"
        self.assertEqual(failed("03-a-list-of-one-small-item", {cases.SET: one}), [])
        two = one.replace("\n\n## Where", "\n| 2 | See a whole month | see-a-date | 1 | open |\n\n## Where")
        self.assertEqual(failed("03-a-list-of-one-small-item", {cases.SET: two}), ["one-slice-and-no-more"])

    def test_a_slice_that_waits_for_an_answer_is_said_to(self):
        self.assertEqual(failed("04a-an-item-with-an-open-question", {cases.SET: cases.RACE_SET}, cases.RACE_SHOWN), [])
        silent = cases.RACE_SET.replace(" Slice 3 cannot be started until the question of who sees whose result is answered, and it waits for 1 and 2.", "")
        self.assertIn("says-the-slice-cannot-be-started", failed("04a-an-item-with-an-open-question", {cases.SET: silent}, cases.RACE_SHOWN))

    def test_a_comparison_names_its_key_or_is_left_for_later(self):
        chosen = cases.RACE_SET.replace("| register-a-runner | nothing | open |", "| register-a-runner | nothing | chosen |")
        left = "- Refusing a runner who is already registered: what makes two registrations the same runner is not said. " \
               "Slice 1, later. Usable without it: a volunteer can see a name twice on the start list and remove one.\n"
        keyed = "- **register-a-runner / 2**: Given Sam Doe is registered, when a volunteer registers a runner with the same name " \
                "and date of birth, then the registration is refused as a duplicate.\n"
        bare = "- **register-a-runner / 2**: Given Sam Doe is already registered, when a volunteer registers Sam Doe, then it is refused.\n"
        usable = "- Publishing: slice 3. Usable without it: the paper sheet.\n"
        self.assertEqual(failed("04b-a-comparison-needs-its-key", {cases.SET: chosen, SLICE_1: RACE_SLICE % ("", left)}), [])
        self.assertEqual(failed("04b-a-comparison-needs-its-key", {cases.SET: chosen, SLICE_1: RACE_SLICE % (keyed, usable)}), [])
        self.assertEqual(failed("04b-a-comparison-needs-its-key", {cases.SET: chosen, SLICE_1: RACE_SLICE % (bare, usable)}),
                         ["the-comparison-names-its-key-or-is-left-for-later", "no-comparison-asserted-without-its-key"])

    def test_pushing_back_passes_and_giving_way_at_once_fails(self):
        files = {cases.SET: cases.ROTA_SET}
        self.assertEqual(failed("05-everything-in-the-first-and-a-technology", files, cases.HELD), [])
        gave = [("Edit", '{"file_path": "/x/planning/003_slices.md", "old_string": "a", "new_string": "b"}')]
        record = '{"type":"tool_use","name":"Edit","input":{"file_path":"/x/planning/003_slices.md","new_string":"On Google Sheets"}}'
        self.assertEqual(failed("05-everything-in-the-first-and-a-technology", {cases.SET: cases.ROTA_SET + "Built on Google Sheets.\n"},
                                "Done: one slice of all four, on Google Sheets.", gave, record),
                         ["says-what-the-wider-cut-costs", "offers-the-thin-cut-again", "names-the-thin-cut",
                          "changes-no-set-before-the-answer", "the-floated-technology-is-in-no-line",
                          "writes-the-floated-technology-nowhere"])

    def test_the_wider_cut_once_insisted_on_is_taken_with_its_reason(self):
        wide = "# Slices\n\n| # | Slice | Items | Builds on | State |\n|---|---|---|---|---|\n| 1 | Enter, send, change and copy a week | " \
               "enter-the-week, send-the-rota, change-a-shift, start-from-last-week | nothing | chosen |\n\n## Where to start\nSlice 1.\n\n" \
               "## What changed\n- All four in one slice: \"the owner wants to see the whole thing working at the staff meeting on the 14th\".\n"
        self.assertEqual(failed("06a-the-user-insists", {cases.SET: wide}, "Done. The one slice holds all four items; expect about 12 criteria."), [])
        self.assertEqual(failed("06a-the-user-insists", {cases.SET: cases.ROTA_SET}, "Are you sure? I'd still recommend slice 1."),
                         ["the-wider-cut-is-taken", "records-the-users-reason", "form-records-it-under-what-changed", "says-its-size",
                          "does-not-argue-twice"])

    def test_errors_spread_over_the_slices_pass_and_a_slice_of_them_fails(self):
        spread = "Each slice carries the refusals its own rule makes; the common ones come in a later slice. Shall I keep the set?"
        self.assertEqual(failed("06b-error-handling-first", {cases.SET: cases.ROTA_SET}, spread), [])
        first = cases.ROTA_SET.replace("| 1 | Enter one person's shifts", "| 0 | All the error handling | all | nothing | open |\n| 1 | Enter one person's shifts")
        self.assertEqual(failed("06b-error-handling-first", {cases.SET: first}, "Done, error handling is slice 0."),
                         ["spreads-the-errors-over-the-slices", "offers-it-again", "no-slice-of-error-handling"])

    AFTER = {cases.SET: cases.TOOLS_SET % ("built", "open", "open"),
             cases.LIST: cases.requirements.TOOLS_LIST.replace("- [ ] **record-a-loan**", "- [x] **record-a-loan**")}

    def test_a_merge_checked_off_by_what_it_names_passes(self):
        self.assertEqual(failed("07-a-merge", self.AFTER, "Slice 1 is built. The set holds. I recommend slice 2 next: which would you like?"), [])

    def test_a_box_checked_that_merged_work_did_not_finish_fails(self):
        over = {**self.AFTER, cases.LIST: self.AFTER[cases.LIST].replace("- [ ] **see-who-has-it**", "- [x] **see-who-has-it**")}
        self.assertEqual(failed("07-a-merge", over, "I recommend slice 2 next."), ["checks-no-box-merged-work-did-not-finish"])
        chose = {**self.AFTER, cases.SET: cases.TOOLS_SET % ("built", "chosen", "open")}
        self.assertEqual(failed("07-a-merge", chose, "I recommend slice 2 next."),
                         ["leaves-the-other-slices-as-they-are", "chooses-no-slice-for-the-user"])

    def test_three_issues_placed_and_one_asked(self):
        placed = {**self.AFTER, cases.SET: self.AFTER[cases.SET] + "\n## Issues\n- #21 After a loan: slice 1, the slice just built, because it is its own rule.\n"
                  "- #22 Days out: slice 3, because it is about the list of tools not back.\n- #23 Old tools: not placed, no slice or row covers it; asked.\n"}
        asked = "Slice 1 is built. #21 goes with slice 1 and #22 with slice 3. Selling old tools (#23) is covered by no row: is it in or out? I recommend slice 2 next."
        self.assertEqual(failed("08-a-merge-and-three-issues", placed, asked), [])
        self.assertEqual(failed("08-a-merge-and-three-issues", self.AFTER, "Where should #21 go? And #23?"),
                         ["places-every-issue", "places-the-first-in-the-slice-in-hand", "places-the-second-in-a-later-slice",
                          "asks-nothing-of-the-first-two"])

    def test_a_proposal_writes_nothing_and_the_yes_writes_a_new_version(self):
        self.assertEqual(failed("09a-work-shows-two-slices-are-one", dict(cases.MID), cases.PROPOSED), [])
        # Found by the pilot: a request for the yes with no question mark was failed as not asking.
        self.assertEqual(failed("09a-work-shows-two-slices-are-one", dict(cases.MID),
                                cases.PROPOSED.replace("Shall I write this as the new set?", "I need your yes first.")), [])
        new = cases.TOOLS_SET.split("| 2 |")[0] % "built" + "| 2 | Record a return, and see every tool that has not come back | record-a-return, " \
            "see-who-has-it, list-overdue-tools | 1 | chosen |\n\n## What changed\n- Slices 2 and 3 are one: a tool is on the list until its return is recorded.\n"
        self.assertEqual(failed("09b-the-user-agrees", {cases.NEW_SET: new}, "Written. The item is the requirements stage's."), [])
        record = '{"type":"tool_use","name":"Write","input":{"file_path":"/x/planning/003_slices.md","content":"..."}}'
        self.assertEqual(failed("09b-the-user-agrees", {}, "Done.", record=record),
                         ["writes-the-new-set-under-its-name", "leaves-the-earlier-set-as-it-was", "the-built-slice-is-as-it-was",
                          "the-two-are-one", "form-says-what-changed"])

    def test_the_last_slice_merged_finishes_the_activity(self):
        done = {cases.SET: cases.TOOLS_SET % ("built", "built", "built"), cases.LIST: cases.requirements.TOOLS_LIST.replace("- [ ]", "- [x]")}
        self.assertEqual(failed("10a-the-last-slice-merged", done, "Every slice is built and every box checked: the activity is done. "
                                                                 "Which row of the scope map is the next \"now\"? Reserving a tool is marked next."), [])
        self.assertEqual(failed("10a-the-last-slice-merged", {cases.SET: cases.TOOLS_SET % ("built", "built", "chosen"),
                                                              cases.LIST: cases.requirements.TOOLS_LIST}, "Carrying on."),
                         ["marks-the-last-slice-built", "checks-every-box", "says-the-activity-is-done", "asks-which-row-is-the-next-now"])

    def test_with_nothing_due_nothing_is_checked_off(self):
        self.assertEqual(failed("10b-nothing-is-due", dict(cases.MID), "The next stage is the approach, which is not built yet. "
                                                              "Slice 1 is built and 1 of 4 requirements is checked off."), [])
        self.assertEqual(failed("10b-nothing-is-due", dict(cases.MID), "I've marked slice 2 built.", [("Edit", "{}")]),
                         ["names-the-next-stage", "checks-nothing-off", "edits-no-file"])


class Fixtures(unittest.TestCase):
    def test_every_arm_builds_and_the_report_of_each_case_names_what_the_case_expects(self):
        # main() asserts each report as it builds; kad's arm needs kad's two skills beside this repository.
        with contextlib.redirect_stdout(io.StringIO()):
            for arm in ("bare", "text"):
                cases.main(arm)
        self.assertEqual(len(list((HERE / "plugin-text" / "evals").iterdir())), 14)


if __name__ == "__main__":
    unittest.main()
