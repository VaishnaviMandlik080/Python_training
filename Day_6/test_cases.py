"""
Log File Analyzer and Error Monitoring Tool - Test Cases Module
----------------------------------------------------------------
Author      : Arpit Kanungo
Maintainer  : Arpit Kanungo
Module      : Unit Tests for File Reader, Parser, Analyzer, and Reporter Modules
Description : Contains unit tests for the core modules of the log file analyzer tool, ensuring correct functionality and integration.
"""
import unittest
import tempfile
import os
from src.reader import read_log_stream
from src.parser import parse_log_line
from src.analyzer import LogAnalyzer
from src.reporter import generate_console_summary, export_csv_breakdown, export_text_report, export_html_dashboard

class TestReader(unittest.TestCase):
    # Importance: the reader must fail loudly on a missing file so the tool
    # reports a clear error instead of silently producing an empty report.
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            list(read_log_stream("invalid_file.log"))

    # Importance: an empty or non-string path is a programming error and must
    # raise ValueError instead of being silently treated as a real file.
    def test_invalid_path(self):
        with self.assertRaises(ValueError):
            list(read_log_stream(""))

    # Importance: a directory is not a readable log file, so the reader must
    # reject it clearly rather than crash later during iteration.
    def test_directory_path_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(ValueError):
                list(read_log_stream(temp_dir))

    # Importance: an empty file must stream zero lines without error so the
    # tool degrades gracefully instead of failing on valid-but-empty input.
    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file_name = temp_file.name
        try:
            self.assertEqual(list(read_log_stream(temp_file_name)), [])
        finally:
            os.remove(temp_file_name)

    # Importance: verifies the generator yields every line exactly once,
    # proving the memory-safe streaming reads the whole file correctly.
    def test_stream_line(self):
        
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write("line1\nline2\nline3\n")
            temp_file_name = temp_file.name
        try:
            lines = list(read_log_stream(temp_file_name))
            self.assertEqual(len(lines), 3)
        finally:
            os.remove(temp_file_name)

class TestParser(unittest.TestCase):

    # Importance: confirms the regex correctly extracts the structured fields
    # (level, module) that every downstream stage depends on.
    def test_parse_log_line(self):
        log_line = "2026-03-31 10:15:30 [ERROR] [auth_service] Invalid credentials for user "
        parsed = parse_log_line(log_line)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed['level'], "ERROR")
        self.assertEqual(parsed['module'], "auth_service")

    # Importance: bad/empty lines must return None (not crash), so one corrupt
    # line never stops analysis of the rest of the file.
    def test_malformed_line(self):
        self.assertIsNone(parse_log_line("malformed line"))
        self.assertIsNone(parse_log_line(""))

    # Importance: non-string input must be handled defensively and return None
    # rather than raising, keeping the parser robust against bad callers.
    def test_non_string_input(self):
        self.assertIsNone(parse_log_line(None))
        self.assertIsNone(parse_log_line(123))

    # Importance: timestamp and message are part of the structured event and
    # must be captured accurately, not just level/module.
    def test_parses_all_fields(self):
        parsed = parse_log_line("2026-03-31 10:15:30 [WARNING] [cache] Low memory")
        self.assertEqual(parsed["timestamp"], "2026-03-31 10:15:30")
        self.assertEqual(parsed["level"], "WARNING")
        self.assertEqual(parsed["message"], "Low memory")

class TestAnalyzer(unittest.TestCase):

    # Importance: end-to-end check of the counting logic — totals, skipped
    # malformed lines, per-level counts, and top recurring error ranking.
    def test_analyze_empty_logs(self):    
        lines = ["2026-03-31 10:15:30 [ERROR] [db] Timeout ",
                 "2026-03-31 10:16:30 [ERROR] [db] Timeout",
                 "2026-03-31 10:17:30 [INFO] [web] Success",
                 "malformed line"
                ]
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)
        self.assertEqual(analyzer.total_lines, 4)      # every line is counted
        self.assertEqual(analyzer.total_parsed, 3)     # malformed line is skipped
        self.assertEqual(analyzer.level_counts["ERROR"], 2)
        self.assertEqual(analyzer.get_top_errors(1)[0], ("db: Timeout", 2))  # most frequent error

    # Importance: warnings are ranked and reported separately from errors, so
    # their aggregation and module counting must be verified independently.
    def test_warnings_and_modules(self):
        lines = [
            "2026-03-31 10:15:30 [WARNING] [cache] Low memory",
            "2026-03-31 10:16:30 [WARNING] [cache] Low memory",
            "2026-03-31 10:17:30 [INFO] [web] Success",
        ]
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)
        self.assertEqual(analyzer.get_top_warnings(1)[0], ("cache: Low memory", 2))
        self.assertEqual(analyzer.module_counts["cache"], 2)

    # Importance: with no parsed lines the rate calculations must guard against
    # division by zero and return 0.0 instead of raising.
    def test_summary_rates_no_division_error(self):
        analyzer = LogAnalyzer()
        summary = analyzer.get_overall_summary()
        self.assertEqual(summary["Error rate"], 0.0)
        self.assertEqual(summary["Warning rate"], 0.0)
        self.assertEqual(summary["Parse success rate"], 0.0)

class TestReporter(unittest.TestCase):
    
    # Importance: ensures the summary string is built correctly AND the CSV
    # file is actually written to disk, validating the final output stage.
    def test_report_generation_and_export(self):
        analyzer = LogAnalyzer()
        report_str = generate_console_summary(analyzer)
        self.assertIn("OPERATIONAL LOG MONITORING REPORT", report_str)
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = os.path.join(temp_dir, "test.csv")
            export_csv_breakdown(analyzer, csv_path)
            self.assertTrue(os.path.exists(csv_path))

    # Importance: with no data the summary must show the empty-state messages
    # instead of blank or broken sections.
    def test_empty_summary_messages(self):
        report_str = generate_console_summary(LogAnalyzer())
        self.assertIn("No recurring warnings found.", report_str)
        self.assertIn("No recurring errors found.", report_str)

    # Importance: the text report must be persisted to disk with its content
    # intact, validating the plain-text export path.
    def test_text_report_export(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            txt_path = os.path.join(temp_dir, "report.txt")
            export_text_report("hello report", txt_path)
            with open(txt_path) as f:
                self.assertEqual(f.read(), "hello report")

    # Importance: the HTML dashboard must be written and contain the analyzed
    # data, validating the new interactive export feature.
    def test_html_dashboard_export(self):
        lines = ["2026-03-31 10:15:30 [ERROR] [db] Timeout"]
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)
        with tempfile.TemporaryDirectory() as temp_dir:
            html_path = os.path.join(temp_dir, "dashboard.html")
            export_html_dashboard(analyzer, html_path)
            self.assertTrue(os.path.exists(html_path))
            with open(html_path) as f:
                content = f.read()
            self.assertIn("<!DOCTYPE html>", content)
            self.assertIn("db: Timeout", content)

if __name__ == "__main__":
    unittest.main()
