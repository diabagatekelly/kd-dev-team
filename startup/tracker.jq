# Turns the code host's answer into the lines tracker.sh reads: one "ok" line with the two
# totals, then one line per pull request and per issue, fields separated by tabs, none empty.
def flat: gsub("[\\t\\n\\r]"; " ");
.data.repository as $r
| (["ok", $r.pullRequests.totalCount, $r.issues.totalCount] | @tsv),
  ($r.pullRequests.nodes[] | . as $p | .commits.nodes[0].commit as $c
    | ["pr", .number, .headRefName, .isDraft, .mergeable, (.reviewDecision // "-"),
       ($c.statusCheckRollup.state // "-"),
       ([.reviewThreads.nodes[] | select(.isResolved | not)] | length),
       ([.comments.nodes[]
         | select(.createdAt > $c.committedDate and (.author.login // "") != ($p.author.login // ""))] | length),
       (.title | flat)] | @tsv),
  ($r.issues.nodes[]
    | ["issue", .number, ([.labels.nodes[].name | flat] | join(",") | if . == "" then "-" else . end),
       (.title | flat)] | @tsv)
