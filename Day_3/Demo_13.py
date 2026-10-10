
'''
Write a Python program:
1. Read network.cfg into an empty dictionary.
2. Update Interface to eth1, onboot to yes and bootproto to static.
3. Add IPADDR, PREFIX and DNS1.
4. Use pprint to display the original and updated dictionaries.
5. Write the updated settings to new_network.cfg.
'''

import pprint


def read_file():
    config_dict = {}

    with open('network.cfg', 'r') as fobj:
        for line in fobj:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            k, v = line.split('=', 1)
            config_dict[k.strip()] = v.strip()

    return config_dict


def update_configurations(config_dict):
    config_dict['Interface'] = 'eth1'
    config_dict['onboot'] = 'yes'
    config_dict['bootproto'] = 'static'
    config_dict['IPADDR'] = '192.168.1.10'
    config_dict['PREFIX'] = '24'
    config_dict['DNS1'] = '122.33.344.555'
    return config_dict


def write_to_file(config_dict, filename):
    with open(filename, 'w') as wobj:
        for k, v in config_dict.items():
            wobj.write(f"{k}={v}\n")


config_dict = read_file()

print("Original configuration:")
pprint.pprint(config_dict)

config_dict = update_configurations(config_dict)

print("\nUpdated configuration:")
pprint.pprint(config_dict)

write_to_file(config_dict, 'new_network.cfg')