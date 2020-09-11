# 111. Minimum Depth of Binary Tree
#
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)
        if root.left is None:
            return right_min_depth + 1
        if root.right is None:
            return left_min_depth + 1

        return 1 + min(left_min_depth, right_min_depth)


sol = Solution()
root = deserialize('[1,2]')
assert sol.minDepth(root) == 2
