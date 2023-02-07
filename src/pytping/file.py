#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Manage option file."""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple, Optional

import yaml

from pytping.__config__ import Config, ExitStatus

ConfigType = Optional[dict[str, dict[str, dict[str, str]]]]


class MyYAMLConfigFile(NamedTuple):
    r"""Describe a file with a NamedTuple.

    Notes:
        The objective is to define a file with only one NamedTuple.
        The NamedTuple will be created by the set_path function to
        define the path.

    Examples:
        >>> conf = MyYAMLConfigFile.set_path("lorem")
        >>> conf.status
        <ExitStatus.EX_OSFILE: 72>
        >>> conf.config is None
        True
        >>> import os
        >>> dirname = os.path.dirname(__file__)
        >>> file = f"{dirname}/../../sample/config.yml"
        >>> conf = MyYAMLConfigFile.set_path(file)
        >>> conf.status
        <ExitStatus.EX_OK: 0>
        >>> for index, node in enumerate(conf.config["nodes"]):
        ...     print(node)
        ...     print(conf.config["nodes"][node])
        Internet(80)
        {'host': 'www.google.fr', 'port': 80}
        Google IPV6(ICMP)
        {'host': '2001:4860:4860::8888', 'port': 'ICMP'}
        Google IPV6(53)
        {'host': '2001:4860:4860::8888', 'port': 53}
        ESX1(22)
        {'host': '192.168.1.230', 'port': 22}
        ESX2(ICMP)
        {'host': '192.168.1.240', 'port': 'ICMP'}

    """

    path: Optional[Path]
    exists: bool
    status: ExitStatus
    config: ConfigType

    @classmethod
    def set_path(cls, path: Optional[str]) -> MyYAMLConfigFile:
        """Set path and create the object.

        if path is None        -> status = ExitStatus.EX_CANTCREAT
        if path exists         -> status = ExitStatus.EX_OK
        If path does not exist -> status = ExitStatus.EX_OSFILE
        if yaml is not valid   -> status = ExitStatus.EX_CONFIG

        Args:
            path: The file's path.

        Returns:
            MyYAMLConfigFile or None

        """
        if path is None:
            return cls(path=None, exists=False,
                       status=ExitStatus.EX_CANTCREAT, config=None)
        _exists: bool = Path(path).exists()
        _config: ConfigType = yaml.safe_load(
            Path(path).read_text(encoding=Config.ENCODING.value)) \
            if _exists else None
        _status: ExitStatus = ExitStatus.EX_OSFILE if not _exists \
            else ExitStatus.EX_CONFIG \
            if _config is not None and "nodes" not in _config.keys() \
            else ExitStatus.EX_OK
        return cls(
            path=Path(path), exists=_exists, status=_status, config=_config)

    def __repr__(self) -> str:
        """Get the repr."""
        _repr: str = f"path={repr(self.path)}, exists={self.exists}, status" \
                     f"={self.status}"
        return f'{self.__class__.__name__}({_repr})'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
