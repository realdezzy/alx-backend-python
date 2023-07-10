#!/usr/bin/env python3
"""
Measure time
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure time

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: Average time
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start

    return end / n
