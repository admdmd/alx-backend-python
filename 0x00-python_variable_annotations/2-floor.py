#!/usr/bin/env python3
""" 2. Basic annotations - floor operation
"""


def floor(n: float) -> int:
    """ Returns floor of number
    """
    return int(n) if n >= 0 else int(n) - 1
