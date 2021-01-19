# 74. Search a 2D Matrix
# Medium
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.find_row_index(matrix, target)
        return self.binary_search(nums=matrix[idx], target=target)

    def find_row_index(self, matrix, target):
        last_col_idx = len(matrix[0]) - 1
        small = 0
        large = len(matrix) - 1

        while small + 1 < large:
            mid = (small + large) // 2
            if matrix[mid][last_col_idx] < target:
                small = mid
            elif matrix[mid][last_col_idx] > target:
                large = mid
            else:
                return mid

        if matrix[small][last_col_idx] >= target:
            return small
        else:
            return large

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return True

        return nums[left] == target or nums[right] == target


sol = Solution()
sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)

sol.searchMatrix(matrix=[[1], [3]], target=1)
