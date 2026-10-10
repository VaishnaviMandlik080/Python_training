
'''
Read all lines from emp.csv into a list.
Display the list's type, number of lines and contents.
'''

fobj = open("emp.csv", "r")
L = fobj.readlines()
fobj.close()

print(type(L), len(L))
print("")
print("Display the contents of the file")
print(L)