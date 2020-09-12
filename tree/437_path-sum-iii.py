# 437. Path Sum III
#
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        rslt = []
        self.dfs_traverse(root, rslt, target=sum)
        return len(rslt)

    def dfs_traverse(self, root, rslt, target):
        if root is None:
            return
        self.dfs_select_path(root, [], rslt, target)

        self.dfs_traverse(root.left, rslt, target)
        self.dfs_traverse(root.right, rslt, target)

    def dfs_select_path(self, root, curr_path, rslt, target):
        if root is None:
            return
        curr_path.append(root.val)
        if root.val == target:
            rslt.append(curr_path[:])

        self.dfs_select_path(root.left, curr_path, rslt, target - root.val)
        self.dfs_select_path(root.right, curr_path, rslt, target - root.val)
        curr_path.pop()


class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        # divide and conquer
        return self.number_of_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def number_of_paths(self, root, target):
        if root is None:
            return 0
        count = 0
        if root.val == target:
            count += 1
        count += self.number_of_paths(root.left, target - root.val)
        count += self.number_of_paths(root.right, target - root.val)

        return count

sol = Solution()
root = deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]')
assert sol.pathSum(root, 8) == 3

sol = Solution()
root = deserialize('[1,null,2,null,3,null,4,null,5]')
assert sol.pathSum(root, 3) == 2
