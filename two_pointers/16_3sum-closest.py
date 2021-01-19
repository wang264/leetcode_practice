# 16. 3Sum Closest
# Medium
#
# Given an array nums of n integers and an integer target, find three integers in nums
# such that the sum is closest to target. Return the sum of the three integers. You may
# assume that each input would have exactly one solution.
#
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Constraints:
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4


import sys
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # write your code here
        nums.sort()
        closest_diff = sys.maxsize
        closest_sum = sys.maxsize
        # a+ b + c closest to target ------> a+b closest to    target - c
        # we assume a < b < c to prevent duplicate answer
        for idx_c, c in enumerate(nums):
            two_sum_closest_diff, two_sum_closest_sum = \
                self.two_sum_closest(nums, start=0, end=idx_c - 1,
                                     target=target - c)
            if two_sum_closest_diff < closest_diff:
                closest_diff = two_sum_closest_diff
                closest_sum = two_sum_closest_sum + c
        return closest_sum

    def two_sum_closest(self, numbers, start, end, target):
        if start >= end:
            return sys.maxsize, sys.maxsize
        left = start
        right = end
        closest_diff = sys.maxsize
        closest_sum = sys.maxsize
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if abs(two_sum - target) < closest_diff:
                closest_diff = abs(two_sum - target)
                closest_sum = two_sum
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                return 0, two_sum

        return closest_diff, closest_sum


sol = Solution()
sol.threeSumClosest(nums=[2, 7, 11, 15], target=3)