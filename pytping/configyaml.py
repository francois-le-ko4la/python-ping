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

mlk = ConfigYAML("./onfig.yml")
print(mlk.config)
"""

import pathlib
import yaml


class ConfigYAML(object):
    """
    This class manage YAML config file
    """
    def __init__(self, filename):
        self.__filename = None
        self.filename = filename

    @property
    def filename(self):
        """
        @property filename
        """
        return self.__filename

    @filename.setter
    def filename(self, filename):
        """
        This function check the path and store it in self.__filename
        """
        if pathlib.Path(filename).exists():
            self.__filename = filename
        else:
            raise IOError("File not found ! ({})".format(filename))

    @property
    def config(self):
        """
        Open/read the YAML config file.
        Returns the config.
        """
        with open(self.__filename, 'r') as yaml_file:
            try:
                return yaml.load(yaml_file)
            except yaml.YAMLError:
                raise
