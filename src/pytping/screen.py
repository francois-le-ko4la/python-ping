#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Manage the screen."""

from __future__ import annotations

import curses
from collections import deque
from dataclasses import dataclass, field

from pytping.__about__ import __pkg_name__, __version__
from pytping.__config__ import Config
from pytping.multithreading import MultiThread
from pytping.netnode import NetworkNode


@dataclass
class ProgressIndicator:
    r"""Define a progress indicator.

    This class return the next elem each time we call get_value.
    We rotate a deque to get a circular effect.

    +-----+    +-----+    +-----+           +-------+
    |  0  | -> |  1  | -> |  2  | -> ... -> |  max  |
    +-----+    +-----+    +-----+           +-------+
      ^                                         |
      |                                         |
      +-----------------------------------------+

    Use:
        >>> a = ProgressIndicator()
        >>> for i in range(4):
        ...     print(a.get_value())
        -
        \
        |
        /
    """

    circular_anim: deque[str] = field(default_factory=deque)

    def __post_init__(self) -> None:
        """Define default value after obj creation."""
        self.circular_anim = Config.PROGRESS.value
        self.circular_anim.rotate(1)

    def get_value(self) -> str:
        """Rotate and get the current value."""
        self.circular_anim.rotate(-1)
        return self.circular_anim[0]


@dataclass
class ScreenPosition:
    """Define an element location."""

    y: int = 0
    x: int = 0


@dataclass
class ElemSize:
    """Define an element size."""

    height: int = 0
    width: int = 0


@dataclass
class ViewString(ScreenPosition):
    """Define a string."""

    ch: str = ""

    def get_tuple(self) -> tuple[int, int, str]:
        """Get tuple to use it in curse function."""
        return self.y, self.x, self.ch


@dataclass
class ViewBoxNetworkNode(ScreenPosition, ElemSize):
    """Define a box to print a network node."""

    def __post_init__(self) -> None:
        """Define default value after obj creation."""
        self.width, self.height = (Config.BOX_WIDTH.value,
                                   Config.BOX_HEIGHT.value)

    def set_pos_yx(self, cur_width: int, cur_id: int) -> None:
        """Get real position."""
        elem_size = Config.BOX_WIDTH.value + Config.BOX_MARGIN_X.value
        cur_ratio = int(cur_width / elem_size) if cur_width >= elem_size else 1
        row = int(cur_id / cur_ratio)
        column = cur_id - (row * cur_ratio)
        self.x = (column * (Config.BOX_WIDTH.value + Config.BOX_MARGIN_X.value)
                  + Config.BOX_MARGIN_X.value)
        self.y = (row * (Config.BOX_HEIGHT.value + Config.BOX_MARGIN_Y.value)
                  + Config.BOX_MARGIN_Y.value + 1)

    def get_tuple(self) -> tuple[int, int, int, int]:
        """Get tuple to use it in curse function."""
        return self.height, self.width, self.y, self.x


class ViewNetworkNode(NetworkNode):
    """Define a network node.

    - label (netnode.NetworkNode)
    - host (netnode.NetworkNode)
    - port (netnode.NetworkNode)

    use:
        >>> node = ViewNetworkNode(0, "Google", "www.google.fr", 80)
        >>> node.refresh()
        >>> node.refresh_view(78)
        >>> node.view_box
        ViewBoxNetworkNode(height=4, width=30, y=2, x=3)
        >>> node.view_box.get_tuple()
        (4, 30, 2, 3)
        >>> node.view_label
        ViewString(y=1, x=2, ch='Google')
        >>> node.view_name
        ViewString(y=2, x=5, ch='www.google.fr')
        >>> node.stop()
    """

    view_box: ViewBoxNetworkNode = ViewBoxNetworkNode()
    view_label: ViewString = ViewString(y=1, x=2, ch="")
    view_name: ViewString = ViewString(y=2, x=5, ch="")
    view_rtt: ViewString = ViewString(y=1, x=1, ch="")

    def refresh_view(self, screen_width: int) -> None:
        """Refresh the view."""
        self.view_box.set_pos_yx(screen_width, self.id)
        self.view_label.ch = self.label
        self.view_name.ch = self.host
        self.view_rtt.ch = f"{self.rtt:>6.2f} ms"
        self.view_rtt.x = (Config.BOX_WIDTH.value
                           - len(self.view_rtt.ch) - 2)


class ScreenCurses:
    """Manage the screen.

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

    """

    def __init__(self, host_list: deque[ViewNetworkNode]) -> None:
        """Init the Screen."""
        self.__host_list = host_list
        self.__count = ProgressIndicator()
        self.__mthr = MultiThread(Config.REFRESH_SCREEN.value, self.build)
        self.screen = curses.initscr()
        self.screen.immedok(True)
        self.height, self.width = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.screen.keypad(True)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.curs_set(0)

    def menubar(self) -> None:
        """Draw the bar.

        Returns:
            None
        """
        box = self.screen.subwin(3, self.width, self.height - 3, 0)
        box.border()
        box.box()
        txt = f"{__pkg_name__}({__version__}) | {Config.MSG.value}"
        txt = f"{txt} {self.__count.get_value()}"
        box.addstr(1, 2, txt)

    def build(self) -> None:
        """Build the screen.

        Returns:
            None
        """
        self.height, self.width = self.screen.getmaxyx()
        self.screen.border(0)
        self.menubar()

        for host in self.__host_list:
            host.refresh_view(self.width)
            try:
                box = self.screen.subwin(*host.view_box.get_tuple())
            except curses.error:
                return

            box.box()
            box.addstr(0, 0, Config.BOX_LABEL.value)
            box.addstr(*host.view_label.get_tuple())
            box.addstr(*host.view_rtt.get_tuple())
            box.addstr(*host.view_name.get_tuple())
            if host.connected:
                box.addstr(2, Config.BOX_WIDTH.value - 4,
                           Config.NODE_STATUS_OK.value, curses.color_pair(4))
            else:
                box.addstr(2, Config.BOX_WIDTH.value - 4,
                           Config.NODE_STATUS_KO.value, curses.color_pair(5))

    def run(self) -> None:
        """Run Curses loop.

        Returns:
            None
        """
        keypressevent = 0
        self.__mthr.start()

        while keypressevent != 27:
            self.screen.erase()
            self.build()
            keypressevent = self.screen.getch()

        self.__mthr.stop()
        curses.endwin()
