#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import sys
import argparse
from pytping import __about__
from pytping import *


class ArgsManagement(object):

    def __init__(self, argv):
        self.parser = argparse.ArgumentParser(
            prog=pathlib.Path(__file__).name,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=__about__.__script_description__,
            epilog="Enjoy...",
            add_help=False
        )
        self.optional = self.parser.add_argument_group('optional arguments')
        self.optional.add_argument(
            "-h",
            "--help",
            action="help",
            help="show this help message and exit"
        )
        self.optional.add_argument(
            '-v',
            '--version',
            action='version',
            version=__about__.__version__
        )
        self.required = self.parser.add_argument_group('required arguments')
        self.required.add_argument(
            '-i',
            '--input',
            help='Input file name',
            required=True
        )
        self.args = self.parser.parse_args()

    def get(self):
        return self.args


def main(argv):
    args = ArgsManagement(argv)
    current_args = args.get()
    pyt_ping = PythonPing(current_args.input)
    pyt_ping.run()


if __name__ == '__main__':
    main(sys.argv[1:])
