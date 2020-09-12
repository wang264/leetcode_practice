# 129. Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.
#
# Example:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

from binary_tree_helper import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        rslt = []
        self.dfs_helper(root, 0, rslt)
        return sum(rslt)

    def dfs_helper(self, root, curr_sum, rslt):
        if root is None:
            return
        curr_sum = curr_sum * 10 + root.val
        if root.left is None and root.right is None:
            rslt.append(curr_sum)

        self.dfs_helper(root.left, curr_sum, rslt)
        self.dfs_helper(root.right, curr_sum, rslt)

