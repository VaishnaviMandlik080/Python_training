# Read employee details from the user
ename = input('Enter employee name: ')
eage = int(input('Enter employee age: '))
ecost = float(input('Enter employee cost: '))
eloginStatus = input('Enter login status (True/False): ').strip().lower() == 'true'

# Display details using a multi-line f-string
print(f'''Employee Name: {ename}
-----------------------------------
Employee Age: {eage}
------------------------
Employee Cost: {ecost}
------------------------
Employee Login Status: {eloginStatus}
-----------------------------------''')