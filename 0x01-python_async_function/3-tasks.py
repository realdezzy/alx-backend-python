#!/usr/bin/env python3
"""
Task Wait Random
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Task Wait Random

    Args:
        max_delay (int): maximum delay to wait for

    Returns:
        Asyncio task
    """
    return asyncio.ensure_future(wait_random())
