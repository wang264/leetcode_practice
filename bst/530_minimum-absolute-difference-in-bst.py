# 530. Minimum Absolute Difference in BST
# Easy

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
#
# Note:
# There are at least two nodes in this BST.
# This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from sys import maxsize

from helperfunc import TreeNode


# because in order traversal of BST is increasing,
# we can get the minimum difference by comparing each node with
# its previous node in the in oder traversal.

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min_diff = maxsize

        def in_order_traverse(root: TreeNode):
            if root is None:
                return
            in_order_traverse(root.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val
            in_order_traverse(root.right)

        in_order_traverse(root)
        return self.min_diff
