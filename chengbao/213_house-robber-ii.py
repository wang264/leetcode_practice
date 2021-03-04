# 213. House Robber II
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [0]
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # the key of this question is
        # if you rob the first one you can not rob the last house
        # if you rob the last one, then you can not rob the first house
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        case_1 = self._rob_helper_from_198(nums=nums[0:-1])
        case_2 = self._rob_helper_from_198(nums=nums[1:])
        return max(case_1, case_2)

    def _rob_helper_from_question_198(self, nums: List[int]) -> int:
        # dp[i] the maximum amount of money you can get from robing first i house
        dp = [None] * (len(nums) + 1)

        # if you rob first 0 houses, you get 0
        dp[0] = 0
        # if you rob first 1 houses, you get nums[0]
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            # maximum profit for rob first i houses is the maximum of the following cases.
            # 1. you rob the i-1th house(index in i-2, so you can not rob ith house
            # 2. you rob the first i-2th house, so you can rob the ith house
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[len(nums)]

