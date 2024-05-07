#!/usr/bin/env python3
'''Basic Dictionary Cache Class inheriting from a Base Cache Class
'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Iherits from BaseCaching
    '''

    def put(self, key, item):
        '''Add an item in the cache
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key
        '''
        if key is None:
            return None
        return self.cache_data.get(key)
