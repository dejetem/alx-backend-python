#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    write a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time_end = time.perf_counter() - start
    return total_time_end
