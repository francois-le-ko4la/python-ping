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
    In the end (max_value+1), the value becomes 0
    """
    def __init__(self, max_value):
        """
        Init current value and stores max_value
        """
        self.__value = 0
        self.__max_value = max_value

    @property
    def value(self):
        """
        Returns current value
        """
        if self.__value is (self.__max_value + 1):
            self.__value = 0

        result = self.__value
        self.__value += 1
        return result

    def reset(self):
        """
        reset current value
        """
        self.__value = 0
