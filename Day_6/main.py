"""
Log File Analyzer and Error Monitoring Tool - Main Module
----------------------------------------------------------------
Author      : Arpit Kanungo
Maintainer  : Arpit Kanungo
Module      : Main Operational Log Monitoring
Description : This module handles the generation of reports based on the analyzed log data, 
including console summaries, text reports, and CSV breakdowns.
"""


import argparse
import sys
import logging
# Pipeline stages: read raw lines -> parse each line -> analyze -> report
from src.reader import read_log_stream
from src.parser import parse_log_line
from src.analyzer import LogAnalyzer
from src.reporter import generate_console_summary, export_text_report, export_csv_breakdown, export_html_dashboard

def configure_app_logging(log_file = "application.log"):
    # Send log output to both a file (appended) and the console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode = "a"),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    # Define the command-line options the tool accepts
    parser = argparse.ArgumentParser(description="Operational Log Monitoring Tool") # argparse is a standard library tool for writing user-friendly command-line interfaces
    parser.add_argument("--input", "-i", type = str, default = "data/sample.log")  # path to the log file to analyze
    parser.add_argument("--output-text", type = str, default = "reports/summary_report.txt")  # text summary output path
    parser.add_argument("--output-csv", type = str, default = "reports/error_distribution.csv")  # CSV breakdown output path
    parser.add_argument("--output-html", type = str, default = "reports/dashboard.html")  # HTML dashboard output path
    parser.add_argument("--top", type = int, default = 5, help = "Number of top recurring errors/warnings to report") # top N errors/warnings to display

    # Parse the arguments and set up logging before doing any work
    args = parser.parse_args()
    configure_app_logging()
    logger = logging.getLogger("LogAnalyzer.Main")
    logger.info(f"Starting Operational Log Monitoring Tool for {args.input}")

    try:
        # 1. Read the log file into a stream of raw lines
        lines = read_log_stream(args.input)

        # 2. Feed each line through the parser so the analyzer can aggregate the events
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)

        # 3. Build the human-readable summary and print it to the console
        report_str = generate_console_summary(analyzer, args.top)
        print(report_str)

        # 4. Persist the results as a text report, a CSV breakdown, and an HTML dashboard
        export_text_report(report_str, args.output_text)
        export_csv_breakdown(analyzer, args.output_csv, args.top)
        export_html_dashboard(analyzer, args.output_html, args.top)
        logger.info("Reports generated successfully.")
        print(f"\nReports written:\n  - {args.output_text}\n  - {args.output_csv}\n  - {args.output_html}")

    except (FileNotFoundError, PermissionError, IOError) as e:
        # Handle expected file-related problems with a clean exit
        logger.error(f"File error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        # Catch-all for any unexpected failure
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()