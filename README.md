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

- PIP3:

```shell
sudo pip3 install --extra-index-url https://francois-le-ko4la.github.io/pep-503/ pytping --upgrade
```

- Or GIT:
```shell
$ git clone https://github.com/francois-le-ko4la/python-ping.git
$ cd python-ping
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
- [X] Release 0.5.1

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
[@Property NetworkNode.rtt](#property-networknodertt)<br />
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
[ElementLocation()](#elementlocation)<br />
[@Property ElementLocation.stripe_size](#property-elementlocationstripe_size)<br />
[@Property ElementLocation.element_size](#property-elementlocationelement_size)<br />
[@Property ElementLocation.ratio](#property-elementlocationratio)<br />
[@Property ElementLocation.current_id](#property-elementlocationcurrent_id)<br />
[@Property ElementLocation.row](#property-elementlocationrow)<br />
[@Property ElementLocation.column](#property-elementlocationcolumn)<br />
[PytPingError()](#pytpingerror)<br />
[PytPingPortConfigError()](#pytpingportconfigerror)<br />


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
class NetworkNode(object):
```

```
Define a network node :
- label
- host
- port
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
##### @Property NetworkNode.rtt
```python
@property
def NetworkNode.rtt(self):
```
> <br />
> provide device rtt<br />
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
#### ElementLocation()
```python
class ElementLocation(object):
```

```
Calc element position according to element stripe size and
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
   >>> a = ElementLocation()
   >>> a.element_size = 3
   >>> a.stripe_size = 11
   >>> a.current_id = 0
   >>> print(a.row)
   0
   >>> print(a.column)
   0
   >>> a.current_id = 2
   >>> print(a.row)
   0
   >>> print(a.column)
   2
   >>> a.current_id = 3
   >>> print(a.row)
   1
   >>> print(a.column)
   0
```

##### @Property ElementLocation.stripe_size
```python
@property
def ElementLocation.stripe_size(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: stripe size<br />
> <br />
##### @Property ElementLocation.element_size
```python
@property
def ElementLocation.element_size(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: element size<br />
> <br />
##### @Property ElementLocation.ratio
```python
@property
def ElementLocation.ratio(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: number of element per stripe<br />
> <br />
##### @Property ElementLocation.current_id
```python
@property
def ElementLocation.current_id(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: current element id<br />
> <br />
##### @Property ElementLocation.row
```python
@property
def ElementLocation.row(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: row<br />
> <br />
##### @Property ElementLocation.column
```python
@property
def ElementLocation.column(self):
```
> <br />
> <b>@Property:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: column<br />
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
