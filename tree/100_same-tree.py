# 100. Same Tree

# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

from binary_tree_helper import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            val_same = p.val == q.val
            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)

            return val_same and left_same and right_same

        else:
            return False