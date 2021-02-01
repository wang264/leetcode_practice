# 114. Flatten Binary Tree to Linked List
# Medium

# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Example 1:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
#
# Example 2:
# Input: root = []
# Output: []
#
# Example 3:
# Input: root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

from helperfunc import TreeNode, build_tree_breadth_first
from collections import deque


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        # use a queue to push nodes into the queue by pre order.
        q = deque([root])

        while q:
            node = q.popleft()
            if node.right:
                q.appendleft(node.right)
            if node.left:
                q.appendleft(node.left)
            node.left = None
            if len(q) > 0:
                node.right = q[0]


root = build_tree_breadth_first(sequence=[1, 2, 5, 3, 4, None, 6])

sol = Solution()
sol.flatten(root=root)

root