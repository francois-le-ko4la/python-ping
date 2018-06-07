#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module allow us to define a network node with all curse parameters.

"""

from collections import namedtuple
from pytping.netnode.node import NetworkNode
from pytping.util import CONFIG
from pytping.screen.location import NodeSubWin


StringPos = namedtuple('StrPos', ['y', 'x', 'ch'])


class CNetworkNode(NetworkNode):
    """
    Define a network node :
    - label (netnode.NetworkNode)
    - host (netnode.NetworkNode)
    - port (netnode.NetworkNode)
    - get_nodesubwin() (value & position)
    - get_nodelabel() (value & position)
    - get_nodename() (value & position)
    - get_nodertt() (value & position)

    use:
        >>> import time
        >>> node = CNetworkNode("label", "localhost", "ICMP")
        >>> # start hyperthreading
        >>> node.start()
        >>> time.sleep(0.2)
        >>> node.isconnected
        True
        >>> "ms" in node.rtt # '3.63 ms'
        True
        >>> node.label
        'label'
        >>> node.get_nodesubwin(80,0)
        NodeSubWin(height=4, width=30, y=2, x=3)
        >>> node.get_nodelabel()
        StrPos(y=1, x=2, ch='label')
        >>> node.get_nodename()
        StrPos(y=2, x=5, ch='localhost')

    """
    def __init__(self, label, host, port):
        super().__init__(label, host, port)
        self.__node_subwin = NodeSubWin()
        self.__node_label = StringPos(y=1, x=2, ch=self.label)
        self.__node_name = StringPos(y=2, x=5, ch=self.host)
        self.__node_rtt = StringPos(y=0, x=0, ch="")

    def get_nodesubwin(self, screen_width, id_value):
        """
        NamedTuple to create subwin
        """
        return self.__node_subwin.get_nodesubwin(screen_width, id_value)

    def get_nodelabel(self):
        """
        NamedTuple to create the node label
        """
        return self.__node_label

    def get_nodename(self):
        """
        NamedTuple to create the nodename
        """
        return self.__node_name

    def get_nodertt(self):
        """
        NamedTuple to create the rtt
        """
        self.__node_rtt = StringPos(
            y=1,
            x=(CONFIG.box["width"] - len("  " + str(self.rtt)) - 2),
            ch="  " + str(self.rtt)
        )
        return self.__node_rtt
