#!/bin/sh
# Run once inside the evaluation VM, from the repository's root: puts the stand-ins on the
# path ahead of any real tool and gives the trial plugin the startup scripts it reports on.
#   sh steps/00-startup/eval/setup-vm.sh BIN_FOLDER     (a folder early on the PATH)
set -eu
bin=${1:?name a folder early on the PATH}
here=$(cd "$(dirname "$0")" && pwd); root=$(cd "$here/../../.." && pwd)
sudo mkdir -p /opt/standin "$bin"
sudo cp "$root"/startup/standin/* /opt/standin/
for tool in sbx gh brew winget sw_vers uname curl; do
  sudo cp "$here/standin-wrapper.sh" "$bin/$tool"; sudo chmod 755 "$bin/$tool"
done
python3 -I "$here/make_cases.py" >/dev/null
python3 -I "$here/make_cases.py" --table >/dev/null
echo "stand-ins in $bin; uname here answers: $(uname -s)"
