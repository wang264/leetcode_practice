# 138. Copy List with Random Pointer
# Medium
#
# A linked list is given such that each node contains an additional random pointer which could point to any
# node in the list or null.
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a
# pair of [val, random_index] where:
# * val: an integer representing Node.val
# * random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if
# it does not point to any node.
#
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
# Example 4:
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
# Constraints:
# * -10000 <= Node.val <= 10000
# * Node.random is null or pointing to a node in the linked list.
# * The number of nodes will not exceed 1000.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        old_to_new = dict()
        curr_node = head
        while curr_node:
            old_to_new[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            # fix the next and random node
            if curr_node.next is not None:
                old_to_new[curr_node].next = old_to_new[curr_node.next]
            if curr_node.random is not None:
                old_to_new[curr_node].random = old_to_new[curr_node.random]
            curr_node = curr_node.next
        return old_to_new[head]