#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as an argument
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
