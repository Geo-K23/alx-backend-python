#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between,
    0 and max_delay seconds.

    Parameters:
    - max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
    - float: The random delay.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time