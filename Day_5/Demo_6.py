
'''
Handle division by zero.
Log the error and an execution completion message.
'''

import logging

logging.basicConfig(level=logging.INFO)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)
finally:
    logging.info("Execution finished")