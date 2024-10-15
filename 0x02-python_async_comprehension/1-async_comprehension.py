#!/usr/bin/env python3
"""alx-backend-python"""

async_generator = __import__("0-async_generator").async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: _description_
    """
    return [i async for i in async_generator()]
