# 416. Partition Equal Subset Sum
# Medium
#
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # using DP
        # dp[i][j] = whether we can use the first i number to sum to j
        # after iterate over all i and j,
        # let sum = sum(nums) n = len(nums)
        # we check if dp[n][sum//2] is True.

        nums_sum = sum(nums)
        n = len(nums)
        # if sum is odd,
        if nums_sum % 2 != 0:
            return False

        dp = [[False] * (nums_sum+1) for _ in range(n+1)]

        # base case, we can use first zero numbers to sum to 0
        dp[0][0] = True

        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(nums_sum +1):
                if j - num >= 0:
                    if dp[i - 1][j - num]:
                        # if we use the ith number
                        dp[i][j] = True
                        # if we do not use the ith number
                        dp[i][j - num] = True

        return dp[n][nums_sum // 2]


sol = Solution()
sol.canPartition(nums=[1, 5, 11, 5])

sol.canPartition(nums=[1,1])

