port_number = int(input("Enter a port number: "))
applicationName = ""
if port_number > 501 and port_number < 599:
    applicationName = "Test-App1"
else:
    print("Invalid port number")

if applicationName != "":
    print("Application Name: " + applicationName)
else:
    print("No valid application found")