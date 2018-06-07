#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

sudo iptables -P OUTPUT ACCEPT
myhost = PingNetworkObj('http://www.google.fr')
print(myhost.isconnected)
"""

import subprocess
import socket
import time
from pytping import (
    CONFIG,
    PytPingPortConfigError,
    PytPingHostConfigError
)


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
        self.__rtt = None
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
            raise PytPingHostConfigError(host)

    @property
    def rtt(self):
        """
        @Property:
        """
        if self.__rtt is 'UKN':
            return self.__rtt
        return self.__rtt

    @property
    def port(self):
        """
        @Property:
            str/int: "ICMP" or port number
        """
        return self.__port

    @port.setter
    def port(self, port):
        if isinstance(port, (int, str)):
            self.__port = port
        else:
            raise PytPingPortConfigError(port)

    @property
    def isconnected(self):
        """
        @Property:
            bool: True if the node is connected. False otherwise.
        """
        if isinstance(self.__port, str) and CONFIG.ICMP in self.__port:
            return self.__ping()
        else:
            return self.__socket()

    def __socket(self):
        try:
            socket.setdefaulttimeout(CONFIG.timeout)
            start = time.time()
            socket.socket().connect((self.__host, self.__port))
            self.__rtt = "{} ms".format(
                int(100000 * (time.time() - start)) / 100)

        except Exception:
            self.__rtt = "UKN"
            return False
        return True

    def __ping(self):
        try:
            proc = subprocess.Popen(CONFIG.ping_cmd + self.__host,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            p_status = proc.wait()
            rtt = proc.stdout.read()
            rtt = (((rtt.decode("utf-8").split("\n"))[1]).split("="))[3]
            self.__rtt = rtt
            return True
        except Exception:
            self.__rtt = "UKN"
            return False
