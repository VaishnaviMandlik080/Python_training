"""
Log File Analyzer and Error Monitoring Tool - Reporting Module
----------------------------------------------------------------
Author      : Arpit Kanungo
Maintainer  : Arpit Kanungo
Module      : Operational Log Reporting
Description : Provides functionality for generating reports based on analyzed log data.
"""
import os
import csv
import json
import html
import logging
from datetime import datetime
from src.analyzer import LogAnalyzer

logger = logging.getLogger("LogAnalyzer.Reporter") # Logger for the reporter module

def _ensure_parent_dir(file_path):
    """Create the parent directory of file_path if it does not already exist."""
    parent = os.path.dirname(file_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

def generate_console_summary(analyzer: LogAnalyzer, top_n: int = 5):
    """
    Generates a console summary of the analyzed log data.
    """
    summary = analyzer.get_overall_summary()
    summary_lines = [
        "=" * 60,
        "               OPERATIONAL LOG MONITORING REPORT",
        "=" * 60,
        "--- OVERALL METRICS AND HEALTH STATUS ---",
        f" Total lines Read: {summary['Total lines']}",
        f" Successfully parsed: {summary['Total parsed']} ({summary['Parse success rate']})",
        f" Malformed/Skipped lines: {summary['Skipped lines']}",
        f" Total Warnings: {summary['Warning count']}",
        f" Total Errors: {summary['Error count']}",
        "-" * 60,
        "--- LOG LEVEL DISTRIBUTION ---",
    ]

    for level, count in sorted(analyzer.level_counts.items()):
        summary_lines.append(f" {level}: {count}")

    summary_lines.append("=" * 60)
    summary_lines.append("--- TOP RECURRING WARNINGS ---")
    top_warning = analyzer.get_top_warnings(top_n)
    if not top_warning:
        summary_lines.append(" No recurring warnings found.")
    else:
        for index, (warning, count) in enumerate(top_warning, start=1):
            summary_lines.append(f" {index}. {warning}: {count}")
    summary_lines.append("=" * 60)
    summary_lines.append("--- TOP RECURRING ERRORS ---")
    top_error = analyzer.get_top_errors(top_n)
    if not top_error:
        summary_lines.append(" No recurring errors found.")
    else:
        for index, (error, count) in enumerate(top_error, start=1):
            summary_lines.append(f" {index}. {error}: {count}")
    summary_lines.append("=" * 60)
    report_str = "\n".join(summary_lines)
    return report_str

def export_text_report(report_text, file_path):
    """
    Exports the given report text to a specified file.
    """
    try:
        _ensure_parent_dir(file_path)
        with open(file_path, "w") as file:
            file.write(report_text)
        logger.info(f"Report successfully exported to {file_path}")
    except Exception as e:
        logger.error(f"Failed to export report to {file_path}: {e}")
        raise e

def export_csv_breakdown(analyzer, file_path, top_n: int = 5):
    """
    Exports a CSV breakdown of log levels, top warnings, and top errors.
    """
    try:
        _ensure_parent_dir(file_path)
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # Write log level breakdown
            writer.writerow(["Log Level", "Count"])
            for level, count in sorted(analyzer.level_counts.items()):
                writer.writerow([level, count])
            writer.writerow([])

            # Write top warnings
            writer.writerow(["Top Warnings", "Count"])
            top_warning = analyzer.get_top_warnings(top_n)
            for warning, count in top_warning:
                writer.writerow([warning, count])
            writer.writerow([])

            # Write top errors
            writer.writerow(["Top Errors", "Count"])
            top_error = analyzer.get_top_errors(top_n)
            for error, count in top_error:
                writer.writerow([error, count])

        logger.info(f"CSV breakdown successfully exported to {file_path}")
    except Exception as e:
        logger.error(f"Failed to export CSV breakdown to {file_path}: {e}")
        raise e

def export_html_dashboard(analyzer, file_path, top_n: int = 5):
    """
    Exports an interactive HTML dashboard summarizing the analyzed log data.
    """
    try:
        _ensure_parent_dir(file_path)
        summary = analyzer.get_overall_summary()
        level_counts = dict(sorted(analyzer.level_counts.items()))
        top_warnings = analyzer.get_top_warnings(top_n)
        top_errors = analyzer.get_top_errors(top_n)
        generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Build the metric cards shown at the top of the dashboard
        cards = [
            ("Total Lines", summary["Total lines"]),
            ("Parsed", f"{summary['Total parsed']} ({summary['Parse success rate']}%)"),
            ("Skipped", summary["Skipped lines"]),
            ("Warnings", summary["Warning count"]),
            ("Errors", summary["Error count"]),
        ]
        cards_html = "".join(
            f'<div class="card"><div class="card-value">{html.escape(str(value))}</div>'
            f'<div class="card-label">{html.escape(label)}</div></div>'
            for label, value in cards
        )

        # Build table rows for top warnings and errors (escaped for safety)
        def _rows(items):
            if not items:
                return '<tr><td colspan="3">None found.</td></tr>'
            return "".join(
                f"<tr><td>{i}</td><td>{html.escape(msg)}</td><td>{count}</td></tr>"
                for i, (msg, count) in enumerate(items, start=1)
            )

        # Data passed to Chart.js, JSON-encoded so it is safe to embed in a script tag
        chart_data = json.dumps({
            "labels": list(level_counts.keys()),
            "values": list(level_counts.values()),
        })

        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Operational Log Monitoring Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }}
  header {{ padding: 24px 32px; background: #1e293b; border-bottom: 1px solid #334155; }}
  header h1 {{ margin: 0; font-size: 20px; }}
  header p {{ margin: 4px 0 0; color: #94a3b8; font-size: 13px; }}
  main {{ padding: 24px 32px; max-width: 1100px; margin: 0 auto; }}
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 16px; }}
  .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 18px; }}
  .card-value {{ font-size: 26px; font-weight: 700; }}
  .card-label {{ color: #94a3b8; font-size: 13px; margin-top: 4px; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 24px; }}
  .panel {{ background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 18px; }}
  .panel h2 {{ margin: 0 0 12px; font-size: 15px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #334155; }}
  th {{ color: #94a3b8; font-weight: 600; }}
  td:last-child, th:last-child {{ text-align: right; }}
  @media (max-width: 760px) {{ .grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<header>
  <h1>Operational Log Monitoring Dashboard</h1>
  <p>Generated {html.escape(generated_at)}</p>
</header>
<main>
  <div class="cards">{cards_html}</div>
  <div class="grid">
    <div class="panel">
      <h2>Log Level Distribution</h2>
      <canvas id="levelChart"></canvas>
    </div>
    <div class="panel">
      <h2>Top Recurring Errors</h2>
      <table><thead><tr><th>#</th><th>Error</th><th>Count</th></tr></thead>
      <tbody>{_rows(top_errors)}</tbody></table>
    </div>
  </div>
  <div class="grid">
    <div class="panel">
      <h2>Top Recurring Warnings</h2>
      <table><thead><tr><th>#</th><th>Warning</th><th>Count</th></tr></thead>
      <tbody>{_rows(top_warnings)}</tbody></table>
    </div>
  </div>
</main>
<script>
  const data = {chart_data};
  new Chart(document.getElementById("levelChart"), {{
    type: "bar",
    data: {{
      labels: data.labels,
      datasets: [{{ label: "Count", data: data.values, backgroundColor: "#38bdf8" }}]
    }},
    options: {{
      plugins: {{ legend: {{ display: false }} }},
      scales: {{
        x: {{ ticks: {{ color: "#94a3b8" }}, grid: {{ color: "#334155" }} }},
        y: {{ ticks: {{ color: "#94a3b8" }}, grid: {{ color: "#334155" }}, beginAtZero: true }}
      }}
    }}
  }});
</script>
</body>
</html>"""

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(page)
        logger.info(f"HTML dashboard successfully exported to {file_path}")
    except Exception as e:
        logger.error(f"Failed to export HTML dashboard to {file_path}: {e}")
        raise e