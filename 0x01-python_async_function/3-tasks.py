#!/usr/bin/env python3
"""
Task Wait Random
"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Task Wait Random

    Args:
        max_delay (int): maximum delay to wait for

    Returns:
        Asyncio task
    """
    return create_task(wait_random(max_delay))
