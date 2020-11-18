# 501. Find Mode in Binary Search Tree
# Easy
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

from typing import List

from helperfunc import TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.curr_num = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def visit(root: TreeNode):
            if self.curr_num is None:
                self.curr_num = root.val
                self.curr_count += 1
            else:
                if root.val == self.curr_num:
                    self.curr_count += 1
                else:
                    self.curr_num = root.val
                    self.curr_count = 1

            if self.curr_count > self.max_count:
                self.modes = []
                self.modes.append(self.curr_num)
                self.max_count = self.curr_count
            elif self.curr_count == self.max_count:
                self.modes.append(self.curr_num)
            else:
                pass

        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            visit(root)
            in_order(root.right)

        in_order(root)
        return self.modes


