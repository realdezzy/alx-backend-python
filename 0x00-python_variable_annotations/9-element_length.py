#!/usr/bin/env python3
"""
    Element length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Return the element length

    Args:
        lst (Iterable[Sequence]): iterable sequence

    Returns:
        List[Tuple[Sequence, int]]: list of elements
    """
    return [(i, len(i)) for i in lst]
