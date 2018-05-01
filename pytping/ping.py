#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

sudo iptables -P OUTPUT ACCEPT
myhost = PingNetworkObj('http://www.google.fr')
print(myhost.isconnected)
"""

import subprocess


class PingNetworkNode(object):
    """
    This class ping a network equipement
    """
    def __init__(self, host):
        self.__host = None
        self.host = host

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
    def isconnected(self):
        """Test network connection

        Args:
            None

        Returns:
            bool

        """
        try:
            subprocess.run("ping -c 1 -w 1 " + self.__host,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            return True
        except Exception:
            return False
