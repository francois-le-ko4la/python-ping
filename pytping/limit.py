#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple way :
def calc_limit(stripe_size, element_size, current_id):

    ratio = int(stripe_size/element_size)
    print("nmbr elem / stripe: {}".format(ratio))

    row = int(current_id/ratio)

    column = current_id - (row * ratio)
    print(row, column)

... but I want an object

"""
import numbers


class CalcLimit(object):
    """
    Calc element location according to element stripe size and
    stripe size.
    """
    def __init__(self, stripe_size, element_size):
        """
        Init default value and test
        """
        self.__stripe_size = None
        self.__element_size = None
        self.__current_id = None
        self.current_id = 0
        self.stripe_size = stripe_size
        self.element_size = element_size

    @property
    def stripe_size(self):
        """
        Property
        """
        return self.__stripe_size

    @stripe_size.setter
    def stripe_size(self, value):
        """
        Test & store the value
        """
        if isinstance(value, numbers.Integral) and value > 0:
            self.__stripe_size = value
        else:
            raise TypeError("invalid stripe_size")

    @property
    def element_size(self):
        """
        Property
        """
        return self.__element_size

    @element_size.setter
    def element_size(self, value):
        """
        Test & stores the value
        """
        if isinstance(value, numbers.Integral) and value > 0:
            self.__element_size = value
        else:
            raise TypeError("invalid element_size")

    @property
    def ratio(self):
        """
        Calculates the number of elements per stripe
        """
        current_ratio = int(self.__stripe_size/self.__element_size)
        if current_ratio is 0:
            current_ratio = 1
        return current_ratio

    @property
    def current_id(self):
        """
        Property
        """
        return self.__current_id

    @current_id.setter
    def current_id(self, value):
        """
        Test and stores the value
        """
        if isinstance(value, numbers.Integral):
            self.__current_id = value
        else:
            raise TypeError("invalid current_id")

    @property
    def row(self):
        """
        returns the element location (row/stripe id)
        """
        return int(self.__current_id/self.ratio)

    @property
    def column(self):
        """
        returns the element location (column/location in a stripe)
        """
        return self.__current_id - (self.row * self.ratio)
