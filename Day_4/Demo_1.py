
'''
Read employee records from emp.csv.
Calculate and display the total cost of sales employees.
'''

fobj = open("emp.csv", "r")
L = fobj.readlines()
fobj.close()

total = 0

for var in L:
    if 'sales' in var:
        var = var.strip()
        empList = var.split(",")
        eCost = int(empList[-1])
        total += eCost

print("Total cost for sales employees:", total)

