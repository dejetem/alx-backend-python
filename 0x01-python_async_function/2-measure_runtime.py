#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import random
from time import perf_counter


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): times
        max_delay (int): dalay max number
    """
    counter = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = perf_counter() - counter
    return
