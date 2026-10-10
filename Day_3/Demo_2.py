'''
Read the first line of emp.csv.
Display its type, character count and contents.
'''

fobj = open("emp.csv", "r")
L = fobj.readline()
fobj.close()

print(type(L), len(L))
print("")
print("Display the first line of the file")
print(L)