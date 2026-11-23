import json
import shutil
import subprocess
import unittest

from standin_machine import HERE, Machine

REMOTE = "https://github.com/someone/something.git"


def pull(number, title="A change", branch="a-branch", draft="false", mergeable="MERGEABLE",
         review="-", checks="SUCCESS", unresolved=0, later=0):
    return "\t".join(["pr", str(number), branch, draft, mergeable, review, checks, str(unresolved), str(later), title])


def issue(number, title="A fault", labels="-"):
    return "\t".join(["issue", str(number), labels, title])


def merged(number, names, title="A slice built"):
    return "\t".join(["merged", str(number), names, title])


class Tracker(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def read(self, *lines, issues=None, pulls=None):
        """The tracker's section when the code host answers with these pull requests and issues."""
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        count = lambda kind: sum(line.startswith(kind) for line in lines)
        head = f"ok\t{count('pr') if pulls is None else pulls}\t{count('issue') if issues is None else issues}"
        self.machine.set("gh/lines", "\n".join([head, *lines]))
        done = self.machine.run("tracker.sh")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def test_a_folder_that_is_not_a_repository_has_no_tracker(self):
        out = self.machine.run("tracker.sh").stdout
        self.assertIn("- repository: none (this folder is not a git repository)", out)

    def test_a_repository_with_no_remote_has_no_tracker(self):
        self.machine.repository()
        self.assertIn("- repository: a git repository with no remote named origin", self.machine.run("tracker.sh").stdout)

    def test_a_remote_on_another_host_is_not_read(self):
        self.machine.repository("https://example.org/someone/something.git")
        self.machine.have("gh")
        out = self.machine.run("tracker.sh").stdout
        self.assertIn("- tracker: not read (the remote is not on GitHub, the one code host read so far)", out)
        self.assertEqual(self.machine.calls(), [])

    def test_no_tool_for_the_code_host_is_said(self):
        self.machine.repository("git@github.com:someone/something.git")
        out = self.machine.run("tracker.sh").stdout
        self.assertIn("- repository: someone/something on GitHub", out)
        self.assertIn("- tracker: not read (the code host's tool, `gh`, is not installed)", out)

    def test_a_tool_that_is_signed_out_is_said_with_the_step_that_signs_in(self):
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        self.machine.set("gh/signed_out", "")
        out = self.machine.run("tracker.sh").stdout
        self.assertIn("- tracker: not read (`gh` is not signed in; `gh auth login` asks questions in a terminal)", out)

    def test_the_repository_is_asked_for_by_owner_and_name(self):
        self.read()
        asked = [c for c in self.machine.calls() if c.startswith("gh api graphql")]
        self.assertEqual(len(asked), 1)
        self.assertIn("owner=someone", asked[0])
        self.assertIn("name=something", asked[0])

    def test_nothing_open(self):
        out = self.read()
        self.assertIn("- open pull requests: 0", out)
        self.assertIn("- open issues: 0", out)

    def test_a_pull_request_with_nothing_against_it_is_ready_to_merge(self):
        self.assertIn('  - #4 "A change" (branch a-branch): ready to merge', self.read(pull(4)))

    def test_an_approved_pull_request_with_no_checks_is_ready_to_merge(self):
        self.assertIn("ready to merge", self.read(pull(4, review="APPROVED", checks="-")))

    def test_unresolved_threads_are_comments_to_address(self):
        self.assertIn("(branch a-branch): comments to address (2 unresolved review threads)",
                      self.read(pull(4, unresolved=2)))

    def test_changes_requested_and_later_comments_are_comments_to_address(self):
        out = self.read(pull(4, review="CHANGES_REQUESTED", unresolved=1, later=3))
        self.assertIn("comments to address (1 unresolved review thread; changes requested; "
                      "3 comments by others since its last commit)", out)

    def test_a_pull_request_that_cannot_merge_yet_says_why(self):
        out = self.read(pull(4, draft="true", mergeable="CONFLICTING", checks="FAILURE", review="REVIEW_REQUIRED"))
        self.assertIn("not ready (a draft; conflicts with its base branch; checks failing; a review is required)", out)

    def test_checks_still_running_are_not_ready(self):
        self.assertIn("not ready (checks still running)", self.read(pull(4, checks="PENDING")))

    def test_issues_with_a_severity_are_ranked_and_the_rest_counted_and_shown(self):
        out = self.read(issue(7, "Data lost", "bug,severity: Critical"), issue(8, "Slow", "High"),
                        issue(9, "A typo"), issue(10, "An idea", "enhancement,highlight"),
                        issue(11, "Stops the slice", "blocker"))
        self.assertIn("- open issues: 5, of which 3 are labelled critical, high or blocking", out)
        self.assertIn('  - #7 "Data lost" [severity: Critical]', out)
        self.assertIn('  - #8 "Slow" [High]', out)
        self.assertIn('  - #11 "Stops the slice" [blocker]', out)
        self.assertIn('  - with no such label: #9 "A typo", #10 "An idea"', out)

    def test_more_issues_than_were_fetched_is_said(self):
        self.assertIn("- open issues: 240 (the first 1 read)", self.read(issue(9), issues=240))

    # The coming-back of the slice stage (decision 37): what merged work says it completes.
    def test_merged_work_that_names_what_it_completes_is_shown(self):
        out = self.read(merged(12, "slice 2: record-a-loan / 1, record-a-loan / 2", "Record a loan"))
        self.assertIn("- merged pull requests that name what they complete: 1", out)
        self.assertIn('  - #12 "Record a loan": slice 2: record-a-loan / 1, record-a-loan / 2', out)
        self.assertIn("- open pull requests: 0", out)

    def test_with_no_merged_work_nothing_is_said_of_it(self):
        self.assertNotIn("merged", self.read(pull(4)))

    def test_the_work_is_given_to_the_stage_script_a_line_each(self):
        self.read(merged(12, "slice 2: record-a-loan / 1"), issue(14, "Loans show twice", "bug"), pull(4))
        done = self.machine.run("tracker.sh", "work")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(done.stdout.splitlines(), ["merged\t12\tslice 2: record-a-loan / 1", "issue\t14\tLoans show twice"])

    def test_where_no_tracker_is_read_the_work_is_nothing(self):
        done = self.machine.run("tracker.sh", "work")
        self.assertEqual((done.returncode, done.stdout), (0, ""))
        self.machine.repository(REMOTE)
        self.assertEqual(self.machine.run("tracker.sh", "work").stdout, "")

    def test_work_that_cannot_be_read_is_refused(self):
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        self.machine.set("gh/lines", "ok\t0\t0\n" + "merged\ttwelve\tslice 2: a / 1\tA title")
        for mode in ((), ("work",)):
            done = self.machine.run("tracker.sh", *mode)
            self.assertEqual(done.returncode, 3, done.stdout)
            self.assertIn("REFUSED", done.stdout)

    def test_a_word_it_does_not_know_is_refused(self):
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        self.machine.set("gh/lines", "ok\t1\t0\n" + pull(4, mergeable="PERHAPS"))
        done = self.machine.run("tracker.sh")
        self.assertEqual(done.returncode, 3)
        self.assertIn("REFUSED", done.stdout)
        self.assertIn("PERHAPS", done.stdout)

    def test_an_answer_without_its_first_line_is_refused(self):
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        self.machine.set("gh/lines", '{"message": "Bad credentials"}')
        self.assertEqual(self.machine.run("tracker.sh").returncode, 3)

    def test_a_call_that_fails_is_refused_with_the_tools_words(self):
        self.machine.repository(REMOTE)
        self.machine.have("gh")
        self.machine.set("gh/api_fail", "")
        done = self.machine.run("tracker.sh")
        self.assertEqual(done.returncode, 3)
        self.assertIn("Could not resolve to a Repository", done.stdout)


ANSWER = {"data": {"repository": {
    "pullRequests": {"totalCount": 1, "nodes": [{
        "number": 4, "title": "A\tchange", "isDraft": False, "mergeable": "MERGEABLE", "reviewDecision": None,
        "headRefName": "a-branch", "author": {"login": "writer"},
        "commits": {"nodes": [{"commit": {"committedDate": "2026-01-02T00:00:00Z", "statusCheckRollup": None}}]},
        "reviewThreads": {"nodes": [{"isResolved": True}, {"isResolved": False}, {"isResolved": False}]},
        "comments": {"nodes": [
            {"createdAt": "2026-01-01T00:00:00Z", "author": {"login": "reviewer"}},
            {"createdAt": "2026-01-03T00:00:00Z", "author": {"login": "reviewer"}},
            {"createdAt": "2026-01-03T00:00:00Z", "author": None},
            {"createdAt": "2026-01-03T00:00:00Z", "author": {"login": "writer"}}]}}]},
    "merged": {"nodes": [
        {"number": 3, "title": "Record a loan", "body": "What it does.\r\n\r\ncompletes:  slice 2: record-a-loan / 1,\trecord-a-loan / 2 \r\nMore."},
        {"number": 2, "title": "A tidy-up", "body": "Nothing named."},
        {"number": 1, "title": "No body", "body": None}]},
    "issues": {"totalCount": 2, "nodes": [
        {"number": 7, "title": "Data lost", "labels": {"nodes": [{"name": "bug"}, {"name": "critical"}]}},
        {"number": 9, "title": "A typo", "labels": {"nodes": []}}]}}}}


@unittest.skipUnless(shutil.which("jq"), "jq is not installed; the code host's tool carries its own")
class Filter(unittest.TestCase):
    def test_the_filter_turns_the_code_hosts_answer_into_the_lines_the_script_reads(self):
        done = subprocess.run(["jq", "-r", "-f", str(HERE / "tracker.jq")], input=json.dumps(ANSWER),
                              capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(done.stdout.splitlines(), [
            "ok\t1\t2",
            "pr\t4\ta-branch\tfalse\tMERGEABLE\t-\t-\t2\t2\tA change",
            "merged\t3\tslice 2: record-a-loan / 1, record-a-loan / 2\tRecord a loan",
            "issue\t7\tbug,critical\tData lost",
            "issue\t9\t-\tA typo"])


if __name__ == "__main__":
    unittest.main()
