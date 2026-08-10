import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNNER = REPO_ROOT / "tools" / "okf_source_manager.py"
sys.path.insert(0, str(REPO_ROOT / "tools"))
import okf_source_manager as manager


class SourceManagerWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "Project"
        (self.project / "evidence").mkdir(parents=True)
        (self.project / "evidence" / "alpha.md").write_text(
            "# Alpha\n\nA Markdown source.\n", encoding="utf-8"
        )
        (self.project / "evidence" / "beta.html").write_text(
            "<html><body><h1>Beta</h1><p>An <strong>HTML</strong> source.</p></body></html>",
            encoding="utf-8",
        )
        source_dir = self.project / "okf" / "sources" / "mixed"
        source_dir.mkdir(parents=True)
        manifest = {
            "schema_version": 1,
            "id": "mixed",
            "storage": {"originals": "reference-only", "normalized": "reference-only"},
            "items": [
                {
                    "id": "alpha",
                    "fetch": {"adapter": "local-file", "path": "evidence/alpha.md"},
                    "output": "notes/alpha.md",
                    "transform": [{"name": "markdown-copy", "version": 1}],
                },
                {
                    "id": "beta",
                    "fetch": {"adapter": "local-file", "path": "evidence/beta.html"},
                    "output": "notes/beta.md",
                    "transform": [{"name": "html-to-markdown", "version": 1}],
                },
            ],
        }
        (source_dir / "source.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    def run_manager(self, *args, expect=0):
        result = subprocess.run(
            [sys.executable, str(RUNNER), *map(str, args)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expect, result.returncode, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        output = result.stdout if result.stdout.strip() else result.stderr
        return json.loads(output)

    def test_refresh_hydrate_and_validation(self):
        refreshed = self.run_manager("refresh", "--project", self.project, "--source", "mixed")
        self.assertTrue(refreshed["ok"])
        self.assertEqual(2, refreshed["document_count"])
        self.assertEqual(["alpha", "beta"], refreshed["changes"]["added"])

        portable = self.run_manager(
            "validate", "--project", self.project, "--source", "mixed", "--mode", "portable"
        )
        hydrated = self.run_manager(
            "validate", "--project", self.project, "--source", "mixed", "--mode", "hydrated"
        )
        self.assertTrue(portable["ok"])
        self.assertTrue(hydrated["ok"])

        beta = self.project / "okf" / "raw" / "mixed" / "cache" / "documents" / "notes" / "beta.md"
        self.assertIn("# Beta", beta.read_text(encoding="utf-8"))
        self.assertIn("**HTML**", beta.read_text(encoding="utf-8"))

        beta.unlink()
        failed = self.run_manager(
            "validate", "--project", self.project, "--source", "mixed", "--mode", "hydrated", expect=1
        )
        self.assertFalse(failed["ok"])
        self.assertTrue(any("materialized" in issue for issue in failed["issues"]))

        hydrated_again = self.run_manager("hydrate", "--project", self.project, "--source", "mixed")
        self.assertTrue(hydrated_again["ok"])
        self.assertTrue(beta.exists())

    def test_archived_unavailable_retains_verified_evidence_and_skips_refresh(self):
        self.run_manager("refresh", "--project", self.project, "--source", "mixed")
        archived = self.run_manager(
            "mark-unavailable",
            "--project",
            self.project,
            "--source",
            "mixed",
            "--document",
            "alpha",
            "--reason",
            "Source owner withdrew the document",
        )
        self.assertTrue(archived["ok"])
        self.assertTrue(Path(archived["retained_original"]).exists())
        self.assertTrue(Path(archived["retained_normalized"]).exists())
        self.assertTrue(Path(archived["provenance"]).exists())

        (self.project / "evidence" / "alpha.md").unlink()
        refreshed = self.run_manager("refresh", "--project", self.project, "--source", "mixed")
        self.assertTrue(refreshed["ok"])
        status = self.run_manager("status", "--project", self.project, "--source", "mixed")
        self.assertEqual(1, status["lifecycle_counts"]["archived-unavailable"])

        portable = self.run_manager(
            "validate", "--project", self.project, "--source", "mixed", "--mode", "portable"
        )
        self.assertTrue(portable["ok"])

    def test_check_does_not_advance_lock(self):
        self.run_manager("refresh", "--project", self.project, "--source", "mixed")
        lock_path = self.project / "okf" / "sources" / "mixed" / "source.lock.json"
        before = lock_path.read_bytes()
        (self.project / "evidence" / "alpha.md").write_text("# Alpha\n\nChanged.\n", encoding="utf-8")
        checked = self.run_manager("check", "--project", self.project, "--source", "mixed")
        self.assertEqual(["alpha"], checked["changes"]["changed"])
        self.assertEqual(before, lock_path.read_bytes())

    def test_random_selection_is_repeatable_and_ordered(self):
        candidates = [{"source_path": f"dictionary/{index:02}.md"} for index in range(30)]
        selection = {"strategy": "random", "count": 10, "seed": 20260810}
        first = manager.deterministic_selection(candidates, selection)
        second = manager.deterministic_selection(list(reversed(candidates)), selection)
        self.assertEqual(first, second)
        self.assertEqual(10, len(first))
        self.assertEqual(sorted(entry["source_path"] for entry in first), [entry["source_path"] for entry in first])


if __name__ == "__main__":
    unittest.main()
