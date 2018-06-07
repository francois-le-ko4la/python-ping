#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #####   ######  ######  #    #
 #       #    #  #    #  #       #       ##   #
  ####   #       #    #  #####   #####   # #  #
      #  #       #####   #       #       #  # #
 #    #  #    #  #   #   #       #       #   ##
  ####    ####   #    #  ######  ######  #    #

export NCURSES_NO_UTF8_ACS=1
"""

import curses
from pythread import PThread
from pytping import CONFIG
from pytping.util import __pkg_name__, __version__
from pytping.screen.counter import Counter


class ScreenCurses(object):
    """
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

    """
    def __init__(self, host_list):
        self.__timer = ""
        self.__host_list = host_list
        self.__count = Counter(len(CONFIG.progress) - 1)
        self.__mthr = PThread(self.build, CONFIG.refresh_screen)
        self.screen = curses.initscr()
        self.screen.immedok(True)
        self.height, self.width = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.screen.keypad(1)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.curs_set(0)

    def menubar(self):
        """
        draw the bar

        Args:
            None

        Returns:
            None
        """
        box = self.screen.subwin(3, self.width, self.height - 3, 0)
        box.border()
        box.box()
        txt = "{}({}) | {} {}".format(
            __pkg_name__,
            __version__,
            CONFIG.msg,
            CONFIG.progress[self.__count.value]
        )
        box.addstr(1, 2, txt)

    def build(self):
        """
        Build the screen

        Args:
            None

        Returns:
            None
        """
        self.height, self.width = self.screen.getmaxyx()
        self.screen.border(0)
        self.menubar()

        for i, host in enumerate(self.__host_list):

            try:
                box = self.screen.subwin(
                    *host.get_nodesubwin(self.width, i)
                )

            except Exception:
                return
            box.box()
            box.addstr(0, 0, CONFIG.box["label"])
            box.addstr(*host.get_nodelabel())
            box.addstr(*host.get_nodertt())
            box.addstr(*host.get_nodename())
            if host.isconnected:
                box.addstr(2, CONFIG.box["width"] - 4,
                           CONFIG.node["ok"], curses.color_pair(4))
            else:
                box.addstr(2, CONFIG.box["width"] - 4,
                           CONFIG.node["ko"], curses.color_pair(5))

    def run(self):
        """
        Curses getch loop

        Args:
            None

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
