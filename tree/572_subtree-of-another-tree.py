# 572. Subtree of Another Tree
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
# a subtree of s. A subtree of s is a tree consists of a node in s and all of this
# node's descendants. The tree s could also be considered as a subtree of itself.
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#    4
#   / \
#  1   2
#
# return

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.contain_subtree(s, t)

    def equal(self, tree_1: TreeNode, tree_2: TreeNode):
        if tree_1 is None and tree_2 is None:
            return True
        elif tree_1 and tree_2:
            return tree_1.val == tree_2.val and self.equal(tree_1.left, tree_2.left) and self.equal(tree_1.right,
                                                                                                    tree_2.right)
        else:
            return False

    def contain_subtree(self, s: TreeNode, sub_tree: TreeNode):
        if s is None:
            return False
        if self.equal(s, sub_tree):
            return True
        if self.contain_subtree(s.left, sub_tree) or self.contain_subtree(s.right, sub_tree):
            return True
        else:
            return False


sol = Solution()
s = deserialize('[3,4,5,1,2')
t = deserialize('[4,1,2]')

assert sol.isSubtree(s, t) == True

sol = Solution()
s = deserialize('[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]')
t = deserialize('[1,null,1,null,1,null,1,null,1,null,1,2]')

sol.isSubtree(s, t)
