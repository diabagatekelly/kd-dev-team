import os
import tempfile
import unittest

import settings_inventory as si


class ReadLookups(unittest.TestCase):
    def test_a_dotted_lookup_is_read(self):
        self.assertEqual(si.read_lookups("const p = process.env.PORT;")[0], {"PORT"})

    def test_a_bracketed_lookup_with_either_quote_is_read(self):
        text = 'a = process.env["BASE_ADDRESS"]\nb = process.env[\'MODE\']'
        self.assertEqual(si.read_lookups(text)[0], {"BASE_ADDRESS", "MODE"})

    def test_the_three_python_forms_are_read(self):
        text = 'a = os.environ["A_ONE"]\nb = os.environ.get("B_TWO", "x")\nc = os.getenv("C_THREE")'
        self.assertEqual(si.read_lookups(text)[0], {"A_ONE", "B_TWO", "C_THREE"})

    def test_a_lookup_whose_name_is_built_at_run_time_is_reported_with_its_line(self):
        names, computed = si.read_lookups("x\nconst v = process.env[`PREFIX_${id}`];")
        self.assertEqual(names, set())
        self.assertEqual(computed, [(2, "const v = process.env[`PREFIX_${id}`];")])

    def test_a_computed_lookup_beside_a_literal_one_on_the_same_line_is_still_reported(self):
        names, computed = si.read_lookups("const a = process.env.PORT || process.env[key];")
        self.assertEqual(names, {"PORT"})
        self.assertEqual(len(computed), 1)

    def test_a_line_with_no_lookup_gives_nothing(self):
        self.assertEqual(si.read_lookups("const environment = 'x';"), (set(), []))


class Scan(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.source = os.path.join(self.root, "src")
        self.plan = os.path.join(self.root, "plan")
        os.makedirs(os.path.join(self.source, "node_modules", "lib"))
        os.makedirs(self.plan)
        self.write(self.source, "main.ts", 'const p = process.env["PORT"];\nconst k = process.env.API_KEYNAME;')
        self.write(self.source, "node_modules/lib/x.js", "process.env.IGNORED_ONE")
        self.write(self.source, "notes.md", "process.env.NOT_SOURCE")
        self.write(self.plan, "design.md", "The app reads `API_KEYNAME` at start. Support is planned.")

    def write(self, base, name, text):
        with open(os.path.join(base, name), "w", encoding="utf-8") as handle:
            handle.write(text)

    def test_source_files_are_read_and_dependencies_and_other_files_are_not(self):
        where, _ = si.scan_source(self.source)
        self.assertEqual(where, {"PORT": ["main.ts"], "API_KEYNAME": ["main.ts"]})

    def test_a_name_counts_as_in_the_plan_only_as_a_whole_word(self):
        self.assertEqual(si.named_in_plan(self.plan, {"PORT", "API_KEYNAME"}), {"API_KEYNAME"})

    def test_the_report_separates_named_from_never_named(self):
        where, computed = si.scan_source(self.source)
        result = si.report(where, computed, si.named_in_plan(self.plan, where))
        self.assertEqual(result["named_in_the_plan"], ["API_KEYNAME"])
        self.assertEqual(result["never_named_in_the_plan"], {"PORT": ["main.ts"]})


if __name__ == "__main__":
    unittest.main()
