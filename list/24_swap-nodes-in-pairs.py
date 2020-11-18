# 24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # length of 0 or 1
        if not head or head.next is None:
            return head
        # at least length 2

        curr_1 = head
        curr_2 = head.next
        dummy = ListNode(-1, next=curr_1)
        prev = dummy
        next = None

        while curr_1 and curr_2:
            # prev ---> curr_1 ----> curr_2 ----> next
            next = curr_2.next
            prev.next = curr_2
            curr_1.next = next
            curr_2.next = curr_1

            # curr_1 and curr_2 has been swapped\
            # prev ---> curr_2 ----> curr_1 ----> next
            if next is None or next.next is None:
                break
            prev = curr_1
            curr_1 = next
            curr_2 = next.next

        return dummy.next


sol = Solution()
bla = sol.swapPairs(head=build_linked_list_from_array(vals=[1, 2, 3, 4, 5]))
bla
