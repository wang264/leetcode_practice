from typing import List

from binary_tree_helper import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rslt = []
        stack = [root]

        while stack:
            node = stack.pop()
            rslt.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return rslt
