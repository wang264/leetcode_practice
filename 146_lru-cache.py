# 146. LRU Cache
# Medium

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# Follow up:
# Could you do get and put in O(1) time complexity?
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    # def __repr__(self):
    #    return f"key:{self.key} val:{self.val} next:{self.next}, prev:{self.prev}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.key_to_node[node.key]

    def _append_to_tail(self, node: ListNode):
        prev_ptr = self.tail.prev
        prev_ptr.next = node
        node.next = self.tail
        node.prev = prev_ptr
        self.tail.prev = node

        self.key_to_node[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node.keys():
            return -1
        node = self.key_to_node[key]

        self._remove_node(node)
        self._append_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # exist in cache
        if key in self.key_to_node.keys():
            node = self.key_to_node[key]
            node.val = value  # reset value
            self._remove_node(node)
            self._append_to_tail(node)
        else:
            # if capacity reach, need to pop on free space from cache
            if len(self.key_to_node) >= self.capacity:
                self._remove_node(self.head.next)

            node = ListNode(key, value)
            self._append_to_tail(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

obj = LRUCache(2)
obj.put(1, 1)  # cache is {1=1}
obj.put(2, 2)  # cache is {1=1, 2=2}
obj.get(1)  # return 1
obj.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
obj.get(2)  # returns -1 (not found)
obj.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
obj.get(1)  # return -1 (not found)
obj.get(3)  # return 3
obj.get(4)  # return 4

#
# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
obj.get(2)  # should return 2
obj.put(1, 1)
obj.put(4, 1)
obj.get(2)  # should return -1
