#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #    #  ######  #    #  #####   ######  #####    ####
 ##  ##  #       ##  ##  #    #  #       #    #  #
 # ## #  #####   # ## #  #####   #####   #    #   ####
 #    #  #       #    #  #    #  #       #####        #
 #    #  #       #    #  #    #  #       #   #   #    #
 #    #  ######  #    #  #####   ######  #    #   ####

a = MembersObj()
b = test()
a.append({'zefjh':b })
a.append({'sdjsdlv':b})

print(a.items())
for member in a  :
    print(member)
"""

from pytping import NetworkNode


class NetworkNodeList(dict):

    """
    {} to store a python object's members (NetworkNode).
    We want to test object type before store.
    We use a dict() in order to make a complex object :

       +-------------------------------------+ --*
       |  label                              |   |
       | +------+    +------------+          |   |- __str__
       | | type | => |  obj type  |     obj  |   |  __iter__
       | +------+    +------------+          |   |  ...
       |                                     |   |
       | +------+    +------------+  *       |   |     --*
       | | data | => |  Object 0  |  |       |   |       |
       | +------+    +------------+  |       |   |       |
       |             +------------+  |       |   |       |
       |             |  Object 1  |  |- list |   |       |- append
       |             +------------+  |       |   |       |  items
       |                  ...        |       |   |       |  __len__
       |             +------------+  |       |   |       |  __next__
       |             |  Object n  |  |       |   |       |
       |             +------------+  *       |   |     --*
       +-------------------------------------+ --*

    Obj type is protected by design and is NetworkNode type.
    A new element type is compare with Obj type.
    Another type will create a raise exception.

    str(NetworkNodeList()) => str(ALL)
    len(NetworkNodeList()) => len(list())
    NetworkNodeList.append => list().append

        >>> from pytping import NetworkNode
        >>> a = NetworkNodeList()
        >>> b = NetworkNode("", "", "")
        >>> c = NetworkNode("", "", "")
        >>> a.append(b)
        >>> print(len(a))
        1
        >>> for member in a: print(type(member))
        <class 'pytping.netnode.NetworkNode'>
        >>> a.append(c)
        >>> print(len(a))
        2
        >>> for member in a: print(type(member))
        <class 'pytping.netnode.NetworkNode'>
        <class 'pytping.netnode.NetworkNode'>
        >>> a.append(3)
        Traceback (most recent call last):
        ...
        TypeError: This object is not a NetworkNode

    """

    def __init__(self):
        super().__init__()
        self.__obj_type = NetworkNode("", "", "")
        self['type'] = self.__obj_type
        self['data'] = []
        self.__currentindex = 0
        self.__index = 0

    def __len__(self):
        return len(super().__getitem__('data'))

    def __iter__(self):
        return iter(super().__getitem__('data'))

    def __next__(self):
        try:
            # key = self.__currentindex
            member = super().__getitem__('data')
            member = member[self.__currentindex]
        except IndexError:
            self.__currentindex = 0
            raise StopIteration()
        self.__currentindex += 1
        return member

    def append(self, value):
        """
        add a member
        """
        if isinstance(value, type(self['type'])):
            self['data'].append(value)
        else:
            raise TypeError("This object is not a NetworkNode")

    def items(self):
        """
        get members
        """
        return self['data']
