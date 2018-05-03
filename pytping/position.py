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


class ElementPosition(object):
    """
    Calc element position according to element stripe size and
    stripe size.

      +------------+
      | Element 0  |
      +------------+
      <------------>
       Element size
                         Stripe Size
      <-------------------------------------------->
      .                                            .
      .                  Stripe 0                  .
      +--------------------------------------------+
      | +-----------+ +-----------+                |
      | | Element 0 | | Element 1 | ...            |
      | +-----------+ +-----------+                |
      +--------------------------------------------+

                         Stripe 1
      +--------------------------------------------+
      | +-----------+ +-----------+                |
      | | Element 0 | | Element 1 | ...            |
      | +-----------+ +-----------+                |
      +--------------------------------------------+

    Use:
       >>> a = ElementPosition()
       >>> a.element_size = 3
       >>> a.stripe_size = 11
       >>> a.current_id = 0
       >>> print(a.row)
       0
       >>> print(a.column)
       0
       >>> a.current_id = 2
       >>> print(a.row)
       0
       >>> print(a.column)
       2
       >>> a.current_id = 3
       >>> print(a.row)
       1
       >>> print(a.column)
       0

    """
    def __init__(self):
        self.__stripe_size = None
        self.__element_size = None
        self.__current_id = None
        self.current_id = 0

    @property
    def stripe_size(self):
        """
        @Property:
            int: stripe size
        """
        return self.__stripe_size

    @stripe_size.setter
    def stripe_size(self, value):
        if isinstance(value, numbers.Integral) and value > 0:
            self.__stripe_size = value
        else:
            raise TypeError("invalid stripe_size")

    @property
    def element_size(self):
        """
        @Property:
            int: element size
        """
        return self.__element_size

    @element_size.setter
    def element_size(self, value):
        if isinstance(value, numbers.Integral) and value > 0:
            self.__element_size = value
        else:
            raise TypeError("invalid element_size")

    @property
    def ratio(self):
        """
        @Property:
            int: number of element per stripe
        """
        current_ratio = int(self.__stripe_size/self.__element_size)
        if current_ratio is 0:
            current_ratio = 1
        return current_ratio

    @property
    def current_id(self):
        """
        @Property:
            int: current element id
        """
        return self.__current_id

    @current_id.setter
    def current_id(self, value):
        if isinstance(value, numbers.Integral):
            self.__current_id = value
        else:
            raise TypeError("invalid current_id")

    @property
    def row(self):
        """
        @Property:
            int: row
        """
        return int(self.__current_id/self.ratio)

    @property
    def column(self):
        """
        @Property:
            int: column
        """
        return self.__current_id - (self.row * self.ratio)
