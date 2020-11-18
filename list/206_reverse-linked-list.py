# 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

from helperfunc import ListNode, build_linked_list_from_array

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

l1 = build_linked_list_from_array([1,2,3])
sol=Solution()
bla = sol.reverseList(head=l1)
