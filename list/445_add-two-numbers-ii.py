# 445. Add Two Numbers II
#
#
# Share
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

from helperfunc import ListNode, build_linked_list_from_array
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbers_one(l1, l2))

    # code for 2_add-two-numbers
    def addTwoNumbers_one(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr_1 = l1
        ptr_2 = l2
        carry = 0
        head = ListNode(-1)
        prev = head
        while ptr_1 and ptr_2:
            value = ptr_1.val + ptr_2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(value)
            prev.next = node
            prev = node

            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next

        if ptr_1 is None and ptr_2 is None:
            pass
        else:
            if ptr_1 is None:
                rest_ptr = ptr_2
            else:
                rest_ptr = ptr_1
            while rest_ptr is not None:
                value = rest_ptr.val + carry
                if value >= 10:
                    value -= 10
                    carry = 1
                else:
                    carry = 0
                node = ListNode(value)
                prev.next = node
                prev = node
                rest_ptr = rest_ptr.next
        if carry == 1:
            prev.next = ListNode(1)
        return head.next

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


sol = Solution()
l1 = build_linked_list_from_array([7,2,4,3])
l2 = build_linked_list_from_array([5,6,4])

sol.addTwoNumbers(l1,l2)