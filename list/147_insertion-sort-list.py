# 147. Insertion Sort List
#
# Sort a linked list using insertion sort.
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        curr = head.next
        prev = head
        tail = curr

        # iteratively, pop element from the list and append it to the correct location.
        while curr is not None:
            # print(curr)
            self.remove_from_list(prev=prev, curr=curr)
            head, tail = self.insert_to_sorted_list(head=head, tail=prev, node_to_insert=curr)
            prev = tail
            curr = tail.next

        return head

    # remove the node "curr" from the list
    def remove_from_list(self, prev: ListNode, curr: ListNode):
        prev.next = curr.next
        return curr

    # insert into list(given the list's head to tail) , and return the new tail.

    def insert_to_sorted_list(self, head: ListNode, tail: ListNode, node_to_insert: ListNode):
        curr = head
        prev = ListNode(-1)
        prev.next = curr
        while curr is not None and node_to_insert.val > curr.val and prev != tail:
            prev = curr
            curr = curr.next

        prev.next = node_to_insert
        node_to_insert.next = curr

        if node_to_insert.val > tail.val:
            tail = node_to_insert

        if node_to_insert.val <= head.val:
            head = node_to_insert

        # return the updated head and tail.
        return head, tail


sol = Solution()
l = build_linked_list_from_array([-1, 5, 3, 4, 0])
bla = sol.insertionSortList(head=l)

l2 = build_linked_list_from_array([4, 2, 1, 3])
bla_2 = sol.insertionSortList(head=l2)

l3 = build_linked_list_from_array([1, 1])
bla_3 = sol.insertionSortList(head=l3)

l4 = build_linked_list_from_array([3, 2, 4])
bla_4 = sol.insertionSortList(head=l4)


class Solution2:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        while head:
            t = head.next
            curr = dummy
            while curr.next and curr.next.val<=head.val:
                curr = curr.next

            head.next = curr.next
            curr.next = head
            head = t

        return dummy.next


sol = Solution2()
l = build_linked_list_from_array([-1, 5, 3, 4, 0])
bla5 = sol.insertionSortList(head=l)