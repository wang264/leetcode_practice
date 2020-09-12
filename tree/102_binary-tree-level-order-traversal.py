# 102. Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],

from collections import deque
from binary_tree_helper import TreeNode
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        rslt = []

        queue = deque([root])
        while queue:
            this_lvl = []
            for _ in range(len(queue)):
                node = queue.popleft()
                this_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rslt.append(this_lvl[:])

        return rslt