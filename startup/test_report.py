import unittest

from standin_machine import Machine


class Audit(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def audit(self, *args):
        return self.machine.run("audit.sh", *args)

    def test_off_keeps_no_record(self):
        done = self.audit("off")
        self.assertEqual((done.returncode, done.stdout.strip()), (0, "audit: off"))

    def test_no_answer_yet_is_off(self):
        self.assertEqual(self.audit().stdout.strip(), "audit: off")

    def test_on_keeps_the_record_in_a_folder_on_this_machine(self):
        done = self.audit("on")
        self.assertEqual(done.stdout.strip(), f"audit: on; the record is kept in {self.machine.data.as_posix()}/audit")

    def test_on_with_a_repository_keeps_the_record_there(self):
        done = self.audit("ON", "https://example.org/someone/record.git")
        self.assertEqual(done.stdout.strip(),
                         "audit: on; the record is kept in the repository https://example.org/someone/record.git")

    def test_the_tools_own_words_for_yes_and_no_are_read(self):
        self.assertEqual(self.audit("true").stdout.split(";")[0], "audit: on")
        self.assertEqual(self.audit("false").stdout.strip(), "audit: off")

    def test_any_other_word_is_refused_and_nothing_is_recorded(self):
        done = self.audit("maybe")
        self.assertEqual(done.returncode, 3)
        self.assertIn("REFUSED", done.stdout)


class Report(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def report(self):
        done = self.machine.run("report.sh")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def test_inside_a_vm_one_report_holds_the_machine_the_tracker_and_the_documents_in_that_order(self):
        self.machine.inside_vm()
        out = self.report()
        self.assertTrue(out.startswith("kd-dev-team: startup report\n"))
        places = [out.index(f"\n{title}\n") for title in ("Machine", "Tracker", "Documents")]
        self.assertEqual(places, sorted(places))
        self.assertIn("- this session is inside a VM", out)
        self.assertIn("- repository: none", out)
        self.assertIn("- planning folder: not chosen yet", out)

    def test_outside_a_vm_the_report_is_of_the_machine_only(self):
        self.machine.repository("https://github.com/someone/something.git")
        self.machine.have("gh")
        self.machine.vm_tool()
        out = self.report()
        self.assertIn("- locks: all 6 on", out)
        self.assertIn("\nThe tracker and the documents are read inside the project's VM, not here.\n", out)
        self.assertNotIn("\nTracker\n", out)
        self.assertNotIn("planning folder", out)
        self.assertEqual([c for c in self.machine.calls() if c.startswith("gh")], [])

    def test_the_report_changes_nothing(self):
        self.machine.vm_tool(locks_off=["browser.enabled"])
        self.report()
        self.assertEqual([c for c in self.machine.calls() if " set " in c or " init " in c or " allow " in c], [])

    def test_a_part_that_refuses_is_shown_and_the_rest_still_comes(self):
        self.machine.inside_vm()
        self.machine.repository("https://github.com/someone/something.git")
        self.machine.have("gh")
        self.machine.set("gh/lines", "not the answer expected")
        out = self.report()
        self.assertIn("- REFUSED:", out)
        self.assertIn("- planning folder: not chosen yet", out)
        self.assertIn("Startup could not read everything: see REFUSED above.", out)

    def test_a_machine_that_cannot_be_read_is_refused_outside_a_vm_too(self):
        self.machine.vm_tool()
        self.machine.set("sbx/garble", "version")
        out = self.report()
        self.assertIn("- REFUSED:", out)
        self.assertIn("Startup could not read everything: see REFUSED above.", out)

    def test_a_report_with_nothing_refused_does_not_say_so(self):
        self.machine.vm_tool()
        self.assertNotIn("REFUSED", self.report())

    def test_the_report_stays_under_the_size_a_session_is_given_whole(self):
        self.machine.vm_tool(locks_off=["browser.enabled"], vms=["a", "b"])
        self.assertLess(len(self.report()), 10000)


if __name__ == "__main__":
    unittest.main()
