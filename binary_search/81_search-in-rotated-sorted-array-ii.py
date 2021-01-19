# 81. Search in Rotated Sorted Array II
# Medium
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

#
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         if len(nums) == 0:
#             return False
#         if len(nums) == 1:
#             return target == nums[0]
#
#         min_idx = self.find_min_index(nums)
#
#         in_first_half = self.binary_search(nums[0:min_idx], target)
#         in_second_half = self.binary_search(nums[min_idx:], target)
#
#         return in_first_half or in_second_half
#
#     def find_min_index(self, nums: List[int]) -> int:
#
#         left = 0
#         right = len(nums) - 1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             num = nums[mid]
#
#             # 这道是之前那道Search in Rotated Sorted Array 的延伸，现在数组中允许出现重复数字，这个也会影响我们选择哪
#             # 半边继续搜索，由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：
#             # 如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的。
#             #
#             # 而如果可以有重复值，就会出现来面两种情况，[3 1 1]和[1 1 3 1]，对于这两种情况中间值(mid)等于最右值(right)时，要把最右值向左一位，
#             # 如果还相同则继续移，直到移到不同值为止，然后其他部分还采用 Search in Rotated Sorted Array
#             # 中的方法，可以得到代码如下：
#
#             if num == nums[right]:
#                 while nums[right-1] == nums[right] and left + 1 < right:
#                     right -= 1
#                 mid = (left + right) // 2
#                 num = nums[mid]
#
#             if num > nums[right]:
#                 left = mid
#             elif num < nums[right]:
#                 right = mid
#
#         if nums[left] <= nums[right]:
#             return left
#         else:
#             return right
#
#     def binary_search(self, nums: List[int], target: int) -> bool:
#         if len(nums) == 0:
#             return False
#         if len(nums) == 1:
#             return target == nums[0]
#         left = 0
#         right = len(nums) - 1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return True
#             if nums[mid] > target:
#                 right = mid
#             else:
#                 left = mid
#
#         if nums[left] == target or nums[right] == target:
#             return True
#         else:
#             return False

#https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51602234

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


nums = [1, 3]
sol = Solution()
sol.search(nums=nums, target=3)

# nums = [2, 2, 2, 0, 2, 2]
# sol = Solution()
# sol.search(nums=nums, target=0)

sol = Solution()
nums = [1, 1, 1, 1, 1, 2, 1, 1, 1]

sol.search(nums=nums, target=2)

sol.search(nums = [2,2,2,5,6,0,0,1,2], target = 0)
