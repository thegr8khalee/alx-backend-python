#!/usr/bin/env python3
"""alx-backend-python"""

from asyncio import Task, create_task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """_summary_

    Args:
        max_delay (int): _description_

    Returns:
        Task: _description_
    """
    task = create_task(wait_random(max_delay))
    return task
