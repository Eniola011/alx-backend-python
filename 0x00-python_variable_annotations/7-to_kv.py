#!/usr/bin/env python3
"""
  to_kv annotated function
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: The first element of the tuple is the string k.
            v: The second element is the square of the int/float v.
        Return:
            Tuple.
    """
    return (k, v * v)
