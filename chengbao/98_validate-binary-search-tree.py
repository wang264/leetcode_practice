# 98. Validate Binary Search Tree
# Medium
#
# 5378
#
# 639
#
# Add to List
#
# Share
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
from helperfunc import TreeNode
import sys


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        is_valid, _, _ = self.helper(root)
        return is_valid

    def helper(self, root):
        """
        :param root:
        :return: tuple of (is_valid_bst, max_val, min_val)
        """
        if root is None:
            return True, -1 * sys.maxsize, 1 * sys.maxsize

        l_isvalid, l_max, l_min = self.helper(root.left)
        r_isvalid, r_max, r_min = self.helper(root.right)

        # bst is valid if
        # 1. root.val > l_max  root.val<r_min
        # 2. root.left and root.right are both valid bst
        root_valid = root.val > l_max and root.val < r_min and l_isvalid and r_isvalid
        root_max = max([l_max, r_max, root.val])
        root_min = min([l_min, r_min, root.val])

        return root_valid, root_max, root_min


