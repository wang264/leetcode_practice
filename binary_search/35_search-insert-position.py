# 35. Search Insert Position
# Easy
#
# Given a sorted array of distinct integers and a target value, return the index if the target
# is found. If not, return the index where it would be if it were inserted in order.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
#
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
#
#
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        # no answer, find position
        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        else:
            return left + 1


sol = Solution()
sol.searchInsert(nums=[1, 3, 5, 6], target=2)
