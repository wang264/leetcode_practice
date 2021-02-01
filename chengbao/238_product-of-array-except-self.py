# 238. Product of Array Except Self
# Medium
#
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
# all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the ' \
#               'whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefix[i] = nums[0]*nums[1]*....nums[i-1]
        prefix = [1] * n
        # suffix[i] = nums[n-1]*nums[n-2].....* nums[i+1]
        suffix = [1] * n

        prefix[0]=1
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        suffix[n-1] = 1
        for i in reversed(range(0,n-1)): # need to set 0....n-2
            suffix[i]=suffix[i+1]*nums[i+1]

        rslt = [p * s for p, s in zip(prefix, suffix)]

        return rslt
