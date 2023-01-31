#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Metadata with importlib_metadata:
# mypy: disable-error-code=no-redef
"""Define about."""
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # type: ignore

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")

__pkg_name__ = "pytping"
__version__: str = metadata.version(__pkg_name__)
__author__: str = metadata.metadata(__pkg_name__)["Author"]
__url__: str = metadata.metadata(__pkg_name__)["Project-URL"]
__license__: str = metadata.metadata(__pkg_name__)["License"]
__description__: str = metadata.metadata(__pkg_name__)["Summary"]
