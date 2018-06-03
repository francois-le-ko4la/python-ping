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
from collections import namedtuple
from pytping.util import TEMPLATE


class NodeSubWin(namedtuple('NodeSubWin', ['height', 'width', 'y', 'x'])):
    """
    >>> a = NodeSubWin()
    >>> for i in range(5): a.get_nodesubwin(80, i)
    NodeSubWin(height=4, width=30, y=2, x=3)
    NodeSubWin(height=4, width=30, y=2, x=36)
    NodeSubWin(height=4, width=30, y=7, x=3)
    NodeSubWin(height=4, width=30, y=7, x=36)
    NodeSubWin(height=4, width=30, y=12, x=3)
    """
    def __new__(cls, height=0, width=0, y=0, x=0):
        return super(NodeSubWin, cls).__new__(cls, height, width, y, x)

    def __init__(self, height=0, width=0, y=0, x=0):
        self.elemlocation = ElemLocation()
        self.elemlocation.element_size = TEMPLATE["box_width"] + \
            TEMPLATE["box_margin_x"]

    def get_nodesubwin(self, screen_width, id_value):
        self.elemlocation.stripe_size = screen_width - 2
        host_location = self.elemlocation.getposyx(id_value)
        height = TEMPLATE["box_height"]
        width = TEMPLATE["box_width"]
        y = host_location.y
        x = host_location.x
        return NodeSubWin(height, width, y, x)


class ElemLocation(namedtuple('ElemLocation', ['y', 'x'])):
    """
    Calc element logical position according to element stripe size and
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
        >>> # simple test
        >>> a = ElemLocation()
        >>> a.element_size = 3
        >>> a.stripe_size = 11
        >>> for i in range(5): a.getlogposyx(i)
        ElemLocation(y=0, x=0)
        ElemLocation(y=0, x=1)
        ElemLocation(y=0, x=2)
        ElemLocation(y=1, x=0)
        ElemLocation(y=1, x=1)
        >>> # real test
        >>> a = ElemLocation()
        >>> a.element_size = TEMPLATE["box_width"] + TEMPLATE["box_margin_x"]
        >>> a.element_size
        33
        >>> a.stripe_size = 80 - 2
        >>> a.stripe_size
        78
        >>> for i in range(5): a.getposyx(i)
        ElemLocation(y=2, x=3)
        ElemLocation(y=2, x=36)
        ElemLocation(y=7, x=3)
        ElemLocation(y=7, x=36)
        ElemLocation(y=12, x=3)
    """

    __slot__ = ('y', 'x')

    def __new__(cls, y=0, x=0):
        return super().__new__(cls, y=y, x=x)

    def __init__(self, y=0, x=0):
        super().__init__()
        self.__stripe_size = None
        self.__element_size = None
        self.__current_id = None
        self.__current_id = 0

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

    def getlogposyx(self, current_id):
        if isinstance(current_id, numbers.Integral):
            self.__current_id = current_id
            row = int(self.__current_id/self.ratio)
            column = self.__current_id - (row * self.ratio)
            self = ElemLocation(y=row, x=column)
            return self
        else:
            raise TypeError("invalid current_id")

    def getposyx(self, current_id):
        self = self.getlogposyx(current_id)
        x = self.x * (TEMPLATE["box_width"] + TEMPLATE["box_margin_x"]) + \
            TEMPLATE["box_margin_x"]
        y = self.y * (TEMPLATE["box_height"] + TEMPLATE["box_margin_y"]) + \
            TEMPLATE["box_margin_y"] + 1

        return ElemLocation(y=y, x=x)
