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

from pythread import PThread
from pytping.util import DEFAULT
from pytping.netnode.ping import PingNetworkNode


class NetworkNode(object):
    """
    Define a network node :
    - label
    - host
    - port
    """
    def __init__(self, label, host, port):
        self.__isconnected = False
        self.label = label
        self.host = host
        self.__ping = PingNetworkNode(host, port)
        self.__port = port
        self.__mthr = PThread(self.__refresh, DEFAULT["refresh"])

    @property
    def isconnected(self):
        """
        @Property:
            bool: True if the node is connected. False otherwise.
        """
        return self.__isconnected

    @property
    def rtt(self):
        """
        provide device rtt
        """
        return str(self.__ping.rtt)

    def __refresh(self):
        self.__isconnected = self.__ping.isconnected

    def stop(self):
        """
        Stop multithreading

        Args:
            None

        Returns:
            None
        """
        self.__mthr.stop()

    def start(self):
        """
        Start multithreading to ping the node.

        Args:
            None

        Returns:
            None
        """
        self.__mthr.start()
