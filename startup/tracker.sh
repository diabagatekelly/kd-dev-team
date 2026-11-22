#!/bin/sh
# What is open on the project's tracker: pull requests and issues. Changes nothing.
#
#   tracker.sh    print the repository, each open pull request with whether it is ready to merge
#                 or has comments to address, and the open issues, those labelled critical, high
#                 or blocking first
#
# GitHub is the one code host read so far, through its own tool (`gh`). Exit 3 with a line
# starting "REFUSED" when the tool answers in a way this script does not recognise.
set -u

say() { printf '%s\n' "$*"; }
refuse() { say "- REFUSED: $*"; exit 3; }
HERE=$(cd "$(dirname "$0")" && pwd)

QUERY='query($owner:String!,$name:String!){repository(owner:$owner,name:$name){pullRequests(states:OPEN,first:30,orderBy:{field:CREATED_AT,direction:ASC}){totalCount nodes{number title isDraft mergeable reviewDecision headRefName author{login} commits(last:1){nodes{commit{committedDate statusCheckRollup{state}}}} reviewThreads(first:100){nodes{isResolved}} comments(last:50){nodes{createdAt author{login}}}}} issues(states:OPEN,first:100,orderBy:{field:CREATED_AT,direction:ASC}){totalCount nodes{number title labels(first:20){nodes{name}}}}}}'

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  say "- repository: none (this folder is not a git repository)"; exit 0
fi
if ! url=$(git remote get-url origin 2>/dev/null); then
  say "- repository: a git repository with no remote named origin"; exit 0
fi
case "$url" in
  *github.com[:/]*/*) ;;
  *) say "- repository: a git repository whose remote is $url"
     say "- tracker: not read (the remote is not on GitHub, the one code host read so far)"; exit 0 ;;
esac
slug=${url#*github.com[:/]}; slug=${slug%.git}; slug=${slug%/}
owner=${slug%%/*}; name=${slug#*/}
case "$owner$name" in *[!A-Za-z0-9._-]*|"") refuse "cannot read an owner and a name from the remote $url" ;; esac
say "- repository: $owner/$name on GitHub"
if ! command -v gh >/dev/null 2>&1; then
  say "- tracker: not read (the code host's tool, \`gh\`, is not installed)"; exit 0
fi
if ! gh auth status >/dev/null 2>&1; then
  say "- tracker: not read (\`gh\` is not signed in; \`gh auth login\` asks questions in a terminal)"; exit 0
fi
lines=$(gh api graphql -f owner="$owner" -f name="$name" -f query="$QUERY" --jq "$(cat "$HERE/tracker.jq")" 2>&1) \
  || refuse "\`gh api graphql\` failed: $lines"

say "$lines" | awk -F'\t' '
  function bad(what) { print "- REFUSED: the code host answered with " what; refused = 1; exit 3 }
  function count(n, one, many) { return n " " (n == 1 ? one : many) }
  function join_reasons(list, n,    i, out) { for (i = 1; i <= n; i++) out = out (i > 1 ? "; " : "") list[i]; return out }
  NR == 1 {
    if ($1 != "ok" || $2 !~ /^[0-9]+$/ || $3 !~ /^[0-9]+$/) bad("a first line this script does not know: " $0)
    pulls_total = $2; issues_total = $3; next
  }
  $1 == "pr" {
    if (NF != 10 || $2 !~ /^[0-9]+$/ || $8 !~ /^[0-9]+$/ || $9 !~ /^[0-9]+$/) bad("a pull request line this script cannot read: " $0)
    if ($4 != "true" && $4 != "false") bad("a draft state it does not know: " $4)
    if ($5 !~ /^(MERGEABLE|CONFLICTING|UNKNOWN)$/) bad("a merge state it does not know: " $5)
    if ($6 !~ /^(APPROVED|CHANGES_REQUESTED|REVIEW_REQUIRED|-)$/) bad("a review state it does not know: " $6)
    if ($7 !~ /^(SUCCESS|FAILURE|ERROR|PENDING|EXPECTED|-)$/) bad("a state of the checks it does not know: " $7)
    n = 0; split("", why)
    if ($8 > 0) why[++n] = count($8, "unresolved review thread", "unresolved review threads")
    if ($6 == "CHANGES_REQUESTED") why[++n] = "changes requested"
    if ($9 > 0) why[++n] = count($9, "comment", "comments") " by others since its last commit"
    if (n > 0) state = "comments to address (" join_reasons(why, n) ")"
    else {
      if ($4 == "true") why[++n] = "a draft"
      if ($5 == "CONFLICTING") why[++n] = "conflicts with its base branch"
      if ($5 == "UNKNOWN") why[++n] = "the code host has not yet said whether it can merge"
      if ($7 == "FAILURE" || $7 == "ERROR") why[++n] = "checks failing"
      if ($7 == "PENDING" || $7 == "EXPECTED") why[++n] = "checks still running"
      if ($6 == "REVIEW_REQUIRED") why[++n] = "a review is required"
      state = n > 0 ? "not ready (" join_reasons(why, n) ")" : "ready to merge"
    }
    pulls[++pulls_read] = "  - #" $2 " \"" $10 "\" (branch " $3 "): " state; next
  }
  $1 == "issue" {
    if (NF != 4 || $2 !~ /^[0-9]+$/) bad("an issue line this script cannot read: " $0)
    issues_read++
    labels = ""; m = split($3, each, ",")
    for (i = 1; i <= m; i++)
      if (tolower(each[i]) ~ /(^|[^a-z])(critical|high|blocker|blocking|blocks)([^a-z]|$)/) labels = labels (labels ? ", " : "") each[i]
    if (labels) ranked[++ranked_n] = "  - #" $2 " \"" $4 "\" [" labels "]"
    else if (++others <= 10) rest = rest (rest ? ", " : "") "#" $2 " \"" $4 "\""
    next
  }
  { bad("a line this script does not know: " $0) }
  END {
    if (refused) exit 3
    if (NR == 0) { print "- REFUSED: the code host answered with nothing"; exit 3 }
    print "- open pull requests: " pulls_total (pulls_total > pulls_read ? " (the first " pulls_read " read)" : "")
    for (i = 1; i <= pulls_read; i++) print pulls[i]
    line = "- open issues: " issues_total (issues_total > issues_read ? " (the first " issues_read " read)" : "")
    if (ranked_n) line = line ", of which " ranked_n (ranked_n == 1 ? " is" : " are") " labelled critical, high or blocking"
    print line
    for (i = 1; i <= ranked_n; i++) print ranked[i]
    if (ranked_n && others) print "  - with no such label: " rest (others > 10 ? ", and " (others - 10) " more" : "")
    else if (others) print "  - none labelled critical, high or blocking: " rest (others > 10 ? ", and " (others - 10) " more" : "")
  }'
