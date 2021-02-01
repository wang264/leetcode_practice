# 34. Find First and Last Position of Element in Sorted Array
# Medium
#
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
# Example1:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example2:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Example3:
#
# Input: nums = [], target = 0
# Output: [-1, -1]
#
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                left = mid
                right = mid

        # fine the first and last location
        if nums[left] != target and nums[right] != target:
            return [-1, -1]

        if nums[left] == target:
            left_start = left
        else:
            left_start = right

        if nums[right] == target:
            right_start = right
        else:
            right_start = left

        while left_start - 1 >= 0 and nums[left_start - 1] == target:
            left_start -= 1
        while right_start + 1 < len(nums) and nums[right_start + 1] == target:
            right_start += 1

        return [left_start, right_start]


sol = Solution()
sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)

sol.searchRange(nums=[1, 2, 2], target=2)

sol.searchRange(nums=[1], target=1)
sol.searchRange(nums=[1, 1, 2], target=1)
