#!/usr/bin/env python3
"""
  Make_Multiplier Annotated Function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Return:
            A function that multiplies a float by multiplier.
    """

    def multi_function(x: float) -> float:
        """ multiplier """
        return x * multiplier

    return multi_function
