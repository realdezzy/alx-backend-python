#!/usr/bin/env python3
"""
    Float Sum
"""


def sum_list(input_list: list[float]) -> float:
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
