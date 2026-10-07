'''
Write a Python program:
1. Create a file named p4.py.
2. Read two disk partition names from STDIN.
3. Read the size of each partition from STDIN.
4. Calculate the sum of the partition sizes.
5. Use a multi-line string to display the details.
'''

partition1 = input("Enter a disk partition: ")
size1 = int(input(f"Enter {partition1} partition size: "))

partition2 = input("Enter a disk partition: ")
size2 = int(input(f"Enter {partition2} partition size: "))

totalSize = size1 + size2

print(f'''Partition {partition1} Size: {size1}
Partition {partition2} Size: {size2}
---------------------------------------------
Total Partition Size: {totalSize}
---------------------------------------------''')