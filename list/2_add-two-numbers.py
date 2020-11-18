# # 2. Add Two Numbers
# # You are given two non-empty linked lists representing two non-negative integers. The digits are
# # stored in reverse order, and each of their nodes contains a single digit. Add the two numbers
# # and return the sum as a linked list.
# #
# # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# #
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
# * The number of nodes in each linked list is in the range [1, 100].
# * 0 <= Node.val <= 9
# * It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

sol = Solution()
l1 = build_linked_list_from_array([2,4,3])
l2 = build_linked_list_from_array([5,6,4])

rslt = sol.addTwoNumbers(l1,l2)

l1 = build_linked_list_from_array([0])
l2 = build_linked_list_from_array([0])

rslt = sol.addTwoNumbers(l1,l2)


l1 = build_linked_list_from_array([9,9,9,9,9,9,9])
l2 = build_linked_list_from_array([9,9,9,9])

rslt = sol.addTwoNumbers(l1,l2)