# 33. Search in Rotated Sorted Array
# Medium
#
# You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = self.find_min_index(nums)
        if nums[min_idx] <= target <= nums[-1]:
            left = min_idx
            right = len(nums) - 1
        else:
            left = 0
            right = min_idx - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

    def find_min_index(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 0
            else:
                return 1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        if nums[left] < nums[right]:
            return left
        else:
            return right


sol = Solution()
sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
