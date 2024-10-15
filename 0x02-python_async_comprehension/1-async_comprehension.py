#!/usr/bin/env python3
"""
importation of async_generator from task 0 and writing a couritine called
async_comprehension that takes no argument
"""

from typing import List
import random
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension

    Returns:
        List[float]: list containing 10 random numbers
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]
