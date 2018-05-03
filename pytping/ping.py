#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

sudo iptables -P OUTPUT ACCEPT
myhost = PingNetworkObj('http://www.google.fr')
print(myhost.isconnected)
"""

import subprocess
import socket


class default:
    timeout=0.5
    ICMP="ICMP"


class PingNetworkNode(object):
    """
    This class ping a network equipement
    """
    def __init__(self, host, port):
        self.__host = None
        self.__port = None
        self.host = host
        self.port = port

    @property
    def host(self):
        """
        Property
        """
        return self.__host

    @host.setter
    def host(self, host):
        self.__host = host

    @property
    def port(self):
        """
        Property
        """
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def isconnected(self):
        """Test network connection

        Args:
            None

        Returns:
            bool

        """

        if type(self.__port) is type(str() and default.ICMP in self.__port):
            return self.__ping()
        else:
            return self.__socket()

    def __socket(self):
        try:
            socket.setdefaulttimeout(default.timeout);
            socket.socket().connect((self.__host, self.__port))
        except Exception:
            return False
        return True

    def __ping(self):
        try:
            subprocess.run("ping -c 1 -w 1 " + self.__host,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            return True
        except Exception:
            return False
