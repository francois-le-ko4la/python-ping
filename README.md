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
* `__about__.py` Global parameters
* `configyaml.py` Config file management
* `counter.py` Simple counter to make a progress animation
* `members.py` NetworkNode management
* `netnode.py` NetworkNode def
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
## Dev notes
### Runtime

```
python-3.6.x

```
### Requirements

```
zope.interface==4.3.2
attrs==17.4.0
py==1.5.3
pycodestyle==2.3.1
more_itertools==4.1.0
pluggy==0.6.0
setuptools==39.0.1
six==1.11.0
argcomplete==1.9.4
attr==0.3.1
colorama==0.3.9
funcsigs==1.0.2
numpy==1.14.3
Twisted==18.4.0
PyYAML==3.12
zope==4.0b4

```
### UML Diagram
![alt text](pictures/classes_pytping.png)

### Objects
[ConfigYAML()](#configyaml)<br />
[@Property: ConfigYAML.config](#property-configyamlconfig)<br />
[@Property: ConfigYAML.filename](#property-configyamlfilename)<br />
[ConfigYAML.__init__(self, filename)](#configyamlinitself-filename)<br />
[Counter()](#counter)<br />
[@Property: Counter.value](#property-countervalue)<br />
[Counter.__init__(self, max_value)](#counterinitself-max_value)<br />
[Counter.reset(self)](#counterresetself)<br />
[ElementPosition()](#elementposition)<br />
[@Property: ElementPosition.column](#property-elementpositioncolumn)<br />
[@Property: ElementPosition.current_id](#property-elementpositioncurrent_id)<br />
[@Property: ElementPosition.element_size](#property-elementpositionelement_size)<br />
[@Property: ElementPosition.ratio](#property-elementpositionratio)<br />
[@Property: ElementPosition.row](#property-elementpositionrow)<br />
[@Property: ElementPosition.stripe_size](#property-elementpositionstripe_size)<br />
[ElementPosition.__init__(self)](#elementpositioninitself)<br />
[NetworkNode()](#networknode)<br />
[@Property: NetworkNode.isconnected](#property-networknodeisconnected)<br />
[NetworkNode.__init__(self, label, host, port)](#networknodeinitself-label-host-port)<br />
[NetworkNode.__refresh(self)](#networknode__refreshself)<br />
[NetworkNode.start(self)](#networknodestartself)<br />
[NetworkNode.stop(self)](#networknodestopself)<br />
[NetworkNodeList()](#networknodelist)<br />
[NetworkNodeList.__getitem__(self, index)](#networknodelistgetitemself-index)<br />
[NetworkNodeList.__init__(self)](#networknodelistinitself)<br />
[NetworkNodeList.__iter__(self)](#networknodelistiterself)<br />
[NetworkNodeList.__len__(self)](#networknodelistlenself)<br />
[NetworkNodeList.__next__(self)](#networknodelistnextself)<br />
[NetworkNodeList.__repr__(self)](#networknodelistreprself)<br />
[NetworkNodeList.__str__(self)](#networknodeliststrself)<br />
[NetworkNodeList.append(self, value)](#networknodelistappendself-value)<br />
[NetworkNodeList.items(self)](#networknodelistitemsself)<br />
[PingNetworkNode()](#pingnetworknode)<br />
[@Property: PingNetworkNode.host](#property-pingnetworknodehost)<br />
[@Property: PingNetworkNode.isconnected](#property-pingnetworknodeisconnected)<br />
[@Property: PingNetworkNode.port](#property-pingnetworknodeport)<br />
[PingNetworkNode.__init__(self, host, port)](#pingnetworknodeinitself-host-port)<br />
[PingNetworkNode.__ping(self)](#pingnetworknode__pingself)<br />
[PingNetworkNode.__socket(self)](#pingnetworknode__socketself)<br />
[PythonPing()](#pythonping)<br />
[PythonPing.__init__(self, inputfile)](#pythonpinginitself-inputfile)<br />
[PythonPing.run(self)](#pythonpingrunself)<br />
[ScreenCurses()](#screencurses)<br />
[ScreenCurses.__init__(self, host_list)](#screencursesinitself-host_list)<br />
[ScreenCurses.__refresh(self)](#screencurses__refreshself)<br />
[ScreenCurses.build(self)](#screencursesbuildself)<br />
[ScreenCurses.menubar(self)](#screencursesmenubarself)<br />
[ScreenCurses.run(self)](#screencursesrunself)<br />


#### ConfigYAML()
```python
class ConfigYAML(object):
```

```
This class manage YAML config file
```

##### @Property: ConfigYAML.config
```python
@property
def ConfigYAML.config(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: ConfigYAML.filename
```python
@property
def ConfigYAML.filename(self):
@filename.setter
def ConfigYAML.filename(self, filename):

```
> <br />
> @Property<br />
> <br />
##### ConfigYAML.__init__(self, filename)
```python
def ConfigYAML.__init__(self, filename):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### Counter()
```python
class Counter(object):
```

```
This class count from 0 to max_value.
In the end (max_value+1), the value becomes 0
```

##### @Property: Counter.value
```python
@property
def Counter.value(self):

```
> <br />
> @Property<br />
> <br />
##### Counter.__init__(self, max_value)
```python
def Counter.__init__(self, max_value):
```
> <br />
> Init current value and stores max_value<br />
> <br />
##### Counter.reset(self)
```python
def Counter.reset(self):
```
> <br />
> reset current value<br />
> <br />
#### ElementPosition()
```python
class ElementPosition(object):
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
```

##### @Property: ElementPosition.column
```python
@property
def ElementPosition.column(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: ElementPosition.current_id
```python
@property
def ElementPosition.current_id(self):
@current_id.setter
def ElementPosition.current_id(self, value):

```
> <br />
> @Property<br />
> <br />
##### @Property: ElementPosition.element_size
```python
@property
def ElementPosition.element_size(self):
@element_size.setter
def ElementPosition.element_size(self, value):

```
> <br />
> @Property<br />
> <br />
##### @Property: ElementPosition.ratio
```python
@property
def ElementPosition.ratio(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: ElementPosition.row
```python
@property
def ElementPosition.row(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: ElementPosition.stripe_size
```python
@property
def ElementPosition.stripe_size(self):
@stripe_size.setter
def ElementPosition.stripe_size(self, value):

```
> <br />
> @Property<br />
> <br />
##### ElementPosition.__init__(self)
```python
def ElementPosition.__init__(self):
```
> <br />
> Init default value and test<br />
> <br />
#### NetworkNode()
```python
class NetworkNode(object):
```

```
Docstring empty
```

##### @Property: NetworkNode.isconnected
```python
@property
def NetworkNode.isconnected(self):
@isconnected.setter
def NetworkNode.isconnected(self, value):

```
> <br />
> @Property<br />
> <br />
##### NetworkNode.__init__(self, label, host, port)
```python
def NetworkNode.__init__(self, label, host, port):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### NetworkNode.__refresh(self)
```python
def NetworkNode.__refresh(self):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNode.start(self)
```python
def NetworkNode.start(self):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNode.stop(self)
```python
def NetworkNode.stop(self):
```
> <br />
> Docstring empty<br />
> <br />
#### NetworkNodeList()
```python
class NetworkNodeList(object):
```

```
[] to store a python object's members (NetworkNode).
This object will become an attribute.
```

##### NetworkNodeList.__getitem__(self, index)
```python
def NetworkNodeList.__getitem__(self, index):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNodeList.__init__(self)
```python
def NetworkNodeList.__init__(self):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### NetworkNodeList.__iter__(self)
```python
def NetworkNodeList.__iter__(self):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNodeList.__len__(self)
```python
def NetworkNodeList.__len__(self):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNodeList.__next__(self)
```python
def NetworkNodeList.__next__(self):
```
> <br />
> Docstring empty<br />
> <br />
##### NetworkNodeList.__repr__(self)
```python
def NetworkNodeList.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### NetworkNodeList.__str__(self)
```python
def NetworkNodeList.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
##### NetworkNodeList.append(self, value)
```python
def NetworkNodeList.append(self, value):
```
> <br />
> add a member<br />
> <br />
##### NetworkNodeList.items(self)
```python
def NetworkNodeList.items(self):
```
> <br />
> get members<br />
> <br />
#### PingNetworkNode()
```python
class PingNetworkNode(object):
```

```
This class ping a network equipement
```

##### @Property: PingNetworkNode.host
```python
@property
def PingNetworkNode.host(self):
@host.setter
def PingNetworkNode.host(self, host):

```
> <br />
> @Property<br />
> <br />
##### @Property: PingNetworkNode.isconnected
```python
@property
def PingNetworkNode.isconnected(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: PingNetworkNode.port
```python
@property
def PingNetworkNode.port(self):
@port.setter
def PingNetworkNode.port(self, port):

```
> <br />
> @Property<br />
> <br />
##### PingNetworkNode.__init__(self, host, port)
```python
def PingNetworkNode.__init__(self, host, port):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### PingNetworkNode.__ping(self)
```python
def PingNetworkNode.__ping(self):
```
> <br />
> Docstring empty<br />
> <br />
##### PingNetworkNode.__socket(self)
```python
def PingNetworkNode.__socket(self):
```
> <br />
> Docstring empty<br />
> <br />
#### PythonPing()
```python
class PythonPing(object):
```

```
Docstring empty
```

##### PythonPing.__init__(self, inputfile)
```python
def PythonPing.__init__(self, inputfile):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### PythonPing.run(self)
```python
def PythonPing.run(self):
```
> <br />
> start screen <br />
> <br />
#### ScreenCurses()
```python
class ScreenCurses(object):
```

```
Docstring empty
```

##### ScreenCurses.__init__(self, host_list)
```python
def ScreenCurses.__init__(self, host_list):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### ScreenCurses.__refresh(self)
```python
def ScreenCurses.__refresh(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ScreenCurses.build(self)
```python
def ScreenCurses.build(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ScreenCurses.menubar(self)
```python
def ScreenCurses.menubar(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ScreenCurses.run(self)
```python
def ScreenCurses.run(self):
```
> <br />
> Docstring empty<br />
> <br />
