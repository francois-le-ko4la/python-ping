#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Define pyping."""

from __future__ import annotations

from collections import deque

from pytping.__config__ import ExitStatus
from pytping.file import MyYAMLConfigFile
from pytping.screen import ScreenCurses, ViewNetworkNode


class PythonPing:
    """Main class.

    - Use YAML config file
    - Create NetworkNode deque()
    - Launch the screen manager
    """

    config_file: MyYAMLConfigFile

    def __init__(self, input_file: str) -> None:
        """Init the class.

        - get config
        - build the node list
        - build the screen

        Returns:
            None.

        """
        config_file = MyYAMLConfigFile.set_path(input_file)
        self.__host_list = deque([
            ViewNetworkNode(index,
                            node,
                            config_file.config["nodes"][node]["host"],
                            config_file.config["nodes"][node]["port"])
            for index, node in enumerate(config_file.config["nodes"])
            if (isinstance(config_file.config["nodes"][node], dict) and
                {"host", "port"} <= config_file.config["nodes"][node].keys())
            ]) if (config_file.status is ExitStatus.EX_OK
                   and config_file.config is not None
                   and "nodes" in config_file.config.keys()) else None

        if self.__host_list is None:
            return

        self.__screen = ScreenCurses(self.__host_list)

    def run(self) -> None:
        """Start curses screen.

        User can stop this app with [ESC] key.
        In the end stop all process.

        Returns:
            None.
        """
        if self.__host_list is None:
            return
        self.__screen.run()
        # EXIT
        for host in self.__host_list:
            host.stop()
