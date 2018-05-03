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


class ConfigYAML(object):
    """
    This class manage YAML config file

    Property:
        - filename (str): /path/to/the/config/file
        - config (dict)

    Use:
        >>> import pathlib
        >>> path_pyth = (pathlib.Path(__file__).resolve().parent)
        >>> conf = pathlib.PurePath(path_pyth, '../bin/config.yml.sample')
        >>> a = ConfigYAML(conf)
        >>> print(a.config['Internet access'])
        {'host': 'www.google.fr', 'port': 80}
    """
    def __init__(self, filename):
        self.__filename = None
        self.filename = filename

    @property
    def filename(self):
        """
        @Property:
            filename (str): /path/to/the/config/file
        """
        return self.__filename

    @filename.setter
    def filename(self, filename):
        if pathlib.Path(filename).exists():
            self.__filename = filename
        else:
            raise IOError("File not found ! ({})".format(filename))

    @property
    def config(self):
        """
        @Property:
            config (dict)
        """
        with open(self.__filename, 'r') as yaml_file:
            try:
                return yaml.load(yaml_file)
            except yaml.YAMLError:
                raise


if __name__ == "__main__":
    import doctest
    doctest.testmod()
