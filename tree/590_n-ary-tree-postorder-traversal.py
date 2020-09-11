# 590. N-ary Tree Postorder Traversal
#
# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal, each group of
# children is separated by the null value (See examples)
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        s1 = []
        s2 = [root]

        while s2:
            node = s2.pop()
            s1.append(node.val)
            for child in node.children:
                s2.append(child)

        return s1[::-1]