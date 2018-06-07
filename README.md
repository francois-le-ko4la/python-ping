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

We use Ubuntu to develop this package and python is a core component of the
operating system. Our makefile, has been written according to this
environment.
In other environment, user should use "pip3" command to install thhis package.
If you use virtualenv, then you will not use sudo to launch the setup.

- To use the package:

```shell
$ [sudo] pip3 install --extra-index-url https://francois-le-ko4la.github.io/pep-503/ pytping --upgrade
```

- Or GIT to test & dev:
```shell
$ git clone https://github.com/francois-le-ko4la/python-ping.git
$ cd python-ping
```

If you want a quick setup on Ubuntu:
```shell
$ make install
```
Other:
```shell
$ [sudo] pip3 install --extra-index-url https://francois-le-ko4la.github.io/pep-503/ pytping --upgrade
```

## Test:

This module has been [tested and validated](./last_check.log) on Ubuntu.

```shell
$ [sudo] ./setup test
```

## Use:

- Check network permissions to ping

```shell
$ sudo iptables -P OUTPUT ACCEPT
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
---
nodes:
  Internet:
    host: www.google.fr
    port: 80
  vCenter:
    host: 192.168.1.12
    port: ICMP
  ESX1:
    host: 192.168.1.230
    port: 22
  ESX2:
    host: 192.168.1.240
    port: ICMP
...
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
- %MEM: ~0.4%
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
- [X] Change (un)install process
- [X] Remove MANIFEST.in
- [X] Manage global var: __ version __....
- [X] Improve the doc
- [X] Release 0.4.3
- [X] Improve (un)install process
- [X] Release 0.5.0
- [X] Validate preq install
- [X] Improve screenshot
- [X] Fix doc
- [X] Perf logs
- [X] Release 0.5.1
- [X] test the Python version
- [X] Install automatically pytest
- [X] Fix doc (install)
- [X] Release 0.5.2
- [X] Clean the config file
- [ ] Clean the UML model using NamedTuple and chain
- [ ] Add/remove a network node & save the config
- [ ] Use Snap method

## License

This package is distributed under the [GPLv3 license](./LICENSE)
### Runtime

```

python-3.6.x


```

### UML Diagram
![alt text](pictures/classes_pytping.png)


### Objects

[run()](#run)<br />
[PythonPing()](#pythonping)<br />
[PythonPing.run()](#pythonpingrun)<br />
[NetworkNodeList()](#networknodelist)<br />
[NetworkNodeList.append()](#networknodelistappend)<br />
[NetworkNodeList.items()](#networknodelistitems)<br />
[NetworkNode()](#networknode)<br />
[@Property NetworkNode.isconnected](#property-networknodeisconnected)<br />
[NetworkNode.stop()](#networknodestop)<br />
[NetworkNode.start()](#networknodestart)<br />
[PingNetworkNode()](#pingnetworknode)<br />
[@Property PingNetworkNode.host](#property-pingnetworknodehost)<br />
[@Property PingNetworkNode.rtt](#property-pingnetworknodertt)<br />
[@Property PingNetworkNode.port](#property-pingnetworknodeport)<br />
[@Property PingNetworkNode.isconnected](#property-pingnetworknodeisconnected)<br />
[Counter()](#counter)<br />
[@Property Counter.value](#property-countervalue)<br />
[ScreenCurses()](#screencurses)<br />
[ScreenCurses.menubar()](#screencursesmenubar)<br />
[ScreenCurses.build()](#screencursesbuild)<br />
[ScreenCurses.run()](#screencursesrun)<br />
[NodeSubWin()](#nodesubwin)<br />
[NodeSubWin.get_nodesubwin()](#nodesubwinget_nodesubwin)<br />
[ElemLocation()](#elemlocation)<br />
[@Property ElemLocation.stripe_size](#property-elemlocationstripe_size)<br />
[@Property ElemLocation.element_size](#property-elemlocationelement_size)<br />
[@Property ElemLocation.ratio](#property-elemlocationratio)<br />
[ElemLocation.getlogposyx()](#elemlocationgetlogposyx)<br />
[ElemLocation.getposyx()](#elemlocationgetposyx)<br />
[CNetworkNode()](#cnetworknode)<br />
[CNetworkNode.get_nodesubwin()](#cnetworknodeget_nodesubwin)<br />
[CNetworkNode.get_nodelabel()](#cnetworknodeget_nodelabel)<br />
[CNetworkNode.get_nodename()](#cnetworknodeget_nodename)<br />
[CNetworkNode.get_nodertt()](#cnetworknodeget_nodertt)<br />
[PytPingError()](#pytpingerror)<br />
[PytPingPortConfigError()](#pytpingportconfigerror)<br />
[PytPingHostConfigError()](#pytpinghostconfigerror)<br />


#### run()
```python

def run():
```
> <br />
> CLI runner<br />
> <br />
#### PythonPing()
```python
class PythonPing(object):
```

```
Main class
Use YAML config file
Create NetworkNodeList
Launch the screen manager
```

##### PythonPing.run()
```python

def PythonPing.run(self):
```
> <br />
> Start curses screen<br />
> User can stop this app with [ESC] key.<br />
> In the end stop all process<br />
> <br />
#### NetworkNodeList()
```python
class NetworkNodeList(dict):
```

```
{} to store a python object's members (NetworkNode).
We want to test object type before store.
We use a dict() in order to make a complex object :

   +-------------------------------------+ --*
   |  label                              |   |
   | +------+    +------------+          |   |- __str__
   | | type | => |  obj type  |     obj  |   |  __iter__
   | +------+    +------------+          |   |  ...
   |                                     |   |
   | +------+    +------------+  *       |   |     --*
   | | data | => |  Object 0  |  |       |   |       |
   | +------+    +------------+  |       |   |       |
   |             +------------+  |       |   |       |
   |             |  Object 1  |  |- list |   |       |- append
   |             +------------+  |       |   |       |  items
   |                  ...        |       |   |       |  __len__
   |             +------------+  |       |   |       |  __next__
   |             |  Object n  |  |       |   |       |
   |             +------------+  *       |   |     --*
   +-------------------------------------+ --*

Obj type is protected by design and is NetworkNode type.
A new element type is compare with Obj type.
Another type will create a raise exception.

str(NetworkNodeList()) => str(ALL)
len(NetworkNodeList()) => len(list())
NetworkNodeList.append => list().append

    >>> from pytping.netnode.node import NetworkNode
    >>> a = NetworkNodeList()
    >>> b = "node1"
    >>> c = "node2"
    >>> a.append(b)
    >>> print(len(a))
    1
    >>> for member in a: print(type(member))
    <class 'str'>
    >>> a.append(c)
    >>> print(len(a))
    2
    >>> for member in a: print(type(member))
    <class 'str'>
    <class 'str'>
    >>> a.append(3)
    Traceback (most recent call last):
    ...
    TypeError: This object is not a <class 'str'>
```

##### NetworkNodeList.append()
```python

def NetworkNodeList.append(self, value):
```
> <br />
> add a member<br />
> <br />
##### NetworkNodeList.items()
```python

def NetworkNodeList.items(self):
```
> <br />
> get members<br />
> <br />
#### NetworkNode()
```python
class NetworkNode(PingNetworkNode):
```

```
Define a network node :
- label
- host
- port
use:
    >>> import time
    >>> node = NetworkNode("label", "www.google.fr", 80)
    >>> # start hyperthreading
    >>> node.start()
    >>> time.sleep(0.2)
    >>> node.isconnected
    True
    >>> "ms" in node.rtt # '3.63 ms'
    True
    >>> node.label
    'label'
```

##### @Property NetworkNode.isconnected
```python
@property
def NetworkNode.isconnected(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: True if the node is connected. False otherwise.<br />
> <br />
##### NetworkNode.stop()
```python

def NetworkNode.stop(self):
```
> <br />
> Stop multithreading<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### NetworkNode.start()
```python

def NetworkNode.start(self):
```
> <br />
> Start multithreading to ping the node.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### PingNetworkNode()
```python
class PingNetworkNode(object):
```

```
This class ping a network node.
We store host/port
Host can be defined with a hostname or IP address.
If port = ICMP then we use ping command.
Else, we use socket API.

    >>> a = PingNetworkNode("www.google.fr", 80)
    >>> print(a.isconnected)
    True
    >>> a = PingNetworkNode("localhost", "ICMP")
    >>> print(a.isconnected)
    True
    >>> a = PingNetworkNode("10.10.9.1", "ICMP")
    >>> print(a.isconnected)
    False
```

##### @Property PingNetworkNode.host
```python
@property
def PingNetworkNode.host(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: hostname or IP address<br />
> <br />
##### @Property PingNetworkNode.rtt
```python
@property
def PingNetworkNode.rtt(self):
```
> <br />
> <b>@Property:</b><br />
> <br />
##### @Property PingNetworkNode.port
```python
@property
def PingNetworkNode.port(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str/int: "ICMP" or port number<br />
> <br />
##### @Property PingNetworkNode.isconnected
```python
@property
def PingNetworkNode.isconnected(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: True if the node is connected. False otherwise.<br />
> <br />
#### Counter()
```python
class Counter(object):
```

```
This class count from 0 to max_value.
In the end, we restart the count.

+-----+    +-----+    +-----+           +-------+
|  0  | -> |  1  | -> |  2  | -> ... -> |  max  |
+-----+    +-----+    +-----+           +-------+
  ^                                         |
  |                                         |
  +-----------------------------------------+


The first release was a done with basic idea:
    if self.__value is (self.__max_value + 1):
        self.reset()

    result = self.__value
    self.__value += 1
    return result

Now we suggest a collection:
    >>> from collections import deque
    >>> c=deque(range(3))
    >>> print(c)
    deque([0, 1, 2])
    >>> len(c)
    3
    >>> c[0]
    0
    >>> c.rotate(-1)
    >>> c[0]
    1
    >>> c.rotate(-1)
    >>> c[0]
    2
    >>> c.rotate(-1)
    >>> c[0]
    0

Attributes:
    value (int): current value

Test:
    python3 -m doctest -v <module>

Use:
    >>> max_value = 2
    >>> a = Counter(max_value)
    >>> print(a.value)
    0
    >>> print(a.value)
    1
    >>> print(a.value)
    2
    >>> print(a.value)
    0
```

##### @Property Counter.value
```python
@property
def Counter.value(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  current value (int)<br />
> <br />
#### ScreenCurses()
```python
class ScreenCurses(object):
```

```
This class manage the screen.

+-----------------------------------------------------------------+
|                                                                 |
|     +-------------+  +-------------+  +-------------+           |
|     | NetworkNode |  | NetworkNode |  | NetworkNode |           |
|     +-------------+  +-------------+  +-------------+           |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
+-----------------------------------------------------------------+
|  XXXXX | XXXX (*)                                               |
+-----------------------------------------------------------------+

+-------------+
| NetworkNode |    Network Node : label, IP, status
+-------------+

XXX                Text
(*)                Progress
```

##### ScreenCurses.menubar()
```python

def ScreenCurses.menubar(self):
```
> <br />
> draw the bar<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ScreenCurses.build()
```python

def ScreenCurses.build(self):
```
> <br />
> Build the screen<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ScreenCurses.run()
```python

def ScreenCurses.run(self):
```
> <br />
> Curses getch loop<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### NodeSubWin()
```python
class NodeSubWin():
```

```
>>> a = NodeSubWin()
>>> for i in range(5): a.get_nodesubwin(80, i)
NodeSubWin(height=4, width=30, y=2, x=3)
NodeSubWin(height=4, width=30, y=2, x=36)
NodeSubWin(height=4, width=30, y=7, x=3)
NodeSubWin(height=4, width=30, y=7, x=36)
NodeSubWin(height=4, width=30, y=12, x=3)
```

##### NodeSubWin.get_nodesubwin()
```python

def NodeSubWin.get_nodesubwin(self, screen_width, id_value):
```
> <br />
> Calc NamedTuple in order to create SubWin<br />
> <br />
#### ElemLocation()
```python
class ElemLocation():
```

```
Calc element logical position according to element stripe size and
stripe size.

  +------------+
  | Element 0  |
  +------------+
  <------------>
   Element size
                     Stripe Size
  <-------------------------------------------->
  .                                            .
  .                  Stripe 0                  .
  +--------------------------------------------+
  | +-----------+ +-----------+                |
  | | Element 0 | | Element 1 | ...            |
  | +-----------+ +-----------+                |
  +--------------------------------------------+

                     Stripe 1
  +--------------------------------------------+
  | +-----------+ +-----------+                |
  | | Element 0 | | Element 1 | ...            |
  | +-----------+ +-----------+                |
  +--------------------------------------------+

Use:
    >>> # simple test
    >>> a = ElemLocation()
    >>> a.element_size = 3
    >>> a.stripe_size = 11
    >>> for i in range(5): a.getlogposyx(i)
    ElemLocation(y=0, x=0)
    ElemLocation(y=0, x=1)
    ElemLocation(y=0, x=2)
    ElemLocation(y=1, x=0)
    ElemLocation(y=1, x=1)
    >>> # real test
    >>> a = ElemLocation()
    >>> a.element_size = CONFIG.box["width"] + CONFIG.box["margin_x"]
    >>> a.element_size
    33
    >>> a.stripe_size = 80 - 2
    >>> a.stripe_size
    78
    >>> for i in range(5): a.getposyx(i)
    ElemLocation(y=2, x=3)
    ElemLocation(y=2, x=36)
    ElemLocation(y=7, x=3)
    ElemLocation(y=7, x=36)
    ElemLocation(y=12, x=3)
```

##### @Property ElemLocation.stripe_size
```python
@property
def ElemLocation.stripe_size(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: stripe size<br />
> <br />
##### @Property ElemLocation.element_size
```python
@property
def ElemLocation.element_size(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: element size<br />
> <br />
##### @Property ElemLocation.ratio
```python
@property
def ElemLocation.ratio(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: number of element per stripe<br />
> <br />
##### ElemLocation.getlogposyx()
```python

def ElemLocation.getlogposyx(self, current_id):
```
> <br />
> Get logical position<br />
> <br />
##### ElemLocation.getposyx()
```python

def ElemLocation.getposyx(self, current_id):
```
> <br />
> Get real position<br />
> <br />
#### CNetworkNode()
```python
class CNetworkNode(NetworkNode):
```

```
Define a network node :
- label (netnode.NetworkNode)
- host (netnode.NetworkNode)
- port (netnode.NetworkNode)
- get_nodesubwin() (value & position)
- get_nodelabel() (value & position)
- get_nodename() (value & position)
- get_nodertt() (value & position)

use:
    >>> import time
    >>> node = CNetworkNode("label", "localhost", "ICMP")
    >>> # start hyperthreading
    >>> node.start()
    >>> time.sleep(0.2)
    >>> node.isconnected
    True
    >>> "ms" in node.rtt # '3.63 ms'
    True
    >>> node.label
    'label'
    >>> node.get_nodesubwin(80,0)
    NodeSubWin(height=4, width=30, y=2, x=3)
    >>> node.get_nodelabel()
    StrPos(y=1, x=2, ch='label')
    >>> node.get_nodename()
    StrPos(y=2, x=5, ch='localhost')
```

##### CNetworkNode.get_nodesubwin()
```python

def CNetworkNode.get_nodesubwin(self, screen_width, id_value):
```
> <br />
> NamedTuple to create subwin<br />
> <br />
##### CNetworkNode.get_nodelabel()
```python

def CNetworkNode.get_nodelabel(self):
```
> <br />
> NamedTuple to create the node label<br />
> <br />
##### CNetworkNode.get_nodename()
```python

def CNetworkNode.get_nodename(self):
```
> <br />
> NamedTuple to create the nodename<br />
> <br />
##### CNetworkNode.get_nodertt()
```python

def CNetworkNode.get_nodertt(self):
```
> <br />
> NamedTuple to create the rtt<br />
> <br />
#### PytPingError()
```python
class PytPingError(Exception):
```

```
Generic exception for pytping
```

#### PytPingPortConfigError()
```python
class PytPingPortConfigError(PytPingError):
```

```
Error: the port is not validated.
```

#### PytPingHostConfigError()
```python
class PytPingHostConfigError(PytPingError):
```

```
Error: the host is not validated.
```
