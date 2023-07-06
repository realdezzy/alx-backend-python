#!/usr/bin/env python3
"""
    Sum Mixed Types
"""


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    """
        Returns the sum of both integers and floats in the list

    Args:
        mxd_lst (list[int, float]): list containing integers and floats

    Returns:
        float: sum of elements in mxd_lst
    """
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum