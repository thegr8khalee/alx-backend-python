#!/usr/bin/env python3
"""alx-backend-python"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    before = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - before) / n
