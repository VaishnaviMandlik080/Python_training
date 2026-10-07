'''
s = '123456789'
Given string s, write a python program calculate sum of the digits.
Use 'for' loop.
'''

s = '12345678911'
totalSum = 0
for var in s:
    totalSum = totalSum + int(var)

print(f"Sum of the digits in string s is:{totalSum}")