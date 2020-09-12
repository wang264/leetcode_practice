# 113. Path Sum II
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
from typing import List

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        rslt = []
        self.dfs_helper(root, rslt, [], sum)
        return rslt

    def dfs_helper(self, root: TreeNode, rslt: list, curr_list: list, target: int):
        if root is None:
            return
        curr_list.append(root.val)
        if root.val == target and root.left is None and root.right is None:
            rslt.append(curr_list[:])
            curr_list.pop()
            return
        self.dfs_helper(root.left, rslt, curr_list, target - root.val)
        self.dfs_helper(root.right, rslt, curr_list, target - root.val)
        curr_list.pop()

sol = Solution()
root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
sol.pathSum(root, sum=22)
