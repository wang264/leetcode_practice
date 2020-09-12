# 669. Trim a Binary Search Tree
#
# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that
# all its elements lies in [low, high]. You might need to change the root of the tree, so the result should return
# the new root of the trimmed binary search tree.

# Constraints:
#
# 1. The number of nodes in the tree in the range [1, 104].
# 2. 0 <= Node.val <= 104
# 3. The value of each node in the tree is unique.
# 4. root is guaranteed to be a valid binary search tree.
# 5. 0 <= l <= r <= 104

# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
#
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
#
# Input: root = [1], low = 1, high = 2
# Output: [1]
#
# Input: root = [1,null,2], low = 1, high = 3
# Output: [1,null,2]
#
# Input: root = [1,null,2], low = 2, high = 4
# Output: [2]

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trimmed_tree(node):
            if node is None:
                return None
            elif node.val > high:  # all right subtree including the node should be trimmed.
                return trimmed_tree(node.left)
            elif node.val < low:  # all left subtree including the node should be trimmed.
                return trimmed_tree(node.right)
            else:  # left< node < right
                node.left = trimmed_tree(node.left)
                node.right = trimmed_tree(node.right)
                return node

        return trimmed_tree(root)


sol = Solution()
root = deserialize('[3,0,4,null,2,null,null,1]')
rslt = sol.trimBST(root, 1, 3)
