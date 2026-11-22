import unittest

from standin_machine import Machine

THROUGH_REQUIREMENTS = ["000_problem.md", "001_scope-map.md", "002_requirements.md"]


class Stage(unittest.TestCase):
    def setUp(self):
        self.machine = Machine(self)

    def chosen(self, *documents, folder="planning"):
        (self.machine.project / folder).mkdir(parents=True, exist_ok=True)
        for document in documents:
            self.machine.document(document, folder)
        done = self.machine.run("stage.sh", "remember", folder)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    def report(self):
        done = self.machine.run("stage.sh", "report")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        return done.stdout

    def test_a_project_never_seen_has_no_planning_folder(self):
        out = self.report()
        self.assertIn("- planning folder: not chosen yet for this project", out)
        self.assertNotIn("next stage", out)

    def test_a_chosen_folder_is_remembered_for_that_project_only(self):
        self.chosen()
        self.assertIn("- planning folder: planning (chosen earlier for this project)", self.report())
        elsewhere = self.machine.root / "another"
        elsewhere.mkdir()
        self.assertIn("not chosen yet", self.machine.run("stage.sh", "report", cwd=elsewhere).stdout)

    def test_choosing_again_replaces_the_first_choice(self):
        self.chosen()
        self.chosen(folder="docs/plan")
        out = self.report()
        self.assertIn("- planning folder: docs/plan (chosen earlier", out)
        remembered = (self.machine.data / "planning-folders").read_text(encoding="utf-8")
        self.assertEqual(len(remembered.splitlines()), 1)

    def test_the_folder_is_found_from_a_folder_below_the_repository_root(self):
        self.machine.repository()
        self.chosen("000_problem.md")
        below = self.machine.project / "src"
        below.mkdir()
        self.assertIn("- found: problem (000_problem.md)", self.machine.run("stage.sh", "report", cwd=below).stdout)

    def test_an_empty_folder_starts_at_the_problem(self):
        self.chosen()
        out = self.report()
        self.assertIn("- found: no planning document", out)
        self.assertIn("- next stage by the documents: problem", out)

    def test_the_next_stage_is_named_with_the_document_it_writes(self):
        self.chosen()
        self.assertIn("- next stage by the documents: problem (its document: planning/000_problem.md)", self.report())
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a.md", folder="docs/plan")
        self.assertIn("- next stage by the documents: slice (its document: docs/plan/slice-001/004_slice.md)",
                      self.report())

    def test_a_problem_alone_makes_scope_next(self):
        self.chosen("000_problem.md")
        out = self.report()
        self.assertIn("- found: problem (000_problem.md)", out)
        self.assertIn("- next stage by the documents: scope", out)
        self.assertNotIn("out of order", out)

    def test_documents_through_requirements_make_research_next(self):
        self.chosen(*THROUGH_REQUIREMENTS)
        self.assertIn("- next stage by the documents: research", self.report())

    def test_an_empty_research_folder_is_not_research_done(self):
        self.chosen(*THROUGH_REQUIREMENTS)
        (self.machine.project / "planning" / "research").mkdir()
        self.assertIn("- next stage by the documents: research", self.report())

    def test_research_done_makes_the_slice_next(self):
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a-dependency.md")
        self.assertIn("- next stage by the documents: slice", self.report())

    def test_a_slice_with_no_requirements_behind_it_is_out_of_order(self):
        self.chosen("000_problem.md", "001_scope-map.md", "slice-001/004_slice.md")
        out = self.report()
        self.assertIn("- out of order: slice (slice-001/004_slice.md) exists but nothing was found for: "
                      "requirements, research", out)
        self.assertIn("- next stage by the documents: requirements", out)

    def test_the_latest_slice_is_the_one_read(self):
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a.md",
                    *[f"slice-001/{name}.md" for name in
                      ("004_slice", "005_questions", "006_answers", "007_open-facts", "008_design", "009_screens",
                       "010_stack", "011_readiness", "012_owner-list")],
                    "slice-002/004_slice.md")
        out = self.report()
        self.assertIn("slice (slice-002/004_slice.md)", out)
        self.assertIn("- next stage by the documents: questions", out)

    def test_a_slice_fully_planned_is_ready_to_build(self):
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a.md",
                    *[f"slice-001/{name}.md" for name in
                      ("004_slice", "005_questions", "006_answers", "007_open-facts", "008_design", "009_screens",
                       "010_stack", "011_readiness", "012_owner-list")])
        out = self.report()
        self.assertIn("- every planning document of slice-001 exists", out)
        self.assertIn("- next stage by the documents: none, slice-001 is planned and ready to build", out)

    def test_a_document_takes_the_next_number_in_the_folder_whatever_came_before(self):
        self.chosen("000_problem.md", "001_scope-map.md", "002_scope-map-v002.md")
        out = self.report()
        self.assertIn("scope map (002_scope-map-v002.md)", out)
        self.assertIn("- next stage by the documents: requirements (its document: planning/003_requirements.md)", out)

    def test_a_document_is_found_by_its_name_not_its_number(self):
        self.chosen("000_problem.md", "001_scope-map.md", "005_requirements.md", "007_research/a.md")
        out = self.report()
        self.assertIn("requirements (005_requirements.md)", out)
        self.assertIn("- next stage by the documents: slice (its document: planning/slice-001/008_slice.md)", out)

    def requirements(self, text):
        self.chosen("000_problem.md", "001_scope-map.md")
        (self.machine.project / "planning" / "002_requirements.md").write_text(text, encoding="utf-8")
        return self.report()

    def test_the_requirements_are_counted_and_the_checked_ones_too(self):
        out = self.requirements("# Requirements: borrow a tool\n\n"
                                "- [x] **record-a-loan**: A volunteer records who took which tool.\n"
                                "- [ ] **see-who-has-it**: A volunteer sees who has a tool.\n"
                                "* [X] **loans-of-a-member**: A volunteer sees what a member has out.\n\n"
                                "## Out for now\n- Reserving a tool.\n")
        self.assertIn("- requirements (002_requirements.md): 3 items, 2 checked", out)
        self.assertNotIn("no name", out)
        self.assertNotIn("twice", out)

    def test_a_requirement_with_no_name_of_its_own_is_said_by_its_line(self):
        out = self.requirements("- [ ] **record-a-loan**: A volunteer records a loan.\n"
                                "- [ ] A volunteer sees who has a tool.\n"
                                "- [ ] **Sees Loans**: A volunteer sees the loans.\n")
        self.assertIn("- requirements (002_requirements.md): 3 items, 0 checked", out)
        self.assertIn("- a requirement with no short name of its own: line 2, line 3", out)

    def test_a_name_used_twice_is_said_once(self):
        out = self.requirements("- [ ] **record-a-loan**: One.\n- [x] **record-a-loan**: Two.\n"
                                "- [ ] **record-a-loan**: Three.\n")
        self.assertIn("- a requirement's name used more than once: record-a-loan\n", out)

    def test_a_requirements_document_with_no_box_counts_none(self):
        out = self.requirements("# Requirements\n\nA member adds a book.\n- a plain bullet\n")
        self.assertIn("- requirements (002_requirements.md): 0 items, 0 checked", out)

    def test_nothing_is_counted_before_the_requirements_exist(self):
        self.chosen("000_problem.md", "001_scope-map.md")
        self.assertNotIn("items", self.report())

    # Found by the first end-to-end run: a session asked for the folder and never recorded it, so
    # every document went unnumbered and unfound; and a session that finished a stage had no way
    # to learn the next one's document.
    def test_an_unchosen_folder_comes_with_the_command_that_records_it(self):
        out = self.report()
        self.assertRegex(out, r'- to record the folder the user names \(it is made if it is not there\): '
                              r'.*sh ".*stage\.sh" remember FOLDER')
        self.assertIn("then read the documents again", out)

    def test_a_command_the_report_gives_reaches_the_same_record_as_the_report(self):
        # A session runs these commands in its own shell, which is not told where the plugin keeps its data.
        out = self.report()
        self.assertIn(f'CLAUDE_PLUGIN_DATA="{self.machine.data.as_posix()}" sh "', out)
        self.chosen("000_problem.md")
        self.assertIn(f'read the documents again: CLAUDE_PLUGIN_DATA="{self.machine.data.as_posix()}" sh "', self.report())

    def test_remembering_a_folder_that_is_not_there_makes_it(self):
        done = self.machine.run("stage.sh", "remember", "docs/planning")
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertTrue((self.machine.project / "docs" / "planning").is_dir())
        self.assertIn("- next stage by the documents: problem (its document: docs/planning/000_problem.md)",
                      self.report())

    def test_a_full_path_inside_the_project_is_recorded_as_the_folder_inside_it(self):
        # Found by the end-to-end runs: a session gave the folder by its full path and was refused.
        done = self.machine.run("stage.sh", "remember", (self.machine.project / "planning").as_posix())
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertIn("- planning folder: planning (chosen earlier for this project)", self.report())

    def test_a_folder_outside_the_project_is_refused(self):
        self.assertEqual(self.machine.run("stage.sh", "remember", "../elsewhere").returncode, 3)
        self.assertEqual(self.machine.run("stage.sh", "remember", "/tmp/elsewhere").returncode, 3)

    def test_the_report_says_how_the_documents_are_read_again(self):
        self.chosen("000_problem.md")
        self.assertRegex(self.report(), r'- after a stage is finished, read the documents again: .*sh ".*stage\.sh" report')

    def test_a_remembered_folder_that_is_gone_is_said(self):
        self.chosen()
        (self.machine.project / "planning").rmdir()
        self.assertIn("- planning folder: planning (chosen earlier for this project) no longer exists",
                      self.report())

    def test_remembering_no_folder_is_refused(self):
        self.assertEqual(self.machine.run("stage.sh", "remember").returncode, 3)


if __name__ == "__main__":
    unittest.main()
