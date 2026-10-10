'''
Read employee records from emp.csv.
Display employees in the sales department.
Calculate and display their total salary.
'''

fobj = open("emp.csv", "r")
total = 0
L = fobj.readlines()

for var in L:
    var = var.strip()
    eid, name, dept, salary = var.split(",")

    if dept.lower() == "sales":
        total += int(salary)
        print(
            f"Emp Name is {name.title()}, \t Salary is {salary}, "
            f"\t Department is {dept.upper()}"
        )

fobj.close()

print("Total salary of sales department:", total)
print("*" * 40)
print(f"Sum of sales department salaries: {total}")
print("-" * 35)