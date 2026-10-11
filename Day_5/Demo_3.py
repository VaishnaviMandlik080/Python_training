
'''
Demonstrate handling file-related exceptions.
Display error messages when files cannot be opened.
'''

import sys

try:
    with open("non_existent_file.txt", "r") as fobj:
        pass
except PermissionError as e:
    print("Permission error occurred:", e)
except FileNotFoundError as e:
    print("File not found error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("File operation attempt finished")

print(" ")

try:
    with open("Invalid_File.txt", "r") as fobj:
        pass
except Exception as e:
    sys.exc_info()
    print("An unexpected error occurred:", e)