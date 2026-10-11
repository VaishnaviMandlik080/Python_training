
'''
Write informational, warning and error messages to app.log.
Include the date, time and logging level in each record.
'''

import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Application started")
logging.warning("This is a warning message for missing email")
logging.error("This is an error message for failed login or this is a critical issue")