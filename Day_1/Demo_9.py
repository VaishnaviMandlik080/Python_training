'''
Write a Python program:
- Read the application name from STDIN.
- Use a membership test to check whether the input contains "flask".
- If it contains "flask", set the port to 5000; otherwise, use 8080.
- Display the application name and running port number.
'''

appName = input("Enter application name: ").strip()

if 'flask' in appName.lower():
    port = 5000
else:
    port = 8080

print(f"The application is running on port {port} with app name {appName}")