#!/usr/bin/env python3
'''First In First Out Caching Implementation
'''


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO Caching Implementation
    '''

    def __init__(self):
        '''Initialize FIFOCache
        '''
        super().__init__()
        self.cached_data = OrderedDict()

    def put(self, key, item):
        """Add new item to the cache.

        If the cache is full, remove the least recently used item before
        inserting the new one.

        Args:
            key (str): Item key.
            item: Item value.
        """
        self.cached_data[key] = item
        if key is None or item is None:
            return
        if len(self.cached_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cached_data.popitem(False)
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """Get an item by key.

        Args:
            key (str): Item key.

        Returns:
            The value in self.cached_data linked to key.
            None if key or self.cached_data doesn't exist.
        """
        if key is None or key not in self.cached_data:
            return None
        return self.cached_data[key]
