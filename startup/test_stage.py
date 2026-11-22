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

    def test_a_slice_fully_planned_sends_the_session_back_to_the_scope_map(self):
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a.md",
                    *[f"slice-001/{name}.md" for name in
                      ("004_slice", "005_questions", "006_answers", "007_open-facts", "008_design", "009_screens",
                       "010_stack", "011_readiness", "012_owner-list")])
        out = self.report()
        self.assertIn("- every planning document of slice-001 exists", out)
        self.assertIn("- next stage by the documents: scope map, re-read with the user before the next slice "
                      "(a changed map is a new document, planning/013_scope-map-v002.md; "
                      "001_scope-map.md is kept)", out)

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

    def test_the_third_map_is_numbered_after_everything_there(self):
        self.chosen(*THROUGH_REQUIREMENTS, "003_research/a.md",
                    *[f"slice-001/{name}.md" for name in
                      ("004_slice", "005_questions", "006_answers", "007_open-facts", "008_design", "009_screens",
                       "010_stack", "011_readiness", "012_owner-list")], "013_scope-map-v002.md")
        self.assertIn("(a changed map is a new document, planning/014_scope-map-v003.md; "
                      "013_scope-map-v002.md is kept)", self.report())

    def test_a_remembered_folder_that_is_gone_is_said(self):
        self.chosen()
        (self.machine.project / "planning").rmdir()
        self.assertIn("- planning folder: planning (chosen earlier for this project) no longer exists",
                      self.report())

    def test_remembering_a_folder_that_does_not_exist_is_refused(self):
        done = self.machine.run("stage.sh", "remember", "nowhere")
        self.assertEqual(done.returncode, 3)


if __name__ == "__main__":
    unittest.main()
