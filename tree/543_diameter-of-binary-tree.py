# 543. Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary
# tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.

from binary_tree_helper import TreeNode


# 以ROOT为转折点。。。
# 　顺便遍历子树的可能的根节点。　然后打擂台。
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        self.longest_path_helper(root)
        return self.ans - 1

    # return the max path length that passes root and at most one child.
    def longest_path_helper(self, root: TreeNode):
        if root is None:
            return 0
        else:
            left = self.longest_path_helper(root.left)
            right = self.longest_path_helper(root.right)
            self.ans = max(self.ans, 1 + left + right)
            return 1 + max(left, right)
