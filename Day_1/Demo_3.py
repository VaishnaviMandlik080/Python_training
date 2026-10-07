
dept = 'sales'

print(dept)
print('dept')
print('working dept is :', dept)
print('working dept is : %s' % dept)
print('working dept is : {}'.format(dept))
print(f'working dept is : {dept}')

# print(Dept)  # Would raise NameError: variable names are case-sensitive

print(type(dept))
print(type('production'))
print(type(123))
print(type(123.45))
print(type(True), type(False))
print(type(None))