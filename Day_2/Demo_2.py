'''
Given a list of employee records:
- Iterate through the list.
- Split each record using a comma as the delimiter.
- Display the employee name in title case and department in uppercase.
- Calculate and display the total salary.
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
    print(f"Employee Name: {empName.title()}, Department: {empDept.upper()}")
    totalSalary += int(empSalary)

print(f"Total Salary: {totalSalary}")