"""
Log File Analyzer and Error Monitoring Tool - Parser Module
----------------------------------------------------------------
Author      : Tejas Rathod
Maintainer  : Tejas Rathod
Module      : Regex Processing, Event Classification and Data Structures
Description : Provides functionality for parsing log lines using regular expressions, classifying events, 
              and organizing data into structured formats.
"""
import re
import logging
from typing import Dict, Optional # For type hinting complex data structures like lists and dictionaries

logger = logging.getLogger("LogAnalyzer.Parser") # Logger for the parser module

# Defined regular expressions and parsing logic for log events here
LOG_PATTERN = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] \[(?P<module>\w+)\] (?P<message>.*)") 

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Extracts log components from a single line using the defined regular expression pattern.
    Returns a dictionary with keys 'timestamp', 'level', 'module', and 'message' if the line
    matches the pattern. Returns None if the line does not match the pattern.
    """
    if not isinstance(line, str):
        return None

    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    timestamp, level, module, message = match.groups()

    return {
        "timestamp": timestamp,
        "level": level,
        "module": module,
        "message": message
    }