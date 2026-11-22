import unittest

from standin_machine import Machine

UBUNTU = 'NAME="Ubuntu"\nID=ubuntu\nVERSION_ID="24.04"\n'


class Inspect(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def inspect(self):
        return self.machine.run("machine.sh", "inspect")

    def test_no_vm_tool_says_what_would_install_it_and_runs_nothing(self):
        self.machine.have("brew")
        done = self.inspect()
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("- system: macOS 15.1 on arm64 (supported by the VM tool)", done.stdout)
        self.assertIn("- VM tool (Docker Sandboxes, `sbx`): not installed", done.stdout)
        self.assertIn("brew trust docker/tap && brew install docker/tap/sbx", done.stdout)
        self.assertIn("- Homebrew, which that command uses: installed", done.stdout)
        self.assertEqual(self.machine.calls(), [])

    def test_no_vm_tool_and_no_homebrew_says_so(self):
        self.assertIn("- Homebrew, which that command uses: not installed", self.inspect().stdout)

    def test_a_tool_that_is_signed_out_is_reported_with_the_step_that_signs_in(self):
        self.machine.vm_tool(signed_in=False)
        out = self.inspect().stdout
        self.assertIn("- VM tool (Docker Sandboxes, `sbx`): installed (v0.54.0)", out)
        self.assertIn("- signed in to the VM tool: no", out)
        self.assertIn("`sbx login`", out)
        self.assertNotIn("- VMs:", out)

    def test_a_machine_in_order_has_every_lock_on_and_no_vm(self):
        self.machine.vm_tool()
        out = self.inspect().stdout
        self.assertIn("- signed in to the VM tool: yes", out)
        self.assertIn("- locks: all 6 on", out)
        self.assertIn("- VMs: none", out)
        self.assertNotIn("secure", out)

    def test_a_lock_that_is_off_is_named_with_the_vm_it_leaves_open(self):
        self.machine.vm_tool(locks_off=["browser.enabled"], vms=["trial-1"])
        out = self.inspect().stdout
        self.assertIn("- locks: 1 of 6 OFF", out)
        self.assertIn("  - OFF: It cannot open pages in your own web browser (browser.enabled)", out)
        self.assertIn("- VMs: 1 (trial-1)", out)
        self.assertRegex(out, r"- turning every lock on: sh \".*machine\.sh\" secure")

    def test_a_network_open_by_default_is_a_lock_off(self):
        self.machine.vm_tool(deny_by_default=False)
        out = self.inspect().stdout
        self.assertIn("  - OFF: It can reach only the few websites on its list", out)

    def test_a_host_allowed_for_every_vm_beyond_the_list_is_a_lock_off(self):
        self.machine.vm_tool(hosts=["github.com", "example.org"])
        self.assertIn("every VM can also reach example.org", self.inspect().stdout)

    def test_inspecting_changes_nothing(self):
        self.machine.vm_tool(locks_off=["browser.enabled"], deny_by_default=False)
        self.inspect()
        self.assertEqual([c for c in self.machine.calls() if " set " in c or " init " in c or " allow " in c], [])

    def test_a_version_it_does_not_recognise_is_refused(self):
        self.machine.vm_tool()
        self.machine.set("sbx/garble", "version")
        done = self.inspect()
        self.assertEqual(done.returncode, 3)
        self.assertIn("REFUSED", done.stdout)
        self.assertIn("Docker Sandboxes, build nine", done.stdout)

    def test_a_listing_that_fails_for_a_reason_it_does_not_know_is_refused(self):
        self.machine.vm_tool()
        self.machine.set("sbx/garble", "ls")
        done = self.inspect()
        self.assertEqual(done.returncode, 3)
        self.assertIn("the daemon did not answer", done.stdout)

    def test_a_setting_that_is_neither_true_nor_false_is_refused(self):
        self.machine.vm_tool()
        self.machine.set("sbx/garble", "settings")
        self.assertEqual(self.inspect().returncode, 3)


class Systems(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def system_line(self, *args, **kwargs):
        self.machine.system(*args, **kwargs)
        done = self.machine.run("machine.sh", "inspect")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def test_an_intel_mac_is_not_supported_and_says_why(self):
        out = self.system_line("Darwin", "x86_64", macos="15.1")
        self.assertIn("- system: macOS 15.1 on x86_64: NOT supported by the VM tool "
                      "(on macOS it needs Apple silicon)", out)
        self.assertIn("- VM tool (Docker Sandboxes, `sbx`): no version of it runs on this system", out)
        self.assertNotIn("brew", out)

    def test_an_old_macos_is_not_supported(self):
        self.assertIn("NOT supported by the VM tool (it needs macOS 14 or later)",
                      self.system_line("Darwin", "arm64", macos="13.6.1"))

    def test_ubuntu_24_04_is_supported_with_its_install_command(self):
        out = self.system_line("Linux", "x86_64", release="6.8.0-45-generic", os_release=UBUNTU)
        self.assertIn("- system: Ubuntu 24.04 on x86_64 (supported by the VM tool)", out)
        self.assertIn("curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh && sudo apt install docker-sbx", out)

    def test_an_older_ubuntu_is_not_supported(self):
        out = self.system_line("Linux", "x86_64", os_release=UBUNTU.replace("24.04", "22.04"))
        self.assertIn("NOT supported by the VM tool (on Linux it needs Ubuntu 24.04 or later)", out)

    def test_another_linux_is_not_supported(self):
        out = self.system_line("Linux", "x86_64", os_release='NAME="Fedora Linux"\nID=fedora\nVERSION_ID=41\n')
        self.assertIn("- system: Fedora Linux 41 on x86_64: NOT supported", out)

    def test_linux_inside_windows_is_not_supported(self):
        out = self.system_line("Linux", "x86_64", release="5.15.167.4-microsoft-standard-WSL2", os_release=UBUNTU)
        self.assertIn("NOT supported by the VM tool (its documentation does not list Linux inside Windows (WSL)", out)

    def test_windows_11_is_supported_with_its_install_command(self):
        out = self.system_line("MINGW64_NT-10.0-22631", "x86_64")
        self.assertIn("- system: Windows 11 (build 22631) on x86_64 (supported by the VM tool)", out)
        self.assertIn("winget install -h Docker.sbx", out)

    def test_windows_10_is_not_supported(self):
        self.assertIn("- system: Windows 10 (build 19045) on x86_64: NOT supported by the VM tool "
                      "(it needs Windows 11)", self.system_line("MINGW64_NT-10.0-19045", "x86_64"))

    def test_windows_on_arm_is_not_supported(self):
        self.assertIn("(on Windows it needs an Intel or AMD processor)",
                      self.system_line("MINGW64_NT-10.0-26100", "aarch64"))

    def test_a_system_it_has_never_heard_of_is_not_supported(self):
        self.assertIn("- system: FreeBSD on amd64: NOT supported by the VM tool", self.system_line("FreeBSD", "amd64"))


class Secure(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def test_secure_turns_every_lock_on(self):
        self.machine.vm_tool(locks_off=["browser.enabled", "clipboard.textCopy"], deny_by_default=False, hosts=[])
        done = self.machine.run("machine.sh", "secure")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn("- locks: all 6 on", done.stdout)
        self.assertNotIn("true", self.machine.read("sbx/settings"))
        self.assertIn("github.com", self.machine.read("sbx/hosts"))

    def test_secure_leaves_a_lock_that_is_on_alone(self):
        self.machine.vm_tool()
        self.machine.run("machine.sh", "secure")
        self.assertEqual([c for c in self.machine.calls() if "settings set" in c or "policy init" in c], [])

    def test_secure_fails_when_a_host_beyond_the_list_stays_allowed(self):
        self.machine.vm_tool(hosts=["example.org"])
        done = self.machine.run("machine.sh", "secure")
        self.assertEqual(done.returncode, 1)
        self.assertIn("every VM can also reach example.org", done.stdout)

    def test_secure_without_the_tool_is_refused(self):
        self.assertEqual(self.machine.run("machine.sh", "secure").returncode, 3)


class Install(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)
        self.machine.have("brew")

    def test_install_without_a_yes_installs_nothing(self):
        done = self.machine.run("machine.sh", "install")
        self.assertEqual(done.returncode, 1)
        self.assertIn("not installed: this needs the user's yes", done.stdout)
        self.assertEqual(self.machine.calls(), [])

    def test_install_with_a_yes_runs_the_systems_own_command(self):
        done = self.machine.run("machine.sh", "install", "--yes")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(self.machine.calls(), ["brew trust docker/tap", "brew install docker/tap/sbx"])

    def test_install_on_a_system_the_tool_does_not_support_is_refused(self):
        self.machine.system("Darwin", "x86_64", macos="15.1")
        done = self.machine.run("machine.sh", "install", "--yes")
        self.assertEqual(done.returncode, 3)
        self.assertEqual(self.machine.calls(), [])

    def test_install_when_the_tool_is_there_does_nothing(self):
        self.machine.vm_tool()
        done = self.machine.run("machine.sh", "install", "--yes")
        self.assertEqual(done.returncode, 0)
        self.assertEqual([c for c in self.machine.calls() if c.startswith("brew")], [])



class ProjectVM(unittest.TestCase):
    """The one VM a project is worked on in: named for the project, made with a yes, entered by the user."""

    def setUp(self):
        self.machine = Machine(self)

    def inspect(self):
        done = self.machine.run("machine.sh", "inspect")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def name(self):
        done = self.machine.run("machine.sh", "name")
        self.assertEqual(done.returncode, 0, done.stderr)
        return done.stdout.strip()

    def test_the_vm_is_named_for_the_project_and_two_projects_never_share_a_name(self):
        self.assertRegex(self.name(), r"^kd-project-[0-9]+$")
        elsewhere = self.machine.root / "Other Place" / "project"
        elsewhere.mkdir(parents=True)
        other = self.machine.run("machine.sh", "name", cwd=elsewhere).stdout.strip()
        self.assertRegex(other, r"^kd-project-[0-9]+$")
        self.assertNotEqual(other, self.name())

    def test_the_name_is_the_same_from_a_folder_below_the_repository_root(self):
        self.machine.repository()
        below = self.machine.project / "src"
        below.mkdir()
        self.assertEqual(self.machine.run("machine.sh", "name", cwd=below).stdout.strip(), self.name())

    def test_inside_a_vm_the_machine_is_not_inspected(self):
        self.machine.inside_vm()
        out = self.inspect()
        self.assertEqual(out.strip(), "- this session is inside a VM (Docker Sandboxes): the project is worked on here")
        self.assertEqual(self.machine.calls(), [])

    def test_a_machine_in_order_with_no_vm_for_the_project_says_how_one_is_made(self):
        self.machine.repository()
        self.machine.vm_tool(vms=["kd-another-1"])
        out = self.inspect()
        self.assertIn("- VM for this project: none", out)
        self.assertRegex(out, r"- making it \(a private copy of this repository, inside a new VM\): "
                              r"sh \".*machine\.sh\" create")

    def test_a_folder_that_is_not_a_repository_is_said_with_what_making_the_vm_would_do(self):
        self.machine.vm_tool()
        out = self.inspect()
        self.assertIn("- VM for this project: none", out)
        self.assertRegex(out, r"- making it \(this folder becomes a git repository first; then a private copy "
                              r"of it, inside a new VM\): sh \".*machine\.sh\" create")

    def test_a_vm_for_the_project_is_named_with_the_command_that_continues_inside_it(self):
        self.machine.repository()
        self.machine.vm_tool(vms=[self.name()])
        out = self.inspect()
        self.assertIn(f"- VM for this project: {self.name()}", out)
        self.assertIn(f"- continuing inside it (the user's to run, in their own terminal): sbx run --name {self.name()}",
                      out)
        self.assertNotIn("create", out)

    def test_with_a_lock_off_nothing_is_said_of_making_or_entering_a_vm(self):
        self.machine.repository()
        self.machine.vm_tool(locks_off=["browser.enabled"], vms=[self.name()])
        out = self.inspect()
        self.assertIn(f"- VM for this project: {self.name()}", out)
        self.assertNotIn("sbx run", out)

    def test_secure_ends_by_saying_how_the_projects_vm_is_made_or_entered(self):
        self.machine.repository()
        self.machine.vm_tool(locks_off=["browser.enabled"], vms=[self.name()])
        done = self.machine.run("machine.sh", "secure")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn("- locks: all 6 on", done.stdout)
        self.assertIn(f"sbx run --name {self.name()}", done.stdout)

    def test_secure_that_leaves_a_lock_off_says_nothing_of_entering_a_vm(self):
        self.machine.repository()
        self.machine.vm_tool(hosts=["github.com", "example.org"], vms=[self.name()])
        done = self.machine.run("machine.sh", "secure")
        self.assertNotEqual(done.returncode, 0)
        self.assertNotIn("sbx run", done.stdout)

    def test_create_makes_a_private_copy_under_the_projects_name_and_says_how_to_continue(self):
        self.machine.repository()
        self.machine.vm_tool()
        done = self.machine.run("machine.sh", "create")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn(f"sbx --no-input create --clone --name {self.name()} claude .", self.machine.calls())
        self.assertIn(f"- VM for this project: {self.name()} (just made)", done.stdout)
        self.assertIn(f"sbx run --name {self.name()}", done.stdout)

    def test_create_is_run_from_the_repository_root(self):
        self.machine.repository()
        self.machine.vm_tool()
        below = self.machine.project / "src"
        below.mkdir()
        self.machine.run("machine.sh", "create", cwd=below)
        self.assertEqual(self.machine.read("sbx/created_in").strip(), "the repository root")

    def test_create_makes_the_folder_a_repository_when_it_is_not_one(self):
        self.machine.vm_tool()
        done = self.machine.run("machine.sh", "create")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertTrue((self.machine.project / ".git").is_dir())

    def test_create_turns_the_locks_on_first_and_makes_nothing_if_one_stays_off(self):
        self.machine.repository()
        self.machine.vm_tool(hosts=["github.com", "example.org"])
        done = self.machine.run("machine.sh", "create")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("OFF", done.stdout)
        self.assertEqual([c for c in self.machine.calls() if " create " in c], [])

    def test_create_when_the_vm_is_there_makes_nothing(self):
        self.machine.repository()
        self.machine.vm_tool(vms=[self.name()])
        done = self.machine.run("machine.sh", "create")
        self.assertEqual(done.returncode, 0)
        self.assertEqual([c for c in self.machine.calls() if " create " in c], [])
        self.assertIn(f"sbx run --name {self.name()}", done.stdout)

    def test_create_inside_a_vm_is_refused(self):
        self.machine.inside_vm()
        self.assertEqual(self.machine.run("machine.sh", "create").returncode, 3)

    def test_create_that_fails_is_refused_with_the_tools_words(self):
        self.machine.repository()
        self.machine.vm_tool()
        self.machine.set("sbx/garble", "create")
        done = self.machine.run("machine.sh", "create")
        self.assertEqual(done.returncode, 3)
        self.assertIn("the daemon did not answer", done.stdout)


if __name__ == "__main__":
    unittest.main()
