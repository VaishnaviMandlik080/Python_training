"""Log File Analyzer & Error Monitoring Tool — core package."""

from src.analyzer import LogAnalyzer
from src.parser import parse_log_line
from src.reader import read_log_stream
from src.reporter import (
    export_csv_breakdown,
    export_text_report,
    generate_console_summary,
)

__version__ = "1.0.0"

__all__ = [
    "LogAnalyzer",
    "parse_log_line",
    "read_log_stream",
    "generate_console_summary",
    "export_text_report",
    "export_csv_breakdown",
]
