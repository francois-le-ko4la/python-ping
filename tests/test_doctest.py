#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import sys
import pathlib
import doctest
import unittest
import subprocess

modulelist = ['configyaml.py',
              'counter.py',
              'ping.py',
              'position.py',
              'nodelist.py']


class RunDocTest(unittest.TestCase):
    def run_doctest(self, current_file):
        try:
            subprocess.run("python3 -m doctest -v " + current_file,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


path = pathlib.Path(
                    pathlib.PurePath(
                            pathlib.Path(__file__).resolve().parent, '../')
                    ).resolve()

sys.path.append(path)

for current_file in modulelist:
    def ch(current_file):
        return lambda self: self.run_doctest(current_file)
    setattr(RunDocTest,
            "test_mod_{}".format(current_file),
            ch("pytping/" + current_file)
            )


if __name__ == "__main__":
    unittest.main()