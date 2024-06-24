#!/usr/bin/env python3
"""Pagination helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
        end index (exclusive).
    """
    # Calculate the start index for the items on the current page.
    # The start index is determined by subtracting 1 from the page number and then
    # multiplying by the page size. This is because page numbering typically starts at 1,
    # but indexing in programming starts at 0.
    start = (page - 1) * page_size

    # Calculate the end index for the items on the current page.
    # The end index is the start index plus the page size.
    end = start + page_size

    # Return a tuple of the start and end indices.
    return (start, end)
