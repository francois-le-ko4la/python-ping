#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pytping

![alt text](./pictures/screen.png)

## Why:

When you have to check a network node, you use ping command and all is fine.
Sometimes, you have to manage multiple nodes. As a consequence, you have to
open multiple terminal windows to ping the nodes. In the real life, this kind
of tasks are not really interresting and you have to switch between the
windows. Of course, at the same time, you have to remember IP address.

Basically, you have many ping tools on Windows.
My objective is to provide a __simple/light tool__ that can be used quickly
on linux environments.

The GUI has been build with `curses` library provided by system V/posix
environments. A windows library exists and allow you to adapt the screen
module.

__This project is not :__
- a ping command replacement
- a tool (MultiPing/PingInfoView) replacement
- a network analyzer
- a CMDB tool

## Setup:

```shell
$ git clone https://github.com/francois-le-ko4la/pyt-ping.git
$ cd pyt-ping
$ make install
```

## Test:

This module has been [tested and validated](./last_check.log) on Ubuntu.
```shell
$ make test
```

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

Configuration file should be written according to this example:
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

## Project Structure
```
.
├── bin
│   ├── config.yml.sample
│   └── pyt-ping.py
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_pytping.png
│   ├── packages_pytping.png
│   └── screen.png
├── pytping
│   ├── _ _about_ _.py
│   ├── confyaml.py
│   ├── counter.py
│   ├── _ _init_ _.py
│   ├── main.py
│   ├── netnode.py
│   ├── nodelist.py
│   ├── ping.py
│   ├── position.py
│   ├── pyping.py
│   └── screen.py
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test_doctest.py
    └── test_pycodestyle.py
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

## License

pytping is distributed under the [GPLv3 license](./LICENSE)

"""

from pytping import __about__
from pytping.position import ElementPosition
from pytping.counter import Counter
from pytping.screen import ScreenCurses
from pytping.ping import PingNetworkNode
from pytping.confyaml import ConfigYAML
from pytping.netnode import NetworkNode
from pytping.nodelist import NetworkNodeList
from pytping.pyping import PythonPing
