#!/usr/bin/env python3
"""
Measure Time
"""
import asyncio
from time import perf_counter

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime for four coroutines

    Returns:
        float: Total runtime
    """
    async_comps = [async_comprehension(), async_comprehension(),
                   async_comprehension(), async_comprehension()]
    start = perf_counter()
    await asyncio.gather(*async_comps)
    time_taken = perf_counter() - start

    return time_taken
