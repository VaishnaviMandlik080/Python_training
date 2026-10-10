'''
Validate an ATM PIN with a maximum of three attempts.
Append success, failure and blocked details to pin_history.log.
'''

import time


def pin_test(arg):
    return arg == "1234"


with open("pin_history.log", "a") as history:
    for attempt in range(1, 4):
        p = input("Enter a pin Number: ")

        if pin_test(p):
            message = f"Success - {attempt} - {time.ctime()}"
            print(message)
            history.write(message + "\n")
            break
        else:
            message = (
                f"Failure - {attempt} - PIN: {p} - {time.ctime()}"
            )
            print(message)
            history.write(message + "\n")
    else:
        message = f"Pin is blocked - {time.ctime()}"
        print(message)
        history.write(message + "\n")