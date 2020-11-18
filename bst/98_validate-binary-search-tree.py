# 98. Validate Binary Search Tree
#
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from helperfunc import TreeNode
from sys import maxsize

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # BST is valid is it's left subtree is valid and its right subtree is valid
        # root value > max value of left subtree
        # root vale < min value of right subtree
        _, _, rslt = self.helper(root)
        return rslt

    def helper(self, root: TreeNode)-> tuple:
        # return(max value, min val, is_valid_bst)
        if root is None:
            return -1*maxsize, maxsize, True
        left_max, left_min, left_valid = self.helper(root.left)
        right_max, right_min, right_valid = self.helper(root.right)

        root_max = max([root.val,left_max, right_max])
        root_min = min([root.val, left_min, right_min])

        if root.val>left_max and root.val<right_min and left_valid and right_valid:
            root_valid = True
        else:
            root_valid = False

        return root_max, root_min, root_valid

