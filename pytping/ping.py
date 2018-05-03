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
    """

    def __init__(self, host, port):
        self.__host = None
        self.__port = None
        self.host = host
        self.port = port

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        if type(host) is type(str()):
            self.__host = host
        else:
            raise TypeError(default.msg_typeerror)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if type(port) is type(str()) or type(port) is type(int()):
            self.__port = port
        else:
            raise TypeError(default.msg_typeerror)

    @property
    def isconnected(self):
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
            subprocess.run(default.ping_cmd + self.__host,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            return True
        except Exception:
            return False
