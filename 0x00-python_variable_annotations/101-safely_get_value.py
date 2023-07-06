#!/usr/bin/env python3
"""
    Safely get value
"""
from typing import Mapping, Union,TypeVar, Any


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None]= None) -> Union[Any, TypeVar]:
    """Safely get value

    Args:
        dct (Mapping): safe dict
        key (Any): any type
        default (Union[TypeVar, None], optional): default value. Defaults to None.

    Returns:
        Union[Any, TypeVar]: any
    """
    if key in dct:
        return dct[key]
    else:
        return default
