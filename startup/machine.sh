#!/bin/sh
# The machine a session starts on: its system, the VM tool, its sign-in, its locks, its VMs.
#
#   machine.sh inspect          print what is there; changes nothing
#   machine.sh secure           turn every lock on; exit 0 only when all are on
#   machine.sh install [--yes]  install the VM tool; without --yes, only say what would run
#   machine.sh create           make this project's VM, a private copy of its repository; locks first
#   machine.sh name             the name of this project's VM
#   machine.sh where            inside or outside a VM
#
# Exit 3 with a line starting "REFUSED" when a tool answers in a way this script does not
# recognise: nothing is guessed from an answer it cannot read.
set -u

say() { printf '%s\n' "$*"; }
refuse() { say "- REFUSED: $*"; exit 3; }
have() { command -v "$1" >/dev/null 2>&1; }
SELF="$(cd "$(dirname "$0")" && pwd)/machine.sh"

# Inside a VM the tool made there is nothing of the tool to inspect: the locks are set outside.
# The tool is never installed inside its own VMs, so where it is installed is the outside.
inside() { [ -e "${KD_VM_MARK:-/run/sandbox}" ] && ! have sbx; }
INSIDE="- this session is inside a VM (Docker Sandboxes): the project is worked on here"

# One VM per project, named for its folder; the number keeps two folders of one name apart.
project_root() { git rev-parse --show-toplevel 2>/dev/null || pwd -P; }
vm_name() {
  root=$(project_root)
  short=$(basename "$root" | tr 'A-Z' 'a-z' | tr -c 'a-z0-9\n' '-' | sed 's/^-*//; s/-*$//')
  say "kd-${short:-project}-$(printf '%s' "$root" | cksum | cut -d' ' -f1)"
}
continue_line() { say "- continuing inside it (the user's to run, in their own terminal): sbx run --name $1"; }

# What the VM tool's install page lists (docs.docker.com/ai/sandboxes/install, read 2026-11-21).
# Sets system, supported (yes|no), why, install_cmd, installer, installer_name.
detect_system() {
  kernel=$(uname -s 2>/dev/null) || refuse "uname did not answer"
  arch=$(uname -m 2>/dev/null) || refuse "uname did not answer"
  supported=yes; why=""; install_cmd=""; installer=""; installer_name=""
  case "$kernel" in
    Darwin)
      version=$(sw_vers -productVersion 2>/dev/null) || refuse "sw_vers did not answer"
      major=${version%%.*}
      case "$major" in ''|*[!0-9]*) refuse "sw_vers answered '$version', not a version of macOS" ;; esac
      system="macOS $version on $arch"
      install_cmd="brew trust docker/tap && brew install docker/tap/sbx"; installer=brew; installer_name=Homebrew
      if [ "$arch" != arm64 ]; then supported=no; why="on macOS it needs Apple silicon"
      elif [ "$major" -lt 14 ]; then supported=no; why="it needs macOS 14 or later"; fi ;;
    Linux)
      file="${KD_OS_RELEASE:-/etc/os-release}"
      field() { [ -r "$file" ] && sed -n "s/^$1=//p" "$file" | head -1 | tr -d '"'; }
      id=$(field ID); name=$(field NAME); version=$(field VERSION_ID)
      system="${name:-Linux}${version:+ $version} on $arch"
      install_cmd="curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh && sudo apt install docker-sbx"
      case "$(uname -r 2>/dev/null)" in
        *[Mm]icrosoft*) supported=no; why="its documentation does not list Linux inside Windows (WSL)" ;;
        *)
          number=$(say "$version" | awk -F. '/^[0-9]+(\.[0-9]+)?$/ {print $1 * 100 + $2}')
          if [ "$id" != ubuntu ] || [ -z "$number" ] || [ "$number" -lt 2404 ]; then
            supported=no; why="on Linux it needs Ubuntu 24.04 or later"
          else case "$arch" in x86_64|aarch64|arm64) ;; *) supported=no; why="it needs a 64-bit processor" ;; esac
          fi ;;
      esac ;;
    MINGW*|MSYS*|CYGWIN*)
      build=${kernel##*-}
      case "$build" in ''|*[!0-9]*) refuse "uname answered '$kernel', with no Windows build number" ;; esac
      install_cmd="winget install -h Docker.sbx"; installer=winget; installer_name=winget
      if [ "$build" -lt 22000 ]; then system="Windows 10 (build $build) on $arch"; supported=no; why="it needs Windows 11"
      else
        system="Windows 11 (build $build) on $arch"
        [ "$arch" = x86_64 ] || { supported=no; why="on Windows it needs an Intel or AMD processor"; }
      fi ;;
    *) system="$kernel on $arch"; supported=no; why="it runs on macOS, Windows 11 and Ubuntu only" ;;
  esac
}

DEFAULT_HOSTS="api.anthropic.com,claude.ai,platform.claude.com,github.com,registry.npmjs.org"

# Every setting that lets something inside a VM touch the computer outside it; each must be false.
locks() {
  cat <<'LOCKS'
browser.enabled|It cannot open pages in your own web browser
claude.chrome|It cannot see or control your own browser tabs
claude.remoteControl|It cannot be steered from another device
clipboard.imagePaste|It cannot read pictures you copied
clipboard.textCopy|It cannot put text on your clipboard
LOCKS
}
NETWORK_LOCK="It can reach only the few websites on its list"

# Prints one line per lock that is off; nothing when all are on.
locks_off() {
  settings=$(sbx settings ls 2>&1) || refuse "\`sbx settings ls\` failed: $settings"
  locks | while IFS='|' read -r key words; do
    value=$(say "$settings" | awk -v k="$key" '$1==k {print $2}')
    case "$value" in
      false) ;;
      true) say "  - OFF: $words ($key)" ;;
      *) say "- REFUSED: \`sbx settings ls\` gave '$value' for $key, neither true nor false" ;;
    esac
  done
  policies=$(sbx policy ls 2>&1) || refuse "\`sbx policy ls\` failed: $policies"
  case "$policies" in
    *default-deny-all*)
      rules=$(sbx policy inspect local-policy 2>&1) || refuse "\`sbx policy inspect\` failed: $rules"
      extra=$(say "$rules" | awk -v list=",$DEFAULT_HOSTS," '
        $1=="allow" && $3=="network" && index(list, "," $2 ",")==0 {printf "%s%s", sep, $2; sep=", "}')
      [ -z "$extra" ] || say "  - OFF: $NETWORK_LOCK (every VM can also reach $extra)" ;;
    *) say "  - OFF: $NETWORK_LOCK (the network is not refused by default)" ;;
  esac
}

# Prints the lock lines; returns 0 only when every lock is on.
lock_lines() {
  off=$(locks_off) || { say "$off"; exit 3; }
  case "$off" in *"REFUSED"*) say "$off" | grep REFUSED; exit 3 ;; esac
  total=$(( $(locks | wc -l) + 1 ))
  if [ -z "$off" ]; then say "- locks: all $total on"; return 0; fi
  say "- locks: $(say "$off" | wc -l | tr -d ' ') of $total OFF"
  say "$off"
  return 1
}

# Says whether this project has its VM and, with every lock on, how it is made or entered.
# Reads vms (the VM names) and all_on.
project_lines() {
  mine=$(vm_name)
  if say "$vms" | grep -qx "$mine"; then
    say "- VM for this project: $mine"
    [ "$all_on" != yes ] || continue_line "$mine"
  else
    say "- VM for this project: none"
    [ "$all_on" = yes ] || return 0
    if git rev-parse --git-dir >/dev/null 2>&1; then what="a private copy of this repository, inside a new VM"
    else what="this folder becomes a git repository first; then a private copy of it, inside a new VM"; fi
    say "- making it ($what): sh \"$SELF\" create"
  fi
}

inspect() {
  if inside; then say "$INSIDE"; return 0; fi
  detect_system
  if [ "$supported" = no ]; then
    say "- system: $system: NOT supported by the VM tool ($why)"
    say "- VM tool (Docker Sandboxes, \`sbx\`): no version of it runs on this system"
    return 0
  fi
  say "- system: $system (supported by the VM tool)"
  if ! have sbx; then
    say "- VM tool (Docker Sandboxes, \`sbx\`): not installed"
    say "- the command that would install it (not run): $install_cmd"
    [ -z "$installer" ] || say "- $installer_name, which that command uses: $(have "$installer" && say installed || say "not installed")"
    return 0
  fi
  version=$(sbx version 2>&1 | head -1)
  case "$version" in
    "sbx version v"[0-9]*) version=${version#sbx version }; version=${version%% *} ;;
    *) refuse "\`sbx version\` answered '$version'" ;;
  esac
  say "- VM tool (Docker Sandboxes, \`sbx\`): installed ($version)"
  if vms=$(sbx ls -q 2>&1); then :; else
    case "$vms" in
      *"not signed in"*|*"not authenticated"*)
        say "- signed in to the VM tool: no (\`sbx login\` signs in; it opens a browser and cannot be run by a script)"
        return 0 ;;
      *) refuse "\`sbx ls\` failed: $vms" ;;
    esac
  fi
  say "- signed in to the VM tool: yes"
  all_on=yes; lock_lines || all_on=no
  [ "$all_on" = yes ] || say "- turning every lock on: sh \"$SELF\" secure"
  if [ -z "$vms" ]; then say "- VMs: none"; else
    say "$vms" | grep -qv '^[A-Za-z0-9][A-Za-z0-9_.-]*$' && refuse "\`sbx ls -q\` gave a line that is not a VM's name: $vms"
    say "- VMs: $(say "$vms" | wc -l | tr -d ' ') ($(say "$vms" | tr '\n' ' ' | sed 's/ $//; s/ /, /g'))"
  fi
  project_lines
}

# Always a private copy, never the user's folder itself; never while a lock is off.
create() {
  inside && refuse "this session is already inside a VM: none is made from here"
  have sbx || refuse "the VM tool is not installed: no VM can be made"
  vms=$(sbx ls -q 2>&1) || refuse "\`sbx ls\` failed: $vms"
  mine=$(vm_name)
  if say "$vms" | grep -qx "$mine"; then
    say "- VM for this project: $mine (already there; nothing made)"; continue_line "$mine"; return 0
  fi
  secure >/dev/null || { say "not made: a lock is still off"; lock_lines; return 1; }
  git rev-parse --git-dir >/dev/null 2>&1 || git init -q || refuse "\`git init\` failed in $(pwd -P)"
  mine=$(vm_name)
  made=$(cd "$(project_root)" && sbx --no-input create --clone --name "$mine" claude . 2>&1) \
    || refuse "\`sbx create\` failed: $made"
  say "- VM for this project: $mine (just made)"
  continue_line "$mine"
}

secure() {
  have sbx || refuse "the VM tool is not installed: there is nothing to lock"
  settings=$(sbx settings ls 2>&1) || refuse "\`sbx settings ls\` failed: $settings"
  locks | while IFS='|' read -r key words; do
    [ "$(say "$settings" | awk -v k="$key" '$1==k {print $2}')" = false ] || sbx settings set "$key" false >/dev/null
  done
  case "$(sbx policy ls 2>&1)" in *default-deny-all*) ;; *) sbx policy init deny-all >/dev/null ;; esac
  sbx policy allow network "$DEFAULT_HOSTS" >/dev/null
  lock_lines || return 1
  vms=$(sbx ls -q 2>&1) || refuse "\`sbx ls\` failed: $vms"
  all_on=yes; project_lines
}

install() {
  detect_system
  [ "$supported" = yes ] || refuse "$system is not supported by the VM tool ($why): nothing to install"
  if have sbx; then say "the VM tool is already installed"; return 0; fi
  if [ "${1:-}" != "--yes" ]; then
    say "not installed: this needs the user's yes. It would run: $install_cmd"
    return 1
  fi
  case "$kernel" in
    Darwin)
      have brew || { say "not installed: Homebrew is needed first (https://brew.sh)"; return 1; }
      brew trust docker/tap && brew install docker/tap/sbx ;;
    Linux)
      say "not installed: on Linux the command asks for an administrator's password, so it is the user's to run: $install_cmd"
      return 1 ;;
    *)
      have winget || { say "not installed: winget is needed first"; return 1; }
      winget install -h Docker.sbx ;;
  esac
}

case "${1:-}" in
  inspect) inspect ;;
  secure) secure ;;
  install) shift; install "$@" ;;
  create) create ;;
  name) vm_name ;;
  where) if inside; then say inside; else say outside; fi ;;
  *) sed -n '4,9p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
