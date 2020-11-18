# 153. Find Minimum in Rotated Sorted Array
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums, return the minimum element of this array.

# Example 1:
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid
            elif nums[mid] < nums[-1]:
                right = mid

        return min(nums[left], nums[right])


sol = Solution()
sol.findMin(nums=[11, 13, 15, 17])


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        def find_min(nums, left, right):
            # only one or two elements
            if right - left <= 1:
                return min(nums[left], nums[right])
            # if sorted
            if nums[left]< nums[right]:
                return nums[left]

            mid = (left + right) // 2
            return min(find_min(nums, left, mid - 1), find_min(nums, mid, right))

        return find_min(nums, 0, len(nums) - 1)


sol = Solution2()
sol.findMin(nums=[4, 5, 6, 7, 8, 9, 1, 2, 3])
