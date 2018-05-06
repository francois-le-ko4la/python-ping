#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

#     #    #    #     # #
 #   #    # #   ##   ## #
  # #    #   #  # # # # #
   #    #     # #  #  # #
   #    ####### #     # #
   #    #     # #     # #
   #    #     # #     # #######

"""

import pathlib
import yaml


class Default:
    encode = 'utf-8'
    msg_ioerror = "File not found !"
    msg_badyaml = "Can't load the YAML..."
    key_filename = 'filename'
    key_data = 'data'


class ConfigYAML(dict):
    """
    This class manage YAML config file

    Args:
        - filename (str): /path/to/the/config/file

    Use:
        >>> import pathlib
        >>> path_pyth = (pathlib.Path(__file__).resolve().parent)
        >>> conf = pathlib.PurePath(path_pyth, '../bin/config.yml.samp')
        >>> config = ConfigYAML(conf)
        Traceback (most recent call last):
        ...
        OSError: File not found !
        >>> conf = pathlib.PurePath(path_pyth, '../LICENSE')
        >>> config = ConfigYAML(conf)
        Traceback (most recent call last):
        ...
        ValueError: Can't load the YAML...
        >>> conf = pathlib.PurePath(path_pyth, '../bin/config.yml.sample')
        >>> config = ConfigYAML(conf)
        >>> print(config['Internet access'])
        {'host': 'www.google.fr', 'port': 80}
        >>> print(config.keys())
        dict_keys(['Internet access', 'vCenter', 'ESX1', 'ESX2'])
        >>> print(len(config))
        4
        >>> #import json
        >>> #print(json.dumps(config, indent=4))
    """
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    @property
    def filename(self):
        return self[Default.key_filename]

    @filename.setter
    def filename(self, filename):
        if pathlib.Path(filename).exists():
            self[Default.key_filename] = str(filename)
            with open(filename, 'r') as yaml_file:
                try:
                    self[Default.key_data] = yaml.load(yaml_file)
                except yaml.YAMLError:
                    raise ValueError(Default.msg_badyaml)
        else:
            raise IOError(Default.msg_ioerror)

    def __getitem__(self, key):
        current_data = super().__getitem__(Default.key_data)
        return current_data[key]

    def __len__(self):
        return len(super().__getitem__(Default.key_data))

    def __iter__(self):
        return iter(super().__getitem__(Default.key_data))

    def keys(self):
        return super().__getitem__(Default.key_data).keys()

    def items(self):
        return super().__getitem__(Default.key_data).items()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
