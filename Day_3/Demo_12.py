'''
Write a Python program:
- Read key=value pairs from network.cfg into a dictionary.
- Display the dictionary.
- Update the network settings and display them.
- Write the updated settings to new_network.cfg.
'''

import pprint

network_params = {}

with open('network.cfg', 'r') as fobj:
    for line in fobj:
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        key, value = line.split('=', 1)
        network_params[key.strip()] = value.strip()

pprint.pprint(network_params)

network_params['Interface'] = 'eth1'
network_params['bootproto'] = 'static'
network_params['onboot'] = 'yes'
network_params['IPADD'] = '192.168.1.10'
network_params['PREFIX'] = '24'
network_params['DNS1'] = '8.8.8.8'

print('\nUpdated Dict details:-')
pprint.pprint(network_params)

with open('new_network.cfg', 'w') as wobj:
    for key, value in network_params.items():
        wobj.write(f'{key} = {value}\n')