# 53. Maximum Subarray
# Easy
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [0]
# Output: 0
#
# Example 4:
# Input: nums = [-1]
# Output: -1
#
# Example 5:
# Input: nums = [-100000]
# Output: -100000

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = contiguous subarray that have the largest sum and ending at i'th position
        dp = [None] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] + nums[i] > nums[i]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)


sol = Solution()
sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
