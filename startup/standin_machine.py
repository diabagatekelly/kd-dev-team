"""A made-up machine for the startup scripts' tests: which tools it has and what they answer.

The scripts see only the stand-ins in `standin/` and a short list of ordinary utilities,
so a tool the test did not ask for is missing whatever the real machine has installed.
"""
import os
import pathlib
import shutil
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SH = shutil.which("sh") or shutil.which("bash")
UTILITIES = ("sh awk sed grep head tail tr cat git sort wc basename dirname mkdir rm mv ls cut "
             "printf test cksum").split()
LOCKS = ["browser.enabled", "claude.chrome", "claude.remoteControl",
         "clipboard.imagePaste", "clipboard.textCopy"]
DEFAULT_HOSTS = ["api.anthropic.com", "claude.ai", "github.com", "platform.claude.com", "registry.npmjs.org"]
_farm = None


def _utilities_path():
    """The directories holding the ordinary utilities and nothing a test stands in for."""
    global _farm
    if os.name == "nt":
        return [str(pathlib.Path(shutil.which(tool)).parent) for tool in ("sh", "git")]
    if _farm is None:
        _farm = pathlib.Path(tempfile.mkdtemp(prefix="startup-utilities-"))
        for tool in UTILITIES:
            found = shutil.which(tool)
            if found:
                (_farm / tool).symlink_to(found)
    return [str(_farm)]


class Machine:
    """macOS 15.1 on Apple silicon with nothing installed, until the test says otherwise."""

    def __init__(self, case):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="startup-test-")).resolve()
        case.addCleanup(shutil.rmtree, self.root, True)
        self.bin, self.state = self.root / "bin", self.root / "state"
        self.project, self.data = self.root / "project", self.root / "data"
        for folder in (self.bin, self.state, self.project, self.data):
            folder.mkdir()
        self.system("Darwin", "arm64", macos="15.1")

    def system(self, kernel, arch, release="24.1.0", macos=None, os_release=None):
        self.have("uname")
        self.set("sys/kernel", kernel)
        self.set("sys/arch", arch)
        self.set("sys/release", release)
        for name in ("sw_vers",):
            (self.bin / name).unlink(missing_ok=True)
        if macos:
            self.have("sw_vers")
            self.set("sys/macos", macos)
        self.set("sys/os-release", os_release or "")

    def have(self, *tools):
        for tool in tools:
            shutil.copy(HERE / "standin" / tool, self.bin / tool)
            (self.bin / tool).chmod(0o755)

    def vm_tool(self, signed_in=True, locks_off=(), vms=(), deny_by_default=True, hosts=DEFAULT_HOSTS):
        """The VM tool installed, every lock on unless named in locks_off."""
        self.have("sbx")
        self.set("sbx/settings", "".join(f"{key} {'true' if key in locks_off else 'false'}\n" for key in LOCKS))
        self.set("sbx/vms", "".join(f"{name}\n" for name in vms))
        self.set("sbx/hosts", "".join(f"{host}\n" for host in hosts))
        if deny_by_default:
            self.set("sbx/deny_by_default", "")
        if not signed_in:
            self.set("sbx/signed_out", "")

    def inside_vm(self):
        """This session is inside a VM the tool made: nothing of the tool is installed here."""
        (self.state / "sys" / "inside-vm").mkdir(parents=True, exist_ok=True)

    def set(self, relative, text):
        path = self.state / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text if text.endswith("\n") or not text else text + "\n", encoding="utf-8", newline="\n")

    def read(self, relative):
        return (self.state / relative).read_text(encoding="utf-8")

    def calls(self):
        log = self.state / "calls.log"
        return log.read_text(encoding="utf-8").splitlines() if log.exists() else []

    def git(self, *args):
        subprocess.run(["git", *args], cwd=self.project, check=True, capture_output=True)

    def repository(self, remote=None):
        self.git("init", "-q")
        if remote:
            self.git("remote", "add", "origin", remote)

    def document(self, relative, folder="planning"):
        path = self.project / folder / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("A document.\n", encoding="utf-8")

    def run(self, script, *args, cwd=None):
        env = {
            "PATH": os.pathsep.join([str(self.bin), *_utilities_path()]),
            "STANDIN_STATE": str(self.state),
            "KD_OS_RELEASE": str(self.state / "sys" / "os-release"),
            "KD_VM_MARK": str(self.state / "sys" / "inside-vm"),
            "CLAUDE_PLUGIN_DATA": self.data.as_posix(),
            "HOME": str(self.root),
        }
        for kept in ("SYSTEMROOT", "TEMP", "TMP"):
            if kept in os.environ:
                env[kept] = os.environ[kept]
        return subprocess.run([SH, str(HERE / script), *args], cwd=cwd or self.project, env=env,
                              capture_output=True, text=True, encoding="utf-8")
