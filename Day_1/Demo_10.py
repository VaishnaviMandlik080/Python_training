'''
Write a python program:
- Read an app name from <STDIN>
- Test if flask then initialize port number is 5000
- Test if fastAPI then initialize port number is 8080
- Test if prometheus then initialize port number is 9090
- The default app name is web2.0 and port number 8000
- display app name and running port number
'''
app_name = input("Enter the application name: ")

if app_name.lower() == "flask":
	port = 5000
elif app_name.lower() == "fastAPI":
	port = 8080
elif app_name.lower() == "prometheus":
	port = 9090
else:
	app_name = "web2.0"
	port = 8000

print(f"The application '{app_name}' will run  on port {port}")