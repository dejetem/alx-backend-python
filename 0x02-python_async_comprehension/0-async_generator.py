#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously wait 1 second
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    async generator loop 10 times, each time asynchronously wait 1 second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
