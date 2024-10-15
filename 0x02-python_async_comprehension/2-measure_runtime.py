#!/usr/bin/env python3
"""
importation of async_comprehension from the previous file and writing a
measure_routime coroutine
"""

import random
import asyncio
from importlib import import_module as using
from typing import List
import time

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of four parallel async comprehensions.

    Returns:
        float: Total runtime for executing async_comprehension four times.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()
    return end_time - start_time
