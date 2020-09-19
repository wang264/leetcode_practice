# 337. House Robber III
# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart
# thief realized that "all houses in this place forms a binary tree". It will automatically contact the police
# if two directly-linked houses were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
# Input: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def rob(self, root: TreeNode) -> int:
        rob, not_rob = self.rob_helper(root)

        return max(rob, not_rob)

    def rob_helper(self, root) -> tuple:
        if root is None:
            return 0, 0
        # return the maximum amount that can be rob if we rob_root or we do not rob root.
        rob_left, not_rob_left = self.rob_helper(root.left)
        rob_right, not_rob_right = self.rob_helper(root.right)

        # if you rob root, you can not rob your sons.
        rob_root = root.val + not_rob_left + not_rob_right

        # if you do not root, you can rob children or leave them alone, do what ever you want
        not_rob_root = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)

        return rob_root, not_rob_root

sol = Solution()
root = deserialize("[3,4,5,1,3,null,1]")
sol.rob(root)