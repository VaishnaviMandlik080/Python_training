# 1. Create an empty dictionary
hosts = {}

# 2. Display the number of items
print(f"Number of items: {len(hosts)}")

# 3. Read five hostname and IP pairs using a while loop
count = 0

while count < 5:
    hostname = input(f"\nEnter hostname {count + 1}: ")
    ip = input(f"Enter IP for {hostname}: ")

    hosts[hostname] = ip
    count += 1

# 4. Display the number of items
print(f"\nNumber of items: {len(hosts)}")

# 5. Display hostname and IP using a for loop
print("\nHost details:")
for hostname, ip in hosts.items():
    print(f"{hostname}: {ip}")

# 6. Read a hostname
hostname = input("\nEnter hostname to update or add: ")

# 7. Update an existing host or create a new host
if hostname in hosts:
    hosts[hostname] = "127.0.0.1"
    print(f"Updated IP for {hostname}.")
else:
    hosts[hostname] = "127.0.0.1"
    print(f"Added new host {hostname}.")

# 8. Display the updated dictionary details
print(f"\nNumber of items: {len(hosts)}")
print("Updated host details:")

for hostname, ip in hosts.items():
    print(f"{hostname}: {ip}")