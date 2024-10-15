#!/usr/bin/env python3
"""alx-backend-python"""

async_comprehension = __import__("1-async_comprehension").async_comprehension
import asyncio
from time import time


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
