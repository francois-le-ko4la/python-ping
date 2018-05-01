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
[CalcLimit()](#calclimit)<br />
[@Property: CalcLimit.column](#property-calclimitcolumn)<br />
[@Property: CalcLimit.current_id](#property-calclimitcurrent_id)<br />
[@Property: CalcLimit.element_size](#property-calclimitelement_size)<br />
[@Property: CalcLimit.ratio](#property-calclimitratio)<br />
[@Property: CalcLimit.row](#property-calclimitrow)<br />
[@Property: CalcLimit.stripe_size](#property-calclimitstripe_size)<br />
[CalcLimit.__init__(self, stripe_size, element_size)](#calclimitinitself-stripe_size-element_size)<br />
[ConfigYAML()](#configyaml)<br />
[@Property: ConfigYAML.config](#property-configyamlconfig)<br />
[@Property: ConfigYAML.filename](#property-configyamlfilename)<br />
[ConfigYAML.__init__(self, filename)](#configyamlinitself-filename)<br />
[Counter()](#counter)<br />
[@Property: Counter.value](#property-countervalue)<br />
[Counter.__init__(self, max_value)](#counterinitself-max_value)<br />
[Counter.reset(self)](#counterresetself)<br />
[NetworkNode()](#networknode)<br />
[@Property: NetworkNode.isconnected](#property-networknodeisconnected)<br />
[NetworkNode.__init__(self, label, host, port=False)](#networknodeinitself-label-host-portfalse)<br />
[NetworkNode.__refresh(self)](#networknode__refreshself)<br />
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
[PingNetworkNode.__init__(self, host)](#pingnetworknodeinitself-host)<br />
[PythonPing()](#pythonping)<br />
[PythonPing.__init__(self, inputfile)](#pythonpinginitself-inputfile)<br />
[PythonPing.run(self)](#pythonpingrunself)<br />
[ScreenCurses()](#screencurses)<br />
[ScreenCurses.__init__(self, host_list)](#screencursesinitself-host_list)<br />
[ScreenCurses.__refresh(self)](#screencurses__refreshself)<br />
[ScreenCurses.build(self)](#screencursesbuildself)<br />
[ScreenCurses.menubar(self)](#screencursesmenubarself)<br />
[ScreenCurses.run(self)](#screencursesrunself)<br />


#### CalcLimit()
```python
class CalcLimit(object):
```
> <br />
> Calc element location according to element stripe size and<br />
> stripe size.<br />
> <br />
##### @Property: CalcLimit.column
```python
@property
def CalcLimit.column(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: CalcLimit.current_id
```python
@property
def CalcLimit.current_id(self):
@current_id.setter
def CalcLimit.current_id(self, value):

```
> <br />
> @Property<br />
> <br />
##### @Property: CalcLimit.element_size
```python
@property
def CalcLimit.element_size(self):
@element_size.setter
def CalcLimit.element_size(self, value):

```
> <br />
> @Property<br />
> <br />
##### @Property: CalcLimit.ratio
```python
@property
def CalcLimit.ratio(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: CalcLimit.row
```python
@property
def CalcLimit.row(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: CalcLimit.stripe_size
```python
@property
def CalcLimit.stripe_size(self):
@stripe_size.setter
def CalcLimit.stripe_size(self, value):

```
> <br />
> @Property<br />
> <br />
##### CalcLimit.__init__(self, stripe_size, element_size)
```python
def CalcLimit.__init__(self, stripe_size, element_size):
```
> <br />
> Init default value and test<br />
> <br />
#### ConfigYAML()
```python
class ConfigYAML(object):
```
> <br />
> This class manage YAML config file<br />
> <br />
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
> <br />
> This class count from 0 to max_value.<br />
> In the end (max_value+1), the value becomes 0<br />
> <br />
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
#### NetworkNode()
```python
class NetworkNode(object):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
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
##### NetworkNode.__init__(self, label, host, port=False)
```python
def NetworkNode.__init__(self, label, host, port=False):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### NetworkNode.__refresh(self)
```python
def NetworkNode.__refresh(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
##### NetworkNode.stop(self)
```python
def NetworkNode.stop(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
#### NetworkNodeList()
```python
class NetworkNodeList(object):
```
> <br />
> [] to store a python object's members (NetworkNode).<br />
> This object will become an attribute.<br />
> <br />
##### NetworkNodeList.__getitem__(self, index)
```python
def NetworkNodeList.__getitem__(self, index):
```
> <br />
> <b>- docstring empty -</b><br />
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
> <b>- docstring empty -</b><br />
> <br />
##### NetworkNodeList.__len__(self)
```python
def NetworkNodeList.__len__(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
##### NetworkNodeList.__next__(self)
```python
def NetworkNodeList.__next__(self):
```
> <br />
> <b>- docstring empty -</b><br />
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
> <br />
> This class ping a network equipement<br />
> <br />
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
##### PingNetworkNode.__init__(self, host)
```python
def PingNetworkNode.__init__(self, host):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### PythonPing()
```python
class PythonPing(object):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
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
> <br />
> <b>- docstring empty -</b><br />
> <br />
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
> <b>- docstring empty -</b><br />
> <br />
##### ScreenCurses.build(self)
```python
def ScreenCurses.build(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
##### ScreenCurses.menubar(self)
```python
def ScreenCurses.menubar(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
##### ScreenCurses.run(self)
```python
def ScreenCurses.run(self):
```
> <br />
> <b>- docstring empty -</b><br />
> <br />
