#!/usr/bin/env python3
"""
    Safe first element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safe first element

    Args:
        lst (Sequence[Any]): param of sequence type

    Returns:
        Union[Any, None]: Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
