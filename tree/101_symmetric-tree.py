# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

# Therefore, the question is: when are two trees a mirror reflection of each other?
#
# Two trees are a mirror reflection of each other if:
#
# 1.Their two roots have the same value.
# 2.The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

# This is like a person looking at a mirror. The reflection in the mirror has the same head,
#  but the reflection's right arm corresponds to the actual person's left arm, and vice versa.
# The explanation above translates naturally to a recursive function as follows.

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, root_1: TreeNode, root_2: TreeNode) -> bool:
        if root_1 is None and root_2 is None:
            return True
        elif root_1 and root_2:

            return root_1.val == root_2.val and self.is_mirror(root_1.left, root_2.right) and self.is_mirror(
                root_1.right, root_2.left)
        else:
            return False

sol = Solution()
root = deserialize('[1,2,3]')
sol.isSymmetric(root)
