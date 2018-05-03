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
from pytping.ping import PingNetworkNode


class NetworkNode(object):
    """
    Define a network node :
    - label
    - host
    - port
    """
    def __init__(self, label, host, port):
        self.__timer = None
        self.__isconnected = None
        self.__started = False
        self.isconnected = False
        self.label = label
        self.host = host
        self.__ping = PingNetworkNode(host, port)
        self.__port = port

    @property
    def isconnected(self):
        """
        @Property:
            bool: True if the node is connected. False otherwise.
        """
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
        """
        Stop multithreading

        Args:
            None

        Returns:
            None
        """
        self.__started = False

    def start(self):
        """
        Start multithreading to ping the node.

        Args:
            None

        Returns:
            None
        """
        self.__started = True
        self.__refresh()