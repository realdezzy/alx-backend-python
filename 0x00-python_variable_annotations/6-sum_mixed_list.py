#!/usr/bin/env python3
"""
    Sum Mixed Types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
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
