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

    Property:
        - filename (str): /path/to/the/config/file
        - config (dict)

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
    """
    def __init__(self, filename):
        self.__set_filename(filename)
        self.__getconfig()

    def __set_filename(self, filename):
        if pathlib.Path(filename).exists():
            self.__dict__[Default.key_filename] = filename
        else:
            raise IOError(Default.msg_ioerror)

    def __getconfig(self):
        """
        @Property:
            config (dict)
        """
        with open(self.__dict__[Default.key_filename], 'r') as yaml_file:
            try:
                self.__dict__[Default.key_data] = yaml.load(yaml_file)
            except yaml.YAMLError:
                raise ValueError(Default.msg_badyaml)

    def __getitem__(self, key):
        return self.__dict__[Default.key_data][key]

    def __len__(self):
        return len(self.__dict__[Default.key_data])

    def __iter__(self):
        return iter(self.__dict__[Default.key_data])

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return repr(self)

    def keys(self):
        return self.__dict__[Default.key_data].keys()

    def items(self):
        return self.__dict__[Default.key_data].items()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
