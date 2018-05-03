#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####  ####### #     # #     # #######
 #     # #     # #     # ##    #    #
 #       #     # #     # # #   #    #
 #       #     # #     # #  #  #    #
 #       #     # #     # #   # #    #
 #     # #     # #     # #    ##    #
  #####  #######  #####  #     #    #

"""


class Counter(object):
    """
    This class count from 0 to (max_value - 1).
    In the end, we restart the count.

    +-----+    +-----+    +-----+           +-------+
    |  0  | -> |  1  | -> |  2  | -> ... -> |  max  |
    +-----+    +-----+    +-----+           +-------+
      ^                                         |
      |                                         |
      +-----------------------------------------+

    Attributes:
        value (int): current value

    Test:
        python3 -m doctest -v <module>

    Use:
        >>> max_value = 2
        >>> a = Counter(max_value)
        >>> print(a.value)
        0
        >>> print(a.value)
        1
        >>> print(a.value)
        2
        >>> print(a.value)
        0

    """
    def __init__(self, max_value):
        self.__value = None
        self.__max_value = max_value
        self.reset()

    @property
    def value(self):
        """
        @Property:
            current value (int)
        """
        if self.__value is (self.__max_value + 1):
            self.reset()

        result = self.__value
        self.__value += 1
        return result

    def reset(self):
        """
        reset current value

        Args:
            None

        Returns:
            None
        """
        self.__value = 0
