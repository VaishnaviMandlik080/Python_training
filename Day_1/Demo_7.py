'''
Write a Python program:
- Read employee details (Name, Age, Cost) from STDIN.
- Use print() to display employee details.
- Calculate 18% tax on the employee's basic salary and display the tax.
- Add tax to the basic salary and display the total salary including tax.
'''

eloginStatus = True

# Read employee details
ename = input("Enter employee name: ")
eage = int(input(f"Enter {ename}'s age: "))
ecost = float(input(f"Enter {ename}'s basic salary: "))

# Calculate tax and total salary
tax = ecost * 0.18
total_salary = ecost + tax

# Display employee details
print(f'''Employee Name: {ename}
---------------------------------------
{ename}'s Age is: {eage}
---------------------------------------
{ename}'s Basic Salary is: {ecost:.2f}
---------------------------------------
{ename}'s Login Status is: {eloginStatus}
---------------------------------------
The tax on {ecost:.2f} is: {tax:.2f}
---------------------------------------
The total salary is: {total_salary:.2f}
---------------------------------------''')


