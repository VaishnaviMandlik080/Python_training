
'''
Write a Python program:
- Read a port number from STDIN.
- If the port is between 5001 and 5999, set the app name to Flask.
- Otherwise, set the app name to WebApp.
- Display the app name and running port number.
'''

port = int(input("Enter port number: "))

if 5001 <= port <= 5999:
    appName = "Flask"
else:
    appName = "WebApp"

print(f"The application is running on port {port} with app name {appName}")