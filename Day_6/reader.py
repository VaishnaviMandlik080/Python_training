"""
Log File Analyzer and Error Monitoring Tool - File Reader Module
----------------------------------------------------------------
Author      : Pratik Mohite
Maintainer  : Pratik Mohite
Module      : File Ingestion and Memory-Safe Streaming
Description : Provides functionality for reading log files in a memory-efficient manner, handling errors gracefully.
"""

import os                    # For interacting with the operating system, such as file paths
import logging               # For logging messages within the reader module
from typing import Generator # For type hinting generator functions

logger = logging.getLogger("LogAnalyzer.Reader") # Logger for the reader module

def read_log_stream(file_path: str) -> Generator[str, None, None]:
    """
    Stream the contents of a log file line by line in a memory-efficient manner. Handles file access, permission errors, 
    and encoding issues gracefully.
    """
    if not isinstance(file_path, str) or not file_path.strip(): # Check if the file path is a non-empty string
        logger.error("Invalid file path provided.")
        raise ValueError("File path should be a non-empty string.")
    
    if not os.path.exists(file_path):  # Check if the target log file exists
        logger.error("Target log file does not exist: %s", file_path)
        raise FileNotFoundError(f"File does not exist: {file_path}")

    if not os.path.isfile(file_path):  # Check if the specified path is a valid file
        logger.error("Specified path is not a valid file: %s", file_path)
        raise ValueError(f"Path is not a valid file: {file_path}")

    try:
        with open(file_path, "r") as fobj:
            line_count = 0
            for line in fobj:
                line_count += 1
                yield line        # Yield each line while keeping track of the line count
            if line_count == 0:
                logger.warning("The target log file is empty: %s", file_path)
    except PermissionError:
        logger.error("Permission denied when accessing the file: %s", file_path)
        raise PermissionError(f"Permission denied when accessing the file: {file_path}")
    except Exception as e:
        logger.error("An unexpected error occurred while reading the file: %s", file_path)
        raise RuntimeError(f"Failed to read the file: {file_path}") from e