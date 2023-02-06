#!/usr/bin/env python3
"""
an asynchronous that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an int argument and wait for random delay and returns delay time
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
