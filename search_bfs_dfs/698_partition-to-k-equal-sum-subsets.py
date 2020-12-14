# 698. Partition to K Equal Sum Subsets
# Medium
#
# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
# Note:
# * 1 <= k <= len(nums) <= 16.
# * 0 < nums[i] < 10000.

from typing import List

#
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         sum_nums = sum(nums)
#         if sum_nums % k != 0:
#             return False
#         used = [False] * len(nums)
#
#         nums = sorted(nums, reverse=True)
#         return self.dfs(nums, target=sum_nums // k, curr_idx=0, curr_val=0, groups_needed=k, used=used)
#
#     def dfs(self, nums, target, curr_idx, curr_val, groups_needed, used):
#         if groups_needed == 1:
#             return True
#         if curr_val>target:
#             return False
#
#         if curr_val == target:
#             #print(groups_needed-1)
#             return self.dfs(nums, target, curr_idx=0, curr_val=0, groups_needed=groups_needed - 1, used=used)
#
#         for i in range(curr_idx, len(nums)):
#             if used[i]:
#                 continue
#             next_val = curr_val + nums[i]
#             used[i] = True
#             if self.dfs(nums, target, curr_idx=i + 1, curr_val=next_val, groups_needed=groups_needed, used=used):
#                 return True
#             used[i] = False
#
#         return False

#
# sol = Solution()
# nums = [4, 3, 2, 3, 5, 2, 1]
# k = 4
# nums = [4, 3, 2, 1]
# k = 2
#
# nums = [4, 5, 3, 2, 5, 5, 5, 1, 5, 5, 5, 5, 3, 5, 5, 2]
# k = 13
# sol.canPartitionKSubsets(nums, k)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        Sum = sum(nums)
        if (Sum % k != 0):
            return False
        nums = sorted(nums, reverse=True)
        visited = [False]*len(nums)
        return self.helper(nums, k, Sum // k, 0, 0, visited)

    def helper(self,nums, k, target,start, curSum, visited):
        if k == 1:
            return True
        if curSum > target:
            return False
        if curSum == target:
            return self.helper(nums, k - 1, target, 0, 0, visited)
        for i in range(start,len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            if self.helper(nums, k, target, i + 1, curSum + nums[i], visited):
                return True
            visited[i] = False

        return False

sol =Solution()
nums = [4, 5, 3, 2, 5, 5,5, 1, 5, 5, 5, 5, 3, 5, 5, 2]
k = 13
sol.canPartitionKSubsets(nums,k)