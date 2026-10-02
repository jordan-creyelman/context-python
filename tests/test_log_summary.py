"""Essential behavior and CLI tests using isolated files only."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from projects.log_summary import count_errors, main

SCRIPT = Path(__file__).resolve().parents[1] / "projects" / "log_summary.py"


class LogSummaryTests(unittest.TestCase):
    """Verify exact matching, file failures, and observable CLI behavior."""

    def setUp(self) -> None:
        """Create an isolated directory containing spaces."""
        directory = tempfile.TemporaryDirectory(prefix="python practice ")
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name)
        self.log_file = self.directory / "app log.txt"

    def run_cli(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        """Run the real CLI without a shell, capturing both output streams."""
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            capture_output=True, text=True, encoding="utf-8",
            timeout=10, check=False,
        )

    def test_exact_prefix_and_unicode(self) -> None:
        """Only the exact case-sensitive prefix counts, even on the last line."""
        self.log_file.write_text(
            "ERROR café\nINFO ERROR ignored\nerror ignored\nERROR\n ERROR ignored\nERROR timeout",
            encoding="utf-8",
        )
        self.assertEqual(count_errors(self.log_file), 2)
        result = self.run_cli(str(self.log_file))
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "2\n")
        self.assertEqual(result.stderr, "")

    def test_empty_and_no_matches_are_successful(self) -> None:
        """Zero matches must not become a failure."""
        for content in ("", "INFO ready\nWARNING slow\n"):
            with self.subTest(content=content):
                self.log_file.write_text(content, encoding="utf-8")
                self.assertEqual(count_errors(self.log_file), 0)
                result = self.run_cli(str(self.log_file))
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "0\n")
                self.assertEqual(result.stderr, "")

    def test_missing_file_and_directory(self) -> None:
        """Reject nonexistent files and directories with no misleading total."""
        for path in (self.log_file, self.directory):
            with self.subTest(path=path):
                result = self.run_cli(str(path))
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn("regular file", result.stderr)

    def test_invalid_utf8(self) -> None:
        """Report decoding failure rather than silently discarding bytes."""
        self.log_file.write_bytes(b"ERROR valid\n\xff\n")
        with self.assertRaises(UnicodeError):
            count_errors(self.log_file)
        result = self.run_cli(str(self.log_file))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Cannot read", result.stderr)

    def test_read_failure_propagates_from_logic(self) -> None:
        """The business function must not return zero when opening fails."""
        with self.assertRaises(OSError):
            count_errors(self.log_file)

    def test_read_denied_after_validation(self) -> None:
        """Handle a read failure even when the initial file check succeeded."""
        self.log_file.write_text("ERROR failed\n", encoding="utf-8")
        output = StringIO()
        with patch("projects.log_summary.count_errors", side_effect=PermissionError("denied")):
            with self.assertLogs("projects.log_summary", level="ERROR") as logs:
                with redirect_stdout(output):
                    status = main([str(self.log_file)])
        self.assertEqual(status, 1)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("denied", logs.output[0])

    def test_verbose_uses_stderr(self) -> None:
        """Optional logging must leave machine-readable stdout unchanged."""
        self.log_file.write_text("ERROR failed\n", encoding="utf-8")
        result = self.run_cli(str(self.log_file), "--verbose")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1\n")
        self.assertIn("INFO: Read", result.stderr)

    def test_missing_argument(self) -> None:
        """Argparse reports invalid usage with exit code 2."""
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("usage:", result.stderr)

    def test_help(self) -> None:
        """Users can discover the interface without supplying a file."""
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("--verbose", result.stdout)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
