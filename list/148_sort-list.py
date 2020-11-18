# 148. Sort List
# Medium
#
# Given the head of a linked list, return the list after sorting it in ascending order.
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
#
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        n = self.get_list_length(head)
        if n == 0 or n == 1:
            return head
        elif n == 2:
            first = head
            second = head.next
            if first.val< second.val:
                return first
            else:
                first.next = second.next
                second.next = first
                return second
        else:
            l1, l2 = self.split_first_nth(head, n // 2)
            l1_sorted = self.sortList(l1)
            l2_sorted = self.sortList(l2)
            return self.merge_two_sorted_list(l1_sorted, l2_sorted)

    def split_first_nth(self, head: ListNode, n: int):
        prev = ListNode(-1)
        prev.next = head
        curr = head
        counter = 0
        while head and counter < n:
            counter += 1
            prev = curr
            curr = curr.next

        prev.next = None
        mid = curr
        return head, mid

    def get_list_length(self, head: ListNode):
        if head is None:
            return 0

        counter = 0
        while head:
            counter += 1
            head = head.next

        return counter

    def merge_two_sorted_list(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        tail = dummy

        while l1 and l2:
            # l1 will always be the list with smaller value at the head
            if l1.val < l2.val:
                pass
            else:
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next


sol = Solution()
l = build_linked_list_from_array([-1, 5, 3, 4, 0])

rslt = sol.sortList(head=l)
