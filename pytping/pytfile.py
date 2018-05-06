#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######     #    #       ######
 #          #    #       #
 #####      #    #       #####
 #          #    #       #
 #          #    #       #
 #          #    ######  ######

"""

import pathlib
import os


class PytFile(object):

    """
    >>> fstab = PytFile("/etc/fstab")
    >>> print(fstab.filename.stem)
    fstab
    >>> print(fstab)
    /etc/fstab
    >>> license = PytFile("../LICENSE")
    >>> print(license.filename.stem)
    LICENSE
    >>> #print(license.read())

    """

    def __init__(self, filename):
        self.filename = filename

    @property
    def filename(self):
        return self.__path

    @filename.setter
    def filename(self, value):
        self.__path = pathlib.Path()
        if pathlib.Path(value).exists():
            self.__path = pathlib.Path(value).resolve()
        else:
            raise IOError("File not found !")

    def __repr__(self):
        return str(self.__path)

    def __str__(self):
        return repr(self)

    def read(self):
        return self.filename.read_text()
