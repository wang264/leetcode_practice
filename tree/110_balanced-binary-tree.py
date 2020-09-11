# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

from binary_tree_helper import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, balanced = self.helper(root)
        return balanced

    def helper(self, root: TreeNode) -> bool:
        # return (height, is_balanced)
        if root is None:
            return 0, True

        left_height, left_balanced = self.helper(root.left)
        right_height, right_balanced = self.helper(root.right)

        root_height = 1 + max(left_height, right_height)
        root_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced

        return root_height, root_balanced