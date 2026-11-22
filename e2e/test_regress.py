import pathlib
import tempfile
import unittest

import make_plugin
import regress


class Regress(unittest.TestCase):
    def test_every_adopted_text_and_the_current_table_are_laid_over_a_plugin(self):
        plugin = pathlib.Path(tempfile.mkdtemp()) / "plugin"
        (plugin / "hooks").mkdir(parents=True)
        (plugin / "skills" / "problem").mkdir(parents=True)
        (plugin / "skills" / "problem" / "SKILL.md").write_text("an older text")
        regress.overlay(plugin)
        self.assertEqual(sorted(path.name for path in (plugin / "skills").iterdir()), sorted(make_plugin.SKILLS))
        self.assertNotEqual((plugin / "skills" / "problem" / "SKILL.md").read_text(), "an older text")
        self.assertIn("REFUSED", (plugin / "hooks" / "routing-table.md").read_text())

    def test_every_stage_with_an_adopted_text_is_rebuilt(self):
        self.assertEqual([stage for stage, _, _ in regress.STAGES],
                         ["00-startup", "01-problem", "02-scope-map", "03-requirements"])


if __name__ == "__main__":
    unittest.main()
