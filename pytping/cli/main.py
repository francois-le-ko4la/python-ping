#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #    #    ##       #    #    #
 ##  ##   #  #      #    ##   #
 # ## #  #    #     #    # #  #
 #    #  ######     #    #  # #
 #    #  #    #     #    #   ##
 #    #  #    #     #    #    #

"""
import argparse
import os
from pytping import __version__, CONFIG
from pytping.main import PythonPing


PARSER = argparse.ArgumentParser(
    prog=CONFIG.script['bin'],
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=CONFIG.script['description'],
    epilog="Enjoy...",
    add_help=False
)

OPTION = PARSER.add_argument_group('optional arguments')
OPTION.add_argument(
    "-h",
    "--help",
    action="help",
    help="show this help message and exit"
)
OPTION.add_argument(
    '-v',
    '--version',
    action='version',
    version=__version__
)

REQUIRED = PARSER.add_argument_group('required arguments')
REQUIRED.add_argument(
    '-i',
    '--input',
    help='Input file name',
    required=True
)


def run():
    """
    CLI runner
    """
    args = PARSER.parse_args()
    os.environ["NCURSES_NO_UTF8_ACS"] = "1"
    pyt_ping = PythonPing(args.input)
    pyt_ping.run()


__all__ = ["run"]
