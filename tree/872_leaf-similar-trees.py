# 872. Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Input: root1 = [1], root2 = [1]
# Output: true

# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false

# Input: root1 = [1,2], root2 = [2,2]
# Output: true


from binary_tree_helper import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        rslt_1 = list()
        rslt_2 = list()
        self.traverse_helper(root1, rslt_1)
        self.traverse_helper(root2, rslt_2)

        return rslt_1 == rslt_2

    def traverse_helper(self, root: TreeNode, rslt: list):
        # if it is a leaf node
        if root is not None and root.left is None and root.right is None:
            rslt.append(root.val)
        if root is not None:
            self.traverse_helper(root.left, rslt)
            self.traverse_helper(root.right, rslt)
