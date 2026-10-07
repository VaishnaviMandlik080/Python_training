'''
Write a Python program:
1. Create an empty dictionary.
2. Display the number of items using len().
3. Use a while loop to read five hostname and IP address pairs.
4. Display the number of items after input.
5. Display hostname and IP address pairs using a for loop.
6. Read a hostname to update.
7. If it exists, update its IP to 127.0.0.1.
   Otherwise, display that it does not exist.
8. Display the final dictionary.
'''

hosts = {}
print(f"Initial number of items: {len(hosts)}")

count = 0

while count < 5:
    hostname = input("Enter hostname: ").strip()
    ip_address = input("Enter IP address: ").strip()
    hosts[hostname] = ip_address
    count += 1

print(f"Number of items after input: {len(hosts)}")

for hostname, ip_address in hosts.items():
    print(f"{hostname} -> {ip_address}")

searchHostName = input("Enter hostname to update: ").strip()

if searchHostName in hosts:
    hosts[searchHostName] = "127.0.0.1"
    print(f"Updated {searchHostName} to 127.0.0.1")
else:
    print(f"{searchHostName} does not exist")

print("Final dictionary:")
print(hosts)