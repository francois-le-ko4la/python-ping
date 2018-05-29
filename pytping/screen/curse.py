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
from pytping.util.__about__ import __pkg_name__, __version__
from pytping.util import TEMPLATE, DEFAULT
from pytping.screen.location import ElementLocation
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
        self.__count = Counter(len(TEMPLATE["progress"]) - 1)
        self.__elemnt_position = ElementLocation()
        self.__mthr = PThread(self.build, DEFAULT["refresh_screen"])
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
            TEMPLATE["msg"],
            TEMPLATE["progress"][self.__count.value]
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

        self.__elemnt_position.stripe_size = self.width - 2
        self.__elemnt_position.element_size = TEMPLATE["box_width"] + \
            TEMPLATE["box_margin_x"]
        self.screen.border(0)
        self.menubar()

        for i, host in enumerate(self.__host_list):
            self.__elemnt_position.current_id = i

            pos_x = self.__elemnt_position.column * \
                (TEMPLATE["box_width"] + TEMPLATE["box_margin_x"]) + \
                TEMPLATE["box_margin_x"]
            pos_y = self.__elemnt_position.row * \
                (TEMPLATE["box_height"] + TEMPLATE["box_margin_y"]) + \
                TEMPLATE["box_margin_y"] + 1

            try:
                box = self.screen.subwin(
                    TEMPLATE["box_height"],
                    TEMPLATE["box_width"],
                    pos_y,
                    pos_x
                )

            except Exception:
                return
            box.box()
            box.addstr(TEMPLATE["box_label"])
            box.addstr(1, 2, host.label)
            box.addstr(1, TEMPLATE["box_width"] - len("  " + host.rtt) - 2,
                       "  " + host.rtt)
            box.addstr(2, 5, host.host)
            if host.isconnected:
                box.addstr(2, TEMPLATE["box_width"] - 4,
                           TEMPLATE["node_ok"], curses.color_pair(4))
            else:
                box.addstr(2, TEMPLATE["box_width"] - 4,
                           TEMPLATE["node_ko"], curses.color_pair(5))

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