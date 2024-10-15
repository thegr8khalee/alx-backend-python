#!/usr/bin/env python3
"""alx-backend-python"""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """_summary_

    Returns:
        AsyncGenerator[int, None]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random(0, 10)
