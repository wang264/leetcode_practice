# 154. Find Minimum in Rotated Sorted Array II
# Hard

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
# Input: [1,3,5]
# Output: 1
# Example 2:
#
# Input: [2,2,2,0,1]
# Output: 0
# Note:
#
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            num = nums[mid]

            # 这道是之前那道Search in Rotated Sorted Array 的延伸，现在数组中允许出现重复数字，这个也会影响我们选择哪
            # 半边继续搜索，由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：
            # 如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的。
            #
            # 而如果可以有重复值，就会出现来面两种情况，[3 1 1]和[1 1 3 1]，对于这两种情况中间值(mid)等于最右值(right)时，要把最右值向左一位，
            # 如果还相同则继续移，直到移到不同值为止，然后其他部分还采用 Search in Rotated Sorted Array
            # 中的方法，可以得到代码如下：

            if num == nums[right]:
                while nums[right - 1] == nums[right] and left + 1 < right:
                    right -= 1
                mid = (left + right) // 2
                num = nums[mid]

            if num > nums[right]:
                left = mid
            elif num < nums[right]:
                right = mid

        if nums[left] <= nums[right]:
            return nums[left]
        else:
            return nums[right]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(nums, left, right):
            # only one or two elements
            if right - left <= 1:
                return min(nums[left], nums[right])
            # if sorted
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2
            return min(find_min(nums, left, mid - 1), find_min(nums, mid, right))

        return find_min(nums, 0, len(nums) - 1)


sol = Solution()
sol.findMin(nums=[2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 7, 7, 9, 1, 1, 2, 2, 2, 2, 2])
