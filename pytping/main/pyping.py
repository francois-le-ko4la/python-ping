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

from conf2tuple import NamedTupleConfig
from pytping.screen.curse import ScreenCurses
from pytping.netnode.list import NetworkNodeList
from pytping.screen.node import CNetworkNode


class PythonPing(object):
    """
    Main class
    Use YAML config file
    Create NetworkNodeList
    Launch the screen manager
    """
    def __init__(self, inputfile):
        """ self.__config = ConfigYAML(inputfile) """
        self.__config = NamedTupleConfig(inputfile, NamedTupleConfig.isyaml)
        self.__host_list = NetworkNodeList()
        for node in self.__config.config.nodes:
            current_node = CNetworkNode(
                node,
                self.__config.config.nodes[node]['host'],
                self.__config.config.nodes[node]['port']
            )
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
