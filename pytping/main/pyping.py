#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903, W0105

"""

 #####    #   #  #####      #    #    #   ####
 #    #    # #   #    #     #    ##   #  #    #
 #    #     #    #    #     #    # #  #  #
 #####      #    #####      #    #  # #  #  ###
 #          #    #          #    #   ##  #    #
 #          #    #          #    #    #   ####

"""

from pytconfig import PytConfigFile
from pytping.screen.curse import ScreenCurses
from pytping.netnode.list import NetworkNodeList
from pytping.netnode.node import NetworkNode


class PythonPing(object):
    """
    Main class
    Use YAML config file
    Create NetworkNodeList
    Launch the screen manager
    """
    def __init__(self, inputfile):
        """ self.__config = ConfigYAML(inputfile) """
        self.__config = PytConfigFile(inputfile, PytConfigFile.isyaml)
        self.__host_list = NetworkNodeList()
        for label in self.__config:
            current_node = NetworkNode(label,
                                       self.__config[label]['host'],
                                       self.__config[label]['port'])
            current_node.start()
            self.__host_list.append(current_node)
        self.__screen = ScreenCurses(self.__host_list)

    def run(self):
        """
        Start curses screen
        User can stop this app with [ESC] key.
        In the end stop all process
        """
        self.__screen.run()
        """ EXIT """
        for host in self.__host_list:
            host.stop()