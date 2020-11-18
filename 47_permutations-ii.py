# 47. Permutations II
#
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique
# permutations in any order.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Constraints:
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        selected = [False for _ in range(len(nums))]
        curr_permutation = []
        rslt = []
        nums.sort()
        self.bfs_helper(nums, curr_permutation, selected, rslt)
        return rslt

    def bfs_helper(self, nums, curr_path, selected, rslt):
        if len(curr_path) == len(nums):
            rslt.append(curr_path[:])

        for i, num in enumerate(nums):
            if selected[i]:
                continue
            # 1' 1" 2
            # => 1' 1" 2 => √
            # => 1" 1' 2 => x
            # 不能跳过上一个1选下一个1
            elif i > 0 and nums[i] == nums[i - 1] and (not selected[i - 1]):
                continue

            selected[i] = True
            curr_path.append(num)
            self.bfs_helper(nums, curr_path, selected, rslt)
            curr_path.pop()
            selected[i] = False


sol = Solution()
sol.permuteUnique(nums=[1, 1, 2])
