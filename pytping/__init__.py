#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

# pytping

![alt text](./pictures/screen.png)

## Why:

When you have to check a network node, you use ping command and all is fine.
Sometimes, you have to manage multiple nodes. As a consequence, you have to
open multiple terminals to ping the nodes. In the real life, this kind
of tasks are not really interresting and you have to switch between the
terminals. Of course, at the same time, you have to remember IP address.
Basically, you have many ping tools on Windows.
My objective is to provide a __simple/light tool__ that can be used quickly
on linux environments.
The GUI has been build with `curses` library provided by system V/posix
environments. A windows library exists and allow you to adapt the screen
module.

__This project is not :__

- :x: a ping command replacement
- :x: a tool (MultiPing/PingInfoView) replacement
- :x: a network analyzer
- :x: a CMDB tool

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

- Check network permissions to ping

```shell
sudo iptables -P OUTPUT ACCEPT
```

- Use the script provided in this package :

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

## Feedback

My test environment:
- CPU:
    - 1 x Intel(R) Core(TM) i5-4250U CPU @ 1.30GHz
    - 2 thread per core
    - 2 core per socket
- Mem : 8GB (6927MiB)

With 4 network nodes:
- %CPU: <1% (average) - 2% (higher rate)
- %MEM: 0.3%
- 6 Thread : 1 main thread, 1 screen thread, 1 thread per network node

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
│   ├── classes.png
│   ├── classes_pytping.png
│   ├── packages.png
│   ├── packages_pytping.png
│   └── screen.png
├── pytping
│   ├── cli
│   │   ├── __init__.py
│   │   └── main.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── pyping.py
│   ├── netnode
│   │   ├── __init__.py
│   │   ├── list.py
│   │   ├── node.py
│   │   └── ping.py
│   ├── screen
│   │   ├── counter.py
│   │   ├── curse.py
│   │   ├── __init__.py
│   │   └── position.py
│   └── util
│       ├── __about__.py
│       ├── __config__.py
│       └── __init__.py
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
- [X] Release
- [X] change (un)install process
- [X] remove MANIFEST.in
- [X] manage global var: __version__....
- [X] improve the doc
- [X] Release 0.4.3
- [X] improve (un)install process
- [X] Release 0.5.0

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""
from pytping.util import *
import pytping.main
import pytping.netnode
import pytping.screen
import pytping.cli
