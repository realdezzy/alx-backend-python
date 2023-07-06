#!/usr/bin/env python3
"""
    Typed Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Returns a tuple containing string k and square of v

    Args:
        k (str): string param
        v (Union[int, float]): integer or float param

    Returns:
        Tuple[str, float]: string k and square of v
    """
    return (k, v ** 2)
