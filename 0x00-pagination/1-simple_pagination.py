#!/usr/bin/env python3
""" Module for Simple pagination"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
        end index (exclusive).
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset. Loads data from CSV if not already loaded.

        Returns:
            List[List]: The dataset, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data from the dataset.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of rows for the requested page.
        """
        # Validate inputs
        assert type(page) == int and type(page_size) == int,
        assert page > 0 and page_size > 0,

        # Get the start and end indices for the requested page
        start, end = index_range(page, page_size)

        # Load the dataset
        data = self.dataset()

        # If start index exceeds data length, return empty list
        if start >= len(data):
            return []

        # Return the slice of data for the requested page
        return data[start:end]
