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

from threading import Timer
from pytping.screen import ScreenCurses
from pytping.ping import PingNetworkNode
from pytping.configyaml import ConfigYAML
from pytping.members import NetworkNodeList


class NetworkNode(object):
    def __init__(self, label, host, port=False):
        self.__isconnected = None
        self.__started = True
        self.isconnected = False
        self.label = label
        self.host = host
        self.__ping = PingNetworkNode(host)
        self.__port = port
        self.__refresh()

    @property
    def isconnected(self):
        return self.__isconnected

    @isconnected.setter
    def isconnected(self, value):
        self.__isconnected = value

    def __refresh(self):
        if self.__started is not True:
            return
        self.isconnected = self.__ping.isconnected
        self.__timer = Timer(2, self.__refresh)
        self.__timer.start()

    def stop(self):
        self.__started = False


class PythonPing(object):
    def __init__(self, inputfile):
        self.__yaml = ConfigYAML(inputfile)
        self.__config = self.__yaml.config
        self.__host_list = NetworkNodeList()
        for label in self.__config:
            self.__host_list.append(NetworkNode(label,
                                                self.__config[label]['host']))
        self.__screen = ScreenCurses(self.__host_list)

    def run(self):
        """ start screen """
        self.__screen.run()
        """ EXIT """
        for host in self.__host_list:
            host.stop()
