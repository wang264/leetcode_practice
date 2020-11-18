# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from helperfunc import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy

        curr_1 = l1
        curr_2 = l2
        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                curr = ListNode(curr_1.val)
                curr_1 = curr_1.next
            else:
                curr = ListNode(curr_2.val)
                curr_2 = curr_2.next

            prev.next = curr
            # update prev
            prev = curr

        if curr_1:
            left_over_linklist = curr_1
        else:
            left_over_linklist = curr_2

        while left_over_linklist:
            curr = ListNode(left_over_linklist.val)
            prev.next = curr
            prev = curr
            left_over_linklist = left_over_linklist.next

        return dummy.next
