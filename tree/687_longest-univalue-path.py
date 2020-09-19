# 687. Longest Univalue Path
#
# Given a binary tree, find the length of the longest path where each node in the path has the same value.
# This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

from binary_tree_helper import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 1
        self.path_helper(root)
        return self.ans - 1

    def path_helper(self, root: TreeNode):
        # 1. root must be used
        # 2. when update ans, we can use both children
        # 3. when return: we return the longest path with only one child.
        if root is None:
            return 0

        left = self.path_helper(root.left)
        right = self.path_helper(root.right)
        num_nodes_left_tree = 0
        num_nodes_right_tree = 0
        if root.left and root.val == root.left.val:
            num_nodes_left_tree = left
        if root.right and root.val == root.right.val:
            num_nodes_right_tree = right

        self.ans = max(self.ans, 1 + num_nodes_left_tree + num_nodes_right_tree)
        return 1 + max(num_nodes_left_tree, num_nodes_right_tree)
