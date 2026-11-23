import unittest

from standin_machine import Machine

SHEET = ("Client,Walk,Price,Since\r\n"
         'Okafor,"30 minutes, one dog",14.50,2024-03-01\r\n'
         'Lindqvist,"60 minutes, one dog",22.00,2023-11-15\r\n'
         'Okafor,"30 minutes, two dogs",21.75,2024-03-01\r\n')
VALUES = ["Okafor", "Lindqvist", "14.50", "22.00", "21.75", "2024-03-01", "30 minutes"]


class Source(unittest.TestCase):
    """A file of the user's stays where it is: its shape can be printed, its cells never are."""

    def setUp(self):
        self.machine = Machine(self)
        self.sheet = self.machine.root / "prices.csv"
        self.sheet.write_bytes(SHEET.encode("utf-8"))

    def run_script(self, *args):
        return self.machine.run("source.sh", *[str(arg) for arg in args])

    def write(self, relative, text):
        path = self.machine.project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    # describe
    def test_the_shape_is_printed_and_no_cell(self):
        done = self.run_script("describe", self.sheet)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn("- rows: 3, columns: 4", done.stdout)
        self.assertIn('- column 1 "Client": text, 3 filled, 2 different', done.stdout)
        self.assertIn('- column 3 "Price": number, 3 filled, 3 different', done.stdout)
        self.assertIn('- column 4 "Since": date, 3 filled, 2 different', done.stdout)
        for value in VALUES:
            self.assertNotIn(value, done.stdout)

    def test_a_comma_inside_quotes_does_not_make_a_column(self):
        self.assertIn('- column 2 "Walk": text, 3 filled, 3 different', self.run_script("describe", self.sheet).stdout)

    def test_tabs_and_semicolons_are_read_too(self):
        for name, separator in (("prices.tsv", "\t"), ("prices.txt", ";")):
            path = self.machine.root / name
            path.write_text(f"Client{separator}Price\nOkafor{separator}14.50\n", encoding="utf-8")
            done = self.run_script("describe", path)
            self.assertIn("- rows: 1, columns: 2", done.stdout, name)
            self.assertIn('- column 2 "Price": number', done.stdout, name)

    def test_an_empty_or_mixed_column_is_said_to_be_so(self):
        path = self.machine.root / "mixed.csv"
        path.write_text("A,B\n1,\nx,\n", encoding="utf-8")
        out = self.run_script("describe", path).stdout
        self.assertIn('- column 1 "A": mixed, 2 filled', out)
        self.assertIn('- column 2 "B": empty, 0 filled', out)

    def test_a_cell_that_spans_lines_is_refused_not_guessed(self):
        path = self.machine.root / "notes.csv"
        path.write_text('Client,Note\nOkafor,"rings twice\nthen waits"\n', encoding="utf-8")
        done = self.run_script("describe", path)
        self.assertEqual(done.returncode, 3)
        self.assertIn("REFUSED", done.stdout)
        self.assertNotIn("Okafor", done.stdout)

    def test_a_workbook_or_a_missing_file_is_refused_with_what_to_do(self):
        book = self.machine.root / "prices.xlsx"
        book.write_bytes(b"PK\x03\x04")
        done = self.run_script("describe", book)
        self.assertEqual(done.returncode, 3)
        self.assertIn("save the sheet as CSV", done.stdout)
        self.assertEqual(self.run_script("describe", self.machine.root / "nothing.csv").returncode, 3)

    # scan
    def test_a_value_written_down_is_found_by_where_it_is_never_by_what_it_is(self):
        self.write("planning/002_requirements.md", "# Requirements\n\n- For example Mrs Okafor pays 14.50 a walk.\n")
        done = self.run_script("scan", self.sheet, self.machine.project)
        self.assertEqual(done.returncode, 1)
        self.assertIn('- planning/002_requirements.md line 3: a value of column "Client"', done.stdout)
        self.assertIn('- planning/002_requirements.md line 3: a value of column "Price"', done.stdout)
        for value in VALUES:
            self.assertNotIn(value, done.stdout)

    def test_nothing_written_down_is_said_plainly(self):
        self.write("planning/002_requirements.md", "- For example a client pays 9.99 a walk (invented).\n")
        done = self.run_script("scan", self.sheet, self.machine.project)
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertIn("- no value of prices.csv is written in", done.stdout)

    def test_case_and_a_folder_below_do_not_hide_a_value(self):
        self.write("src/deep/prices_test.py", "CLIENT = 'lindqvist'\n")
        done = self.run_script("scan", self.sheet, self.machine.project)
        self.assertEqual(done.returncode, 1)
        self.assertIn("- src/deep/prices_test.py line 1", done.stdout)

    def test_a_column_name_a_short_value_and_part_of_a_longer_word_are_no_find(self):
        path = self.machine.root / "short.csv"
        path.write_text("Client,Dogs,Tier\nOkafor,2,Gold\n", encoding="utf-8")
        self.write("notes.md", "The Client column. 2 dogs. Golden hour. Okaforth is another word.\n")
        done = self.run_script("scan", path, self.machine.project)
        self.assertEqual(done.returncode, 0, done.stdout)

    def test_what_git_keeps_for_itself_is_not_read(self):
        self.write(".git/COMMIT_EDITMSG", "Okafor\n")
        self.assertEqual(self.run_script("scan", self.sheet, self.machine.project).returncode, 0)

    def test_a_scan_that_cannot_read_the_file_is_a_failure_not_a_pass(self):
        done = self.run_script("scan", self.machine.root / "nothing.csv", self.machine.project)
        self.assertEqual(done.returncode, 3)
        self.assertIn("REFUSED", done.stdout)

    def test_a_scan_that_lacks_a_tool_is_a_failure_not_a_pass(self):
        # Found while writing it: with no `find` on the path the scan printed "no value is written".
        import os, subprocess
        import standin_machine
        self.write("notes.md", "Okafor\n")
        bare = self.machine.root / "bare"
        bare.mkdir()
        for tool in ("awk", "sed", "grep", "basename", "sort", "wc", "tr", "xargs"):
            found = standin_machine.shutil.which(tool)
            if found and os.name != "nt":
                (bare / tool).symlink_to(found)
        if os.name == "nt":
            self.skipTest("the tools of this system cannot be taken apart one by one")
        done = subprocess.run([standin_machine.SH, str(standin_machine.HERE / "source.sh"), "scan", str(self.sheet),
                               str(self.machine.project)], env={"PATH": str(bare)}, capture_output=True, text=True)
        self.assertEqual(done.returncode, 3, done.stdout + done.stderr)
        self.assertIn("REFUSED: this machine has no find", done.stdout)

    def test_with_no_command_it_says_how_it_is_used(self):
        done = self.run_script()
        self.assertEqual(done.returncode, 2)
        self.assertIn("source.sh describe FILE", done.stdout)


if __name__ == "__main__":
    unittest.main()
