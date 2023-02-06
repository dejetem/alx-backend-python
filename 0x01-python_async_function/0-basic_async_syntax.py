#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an int argument and wait for random delay and returns delay time
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

