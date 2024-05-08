#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out Cache
    """

    def __init__(self):
        """init
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Adds item to cache.
        If the cache is full, the least recently used item is discarded.

        :param key: key to store the item under
        :param item: item to store
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                 # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache.

        :param key: key to retrieve the item from
        :return: the item if it is in the cache, None otherwise
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
