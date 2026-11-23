"""The wrapper each stood-in tool is installed under: a scenario's machine in its project, the real tool elsewhere."""
import os
import pathlib
import stat
import subprocess
import sys
import tempfile
import unittest

WRAPPER = pathlib.Path(__file__).resolve().parents[2] / "00-startup" / "eval" / "standin-wrapper.sh"


def script(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n" + text + "\n")
    path.chmod(path.stat().st_mode | stat.S_IEXEC)


@unittest.skipIf(os.name == "nt", "the wrapper runs inside the VM, which is Linux")
class Wrapper(unittest.TestCase):
    def setUp(self):
        self.top = pathlib.Path(tempfile.mkdtemp()).resolve()
        self.project = self.top / "project"
        (self.project / ".cache" / "machine").mkdir(parents=True)
        (self.project / "planning").mkdir()
        (self.top / "elsewhere").mkdir()
        script(self.top / "bin" / "curl", WRAPPER.read_text().split("\n", 1)[1])
        script(self.top / "standin" / "curl", 'echo "made-up $STANDIN_STATE"')
        script(self.top / "real" / "curl", "echo real")

    def run_in(self, folder, command="curl"):
        env = {"PATH": f"{self.top / 'bin'}:{self.top / 'real'}:/usr/bin:/bin", "STANDIN_HOME": str(self.top / "standin")}
        return subprocess.run(["bash", "-c", command], cwd=folder, env=env, capture_output=True, text=True).stdout.strip()

    def test_inside_a_scenarios_project_it_is_that_scenarios_machine(self):
        self.assertEqual(self.run_in(self.project / "planning"), f"made-up {self.project}/.cache/machine")

    def test_anywhere_else_it_is_the_real_tool(self):
        self.assertEqual(self.run_in(self.top / "elsewhere"), "real")

    @unittest.skipIf(sys.platform == "darwin", "macOS's sh forgets the folder a command came from; the VM's keeps it")
    def test_a_command_that_steps_out_of_the_project_first_is_still_on_that_machine(self):
        self.assertEqual(self.run_in(self.project, f'cd "{self.top / "elsewhere"}"; curl'),
                         f"made-up {self.project}/.cache/machine")

    def test_a_tool_the_scenario_says_is_absent_is_not_found(self):
        (self.project / ".cache" / "machine" / "absent").mkdir()
        (self.project / ".cache" / "machine" / "absent" / "curl").write_text("")
        self.assertEqual(self.run_in(self.project), "")


if __name__ == "__main__":
    unittest.main()
