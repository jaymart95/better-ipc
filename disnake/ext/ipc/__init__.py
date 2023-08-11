"""
Better IPC
~~~~~~~~~~

High-performance inter-process communication 
library designed to work with the latest version of disnake.py

:copyright: (C) 2022 DaPandaOfficial
:license: GNU GENERAL PUBLIC LICENSE
"""
import disnake

__title__ = "better-ipc"
__author__ = "DaPandaOfficial"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__copyright__ = "Copyright (C) 2023 DaPandaOfficial"
__version__ = "2.0.3"


from .errors import BaseException, NoEndpointFound, MulticastFailure, InvalidReturn, ServerAlreadyStarted
from .client import Client
from .server import Server
from .objects import ClientPayload, ServerResponse


