#!/usr/bin/env python3
"""MOdule for Basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key associated with the item to store.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
            does not exist in the cache.
        """
        return self.cache_data.get(key, None)
