
'''
Demonstrate raising exceptions:
- Raise ValueError when a number exceeds 100.
- Raise a custom exception for insufficient balance.
- Raise a custom exception when age is below 18.
'''

try:
    n = input("Enter a number: ")
    if int(n) > 100:
        raise ValueError("Number is greater than 100")
except ValueError as e:
    print("Error:", e, "for input:", n)


class InsufficientBalanceError(Exception):
    pass


balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError(
            "Insufficient balance for the withdrawal"
        )
except InsufficientBalanceError as e:
    print("Error:", e)


class InvalidAgeError(Exception):
    pass


age = 15

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
except InvalidAgeError as e:
    print("Error:", e)