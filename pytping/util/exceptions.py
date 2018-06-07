#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######  #####   #####    ####   #####
 #       #    #  #    #  #    #  #    #
 #####   #    #  #    #  #    #  #    #
 #       #####   #####   #    #  #####
 #       #   #   #   #   #    #  #   #
 ######  #    #  #    #   ####   #    #

"""


class PytPingError(Exception):
    """
    Generic exception for pytping
    """
    pass


class PytPingPortConfigError(PytPingError):
    """
    Error: the port is not validated.
    """
    def __init__(self, port):
        super().__init__("Port \"{}\" not valid!".format(port))


class PytPingHostConfigError(PytPingError):
    """
    Error: the host is not validated.
    """
    def __init__(self, host):
        super().__init__("Host \"{}\" not valid!".format(host))


__all__ = [
    'PytPingError',
    'PytPingPortConfigError',
    'PytPingHostConfigError'
]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
