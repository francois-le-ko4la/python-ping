#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####    #   #  #####      #    #    #   ####
 #    #    # #   #    #     #    ##   #  #    #
 #    #     #    #    #     #    # #  #  #
 #####      #    #####      #    #  # #  #  ###
 #          #    #          #    #   ##  #    #
 #          #    #          #    #    #   ####

"""

from pytping.screen import ScreenCurses
from pytping.configyaml import ConfigYAML
from pytping.netnode import NetworkNode
from pytping.members import NetworkNodeList


class PythonPing(object):
    def __init__(self, inputfile):
        self.__yaml = ConfigYAML(inputfile)
        self.__config = self.__yaml.config
        self.__host_list = NetworkNodeList()
        for label in self.__config:
            current_node = NetworkNode(label,
                                       self.__config[label]['host'],
                                       self.__config[label]['port'])
            current_node.start()
            self.__host_list.append(current_node)
        self.__screen = ScreenCurses(self.__host_list)

    def run(self):
        """ start screen """
        self.__screen.run()
        """ EXIT """
        for host in self.__host_list:
            host.stop()
