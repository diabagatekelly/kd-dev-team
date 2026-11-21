#!/usr/bin/env bash
# The launcher's first backend: Docker Sandboxes (sbx) on macOS.
#
#   vm.sh check                    what is present and missing; changes nothing
#   vm.sh install [--yes]          install the VM tool (asks first without --yes)
#   vm.sh secure                   lock the tool down (run by create; safe to repeat)
#   vm.sh status                   say in plain words whether each lock is on
#   vm.sh selftest NAME            try, from inside the VM, to reach what it must not
#   vm.sh create NAME DIR          a VM holding a private clone of the repository in DIR
#   vm.sh allow NAME HOST[,HOST]   allow more hosts, for that VM only
#   vm.sh exec NAME COMMAND        run a shell command in the VM, in the clone
#   vm.sh run NAME PROMPT          run a session in the VM on PROMPT, prompts skipped
#   vm.sh out NAME DEST            copy the VM's transcripts to DEST on the host
#   vm.sh destroy NAME             remove the VM and everything in it
#
# Each verb is one line of the contract in V0 of TODO.md in the kad-dev-team-plugin repository. The hand steps
# no verb can do: `sbx login`, and signing the model in once inside a VM.
set -euo pipefail

say() { printf '%s\n' "$*"; }

need_macos_arm() {
  [ "$(uname -s)" = "Darwin" ] || { say "not macOS: this backend is for macOS only"; return 1; }
  [ "$(uname -m)" = "arm64" ] || { say "not Apple silicon: Docker Sandboxes needs it on macOS"; return 1; }
}

check() {
  local missing=0
  need_macos_arm || missing=1
  if command -v sbx >/dev/null 2>&1; then
    say "sbx: present ($(sbx version 2>/dev/null | head -1 || echo 'version unknown'))"
  else
    say "sbx: missing"; missing=1
  fi
  if command -v brew >/dev/null 2>&1; then say "brew: present"; else say "brew: missing (needed to install sbx)"; fi
  return "$missing"
}

install() {
  need_macos_arm
  if command -v sbx >/dev/null 2>&1; then say "sbx is already installed"; return 0; fi
  command -v brew >/dev/null 2>&1 || { say "Homebrew is needed to install sbx: https://brew.sh"; return 1; }
  if [ "${1:-}" != "--yes" ]; then
    printf 'Install Docker Sandboxes (brew install docker/tap/sbx)? [y/N] '
    read -r answer
    [ "$answer" = "y" ] || { say "not installed"; return 1; }
  fi
  brew trust docker/tap
  brew install docker/tap/sbx
  say "installed. One step is yours: run 'sbx login' (it opens a browser)."
}

DEFAULT_HOSTS="api.anthropic.com,claude.ai,platform.claude.com,github.com,registry.npmjs.org"

# Every setting that lets something inside the VM touch the computer outside it.
# Each is switched off; the words are what `status` shows the owner.
locks() {
  cat <<'LOCKS'
browser.enabled|It cannot open pages in your own web browser
claude.chrome|It cannot see or control your own browser tabs
claude.remoteControl|It cannot be steered from another device
clipboard.imagePaste|It cannot read pictures you copied
clipboard.textCopy|It cannot put text on your clipboard
LOCKS
}

setting() { sbx settings ls 2>/dev/null | awk -v k="$1" '$1==k {print $2}'; }
deny_by_default() { sbx policy ls 2>/dev/null | grep -q 'default-deny-all'; }

# Hosts every VM may reach that are not on the launcher's list: an allow rule
# someone added for all VMs. The lock is not on while one stands.
extra_global_hosts() {
  sbx policy inspect local-policy 2>/dev/null \
    | awk '$1=="allow" && $3=="network" {print $2}' \
    | while read -r host; do
        case ",$DEFAULT_HOSTS," in *",$host,"*) ;; *) printf '%s\n' "$host" ;; esac
      done
}

secure() {
  local key
  while IFS='|' read -r key _; do
    [ "$(setting "$key")" = "false" ] || sbx settings set "$key" false >/dev/null
  done < <(locks)
  deny_by_default || sbx policy init deny-all >/dev/null
  sbx policy allow network "$DEFAULT_HOSTS" >/dev/null
  status
}

# Exit 0 only when every lock is on; create refuses to go on otherwise.
status() {
  local bad=0 key words
  while IFS='|' read -r key words; do
    if [ "$(setting "$key")" = "false" ]; then say "  ok   $words"
    else say "  OFF  $words  (fix: vm.sh secure)"; bad=1; fi
  done < <(locks)
  local extra
  extra=$(extra_global_hosts | tr '\n' ' ')
  if ! deny_by_default; then say "  OFF  It can reach only the few websites on its list  (fix: vm.sh secure)"; bad=1
  elif [ -n "$extra" ]; then say "  OFF  Every VM can also reach: ${extra}(not on the list; remove with: sbx policy rm network --resource HOST --force)"; bad=1
  else say "  ok   It can reach only the few websites on its list; everything else is refused"; fi
  return "$bad"
}

# Runs inside the VM: each line tries something that must fail.
selftest() {
  local name="$1" lan gateway
  lan=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo 192.0.2.1)
  gateway=$(route -n get default 2>/dev/null | awk '/gateway/{print $2}')
  sbx exec -e "LAN=$lan" -e "GATEWAY=${gateway:-192.0.2.1}" "$name" bash -lc '
    bad=0
    blocked() { label="$1"; shift; code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$@" 2>/dev/null)
      case "$code" in 000|403) echo "  ok   $label";; *) echo "  FAIL $label (answered $code)"; bad=1;; esac; }
    blocked "A website that is not on the list is refused" https://example.com
    blocked "It cannot go round the gatekeeper" --noproxy "*" https://example.com
    blocked "It cannot reach this computer" --noproxy "*" "http://$LAN:8765/"
    blocked "It cannot reach this computer through the gatekeeper" "http://$LAN:8765/"
    blocked "It cannot reach your router or home network" --noproxy "*" "http://$GATEWAY/"
    blocked "It cannot reach the cloud settings address" --noproxy "*" http://169.254.169.254/
    if touch /run/sandbox/source/.selftest 2>/dev/null; then echo "  FAIL It can change your copy of the project"; bad=1
    else echo "  ok   It cannot change your copy of the project"; fi
    # With the lock on, the opener only prints the address for a person to open.
    if ! command -v xdg-open >/dev/null || xdg-open https://example.com/vm-selftest 2>&1 | grep -q "Open this URL"; then echo "  ok   It cannot open pages in your own web browser"
    else echo "  FAIL It can open pages in your own web browser"; bad=1; fi
    exit $bad'
}

# The clone sits in the VM at the same path the repository has on the host.
workdir() { sbx inspect "$1" --json 2>/dev/null | python3 -c 'import json,sys; d=json.load(sys.stdin); d=d[0] if isinstance(d,list) else d; print(d.get("workspace") or d.get("Workspace") or "")' 2>/dev/null; }

# Always a private clone, never the owner's folder itself; never without the locks.
create() {
  secure >/dev/null || { say "the locks are not all on; not creating a VM:"; status; return 1; }
  ( cd "$2" && sbx --no-input create --clone ${VM_TEMPLATE:+--template "$VM_TEMPLATE"} --name "$1" claude . )
}
allow() { sbx policy allow network --sandbox "$1" "$2"; }
in_vm() { local name="$1"; shift; sbx exec -w "$(workdir "$name")" "$name" "$@"; }
run() { in_vm "$1" claude -p --dangerously-skip-permissions "$2"; }
out() { mkdir -p "$2" && sbx cp "$1:/home/agent/.claude/projects" "$2"; }
destroy() { sbx rm --force "$1"; }

case "${1:-}" in
  check) check ;;
  install) shift; install "$@" ;;
  secure) secure ;;
  status) status ;;
  selftest) selftest "$2" ;;
  create) create "$2" "$3" ;;
  allow) allow "$2" "$3" ;;
  exec) name="$2"; shift 2; in_vm "$name" bash -lc "$*" ;;
  run) run "$2" "$3" ;;
  out) out "$2" "$3" ;;
  destroy) destroy "$2" ;;
  *) sed -n '4,14p' "$0" | sed 's/^# \{0,3\}//'; exit 2 ;;
esac
