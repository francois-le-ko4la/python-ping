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
from pytping import CONFIG
from pytping.netnode.ping import PingNetworkNode


class NetworkNode(PingNetworkNode):
    """
    Define a network node :
    - label
    - host
    - port
    use:
        >>> import time
        >>> node = NetworkNode("label", "www.google.fr", 80)
        >>> # start hyperthreading
        >>> node.start()
        >>> time.sleep(0.2)
        >>> node.isconnected
        True
        >>> "ms" in node.rtt # '3.63 ms'
        True
        >>> node.label
        'label'
    """
    def __init__(self, label, host, port):
        super().__init__(host, port)
        self.__isconnected = False
        self.label = label
        self.__mthr = PThread(self.__refresh, CONFIG.refresh)

    @property
    def isconnected(self):
        """
        @Property:
            bool: True if the node is connected. False otherwise.
        """
        return self.__isconnected

    def __refresh(self):
        self.__isconnected = super().isconnected

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
