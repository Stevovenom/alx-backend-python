#!/usr/bin/env python3
"""
type-annoted function sum_mixed_list which takes a list mxd_lst of intergers
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns a sum of all numbers inside a list
    """
    return sum(mxd_lst)
