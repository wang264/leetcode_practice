# 897. Increasing Order Search Tree
# Easy
#
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
# the root of the tree, and every node has no left child and only one right child.
#
# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
#
# Constraints:
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000

# Definition for a binary tree node.

from helperfunc import TreeNode, build_tree_breadth_first

class Solution:
    prior_node = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = root
        while new_root.left:
            new_root = new_root.left

        def in_order_helper(root):
            if root is None:
                return
            in_order_helper(root.left)
            self.prior_node.left = None
            self.prior_node.right = root
            self.prior_node = root
            in_order_helper(root.right)

        self.prior_node = TreeNode(None)
        in_order_helper(root)
        # need to set the last node's left to be none.
        self.prior_node.left = None
        return new_root

sol = Solution()
root = build_tree_breadth_first(sequence=[2,1,4,None,None,3])

bla = sol.increasingBST(root=root)

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right