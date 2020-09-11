# 1302. Deepest Leaves Sum
# Medium
#
# Given a binary tree,
# return the sum of values of its deepest leaves.
#
# Example 1:
#
# Input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
# Output: 15


from collections import deque

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque([root])
        lvl_sum = 0
        while queue:
            lvl_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                lvl_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


        return lvl_sum

sol = Solution()
root = deserialize('[1,2,3,4,5,null,6,7,null,null,null,null,8]')
sol.deepestLeavesSum(root=root)
