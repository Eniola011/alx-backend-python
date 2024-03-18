#!/usr/bin/env python3
"""
Create A Async Function
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Task_Wait_Random """
    task = asyncio.create_task(wait_random(max_delay))

    return task
