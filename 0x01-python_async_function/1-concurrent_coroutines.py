#!/usr/bin/env python3
"""
    Concurrent coroutines
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Calls wait_random n times and returns delay

    Args:
        n (int): Number of times wait_random is called
        max_delay (int): Max delay to wait for

    Returns:
        list[float]: list of all delay values
    """
    delay_array: list[float] = [await wait_random(max_delay) for _ in range(n)]

    return sorted(delay_array)
