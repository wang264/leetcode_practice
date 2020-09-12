# 814. Binary Tree Pruning
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
#
#
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
#
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        self.prune_recursive(root)
        if self.contain_one(root):
            return root
        else:
            return None

    def contain_one(self, root: TreeNode):
        if root is None:
            return False
        root_contain_one = root.val == 1
        left_contain_one = self.contain_one(root.left)
        right_contain_one = self.contain_one(root.right)

        return root_contain_one or left_contain_one or right_contain_one

    def prune_recursive(self, root):
        if root is None:
            return None
        if self.contain_one(root.left):
            self.prune_recursive(root.left)
        else:
            root.left = None

        if self.contain_one(root.right):
            self.prune_recursive(root.right)
        else:
            root.right = None


sol = Solution()
root = deserialize('[0,null,0,0,0]')
rslt = sol.pruneTree(root)
assert rslt is None


class Solution2:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            root = None
        return root


sol = Solution2()
root = deserialize('[1,0,1,0,0,0,1]')
rslt = sol.pruneTree(root)

