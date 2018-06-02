#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.

"""
from setuptools import setup, find_packages
from setuptools.config import read_configuration
import sys

if not sys.version_info[0] == 3:
    sys.exit("Sorry, your Python is not supported (yet)")

CFG = read_configuration('./setup.cfg')
CFG["options"].update(CFG["metadata"])
CFG = CFG["options"]
setup(**CFG)
