#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #    #  ######     #     ####
 #    #  #    #  ##   #  #          #    #    #
 #       #    #  # #  #  #####      #    #
 #       #    #  #  # #  #          #    #  ###
 #    #  #    #  #   ##  #          #    #    #
  ####    ####   #    #  #          #     ####

"""


DEFAULT = {
    "timeout": 0.5,
    "refresh": 0.8,
    "refresh_screen": 0.8,
    "ICMP": "ICMP",
    "ping_cmd": "ping -c 1 -w 1 "
}

TEMPLATE = {
    "box_label": "Ping",
    "box_width": 30,
    "box_margin_x": 3,
    "box_margin_y": 1,
    "box_height": 4,
    "box_start_x": 5,
    "box_start_y": 5,
    "node_ok": "OK",
    "node_ko": "KO",
    "msg": "Press ESC to EXIT",
    "progress": ['-', '\\', '|', '/'],
}

__script__ = 'bin/pyt-ping.py'
__script_description__ = "Ping tool..."