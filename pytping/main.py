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
import pathlib
import argparse
import os
from pytping import __about__
from pytping import PythonPing


PARSER = argparse.ArgumentParser(
    prog=pathlib.Path(__file__).name,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__about__.__script_description__,
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
    version=__about__.__version__
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
