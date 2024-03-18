#!/usr/bin/env python3
"""
Measure The Runtime
"""


import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """ Measure_Runtime """
    start_time = time.perf_counter()
    asyncio.run (wait_n(n, max_delay))
    end_time = time.perf_counter() - start_time
    total_time = end_time / n
    return total_time
