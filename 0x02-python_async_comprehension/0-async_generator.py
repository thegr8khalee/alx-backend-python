#!/usr/bin/env python3
"""alx-backend-python"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Returns:
        AsyncGenerator[int, None]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
