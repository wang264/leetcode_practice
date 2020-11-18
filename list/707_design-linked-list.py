# 707. Design Linked List
# Medium
#
# 673
#
# 783
#
# Add to List
#
# Share
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

# Constraints:
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'val:{} next:{}'.format(self.val, self.next.val if self.next else None)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def _get_node(self, index: int) -> ListNode:
        if index < -1 or index >= self.size:
            return None
        if index == -1:
            return ListNode(-1, self.head)
        counter = 0
        curr = self.head
        while counter < index:
            curr = curr.next
            counter += 1

        return curr

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get_node(index=index)
        if node:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val, next=self.head)
        if self.size == 0:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            return self.addAtHead(val=val)

        if index == self.size:
            return self.addAtTail(val=val)

        node = ListNode(val)
        prev = self._get_node(index=index - 1)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if index < 0 or index >= self.size:
        #     return
        #
        # if index == 0:
        #     self.head = self.head.next
        #     self.size -= 1
        #
        # if index == self.size - 1:
        #     prev = self._get_node(index=index - 1)
        #     prev.next = None
        #     self.tail = prev
        #     self.size -= 1
        #
        # else:
        #     prev = self._get_node(index=index - 1)
        #     prev.next = prev.next.next
        #     self.size -= 1
        if index < 0 or index >= self.size:
            return
        prev = self._get_node(index - 1)
        prev.next = prev.next.next
        if index == 0:
            self.head = prev.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
myLinkedList.get(1)  # return 2
myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
myLinkedList.get(1)  # return 3

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.deleteAtIndex(0)

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtHead(2)
myLinkedList.addAtHead(1)
myLinkedList.addAtIndex(3, 0)
myLinkedList.deleteAtIndex(2)
myLinkedList.addAtHead(6)
myLinkedList.addAtTail(4)
myLinkedList.get(4)
myLinkedList.addAtHead(4)
myLinkedList.addAtIndex(5, 0)
myLinkedList.addAtHead(6)
