#!/usr/bin/env python3
""" Module for Last-In First-Out
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        # Use OrderedDict to maintain insertion order
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key associated with the item to store.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        # Check if key is not already in cache
        if key not in self.cache_data:
            # Check if the cache exceeds the max limit
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Pop the last item inserted (LIFO)
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        # Add item to the cache and move it to the end
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
            does not exist in the cache.
        """
        return self.cache_data.get(key, None)
