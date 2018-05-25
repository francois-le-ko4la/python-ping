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
from collections import deque


class Counter(object):
    """
    This class count from 0 to max_value.
    In the end, we restart the count.

    +-----+    +-----+    +-----+           +-------+
    |  0  | -> |  1  | -> |  2  | -> ... -> |  max  |
    +-----+    +-----+    +-----+           +-------+
      ^                                         |
      |                                         |
      +-----------------------------------------+


    The first release was a done with basic idea:
        if self.__value is (self.__max_value + 1):
            self.reset()

        result = self.__value
        self.__value += 1
        return result

    Now we suggest a collection:
        >>> from collections import deque
        >>> c=deque(range(3))
        >>> print(c)
        deque([0, 1, 2])
        >>> len(c)
        3
        >>> c[0]
        0
        >>> c.rotate(-1)
        >>> c[0]
        1
        >>> c.rotate(-1)
        >>> c[0]
        2
        >>> c.rotate(-1)
        >>> c[0]
        0

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
        self.__collection = deque(range(int(max_value + 1)))
        self.__collection.rotate(1)

    @property
    def value(self):
        """
        @Property:
            current value (int)
        """
        self.__collection.rotate(-1)
        return self.__collection[0]
