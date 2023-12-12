#!/usr/bin/env python3
""" Async comprehensions
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that uses async comprehensions,
    to collect 10 random numbers.
    """
    return [num async for num in async_generator()]
