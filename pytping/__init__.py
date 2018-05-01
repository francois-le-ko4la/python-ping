#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pytping
## Description:

This package loads the configuration values defined in external YAML file and
ping equipemments.

The following files comprise the `pytping` package:
* `LICENSE`: The license file. `config-from-json` is released under the terms
of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the `config_from_json` directory:
* `__init__.py` Initialization file for the Python package.
* `XXX`: The code of interest.

## Setup:

```shell
git clone https://github.com/francois-le-ko4la/pyt-ping.git
cd pyt-ping
make install
```

## Test:

This module has been tested and validated on Ubuntu.
```shell
make test
```

## Use:

## Todo:

- [X] Create the project
- [ ] Write code and tests
- [ ] Test installation and requirements (setup.py and/or Makefile)
- [ ] Test code
- [ ] Validate features
- [ ] Write Doc/stringdoc
- [ ] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## Note:

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

from pytping import __about__
from pytping.limit import CalcLimit
from pytping.counter import Counter
from pytping.screen import ScreenCurses
from pytping.ping import PingNetworkNode
from pytping.configyaml import ConfigYAML
from pytping.members import NetworkNodeList
from pytping.pyping import NetworkNode, PythonPing
