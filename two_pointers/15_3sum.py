# 15. 3Sum
# Medium
#
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 10^5


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        nums.sort()
        rslt = []
        for i in range(len(nums)):
            arr = nums[0:i] + nums[i + 1:]
            two_sum_rslts = self.two_sum_sorted(nums=arr, target=-1 * nums[i])
            for partial_rslt in two_sum_rslts:
                partial_rslt.append(nums[i])
                partial_rslt.sort()
                if partial_rslt not in rslt:
                    rslt.append(partial_rslt)
        return rslt

    def two_sum_sorted(self, nums, target):
        left = 0
        right = len(nums) - 1
        two_sum_rslt = []
        while left < right:
            val = nums[left] + nums[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                two_sum_rslt.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return two_sum_rslt


sol = Solution()
sol.threeSum(nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4])
