'''
Filter and display employees from the sales department.
Calculate the total salary of sales employees.
'''

Emp = [
    '101,john,sales,1000',
    '102,ram,prod,2000',
    '103,raju,hr,3000',
    '104,bibu,sales,4000'
]

totalSalary = 0

for employee in Emp:
    empId, empName, empDept, empSalary = employee.split(',')

    if empDept.lower() == 'sales':
        print(f"Employee Name: {empName.title()}, Department: {empDept.upper()}")
        totalSalary += int(empSalary)

print(f"Total Salary: {totalSalary}")