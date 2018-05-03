#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pytping
## Description:

This package loads the configuration values defined in external YAML file and
ping network nodes.

The following files comprise the `pytping` package:
* `LICENSE`: The license file. `config-from-json` is released under the terms
of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the `config_from_json` directory:
* `__init__.py` Initialization file for the Python package.
* `__about__.py` Global parameters
* `configyaml.py` Config file management
* `counter.py` Simple counter to make a progress animation
* `netnode.py` NetworkNode def
* `nodelist.py` NetworkNode management
* `ping.py` check host/port
* `position.py` Element position management
* `pyping.py` main function
* `screen.py` Screen management

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

## Screenshot:

![alt text](./pictures/screen.png)


## Use:

Use the script provided in this package :
```shell
$ pyt-ping.py -h
usage: pyt-ping.py [-h] [-v] -i INPUT

Ping tool...

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

required arguments:
  -i INPUT, --input INPUT
                        Input file name

Enjoy...
```

Configuration file should be write according to this example:
```yaml
Internet access:
  host: www.google.fr
  port: 80
vCenter:
  host: 192.168.1.12
  port: ICMP
ESX1:
  host: 192.168.1.230
  port: 23
ESX2:
  host: 192.168.1.240
  port: ICMP
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
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
from pytping.position import ElementPosition
from pytping.counter import Counter
from pytping.screen import ScreenCurses
from pytping.ping import PingNetworkNode
from pytping.configyaml import ConfigYAML
from pytping.netnode import NetworkNode
from pytping.nodelist import NetworkNodeList
from pytping.pyping import PythonPing
