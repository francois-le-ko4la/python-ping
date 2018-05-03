#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from threading import Timer
import time
from pytping.position import ElementPosition
from pytping.counter import Counter


class Template:
    box_width = 30
    box_margin_x = 3
    box_margin_y = 1
    box_height = 4
    box_start_x = 5
    box_start_y = 5
    msg = "Press ESC to EXIT"
    progress = ['-', '\\', '|', '/']


class ScreenCurses(object):
    def __init__(self, host_list):
        self.__timer = ""
        self.__started = True
        self.__host_list = host_list
        self.__count = Counter(3)
        self.__elemnt_position = ElementPosition()
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
        #self.screen.nodelay(True)

    def menubar(self):
        box = self.screen.subwin(3, self.width, self.height - 3, 0)
        box.border()
        box.box()
        box.addstr(1, 2, Template.msg + " " +
                   Template.progress[self.__count.value])

    def __refresh(self):
        if self.__started:
            self.__timer = Timer(0.5, self.build)
            self.__timer.start()

    def build(self):
        if self.__started is not True:
            return

        self.height, self.width = self.screen.getmaxyx()

        self.__elemnt_position.stripe_size = self.width - 2
        self.__elemnt_position.element_size = Template.box_width + Template.box_margin_x
        self.screen.border(0)
        self.menubar()

        i = 0
        for host in self.__host_list:
            self.__elemnt_position.current_id = i
            try:
                box = self.screen.subwin(Template.box_height,
                                         Template.box_width,
                                         self.__elemnt_position.row *
                                         (Template.box_height + Template.box_margin_y) +
                                         Template.box_margin_y+1,
                                         self.__elemnt_position.column * (Template.box_width + Template.box_margin_x)+Template.box_margin_x)
            except Exception:
                return
            box.box()
            box.addstr("Ping")
            box.addstr(1, 2, host.label)
            box.addstr(2, 5, host.host)
            if host.isconnected:
                box.addstr(2, Template.box_width - 4,
                           "OK", curses.color_pair(4))
            else:
                box.addstr(2, Template.box_width - 4,
                           "KO", curses.color_pair(5))
            i = i + 1
        self.__refresh()

    def run(self):
        keypressevent = 0
        while keypressevent != 27:
            self.screen.erase()
            self.build()
            keypressevent = self.screen.getch()

        self.__started = False
        time.sleep(1)
        curses.endwin()
