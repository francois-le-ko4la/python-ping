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
    This class count from 0 to max_value.
    In the end, we restart the count.

    +---+    +---+    +---+           +---+
    | 0 | -> | 0 | -> | 0 | -> ... -> |max|
    +---+    +---+    +---+           +---+
      ^                                 |
      |                                 |
      +---------------------------------+

    Attributes:
        value (int): current value

    Use:
        a = Counter(max_value)
        print(a.value)
        print(a.value)
        print(a.value)
        print(a.value)

    Results:
        0
        1
        2
        ...
    """
    def __init__(self, max_value):
        self.__value = None
        self.__max_value = max_value
        self.reset()

    @property
    def value(self):
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
