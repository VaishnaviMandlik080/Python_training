
'''
Write a Python program:
- Create an empty dictionary.
- Add employee IDs, names, departments and dates of birth.
- Display the dictionary using pprint.
'''

import pprint

emp = {}

emp['eid'] = [101, 102, 103, 104]
emp['ename'] = ['john', 'ram', 'raju', 'bibu']
emp['edept'] = ['sales', 'prod', 'hr', 'sales']
emp['dob'] = {
    'DOB': [
        {'DOB': '1st Jan'},
        {'DOB': '2nd Jan'},
        {'DOB': '3rd Jan'},
        {'DOB': '4th Jan'}
    ]
}

pprint.pprint(emp)
