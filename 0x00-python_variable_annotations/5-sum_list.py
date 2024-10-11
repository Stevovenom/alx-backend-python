#!/usr/bin/env python3
"""
type-annoted function sum_list which takes input_list of float as argument
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list (float): lists of floats as arguments
    Returns:
        float: the sum
    """
    return (sum(input_list))
