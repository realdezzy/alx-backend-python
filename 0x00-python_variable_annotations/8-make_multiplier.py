#!/usr/bin/env python3
"""
    Multiplier maker
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Make_multiplier that takes a float multiplier as argument
        and returns a function(multiply) that multiplies a float by multiplier.
    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiply(n: float) -> float:
        return multiplier * n
    return multiply
