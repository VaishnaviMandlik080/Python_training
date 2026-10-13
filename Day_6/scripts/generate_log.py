"""
Generates a large sample log file in the exact format src/parser.py expects:
    YYYY-MM-DD HH:MM:SS [LEVEL] [module] message

Run:  python3 generate_log.py
Then: python3 main.py --input data/large_sample.log --top 5
"""

import os
import random
from datetime import datetime, timedelta

OUTPUT_PATH = "data/large_sample.log"
TOTAL_LINES = 100_000
START_TIME = datetime(2026, 3, 29, 0, 0, 0)

# Exact counts for the top recurring ERROR signatures (module, message, count)
ERROR_SIGNATURES = [
    ("db_pool", "Connection timeout reached", 4120),
    ("payment", "Gateway rejected transaction 504", 3040),
    ("auth", "Token signature expired", 1510),
    ("web", "Internal server error 500", 1200),
    ("queue", "Message broker unreachable", 900),
]

# Exact counts for the top recurring WARNING signatures
WARNING_SIGNATURES = [
    ("cache", "Redis key expired for session", 2250),
    ("disk", "Disk usage above 80 percent", 1300),
    ("network", "Transient retry on upstream call", 800),
]

# Routine INFO messages (filler to reach TOTAL_LINES)
INFO_MESSAGES = [
    ("auth", "User login successful"),
    ("web", "Request handled successfully"),
    ("api", "Health check passed"),
    ("worker", "Background job completed"),
    ("payment", "Transaction processed"),
]

MALFORMED_LINES = 180  # lines that do NOT match the regex (counted as skipped)


def build_entries():
    entries = []

    for module, message, count in ERROR_SIGNATURES:
        entries.extend([("ERROR", module, message)] * count)

    for module, message, count in WARNING_SIGNATURES:
        entries.extend([("WARNING", module, message)] * count)

    used = len(entries) + MALFORMED_LINES
    info_needed = TOTAL_LINES - used
    for i in range(info_needed):
        module, message = INFO_MESSAGES[i % len(INFO_MESSAGES)]
        entries.append(("INFO", module, message))

    # Intentionally malformed lines (no bracketed level/module) to exercise the parser's skip path
    entries.extend([("MALFORMED", None, "corrupted syslog fragment without standard format")] * MALFORMED_LINES)

    random.seed(42)
    random.shuffle(entries)
    return entries


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    entries = build_entries()

    with open(OUTPUT_PATH, "w") as f:
        timestamp = START_TIME
        for level, module, message in entries:
            timestamp += timedelta(seconds=1)
            ts = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            if level == "MALFORMED":
                f.write(f"{message}\n")
            else:
                f.write(f"{ts} [{level}] [{module}] {message}\n")

    print(f"Wrote {len(entries):,} lines to {OUTPUT_PATH}")
    print("Now run: python3 main.py --input data/large_sample.log --top 5")


if __name__ == "__main__":
    main()
