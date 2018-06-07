#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #    #  ######     #     ####
 #    #  #    #  ##   #  #          #    #    #
 #       #    #  # #  #  #####      #    #
 #       #    #  #  # #  #          #    #  ###
 #    #  #    #  #   ##  #          #    #    #
  ####    ####   #    #  #          #     ####

"""

import pathlib
from conf2tuple import NamedTupleConfig

YAML_CONF = "/config.yml"
PATH = pathlib.Path(__file__).resolve().parent
YAML_CONF = str(PATH) + YAML_CONF
CONFIG = NamedTupleConfig(YAML_CONF, NamedTupleConfig.isyaml).config
