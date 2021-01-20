# 303. Range Sum Query - Immutable
# Easy
#
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
#
# Example 1:
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
# Constraints:
# 0 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= i <= j < nums.length
# At most 104 calls will be made to sumRange.

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [None]*len(nums)
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            self.prefix_sum[i]=curr_sum
        self.prefix_sum = [0]+self.prefix_sum

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j+1] - self.prefix_sum[i]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
obj.prefix_sum
obj.sumRange(2,5)
obj.sumRange(0,5)
