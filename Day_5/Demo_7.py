
'''
Calculate 10000 divided by the given balance.
Log successful calculations.
Log division-by-zero errors with their traceback.
'''

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def get_balance(balance):
    try:
        result = 10000 / balance
        logging.info("Balance calculation successful")
        return result
    except ZeroDivisionError as e:
        logging.exception("An error occurred: %s", e)
        return None


print(get_balance(2))
print(get_balance(0))