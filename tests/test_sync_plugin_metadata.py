import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "sync_plugin_metadata.py"


class SyncPluginMetadataTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp(prefix="plugin-marketplace-test-"))
        shutil.copytree(REPO_ROOT / "plugins", self.tmpdir / "plugins")

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def run_sync(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.tmpdir), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def read_json(self, relative_path):
        return json.loads((self.tmpdir / relative_path).read_text(encoding="utf-8"))

    def test_generates_platform_marketplaces_and_manifest_copies(self):
        result = self.run_sync()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.read_json(".claude-plugin/marketplace.json")["plugins"][0]["name"],
            "code-reviewer",
        )
        self.assertEqual(
            self.read_json(".github/plugin/marketplace.json")["plugins"][0]["name"],
            "code-reviewer",
        )
        self.assertEqual(
            self.read_json(".agents/plugins/marketplace.json")["plugins"][0]["name"],
            "code-reviewer",
        )
        self.assertEqual(
            self.read_json("plugins/code-reviewer/.claude-plugin/plugin.json")["name"],
            "code-reviewer",
        )
        self.assertEqual(
            self.read_json("plugins/code-reviewer/.codex-plugin/plugin.json")["name"],
            "code-reviewer",
        )
        self.assertEqual(
            self.read_json("plugins/code-reviewer/.claude-plugin/plugin.json")["version"],
            "2.0.0",
        )

    def test_code_reviewer_v2_plugin_assets_are_present(self):
        expected_paths = [
            "plugins/code-reviewer/CHANGELOG.md",
            "plugins/code-reviewer/LICENSE",
            "plugins/code-reviewer/commands/review.md",
            "plugins/code-reviewer/hooks/pre-merge-check.sh",
            "plugins/code-reviewer/mcp/server.json",
            "plugins/code-reviewer/examples/basic-usage.md",
            "plugins/code-reviewer/examples/review-example.md",
        ]

        for relative_path in expected_paths:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((self.tmpdir / relative_path).is_file())

    def test_check_succeeds_when_generated_files_match(self):
        self.assertEqual(self.run_sync().returncode, 0)

        result = self.run_sync("--check")

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_check_fails_when_generated_file_is_stale(self):
        self.assertEqual(self.run_sync().returncode, 0)
        marketplace_path = self.tmpdir / ".agents" / "plugins" / "marketplace.json"
        marketplace = self.read_json(".agents/plugins/marketplace.json")
        marketplace["plugins"][0]["category"] = "Stale"
        marketplace_path.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")

        result = self.run_sync("--check")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale", result.stderr)


if __name__ == "__main__":
    unittest.main()
