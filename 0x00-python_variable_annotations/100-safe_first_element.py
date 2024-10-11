#!/usr/bin/env python3
"""
augmenting teh given code  with the correct duck-typed annotation
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element of a sequence or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
