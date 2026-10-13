"""
Log File Analyzer and Error Monitoring Tool - Log Analyzer Module
----------------------------------------------------------------
Author      : Vaishnavi Mandlik
Maintainer  : Vaishnavi Mandlik
Module      : Counter-based Statistical Analysis and Event Correlation
Description : Provides functionality for analyzing parsed log events, maintaining statistical counters, and generating summaries.
"""

import logging
from collections import Counter
from typing import Callable, Dict, Iterable, List, Optional, Tuple

logger = logging.getLogger("LogAnalyzer.Analyzer") # Logger for the analyzer module

ParsedEvent = Dict[str, str]
ParserFn = Callable[[str], Optional[ParsedEvent]]

class LogAnalyzer:
    def __init__(self) -> None:
        self.level_counts: Counter = Counter()
        self.module_counts: Counter = Counter()
        self.error_messages: Counter = Counter()
        self.warning_messages: Counter = Counter()
        self.total_parsed: int = 0
        self.total_lines: int = 0
    def ingest_events(self, lines: Iterable[str], parser_fn: ParserFn) -> None:
        """
        Processes lines of log data using the provided parser function.
        """
        for line in lines:
            self.total_lines += 1
            event = parser_fn(line)
            if not event:
                continue
            self.total_parsed += 1
            level = event["level"]
            module = event["module"]
            message = event["message"]

            self.level_counts[level] += 1
            self.module_counts[module] += 1

            if level == "ERROR":
                self.error_messages[f"{module}: {message}"] += 1
            elif level == "WARNING":
                self.warning_messages[f"{module}: {message}"] += 1
    
    def get_level_summary(self) -> Dict[str, int]:
        return dict(self.level_counts)

    def get_warning_count(self) -> int:
        """
        Returns the total count of warning messages.
        """
        return self.level_counts.get("WARNING", 0)

    def get_error_count(self) -> int:
        """
        Returns the total count of error messages.
        """
        return self.level_counts.get("ERROR", 0)

    def get_top_errors(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Identifies the top N most frequent error messages.
        """
        limit = n if n > 0 else 5
        return self.error_messages.most_common(limit) # Return the top N error messages

    def get_top_warnings(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Identifies the top N most frequent warning messages.
        """
        limit = n if n > 0 else 5
        return self.warning_messages.most_common(limit) # Return the top N warning messages

    def get_overall_summary(self):
        """
        Returns a summary of the overall log analysis, including total lines parsed and counts per level.
        """
        skipped_lines = self.total_lines - self.total_parsed
        error_count = self.get_error_count()
        warning_count = self.get_warning_count()

        error_rate = round((error_count / self.total_parsed) * 100, 2) if self.total_parsed > 0 else 0.0
        warning_rate = round((warning_count / self.total_parsed) * 100, 2) if self.total_parsed > 0 else 0.0
        parse_success_rate = round((self.total_parsed / self.total_lines) * 100, 2) if self.total_lines > 0 else 0.0

        return {
            "Total lines": self.total_lines,
            "Total parsed": self.total_parsed,
            "Skipped lines": skipped_lines,
            "Error count": error_count,
            "Warning count": warning_count,
            "Error rate": error_rate,
            "Warning rate": warning_rate,
            "Parse success rate": parse_success_rate,
            "Level counts": dict(self.level_counts)
        }
    