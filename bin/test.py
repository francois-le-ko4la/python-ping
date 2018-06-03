from yaml import load, dump
from collections import namedtuple


yaml_file = open('conf2', 'r')
data = load(yaml_file)
configuration = namedtuple('Nodes', data.keys())(*data.values())
yaml_file.close()

print(configuration)
