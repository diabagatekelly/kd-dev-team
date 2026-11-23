# Turns the code host's answer into the lines tracker.sh reads: one "ok" line with the two
# totals, then one line per open pull request, per merged pull request whose description has a
# line "Completes: ..." (what it names there, as written) and per issue, fields separated by
# tabs, none empty.
def flat: gsub("[\\t\\n\\r]"; " ");
def completes: [(. // "") | split("\n")[] | select(test("^\\s*completes\\s*:"; "i"))
    | sub("^\\s*[A-Za-z]+\\s*:"; "") | flat | gsub(" +"; " ") | sub("^ "; "") | sub(" $"; "")] | map(select(. != "")) | .[0];
.data.repository as $r
| (["ok", $r.pullRequests.totalCount, $r.issues.totalCount] | @tsv),
  ($r.pullRequests.nodes[] | . as $p | .commits.nodes[0].commit as $c
    | ["pr", .number, .headRefName, .isDraft, .mergeable, (.reviewDecision // "-"),
       ($c.statusCheckRollup.state // "-"),
       ([.reviewThreads.nodes[] | select(.isResolved | not)] | length),
       ([.comments.nodes[]
         | select(.createdAt > $c.committedDate and (.author.login // "") != ($p.author.login // ""))] | length),
       (.title | flat)] | @tsv),
  (($r.merged.nodes // [])[] | (.body | completes) as $names | select($names != null)
    | ["merged", .number, $names, (.title | flat)] | @tsv),
  ($r.issues.nodes[]
    | ["issue", .number, ([.labels.nodes[].name | flat] | join(",") | if . == "" then "-" else . end),
       (.title | flat)] | @tsv)
