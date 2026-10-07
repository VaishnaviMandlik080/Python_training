'''
Write a Python program:
1. Create an empty list.
2. Display the number of elements using len().
3. Use a while loop to read and append five hostnames.
4. Display the number of elements using len().
5. Display the hostnames using a for loop.
6. Read a hostname to check.
7. If it exists, replace it with a new hostname.
   Otherwise, add it to the list.
8. Display the final hostnames using a for loop.
'''

hosts = []

print(f"Number of elements: {len(hosts)}")

counter = 0
while counter < 5:
    hostname = input("Enter a hostname: ")
    hosts.append(hostname)
    counter += 1

print(f"\nNumber of elements: {len(hosts)}")
print("Hostnames:")
for hostname in hosts:
    print(hostname)

hostName = input("\nEnter a hostname to check: ")

if hostName in hosts:
    index = hosts.index(hostName)
    newHostName = input(
        f"Hostname '{hostName}' exists. Enter new hostname to replace it: "
    )
    hosts[index] = newHostName
else:
    hosts.append(hostName)

print("\nFinal list of hostnames:")
for hostname in hosts:
    print(hostname)