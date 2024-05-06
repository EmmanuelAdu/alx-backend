#!/usr/bin/env python3
'''Simple Helper functions'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Retrieves the index range and page size'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
