#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes, invalid-name
"""Define a network node."""

import ipaddress
import platform
import socket
import subprocess
import time
from dataclasses import dataclass
from typing import Optional, Union

from pytping.__config__ import Config
from pytping.multithreading import MultiThread


@dataclass
class NetworkNode:
    """Define a network node.

    Host can be defined with a hostname or IP address.
    If port = ICMP then we use ping command.
    Else, we use socket API.

        >>> node = NetworkNode(0, "Google", "www.google.fr", 80)
        >>> node.refresh()
        >>> node.connected
        True
        >>> node.stop()
        >>> node = NetworkNode(0, "localhost", "localhost", "ICMP")
        >>> node.refresh()
        >>> node.connected
        True
        >>> node.stop()
        >>> node = NetworkNode(0, "unknown", "10.10.9.1", "ICMP")
        >>> node.refresh()
        >>> node.connected
        False
        >>> node.stop()

    """

    id: int
    label: str
    host: str
    port: Union[int, str]
    ip_address: Union[
        ipaddress.IPv4Address, ipaddress.IPv6Address, None] = None
    connected: bool = False
    rtt: float = 0
    mthr: Optional[MultiThread] = None

    def __post_init__(self) -> None:
        """Manage multithreading after obj creation."""
        try:
            self.ip_address = ipaddress.ip_address(self.host)
        except ValueError:
            self.ip_address = ipaddress.ip_address(
                socket.gethostbyname(self.host))
        self.start()

    def refresh(self) -> None:
        """Refresh the node.

        Returns:
            None.
        """
        self.connected, self.rtt = self.__ping() \
            if isinstance(self.port, str) and Config.ICMP.value in self.port \
            else self.__socket()

    def __socket(self) -> tuple[bool, float]:
        try:
            af_inet = socket.AF_INET \
                if isinstance(self.ip_address, ipaddress.IPv4Address) \
                else socket.AF_INET6
            sock = socket.socket(af_inet, socket.SOCK_STREAM)
            sock.settimeout(Config.TIMEOUT.value)
            start = time.time()
            result = (sock.connect_ex((str(self.ip_address), self.port)) == 0)
            rtt = int(100000 * (time.time() - start)) / 100
        except TimeoutError:
            return False, 0
        return result, rtt

    def __ping(self) -> tuple[bool, float]:
        try:
            cmd = Config.PING6_MAC_CMD.value \
                if (platform.system() == 'Darwin'
                    and isinstance(self.ip_address, ipaddress.IPv6Address)) \
                else Config.PING_CMD.value
            with subprocess.Popen(f"{cmd} {str(self.ip_address)}",
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE) as proc:
                proc.wait()
                rtt = float(proc.stdout.read().decode(
                    "utf-8").split("=")[-1].split("/")[1] \
                    if proc.stdout is not None else "0")
                # rtt = rtt.decode("utf-8").split("=")[-1].split("/")[1]
                return True, rtt
        except IndexError:
            return False, 0

    def start(self) -> None:
        """Start multithreading."""
        if self.mthr is None:
            self.mthr = MultiThread(self.refresh, Config.REFRESH.value)
            self.mthr.start()

    def stop(self) -> None:
        """Stop multithreading."""
        if self.mthr is not None:
            self.mthr.stop()
