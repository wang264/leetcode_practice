# 124. Binary Tree Maximum Path Sum
# Hard

# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
# along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6

# Example 2:
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
import sys

from binary_tree_helper import TreeNode, deserialize

# 1. root must be used.
# 2. at most one child can be used.

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        self._max_path_sum(root)
        return self.ans

    def _max_path_sum(self, root):
        if not root:
            return -sys.maxsize
        left = max(0, self._max_path_sum(root.left))
        right = max(0, self._max_path_sum(root.right))
        self.ans = max(self.ans, root.val+left+right)  # 以Root为根节点的最大的path sum.

        return root.val + max(left, right)

root = deserialize("[-10,9,20,null,null,15,7]")

sol = Solution()
sol.maxPathSum(root=root) == 42