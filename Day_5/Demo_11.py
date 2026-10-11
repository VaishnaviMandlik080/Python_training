
'''
Remove letters from each disk size.
Calculate and display the total size.
Display the unique numeric strings using a set.
'''

import re

s = ['120GB', '500GB', 'GB200', '150Gb', '300gb', '400']

total = 0

for var in s:
    size = re.sub('[A-Za-z]', '', var)
    total += int(size)

print(f'Sum of disk sizes: {total}')
print({re.sub('[A-Za-z]', '', var) for var in s})