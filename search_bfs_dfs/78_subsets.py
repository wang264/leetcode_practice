# 78. Subsets
# Medium
#
# Given an integer array nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        curr_path = []
        rslt = []
        curr_index = 0
        self.dfs(nums, curr_index, curr_path, rslt)
        return rslt

    def dfs(self, nums, curr_index, curr_path, rslt):
        rslt.append(curr_path[:])

        for i in range(curr_index, len(nums)):
            curr_path.append(nums[i])
            self.dfs(nums,curr_index=i+1,curr_path=curr_path,rslt=rslt)
            curr_path.pop()

sol =Solution()
sol.subsets(nums=[1,2,3])

