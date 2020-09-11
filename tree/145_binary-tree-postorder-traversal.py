from typing import List

from binary_tree_helper import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        s1 = []
        s2 = [root]

        while s2:
            node = s2.pop()
            s1.append(node.val)

            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)

        return s1[::-1]
