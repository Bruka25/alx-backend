#!/usr/bin/env python3
"""Module for least Recently Used caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
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
                # Pop the least recently used item (first item)
                lru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", lru_key)
        # Add item to the cache and move it to the front
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
            does not exist in the cache.
        """
        if key is not None and key in self.cache_data:
            # Move accessed item to the front to mark it as recently used
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
