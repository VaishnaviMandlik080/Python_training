
'''
Read employee records from emp.csv.
Find records containing "sales", ignoring case.
Replace "pune" with "HYDERABAD".
Display matching records containing "HYDERABAD".
'''

import re

fname = "emp.csv"

with open(fname, 'r') as fobj:
    for var in fobj:
        if re.search('sales', var, re.I):
            s = re.sub('pune', 'HYDERABAD', var)

            if 'HYDERABAD' in s:
                print(s.strip())