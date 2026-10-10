
'''
Read network.cfg into a dictionary, display it,
update the settings, display them again, and
write them to new_network.cfg.
'''

import pprint


def f1():
    '''Return an empty dictionary.'''
    return {}


def f2(network_params):
    '''Read network configuration from network.cfg.'''
    with open('network.cfg', 'r') as fobj:
        for line in fobj:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            key, value = line.split('=', 1)
            network_params[key.strip()] = value.strip()

    return network_params


def f3(network_params):
    '''Display network parameters.'''
    pprint.pprint(network_params)


def f4(network_params):
    '''Update and add network parameters.'''
    network_params['Interface'] = 'eth1'
    network_params['bootproto'] = 'static'
    network_params['onboot'] = 'yes'
    network_params['IPADDR'] = '192.168.1.10'
    network_params['PREFIX'] = 24
    network_params['DNS1'] = '122.33.344.555'
    return network_params


def f5(network_params):
    '''Write the updated configuration to a new file.'''
    with open('new_network.cfg', 'w') as wobj:
        for key, value in network_params.items():
            wobj.write(f'{key} = {value}\n')


# Call the functions
network_params = f1()
network_params = f2(network_params)

print("Original configuration:")
f3(network_params)

network_params = f4(network_params)

print("\nUpdated configuration:")
f3(network_params)

f5(network_params)