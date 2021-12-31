## LRU Cache
Design a Least Recently Used (LRU) Cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. The expected time complexity of setting and getting operations are O(1).

### Time Complexity
The LRU Cache is implemented with the **OrderedDict** from collections. This class provides useful methods for rearranging the order of the elements in the dictionary. The methods *move_to_end()* and *popitem()* work in constant time (O(1)). The time complexity of accessing an item in a dictionary depends on the input and the hash function. In practice, it is almost certain that items can be accessed in O(1).  

### Space Complexity
The capacity of the LRU Cache depends on the input provided to the constructor. Therefore, the space allocation for this LRU Cache varies depending on the provided capacity. This takes O(n) space.