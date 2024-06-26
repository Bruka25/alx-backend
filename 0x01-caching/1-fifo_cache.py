#!/usr/bin/env python3
""" Module for First-In First-Out caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        # Use OrderedDict to maintain the order of insertion
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key associated with the item to store.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        # Add item to the cache
        self.cache_data[key] = item
        # Check if the cache exceeds the max limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item inserted (FIFO)
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
            does not exist in the cache.
        """
        return self.cache_data.get(key, None)
