#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define config."""

from __future__ import annotations

import os
from collections import deque
from enum import Enum, IntEnum, unique

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")


@unique
class ExitStatus(IntEnum):
    """Define Exit status."""

    EX_OK: int = getattr(os, 'EX_OK', 0)
    EX_OSFILE: int = getattr(os, 'EX_OSFILE', 72)
    EX_CANTCREAT: int = getattr(os, 'EX_CANTCREAT', 73)
    EX_IOERR: int = getattr(os, 'EX_IOERR', 74)
    EX_CONFIG: int = getattr(os, 'EX_CONFIG', 78)


class Config(Enum):
    """Define constants."""

    TIMEOUT: float = 0.5
    REFRESH: float = 0.8
    REFRESH_SCREEN: float = 0.5
    ICMP: str = "ICMP"
    PING_CMD: str = "ping -c 1 -W 1"
    PING6_MAC_CMD: str = "ping6 -c 1"
    BOX_LABEL: str = "Ping"
    BOX_WIDTH: int = 30
    BOX_MARGIN_X: int = 3
    BOX_MARGIN_Y: int = 1
    BOX_HEIGHT: int = 4
    BOX_START_X: int = 5
    BOX_START_Y: int = 5
    NODE_STATUS_OK: str = "OK"
    NODE_STATUS_KO: str = "KO"
    MSG: str = "Press ESC to EXIT"
    PROGRESS: deque[str] = deque(r'-\|/')
    DESCRIPTION: str = "Ping tool..."
    ENCODING: str = "UTF-8"


class PytPingError(Exception):
    """Define generic exception for pytping."""


class PytPingPortConfigError(PytPingError):
    """Define error: the port is not validated."""

    def __init__(self, port: str) -> None:
        """Init the class."""
        super().__init__(f"Port '{port}' not valid!")


class PytPingHostConfigError(PytPingError):
    """Define error: the host is not validated."""

    def __init__(self, host: str) -> None:
        """Init the class."""
        super().__init__(f"Host '{host}' not valid!")
