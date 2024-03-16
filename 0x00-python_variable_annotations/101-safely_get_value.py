#!/usr/bin/env python3
"""
  Add Type-Annotation
"""


from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
        Returns the value associated with the given key in the dictionary
        if it exists,
        Otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
