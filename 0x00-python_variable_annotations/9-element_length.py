#!/usr/bin/env python3
"""
  Element_Length Annotated Function
"""


from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Annotate the below function’s parameters.
        Return: values with the appropriate types.
    """
    return [(i, len(i)) for i in lst]
