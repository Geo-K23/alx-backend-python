#!/usr/bin/env python3
""" Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function

    Parameters:
    - multiplier (float): The multiplier value.
    """
    return lambda x: x * multiplier
