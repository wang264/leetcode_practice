# 257. Binary Tree Paths
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

from binary_tree_helper import TreeNode
from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        else:
            left_paths = self.binaryTreePaths(root.left)
            right_paths = self.binaryTreePaths(root.right)
        return [f"{str(root.val)}->{path}" for path in left_paths+right_paths]
