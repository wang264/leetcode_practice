# 912. Sort an Array
# Medium
#
# Given an array of integers nums, sort the array in ascending order.
#
# Example
# 1:
#
# Input: nums = [5, 2, 3, 1]
# Output: [1, 2, 3, 5]
# Example
# 2:
#
# Input: nums = [5, 1, 1, 2, 0, 0]
# Output: [0, 0, 1, 1, 2, 5]
#
# Constraints:
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
        if left >= right:
            return
        idx = self.partition(nums, left, right)
        self.quicksort(nums, left, idx - 1)
        self.quicksort(nums, idx + 1, right)

    def partition(self, nums, left, right):
        pivot = left
        prev = left
        for curr in range(left + 1, right + 1):
            if nums[curr] > nums[pivot]:
                pass
            else:
                prev += 1
                nums[curr], nums[prev] = nums[prev], nums[curr]
        nums[pivot], nums[prev] = nums[prev], nums[pivot]

        return prev


sol = Solution()
arr = [5, 1, 1, 2, 0, 0]
sol.sortArray(nums=arr)
arr
