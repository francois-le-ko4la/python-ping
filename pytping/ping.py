#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

sudo iptables -P OUTPUT ACCEPT
myhost = PingNetworkObj('http://www.google.fr')
print(myhost.isconnected)
"""

import subprocess
import socket


class Default:
    """
    PingNetworkNode parameters
    """
    timeout = 0.5
    ICMP = "ICMP"
    msg_typeerror = "PingNetworkNode: invalid input type"
    ping_cmd = "ping -c 1 -w 1 "


class PingNetworkNode(object):

    """
    This class ping a network node.
    We store host/port
    Host can be defined with a hostname or IP address.
    If port = ICMP then we use ping command.
    Else, we use socket API.

        >>> a = PingNetworkNode("www.google.fr", 80)
        >>> print(a.isconnected)
        True
        >>> a = PingNetworkNode("localhost", "ICMP")
        >>> print(a.isconnected)
        True
        >>> a = PingNetworkNode("10.10.9.1", "ICMP")
        >>> print(a.isconnected)
        False
    """

    def __init__(self, host, port):
        self.__host = None
        self.__port = None
        self.host = host
        self.port = port

    @property
    def host(self):
        """
        @Property:
            str: hostname or IP address
        """
        return self.__host

    @host.setter
    def host(self, host):
        if isinstance(host, str):
            self.__host = host
        else:
            raise TypeError(Default.msg_typeerror)

    @property
    def port(self):
        """
        @Property:
            str/int: "ICMP" or port number
        """
        return self.__port

    @port.setter
    def port(self, port):
        if isinstance(port, str) or isinstance(port, int):
            self.__port = port
        else:
            raise TypeError(Default.msg_typeerror)

    @property
    def isconnected(self):
        """
        @Property:
            bool: True if the node is connected. False otherwise.
        """
        if isinstance(self.__port, str) and Default.ICMP in self.__port:
            return self.__ping()
        else:
            return self.__socket()

    def __socket(self):
        try:
            socket.setdefaulttimeout(Default.timeout)
            socket.socket().connect((self.__host, self.__port))
        except Exception:
            return False
        return True

    def __ping(self):
        try:
            subprocess.run(Default.ping_cmd + self.__host,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            return True
        except Exception:
            return False
