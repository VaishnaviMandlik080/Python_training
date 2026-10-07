'''
Write a python program 
Demonstrate the ATM Pin Number validation.
Initialize the pin number to 1234
- Use a while loop 
   - Limit is 3 attempts
   - Read an input pin number from <STDIN>
   - Test - if pin number is correct then display "Pin Number is Valid" - display count
- If all 3 attempts are failed then display "Pin is blocked"
'''
# Initial pin number and attempt count
pin = 1234
attemptCount = 0

# Loop until the user has made 3 attempts or entered the correct pin
while(attemptCount < 3):
    userPin = int(input("Enter your pin number: "))
    attemptCount += 1
    if(userPin == pin):
        print(f"Pin Number is Valid - count is:{attemptCount}")
        break

if pin != userPin:
    print("Pin is blocked")