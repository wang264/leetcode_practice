# 90. Subsets II
# Medium
#
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
#
# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

from typing import List


class Solution:
    # to prevent duplicate solution, for example 1, 1', 1'', 2, 2', 2''...
    # we need to first select 1 before we select 1',
    # we need to select 1 and 1' before we select 1''

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        curr_path = []
        rslt = []
        curr_idx = 0
        selected = [False for _ in range(len(nums))]
        self.dfs(nums, curr_idx, curr_path, rslt, selected)
        return rslt

    def dfs(self, nums, curr_idx, curr_path, rslt, selected):
        rslt.append(curr_path[:])
        for i in range(curr_idx,len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and (not selected[i - 1]):
                continue
            selected[i] = True
            curr_path.append(nums[i])
            self.dfs(nums, i + 1, curr_path, rslt, selected)
            curr_path.pop()
            selected[i] = False

sol = Solution()
sol.subsetsWithDup(nums=[1,2,2])