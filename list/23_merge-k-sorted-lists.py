# 23. Merge k Sorted Lists
# Hard
#
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import List

from helperfunc import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        rslt = []
        for i, link_list in enumerate(lists):
            if link_list:
                # (element, list_node)
                heapq.heappush(min_heap, (link_list.val, link_list))

        while len(min_heap) > 0:
            val, list_node = heapq.heappop()
            rslt.append(val)
            if list_node.next:
                heapq.heappush(min_heap, (list_node.next.val, list_node.next))
