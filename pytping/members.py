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


class MembersObj(object):

    """
    [] to store a python object's members.
    This object will become an attribute.
    """

    def __init__(self):
        self.__members = []
        self.__currentindex = 0

    def __repr__(self):
        return str(self.__members)

    def __str__(self):
        return repr(self)

    def __getitem__(self, index):
        return self.__members[index]

    def __len__(self):
        return len(self.__members)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            key = self.__currentindex
            member = self.__members[key]
        except IndexError:
            self.__currentindex = 0
            raise StopIteration()
        self.__currentindex += 1
        return member

    def append(self, value):
        """
        add a member
        """
        self.__members.append(value)

    def items(self):
        """
        get members
        """
        return self.__members
