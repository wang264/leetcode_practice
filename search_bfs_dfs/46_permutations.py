# 46. Permutations
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        curr_permutation = []
        self.dfs_helper(nums, curr_permutation, rslt)
        return rslt

    def dfs_helper(self, nums, curr_permutation, rslt):
        if len(curr_permutation) == len(nums):
            rslt.append(curr_permutation[:])

        for num in nums:
            if num in curr_permutation:
                pass
            else:
                curr_permutation.append(num)
                self.dfs_helper(nums, curr_permutation, rslt)
                curr_permutation.pop()

sol = Solution()
sol.permute(nums=[1,2,3])
