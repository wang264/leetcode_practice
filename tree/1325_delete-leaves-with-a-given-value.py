# 1325. Delete Leaves With a Given Value
#
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value
# target, it should also be deleted (you need to continue doing that until you can't).
#
#
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
#
#
# Input: root = [1, 3, 3, 3, 2], target = 3
# Output: [1, 3, null, null, 2]
#
# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
#
# Input: root = [1, 1, 1], target = 1
# Output: []
#
# Input: root = [1,2,3], target = 1
# Output: [1,2,3]
from binary_tree_helper import TreeNode, deserialize


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val==target:
            return None
        else:
            return root

sol = Solution()
root = deserialize('[1,2,3,2,null,2,4]')
sol.removeLeafNodes(root=root,target=2)

sol = Solution()
root = deserialize('[2,2,2]')
rslt = sol.removeLeafNodes(root=root,target=2)