# 460. LFU Cache
# Hard
# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#
# Implement the LFUCache class:
#
# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When
# the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new
# item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used
# key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the
# smallest use counter is the least frequently used key.
#
# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter
# for a key in the cache is incremented either a get or put operation is called on it.

# Example 1:
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#
# Constraints:
# 0 <= capacity, key, value <= 104
# At most 105 calls will be made to get and put.

from collections import deque, defaultdict


class CacheNode:
    def __init__(self, key, value):
        self.frequency = 1
        self.key = key
        self.value = value


class LFUCache:

    def __init__(self, capacity: int):
        self.freq_to_deque = defaultdict(deque)
        self.key_to_chachenode = dict()
        self.size = 0
        self.capacity = capacity
        # self.min_freq = 0

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        # if key does not exist
        if key not in self.key_to_chachenode.keys():
            return -1
        # if key exist
        # update the Object,
        cache_node = self.key_to_chachenode[key]
        self.touch_node(cache_node)

        return cache_node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # this is existing key
        if key in self.key_to_chachenode.keys():
            # update existing key.
            cache_node = self.key_to_chachenode[key]
            cache_node.value = value
            # update that node's frequency
            self.touch_node(cache_node)
        # key does not exist
        else:
            # check if capacity is reach
            if self.size == self.capacity:
                self.remove_min_freq_node()
                # does not need to update size because we plan to add one and already remove one
            else:
                self.size += 1

            # crate node
            cache_node = CacheNode(key=key, value=value)
            self.freq_to_deque[1].appendleft(cache_node)
            self.key_to_chachenode[key] = cache_node

    def touch_node(self, cache_node: CacheNode):
        # find it in deque
        frequency = cache_node.frequency
        # remove from old, and add to correct frequency
        self.freq_to_deque[frequency].remove(cache_node)
        if len(self.freq_to_deque[frequency])==0:
            del self.freq_to_deque[frequency]
        # update the object
        cache_node.frequency += 1
        self.freq_to_deque[frequency + 1].appendleft(cache_node)

    def remove_min_freq_node(self):
        freq = min(self.freq_to_deque.keys())
        if freq == 0:
            return
        _deque = self.freq_to_deque[freq]
        cache_node = _deque[-1]
        _deque.pop()
        if len(_deque) == 0:
            del self.freq_to_deque[freq]
        # remove from dictionary
        del self.key_to_chachenode[cache_node.key]

lfu = LFUCache(2)
lfu.put(1, 1)    # cache=[1,_], cnt(1)=1
lfu.put(2, 2)    # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1)       # return 1
                 # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)    # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 # cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2)       # return -1 (not found)
lfu.get(3)       # return 3
                 # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)    # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 # cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1)       # return -1 (not found)
lfu.get(3)       # return 3
                 # cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4)       # return 4
                 # cache=[3,4], cnt(4)=2, cnt(3)=3