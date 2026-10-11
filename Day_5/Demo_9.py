
'''
Read r1.log.
Ignore empty lines and display non-empty lines.
'''

import re

with open('r1.log', 'r') as fobj:
    for var in fobj:
        var = var.strip()

        if re.search("^$", var):
            continue
        else:
            print(var)