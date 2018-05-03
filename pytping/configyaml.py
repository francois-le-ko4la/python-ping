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
        a = ConfigYAML("./onfig.yml")
        print(a.config)
    """
    def __init__(self, filename):
        self.__filename = None
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        if pathlib.Path(filename).exists():
            self.__filename = filename
        else:
            raise IOError("File not found ! ({})".format(filename))

    @property
    def config(self):
        with open(self.__filename, 'r') as yaml_file:
            try:
                return yaml.load(yaml_file)
            except yaml.YAMLError:
                raise
