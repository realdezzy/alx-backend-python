#!/usr/bin/env python3
"""
    Float Sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats

    Args:
        input_list (list[float]): list of floats

    Returns:
        float: value of sum_list
    """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
