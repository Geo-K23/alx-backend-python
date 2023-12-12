#!/usr/bin/env python3
""" Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator coroutine that yields random numbers.

    This coroutine loops 10 times, asynchronously waiting 1 second on,
    each iteration, and then yields a random number between 0 and 10,
    using the random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
