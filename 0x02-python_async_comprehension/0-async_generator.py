#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments
"""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
