'''
Write a Python program:
- Open emp.csv in read mode.
- Read the entire file.
- Display the type and number of characters read.
- Display the file contents.
'''

fobj = open("emp.csv", "r")
L = fobj.read()
fobj.close()

print(type(L), len(L))
print("")
print("Display the contents of the file")
print(L)