# %%
from collections import OrderedDict
class LRU_Cache(object):
    """
        Cache that removes the least recently used element if cache memory is full.
        All operations work in constant time O(1).
    """
    
    def __init__(self, capacity: int):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.cache.get(key): # time complexity of dict.get(key) is O(1)
            self.cache.move_to_end(key) # time complexity of move_to_end() is O(1)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Sets the value if the key is not present in the cache. 
        # If the cache is at capacity it removes the oldest item. 
        if not self.cache.get(key): # time complexity of dict.get(key) is O(1)
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False) # time complexity of popitem() is  O(1)
            self.cache[key] = value
            self.cache.move_to_end(key) # time complexity of move_to_end() is O(1)

# %%
def test_cache():
    # Initialize cache object
    our_cache = LRU_Cache(5)

    # Set cache values
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # Get cache values
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))       # returns -1 because 9 is not present in the cache

    # Set additional cache values
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    our_cache.set(7, 7)
    our_cache.set(8, 8)
    print(our_cache.get(3))       # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


if __name__ == "__main__":
    test_cache()
# %%
