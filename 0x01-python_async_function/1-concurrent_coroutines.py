#!/usr/bin/env python3
"""
    Concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls wait_random n times and returns delay

    Args:
        n (int): Number of times wait_random is called
        max_delay (int): Max delay to wait for

    Returns:
        list[float]: list of all delay values
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
