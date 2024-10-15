#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields a random float between 0 and
    10 after a 1 second delay for a total of 10 iterations

    Returns:
        Generator: Asynchronous generator object that can be used in an
        awaitable context.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
