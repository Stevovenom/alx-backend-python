#!/usr/bin/env python3
"""
the use of TypeVar to specify that teh  type of the return  depends on the
default parameter.
"""


from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary or returns default value."""
    if key in dct:
        return dct[key]
    else:
        return defiault
