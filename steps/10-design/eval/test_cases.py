"""The cases of the design: where each starts, that a design which does the work well passes the checks of
its case with the script's own drawing, and that the checks fail a poor one."""
import importlib.util
import io
import json
import pathlib
import re
import shutil
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location("design_cases", HERE / "make_cases.py")
cases = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cases)
design = cases.design
FILE = "planning/slice-001/010_design.md"


def holds(check, text):
    found = re.search(check["pattern"], text, re.I if "i" in check.get("flags", "") else 0) is not None
    return found != (check.get("match") == "not_contains")


@unittest.skipIf(sys.platform == "win32", "the cases are built inside the VM, which is Linux")
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        said, out = io.StringIO(), sys.stdout
        sys.stdout = said
        try:
            cases.main("text")
        finally:
            sys.stdout = out
        cls.built = said.getvalue()
        cls.evals = HERE / "plugin-text" / "evals"

    def case(self, prefix):
        return next(path for path in sorted(self.evals.iterdir()) if path.name.startswith(prefix))

    def report(self, prefix):
        return (self.case(prefix) / "report.txt").read_text(encoding="utf-8")

    def scenario(self, prefix):
        return next(each for each in cases.SCENARIOS if each[0].startswith(prefix))

    def checks(self, prefix, target):
        """The checks of a case that read the design (`file`) or the session's last words (`said`)."""
        wanted = (lambda check: isinstance(check.get("target"), dict)) if target == "file" else (lambda check: check.get("target") == "last_message")
        return [check for check in json.loads(json.dumps(self.scenario(prefix)[5])) if wanted(check)]

    def judged(self, prefix, target, text):
        return {check["name"]: holds(check, text) for check in self.checks(prefix, target)}

    def written(self, prefix, text):
        """The case's project with that design written in it: (what the script says of it, its exit, the design as it stands)."""
        top = pathlib.Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, top, True)
        shutil.copytree(self.case(prefix) / "project", top / "project")
        (top / "project" / FILE).write_text(text, encoding="utf-8", newline="\n")
        said = io.StringIO()
        code = design.main(["draw", str(top / "project/planning/slice-001")], said)
        return said.getvalue(), code, text

    def test_fourteen_cases_are_built_and_each_has_checks(self):
        self.assertEqual(len(re.findall(r"^\d+[ab]?-[a-z-]+: \d+ checks$", self.built, re.M)), 14)
        self.assertEqual(len(cases.SCENARIOS), 14)

    def test_every_case_starts_where_it_says_with_the_commands_given(self):
        for name, *_rest in cases.SCENARIOS:
            report = self.report(name)
            if name.startswith("04b"):   # a finished design the user comes back on: the next stage is named, and the command that draws it again
                self.assertIn("next stage by the documents: screens (", report)
                self.assertIn("the design is changed only in planning/slice-001/010_design.md, and drawn again by script", report)
                continue
            self.assertIn("next stage by the documents: design (its document: planning/slice-001/010_design.md", report, name)
            self.assertRegex(report, r'python3 "@STARTUP@/\.\./designing/design\.py" next planning/slice-001', name)
            self.assertRegex(report, r'python3 "@STARTUP@/\.\./designing/design\.py" draw planning/slice-001', name)
            self.assertNotIn(str(ROOT), report)

    def test_the_first_case_starts_with_twenty_things_to_give_a_home(self):
        said = io.StringIO()
        design.main(["next", str(self.case("01") / "project/planning/slice-001")], said)
        self.assertIn("0 of 20 things settled before have their home; 20 are left", said.getvalue())
        for each in ("- A934: chosen: When the payment was taken and recording it fails", "- A913: decided by the owner: one named person", "- T1: an open fact (high)",
                     "Slices that build on this one: 2: See which season tickets are not renewed"):
            self.assertIn(each, said.getvalue())

    def test_the_design_an_earlier_session_left_passes_the_first_case_and_is_drawn(self):
        said, code, text = self.written("01", cases.PARTS)
        self.assertEqual(code, 0, said)
        self.assertRegex(said, cases.NOTHING_WAITS["pattern"])
        self.assertEqual(set(self.judged("01", "file", text).values()), {True})

    def test_a_design_that_leaves_the_open_fact_or_the_failed_save_homeless_fails_it(self):
        for gone, check in ((", T1", "an-open-fact-has-its-home-in-a-part"), (", A934", "what-fails-with-no-criterion-has-its-home-in-a-part")):
            said, code, text = self.written("01", cases.PARTS.replace(gone, "", 1))
            self.assertEqual(code, 1, said)
            self.assertFalse(self.judged("01", "file", text)[check])

    def test_two_things_at_once_are_refused_until_given_homes_and_pass_when_walked(self):
        said, code, _text = self.written("02", cases.PARTS)
        self.assertEqual(code, 1)
        self.assertIn("2 things settled before have no home (A941, A942)", said)
        said, code, text = self.written("02", cases.PARTS.replace("A931, A934, T1", "A931, A934, A941, A942, T1"))
        self.assertEqual(code, 0, said)
        self.assertEqual(set(self.judged("02", "file", text).values()), {True})

    def test_a_lock_with_a_hole_fails_while_it_is_chosen_and_passes_as_the_owners(self):
        hole = cases.PARTS.replace("Leftover: there is no marker to leave, remove or change.", "Leftover: a lock file left by a crash keeps every start stuck until someone deletes it.")
        self.assertFalse(self.judged("03", "file", hole)["a-hole-is-not-chosen"])
        self.assertTrue(self.judged("03", "file", cases.PARTS)["a-hole-is-not-chosen"])
        owners = hole.replace("## D2: A change to a renewal payment names the state it read\nKind: chosen", "## D2: A lock file with the process number\nKind: owner")
        self.assertTrue(self.judged("03", "file", owners)["a-hole-is-not-chosen"])
        self.assertTrue(all(self.judged("03", "said", "I walked your lock file through its orders: a crash leaves the file behind, and the process number may be given out "
                                                      "again to something else that is alive.").values()))

    def test_what_is_leaned_on_and_not_known_passes_only_when_named_with_what_is_done_either_way(self):
        homed = cases.PARTS.replace("Home of: refund-a-renewal / 1, A913", "Home of: refund-a-renewal / 1, A913, A961")
        said, code, text = self.written("07", homed)
        self.assertEqual(code, 0, said)
        self.assertFalse(self.judged("07", "file", text)["names-what-is-leaned-on-and-not-known"])
        named = homed.replace("; T1; T2\n", "; T1; T2; unknown: that an answered refund request means the money is given back\n"
                                            "Either way: a refund is shown as asked for until the provider says it is given back.\n")
        said, code, text = self.written("07", named)
        self.assertEqual(code, 0, said)
        self.assertRegex(said, r"1 things leaned on and not known")
        self.assertEqual(set(self.judged("07", "file", text).values()), {True})

    def test_a_need_the_approach_lacks_passes_only_when_it_goes_back(self):
        homed = cases.PARTS.replace("A933, T2", "A933, A951, T2")
        back = homed + "\n## Goes back\n- approach: A951 has the product send an email, and nothing the slice is committed to sends one.\n"
        said, code, text = self.written("05", back)
        self.assertEqual(code, 0, said)
        self.assertRegex(said, r"1 go back to an earlier stage")
        self.assertEqual(set(self.judged("05", "file", text).values()), {True})
        self.assertFalse(self.judged("05", "file", homed)["sends-it-back-to-the-approach"])
        self.assertFalse(self.judged("05", "file", back.replace("sends one.", "sends one; SendGrid would do."))["picks-no-way-of-sending-here"])

    def test_the_changed_answers_case_starts_stale_with_the_new_answer_alone_to_place(self):
        self.assertIn("to draw again: the answers, the open facts or the design changed", self.report("10"))
        said = io.StringIO()
        design.main(["next", str(self.case("10") / "project/planning/slice-001")], said)
        self.assertIn("20 of 21 things settled before have their home; 1 are left", said.getvalue())
        self.assertIn("- A971: chosen: Every payment taken and every refund given leaves a line", said.getvalue())

    def test_the_bringing_cases_start_drawn_with_one_decision_of_the_design_waiting(self):
        for prefix in ("11a", "11b"):
            self.assertIn("drawn; 1 decisions of the design wait for the owner", self.report(prefix))
            self.assertIn("### D3: Money taken and no renewal recorded (high)", (self.case(prefix) / "project/planning/slice-001/010_designed.md").read_text(encoding="utf-8"))
        self.assertTrue(all(self.judged("11a", "said", cases.BROUGHT).values()))
        decided = cases.WITH_RISK.replace("Harm: high\n", 'Harm: high\nDecided: given back by itself after an hour (the user, 2026-11-28: "Give it back by itself after an hour.")\n')
        said, code, text = self.written("11b", decided)
        self.assertEqual(code, 0, said)
        self.assertEqual(set(self.judged("11b", "file", text).values()), {True})

    def test_the_case_with_code_has_it_and_the_others_do_not(self):
        self.assertTrue((self.case("08") / "project/app/office_pages.py").is_file())
        self.assertFalse((self.case("01") / "project/app").exists())
        there = cases.PARTS + ("\n## Already there\n- The subscribers part keeps season tickets and their state: used as it is, under its name.\n"
                               "- The office's refund page calls PayRight itself, with the secret key: the provider is known outside the one part that isolates it.\n")
        there = there.replace("\n## At once", "\n## D3: The office's refund page asks through the refund part now\nKind: chosen\nSays: The existing refund page is changed to ask the "
                              "refund part.\nInstead of: leaving it, which keeps a second place that knows the provider.\nBecause: the slice touches it anyway.\nCosts: one more "
                              "page changed in this slice.\nArchitectural: yes: it removes a second way to the provider.\nSignificant: no: one page.\nNon-obvious: no: it follows "
                              "from the boundary.\nLeans on: payright F10 \"A settled payment can be refunded in full or in part within 90 days of settling.\"\n\n## At once")
        said, code, text = self.written("08", there)
        self.assertEqual(code, 0, said)
        self.assertEqual(set(self.judged("08", "file", text).values()), {True})
        self.assertFalse(self.judged("08", "file", cases.PARTS)["says-what-is-already-there"])

    def test_the_words_said_before_pass_their_own_cases(self):
        self.assertTrue(all(self.judged("09a", "said", cases.PUSHED_BACK).values()))
        self.assertTrue(all(self.judged("04a", "said", cases.SAID_THE_COST).values()))
        self.assertFalse(self.judged("04a", "file", cases.PARTS.replace("## C4: Card payments", "## C4: Registry of providers"))["designs-no-registry"])
        self.assertTrue(all(self.judged("06", "said", "Single tickets are out for now in the requirements: that is theirs to change, and nothing of it is designed here.").values()))

    def test_earlier_turns_are_a_user_then_the_session(self):
        for prefix in ("04b", "09b", "11b"):
            lines = [json.loads(line) for line in (self.case(prefix) / "history.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual([line["type"] for line in lines], ["user", "assistant"])

    def test_the_plugin_carries_the_script_and_this_stages_text(self):
        plugin = HERE / "plugin-text"
        self.assertEqual((plugin / "designing/design.py").read_text(encoding="utf-8"), (ROOT / "designing/design.py").read_text(encoding="utf-8"))
        self.assertEqual((plugin / "skills/design/SKILL.md").read_text(encoding="utf-8"), (HERE / "design-skill.md").read_text(encoding="utf-8"))
        self.assertTrue((plugin / "skills/open-facts/SKILL.md").is_file())

    def test_the_bare_arm_has_no_text_for_the_stage_and_says_to_do_it_from_the_report(self):
        said, out = io.StringIO(), sys.stdout
        sys.stdout = said
        try:
            cases.main("bare")
        finally:
            sys.stdout = out
        self.assertFalse((HERE / "plugin-bare/skills/design").exists())
        self.assertIn("The design stage", (HERE / "plugin-bare/hooks/routing-table.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
