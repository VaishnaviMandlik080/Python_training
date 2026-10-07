'''
Write a Python program to store and display product details as:
1. A dictionary containing lists.
2. A list containing dictionaries.
3. A dictionary containing dictionaries.
Use pprint to display each structure.
'''

import pprint

# 1. Dictionary containing lists
products = {}
products['pid'] = [101, 102, 103]
products['pname'] = ['pA', 'pB', 'pC']
products['cost'] = [1000, 2000, 3000]
products['Qty'] = [10, 20, 30]
pprint.pprint(products)

print("\n")

# 2. List containing dictionaries
products = []
products.append({'pid': 101, 'pname': 'pA', 'cost': 1000, 'Qty': 10})
products.append({'pid': 102, 'pname': 'pB', 'cost': 2000, 'Qty': 20})
products.append({'pid': 103, 'pname': 'pC', 'cost': 3000, 'Qty': 30})
pprint.pprint(products)

print("\n")

# 3. Dictionary containing dictionaries
products = {}
products['pid'] = {'id1': 101, 'id2': 102, 'id3': 103}
products['pname'] = {'pname1': 'pA', 'pname2': 'pB', 'pname3': 'pC'}
products['cost'] = {'cost1': 1000, 'cost2': 2000, 'cost3': 3000}
products['Qty'] = {'Qty1': 10, 'Qty2': 20, 'Qty3': 30}
pprint.pprint(products)
